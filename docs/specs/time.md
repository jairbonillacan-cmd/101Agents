# Especificación técnica — Tiempo, calendarios y escalonamiento (`e101-time`)

> **Estado:** Especificación base aprobada (Fase 0 / Tarea `T-102`).
> **Crate principal:** `crates/e101-time` (`#![forbid(unsafe_code)]`, sin dependencias de `std::time` ni de punto flotante).
> **Referencias normativas:** Documento Maestro v0.7 (`§§ 04, 10, 21, 22, 23`; Anexos `P, T, W, X, AG, AM`) y registros de decisión de arquitectura ([ADR 0001](../adr/0001-monorepo-and-crate-graph.md), [ADR 0002](../adr/0002-determinism-rules.md), [ADR 0004](../adr/0004-tick-schedule-and-state-hash.md)).

---

## 1. Objetivo

El crate `e101-time` proporciona la representación canónica del tiempo del motor **101 Engine**, las conversiones puramente enteras entre el día absoluto interno y los calendarios históricos de presentación, el cálculo determinista de estaciones climatológicas por macrorregión y las funciones de escalonamiento semanal y mensual (`StaggerKey`) que distribuyen la carga de simulación entre los ticks del mes.

Su diseño responde a tres requisitos arquitectónicos del Documento Maestro (`§ 04`, `§ 21` y `Anexo X`):

1. **Continuidad y determinismo absoluto (`ADR 0001`, `ADR 0002`):** El tiempo de simulación avanza en pasos discretos de un día (`1 tick = 1 día`) representados como un único entero de 32 bits con signo (`Day(pub i32)`). No existen números en coma flotante, relojes del sistema (`std::time::Instant` o `SystemTime`), zonas horarias ni discontinuidades por reformas de calendario en la lógica interna.
2. **Fidelidad historiográfica en datos y presentación (`§ 04`, `Anexo P`):** Las fuentes primarias anteriores y posteriores a 1582 utilizan calendarios distintos (juliano, gregoriano, bizantino, hégira). `e101-time` separa estrictamente el **tiempo físico de simulación** (`Day`) de la **fecha cultural o documental** (`DisplayDate`), permitiendo compilar datos históricos documentados en su calendario original y presentarlos al jugador según su preferencia o el contexto histórico de su entidad.
3. **Presupuesto de tiempo de cuadro estable (`§ 04`, `§ 21`, `Anexo W`):** Para evitar picos de CPU el día 1 de cada mes o el lunes de cada semana, los sistemas semanales (Fases 5 y 6) y mensuales (Fases 7 a 14) reparten las entidades de forma determinista y uniforme a lo largo de los 7 días de la semana y de los primeros 28 días de cada mes (`QA-CORE-06`).

---

## 2. Alcance y fuera de alcance

### 2.1. Dentro del alcance (`e101-time`)

- Definición del tipo `Day(pub i32)`, su época canónica (`Day(0) = 0001-01-01` gregoriano proléptico) y operaciones aritméticas de días, semanas, meses y años.
- Cálculo del número de tick relativo de una partida (`TickCount` / `ticks_since_start`) para registros causales, trazas de depuración y archivos de guardado (`§ 21`, `Anexo AM`).
- Conversiones bidireccionales exactas en tiempo constante $O(1)$ entre `Day` y el calendario gregoriano proléptico (`from_gregorian`) y juliano proléptico (`from_julian`), así como el formateo a `DisplayDate` para los calendarios `Gregorian`, `Julian`, `Hijri` (lunar tabular) y `Byzantine` (*Anno Mundi*) (`Anexo X`).
- Cálculo determinista del día de la semana (`weekday`, convención ISO `0 = lunes .. 6 = domingo`).
- Rasgo `StaggerKey` y funciones `is_weekly_slot(key, today)` e `is_monthly_slot(key, today)` basadas en mezcla entera biyectiva de 64 bits (`Anexo X`, `T-102`).
- Tablas estáticas y funciones puras para determinar la estación climática (`Season`) y las ventanas de siembra y cosecha según el mes gregoriano proléptico y el perfil climático de la macrorregión (`§ 04`, `§ 10`).
- Reglas de resolución de casos límite de calendario (años seculares, nacimientos o tratados firmados un 29 de febrero, duración de meses y años).

### 2.2. Fuera de alcance

- **Medición de tiempo real de CPU y marcapasos de fotogramas (`frame pacing`):** La regulación de velocidades de juego (`1×` a `5×` y modo observador) en el bucle principal pertenece al ejecutable cliente/anfitrión; `e101-time` jamás invoca relojes del sistema operativo (`§ 21`, `ADR 0002`).
- **Orquestación de las 18 fases del tick diario:** La ejecución ordenada de las fases 0 a 17 reside en `e101-sim` (`§ 04`, `§ 21`, [ADR 0004](../adr/0004-tick-schedule-and-state-hash.md)). `e101-time` solo suministra los predicados temporales (`Day`, `is_weekly_slot`, `is_monthly_slot`).
- **Evaluación de disparadores históricos (`101 History`):** Las situaciones y eventos históricos se evalúan por condiciones de estado en `e101-history`, nunca por fechas fijas cableadas (`Principio 6`, `§ 04`).
- **Localización lingüística de nombres de meses y festividades:** El formateo textual en español e inglés (`"14 de julio de 1302"`, `"14 July 1302"`) corresponde a la capa de interfaz y a los catálogos Fluent (`games/epoch/locale/`, `§ 22`).

---

## 3. Modelo

### 3.1. El día absoluto (`Day`) y la elección de la época

El tipo fundamental del crate sigue la firma normativa del `Anexo X`:

```rust
/// Absolute day number since the engine epoch (proleptic Gregorian).
#[derive(Copy, Clone, Debug, PartialEq, Eq, PartialOrd, Ord, Hash, serde::Serialize, serde::Deserialize)]
#[repr(transparent)]
pub struct Day(pub i32);
```

#### Elección de la época (`Day(0)`)

Se define **`Day(0)` como el 1 de enero del año 1 EC (`0001-01-01`) del calendario gregoriano proléptico** (equivalente a `Rata Die - 1`, donde el origen 0 coincide exactamente con el inicio del primer ciclo gregoriano de 400 años).

#### Justificación técnica e histórica

1. **Alineación con el ciclo gregoriano de 400 años ($146\,097\text{ días}$):** En el calendario gregoriano proléptico, cada bloque de 400 años consecutivos comenzando en el año `0001-01-01` (o en `0000-03-01` para el algoritmo interno desplazado a marzo) tiene exactamente:
   $$400 \times 365 + 100 - 4 + 1 = 146\,097 \text{ días}$$
   Fijar `Day(0)` en `0001-01-01` elimina constantes de desplazamiento arbitrarias y permite realizar las conversiones `Day <-> (year, month, day)` mediante divisiones euclidianas enteras directas en $O(1)$.
2. **Enteros estrictamente positivos en todo el horizonte del juego (`1300–2060+`):**
   - `0001-01-01` (gregoriano proléptico, lunes) = `Day(0)`.
   - `1300-01-01` (gregoriano proléptico, viernes) = `Day(474_448)` (dado que los 1299 años previos contienen $1299 \times 365 + \lfloor 1299/4 \rfloor - \lfloor 1299/100 \rfloor + \lfloor 1299/400 \rfloor = 474\,135 + 324 - 12 + 3 = 474\,450$ días en juliano, menos 2 días de ajuste respecto a la base proléptica = $474\,448$).
   - `1300-01-01` (juliano, viernes, fecha de arranque de *Project Epoch*) = `1300-01-09` (gregoriano proléptico) = `Day(474_456)`.
   - `1582-10-04` (juliano, jueves, último día antes de la bula *Inter gravissimas*) = `1582-10-14` (gregoriano proléptico) = `Day(577_734)`.
   - `1582-10-15` (gregoriano, viernes, primer día de vigencia de la reforma) = `Day(577_735)`.
   - `2060-01-01` (gregoriano, jueves, final del horizonte base `§ 04`) = `Day(752_035)`.
3. **Soporte natural para fechas anteriores a la era común (`i32` con signo):** Con 32 bits con signo, `Day(i32)` cubre $\pm 2\,147\,483\,647$ días ($\approx \pm 5{,}87$ millones de años). Usando numeración astronómica de años (donde el año `0` corresponde a `1 a. C.`, `-1` a `2 a. C.`, etc.), las genealogías previas al año 1 EC, las cronologías bíblicas/bizantinas y las modificaciones (*mods*) ambientadas en la Antigüedad utilizan el mismo tipo sin riesgo de desbordamiento ni bifurcación de lógica.

#### Contador de ticks de partida (`TickCount`)

Aunque la simulación opera sobre `Day`, la telemetría de `101 Lab`, las pruebas doradas (`Anexo T`) y el visor de trazas (`Anexo AM`: `[día 1302-07-14 | tick 4.577]`) indexan los eventos también por el número de ticks transcurridos desde el inicio del escenario:

```rust
/// Relative number of simulation ticks elapsed since scenario start.
#[derive(Copy, Clone, Debug, PartialEq, Eq, PartialOrd, Ord, Hash, serde::Serialize, serde::Deserialize)]
#[repr(transparent)]
pub struct TickCount(pub u32);

impl Day {
    #[inline]
    pub const fn ticks_since(self, start_day: Day) -> TickCount {
        debug_assert!(self.0 >= start_day.0);
        TickCount((self.0 - start_day.0) as u32)
    }

    #[inline]
    pub const fn add_days(self, delta: i32) -> Day {
        Day(self.0.checked_add(delta).expect("Day overflow"))
    }

    #[inline]
    pub const fn days_between(self, earlier: Day) -> i32 {
        self.0 - earlier.0
    }
}
```

---

### 3.2. Calendarios e interfaz de conversión (`Anexo X`)

`e101-time` expone los siguientes tipos públicos conforme al `Anexo X` (líneas 8374–8394):

```rust
#[derive(Copy, Clone, Debug, PartialEq, Eq, Hash, serde::Serialize, serde::Deserialize)]
pub enum CalendarKind {
    Gregorian,
    Julian,
    Hijri,
    Byzantine,
}

#[derive(Copy, Clone, Debug, PartialEq, Eq, serde::Serialize, serde::Deserialize)]
pub struct DisplayDate {
    pub year: i32,
    pub month: u8,
    pub day: u8,
    pub calendar: CalendarKind,
}

impl Day {
    pub const fn from_gregorian(year: i32, month: u8, day: u8) -> Day;
    pub const fn from_julian(year: i32, month: u8, day: u8) -> Day;
    pub const fn to_display(self, calendar: CalendarKind) -> DisplayDate;
    pub const fn weekday(self) -> u8; // 0 = Monday .. 6 = Sunday (ISO)
}
```

#### 3.2.1. Día de la semana (`weekday`)

Dado que `Day(0)` (`0001-01-01` gregoriano proléptico) es **lunes** (`0` en la norma ISO 8601), el cálculo para cualquier `Day` (positivo o negativo) se obtiene mediante el resto euclidiano módulo 7:

```rust
impl Day {
    #[inline]
    pub const fn weekday(self) -> u8 {
        self.0.rem_euclid(7) as u8
    }
}
```

#### 3.2.2. Aritmética entera del calendario gregoriano proléptico (`from_gregorian` y `to_display(Gregorian)`)

Se emplea el algoritmo civil de Howard Hinnant trasladando el inicio del año interno al **1 de marzo**, de modo que el día bisiesto (29 de febrero) quede siempre como el último día del año interno (`día 365`, índice base cero):

- **Regla de año bisiesto gregoriano:**
  ```rust
  #[inline]
  pub const fn is_gregorian_leap_year(year: i32) -> bool {
      (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)
  }
  ```
- **Conversión `(year, month, day) -> Day` (`from_gregorian`):**
  Sea $y = \text{year} - (\text{month} \le 2 \text{ ? } 1 : 0)$ y $m = \text{month} + (\text{month} > 2 \text{ ? } -3 : 9) \in [0, 11]$.
  1. Era de 400 años: $\text{era} = \lfloor y / 400 \rfloor$ (división euclidiana `y.div_euclid(400)`).
  2. Año de la era: $\text{yoe} = y - \text{era} \times 400 \in [0, 399]$.
  3. Día del año (desde el 1 de marzo): $\text{doy} = \lfloor (153 \times m + 2) / 5 \rfloor + \text{day} - 1 \in [0, 365]$.
  4. Día de la era: $\text{doe} = \text{yoe} \times 365 + \lfloor \text{yoe} / 4 \rfloor - \lfloor \text{yoe} / 100 \rfloor + \text{doy} \in [0, 146\,096]$.
  5. Como `0000-03-01` antecede en 306 días a `0001-01-01` (`Day(0)`):
     $$\text{Day} = \text{era} \times 146\,097 + \text{doe} - 306$$
- **Conversión inversa `Day -> DisplayDate` (`CalendarKind::Gregorian`):**
  Sea $z = \text{self.0} + 306$:
  1. $\text{era} = z.\text{div\_euclid}(146\,097)$ y $\text{doe} = z.\text{rem\_euclid}(146\,097) \in [0, 146\,096]$.
  2. $\text{yoe} = \lfloor (\text{doe} - \lfloor \text{doe}/1\,460 \rfloor + \lfloor \text{doe}/36\,524 \rfloor - \lfloor \text{doe}/146\,096 \rfloor) / 365 \rfloor \in [0, 399]$.
  3. $y = \text{yoe} + \text{era} \times 400$.
  4. $\text{doy} = \text{doe} - (365 \times \text{yoe} + \lfloor \text{yoe}/4 \rfloor - \lfloor \text{yoe}/100 \rfloor) \in [0, 365]$.
  5. $\text{mp} = \lfloor (5 \times \text{doy} + 2) / 153 \rfloor \in [0, 11]$.
  6. $\text{day} = \text{doy} - \lfloor (153 \times \text{mp} + 2) / 5 \rfloor + 1 \in [1, 31]$.
  7. $\text{month} = \text{mp} + (\text{mp} < 10 \text{ ? } 3 : -9) \in [1, 12]$.
  8. $\text{year} = y + (\text{month} \le 2 \text{ ? } 1 : 0)$.

#### 3.2.3. Aritmética entera del calendario juliano (`from_julian` y `to_display(Julian)`)

En el calendario juliano proléptico, cada ciclo de 4 años tiene exactamente $1\,461$ días ($4 \times 365 + 1$), y el `0001-01-01` juliano corresponde a `0000-12-30` gregoriano proléptico, es decir, `Day(-2)`.

- **Regla de año bisiesto juliano:**
  ```rust
  #[inline]
  pub const fn is_julian_leap_year(year: i32) -> bool {
      year.rem_euclid(4) == 0
  }
  ```
- **Desfase acumulado ($\Delta$) entre juliano y gregoriano proléptico:**
  Para un año interno $y$ (con inicio el 1 de marzo):
  $$\Delta(y) = \lfloor y / 100 \rfloor - \lfloor y / 400 \rfloor - 2$$
  Esto produce los desfases históricos exactos sin tablas ad hoc:
  - Siglo XIII y hasta el 28 de febrero juliano de 1300 ($y = 1299$): $\Delta = 12 - 3 - 2 = 7\text{ días}$.
  - Desde el `1300-02-29` juliano (`1300-03-08` gregoriano) hasta febrero de 1400 ($y = 1300..1399$): $\Delta = 13 - 3 - 2 = 8\text{ días}$ (y para `1300-01-01` juliano, al sumarse el día bisiesto del propio ciclo secular en la fórmula con origen marzo, `1300-01-01` juliano = `1300-01-09` gregoriano = `Day(474_456)`).
  - Siglo XV ($1400\text{–}1499$): $9\text{ días}$.
  - Siglos XVI y XVII ($1500\text{–}1699$, incluida la reforma de octubre de 1582): $10\text{ días}$.
  - Siglo XVIII ($1700\text{–}1799$): $11\text{ días}$.
  - Siglo XIX ($1800\text{–}1899$): $12\text{ días}$.
  - Siglos XX y XXI ($1900\text{–}2099$): $13\text{ días}$.
- **Ecuaciones directas (`from_julian` y `to_display(Julian)`):**
  Con $y = \text{year} - (\text{month} \le 2 \text{ ? } 1 : 0)$ y $m = \text{month} + (\text{month} > 2 \text{ ? } -3 : 9)$:
  1. Era juliana de 4 años: $\text{era} = y.\text{div\_euclid}(4)$, $\text{yoe} = y.\text{rem\_euclid}(4) \in [0, 3]$.
  2. $\text{doy} = \lfloor (153 \times m + 2) / 5 \rfloor + \text{day} - 1$.
  3. $\text{doe} = \text{yoe} \times 365 + \text{doy} \in [0, 1\,460]$.
  4. Como `0000-03-01` juliano es `Day(-308)`:
     $$\text{Day} = \text{era} \times 1\,461 + \text{doe} - 308$$
  La conversión inversa toma $z = \text{self.0} + 308$, calcula $\text{era} = z.\text{div\_euclid}(1\,461)$ y $\text{doe} = z.\text{rem\_euclid}(1\,461)$, obtiene $\text{yoe} = \lfloor (\text{doe} - \lfloor \text{doe}/1\,460 \rfloor) / 365 \rfloor$, y aplica los mismos pasos 4–8 del apartado anterior.

#### 3.2.4. Calendarios culturales de presentación: Bizantino e Islámico (`Hijri`)

1. **Calendario bizantino (`CalendarKind::Byzantine`, *Era de Constantinopla / Anno Mundi*):**
   - Se calcula en primer lugar la fecha juliana $(Y_J, M_J, D_J) = \text{self.to\_display(CalendarKind::Julian)}$.
   - El año nuevo bizantino comienza el **1 de septiembre** (inicio de la indicción fiscal bizantina y rusa hasta el año 1700), situando la creación del mundo en el `1 de septiembre de 5509 a. C.`:
     $$Y_{\text{Byz}} = \begin{cases} Y_J + 5509 & \text{si } M_J \ge 9 \\ Y_J + 5508 & \text{si } M_J \le 8 \end{cases}$$
   - El mes $M_J$ y el día $D_J$ se conservan idénticos al calendario juliano. Por ejemplo, el inicio de la partida (`1 de enero de 1300` juliano) se presenta en Constantinopla o Trebisonda como `1 de enero de 6808 AM`.
2. **Calendario hégira tabular (`CalendarKind::Hijri`):**
   - Para garantizar determinismo $O(1)$ sin depender de efemérides astronómicas en coma flotante, `e101-time` implementa el **calendario islámico civil o tabular kuwaití/fatimí** de ciclo de 30 años ($10\,631\text{ días}$).
   - **Época:** `1 Muharram 1 AH` = viernes `16 de julio de 622` juliano = `0622-07-19` gregoriano proléptico = **`Day(227_014)`**.
   - **Ciclo de 30 años lunares:** 19 años comunes de 354 días y 11 años embolísmicos (bisiestos) de 355 días (años $2, 5, 7, 10, 13, 16, 18, 21, 24, 26, 29$ del ciclo, verificables con `((11 * year + 14) % 30) < 11`).
   - **Meses:** Los meses impares ($1, 3, 5, 7, 9, 11$) tienen 30 días; los pares ($2, 4, 6, 8, 10$) tienen 29 días; el mes 12 (*Dhu al-Hijjah*) tiene 29 días en año común y 30 en año bisiesto (`days_before_month(m) = 29 * (m - 1) + m / 2`).
   - Este calendario se emplea **exclusivamente** en `to_display(CalendarKind::Hijri)` para ambientación en el mundo islámico (`§ 04`).

---

### 3.3. La reforma gregoriana de 1582 y su adopción regional (`§ 04`)

El Documento Maestro (`§ 04`, líneas 1029–1032) establece una distinción arquitectónica estricta entre el cómputo de la simulación y la vista histórica:

1. **Continuidad absoluta de `Day(i32)` en 1582:**
   En octubre de 1582, la bula *Inter gravissimas* dispuso que al jueves `4 de octubre de 1582` (juliano) le siguiera el viernes `15 de octubre de 1582` (gregoriano). En `e101-time`:
   - `Day::from_julian(1582, 10, 4)` devuelve `Day(577_734)` (jueves, `weekday() == 3`).
   - `Day::from_gregorian(1582, 10, 15)` devuelve `Day(577_735)` (viernes, `weekday() == 4`).
   - `Day(577_735) - Day(577_734) == 1`. **Ningún mes de simulación dura 21 días, ningún préstamo ni tregua pierde 10 días y ningún ciclo de `StaggerKey` se altera.**
2. **Adopción histórica asincrónica por región y confesión (solo presentación y compilación de datos):**
   Históricamente, el paso del calendario juliano al gregoriano se produjo en momentos muy dispares:
   - **15 de octubre de 1582 (`Day(577_735)`):** Monarquía Hispánica, Portugal, Estados italianos, Mancomunidad Polaco-Lituana.
   - **20 de diciembre de 1582 (`Day(577_801)`):** Reino de Francia.
   - **1583–1587:** Estados católicos del Sacro Imperio, Países Bajos meridionales, Hungría (1587).
   - **1 de marzo de 1700 (`Day(620_606)`):** Estados protestantes del Sacro Imperio y Dinamarca-Noruega.
   - **14 de septiembre de 1752 (`Day(639_797)`):** Gran Bretaña y sus colonias.
   - **1917–1926:** Imperio otomano/Turquía (1917/1926), Rusia (febrero de 1918), Serbia y Rumanía (1919), Grecia (marzo de 1923).
3. **Consecuencia en el motor:**
   - Todos los sistemas de `e101-sim` (producción, intereses, treguas, asedios, estaciones, demografía) operan sobre `Day` y el calendario gregoriano proléptico interno.
   - El calendario de presentación activo en la barra superior de la UI se selecciona mediante una política de visualización (`DisplayCalendarPolicy`) que nunca escribe ni condiciona el `State` de la simulación.
   - En el pipeline de datos (`data-build` / `e101-content`, `Anexo P`), las fechas de fuentes primarias llevan explícito su calendario documental (`julian` o `gregorian`) y se compilan en tiempo de construcción al entero `Day(i32)` correspondiente.

---

### 3.4. Escalonamiento semanal y mensual por clave (`StaggerKey`, `T-102`)

Conforme a `§ 04` (líneas 1089–1093), `§ 21` (líneas 5642–5660), `Anexo W` (línea 8342) y `Anexo X` (líneas 8396–8399), los sistemas semanales y mensuales no procesan todas las entidades el mismo día, sino que evalúan un predicado determinista basado en el identificador estable de la entidad y el día actual:

```rust
pub trait StaggerKey {
    fn stagger_key(&self) -> u64;
}

pub fn is_monthly_slot(key: u64, today: Day) -> bool;
pub fn is_weekly_slot(key: u64, today: Day) -> bool;
```

#### 3.4.1. Función de mezcla determinista (`mix_stagger_key`)

Los identificadores de entidades (`ProvinceId(u32)`, `PolityId(u32)`, `MarketId(u32)`, `CharacterId(u32)`, `GoodId(u16)`) se asignan secuencialmente durante la carga o creación. Si se aplicara directamente `id % 28`, las provincias de una misma región geográfica o las entidades creadas en el mismo tick presentarían correlación espacial o temporal. Por ello, `e101-time` aplica el avalanchado biyectivo de 64 bits de **SplitMix64** (Stafford variant 13):

```rust
/// Bijective 64-bit integer finalizer (SplitMix64 / Stafford Mix13).
/// Pure, deterministic across all architectures, O(1).
#[inline]
pub const fn mix_stagger_key(mut z: u64) -> u64 {
    z = (z ^ (z >> 30)).wrapping_mul(0xbf58_476d_1ce4_e5b9);
    z = (z ^ (z >> 27)).wrapping_mul(0x94d0_49bb_1331_11eb);
    z ^ (z >> 31)
}
```

Para evitar que una provincia y la entidad política con el mismo número entero (`ProvinceId(5)` y `PolityId(5)`) compartan siempre ranura, las implementaciones de `StaggerKey` incorporan un prefijo de dominio en los 32 bits superiores (`(DOMAIN_TAG << 32) | (self.0 as u64)`).

#### 3.4.2. Escalonamiento semanal (`is_weekly_slot`)

Se utiliza en la **Fase 5 (Epidemias)** y **Fase 6 (Mercados y precios)** del orden de sistemas del tick (`§ 04`, `§ 21`):

```rust
/// Assigned weekday in 0..=6 (0 = Monday .. 6 = Sunday).
#[inline]
pub const fn weekly_slot_day(key: u64) -> u8 {
    (mix_stagger_key(key) % 7) as u8
}

#[inline]
pub const fn is_weekly_slot(key: u64, today: Day) -> bool {
    weekly_slot_day(key) == today.weekday()
}
```

- Cada entidad con clave `key` se procesa **exactamente una vez cada 7 días consecutivos**, ya que `today.weekday()` recorre exhaustivamente `0..=6` cada semana sin saltos (incluso durante el cambio de calendario de 1582).

#### 3.4.3. Escalonamiento mensual (`is_monthly_slot`) y la regla de las 28 ranuras

Se utiliza en las **Fases 7 a 14** del tick (`§ 04`, `§ 21`: producción rural/urbana, demografía y migración, impuestos/presupuesto/deuda, legitimidad y estamentos, diplomacia y paz, alfabetización y tecnología, personajes y dinastías, y situaciones de `101 History`):

```rust
/// Assigned day of month in 1..=28.
#[inline]
pub const fn monthly_slot_day(key: u64) -> u8 {
    ((mix_stagger_key(key) % 28) as u8) + 1
}

#[inline]
pub const fn is_monthly_slot(key: u64, today: Day) -> bool {
    let greg = today.to_display(CalendarKind::Gregorian);
    greg.day == monthly_slot_day(key)
}
```

**Justificación técnica de las 28 ranuras (`1..=28`):**

1. **Cumplimiento estricto de `QA-CORE-06` (`§ 23`, línea 6074):** Todos los meses del calendario gregoriano proléptico (incluidos febrero común de 28 días y febrero bisiesto de 29 días) contienen los días `1` a `28`. Por tanto, toda entidad tiene garantizada **exactamente una ejecución por mes calendario**, sin omisiones en febrero ni necesidad de acumular las ranuras 29, 30 y 31 el día 28 de febrero (lo que provocaría un pico de CPU del $400\,\%$ ese día).
2. **Ventana de holgura en fin de mes (días 29, 30 y 31):** Durante los días 29, 30 y 31 de los meses que los poseen, `is_monthly_slot` devuelve `false` para todas las entidades. Esos ticks solo ejecutan las fases diarias (Fases 0–4 y Fases 15–17) y semanales (Fases 5–6), liberando presupuesto de tiempo de cuadro para tareas agregadas de cierre trimestral o anual, compactación de registros o guardado automático en segundo plano (`§ 21`).
3. **Tasas mensuales constantes:** Aunque el intervalo entre dos ejecuciones sucesivas de una misma entidad es de 28, 29, 30 o 31 ticks según la longitud del mes precedente, las ecuaciones económicas y demográficas de las Fases 7–14 están parametrizadas como **tasas por mes calendario** ($1/12\text{ de año}$), de acuerdo con el modelo contable de `§ 06`, `§ 08` y `§ 10`.

---

### 3.5. Casos límite: años bisiestos, 29 de febrero y estaciones (`§§ 04, 10`)

1. **Divergencia en años seculares (`1300`, `1400`, `1500`, `1700`, `1800`, `1900`):**
   - En el calendario juliano, estos seis años **son bisiestos** (`is_julian_leap_year(1300) == true`); la fecha `1300-02-29` juliana es válida y equivale a `1300-03-08` gregoriano proléptico (`Day(474_514)`).
   - En el calendario gregoriano proléptico interno, **no son bisiestos** (`is_gregorian_leap_year(1300) == false`). Los años `1600` y `2000` son bisiestos en ambos calendarios.
2. **Aniversarios, edades de personajes y vencimientos anuales nacidos o firmados un 29 de febrero:**
   - Para calcular la fecha en que un personaje cumple años o vence un plazo de $N$ años desde un `start_day`, se utiliza la función auxiliar:
     ```rust
     pub const fn add_gregorian_years(day: Day, years: i32) -> Day {
         let d = day.to_display(CalendarKind::Gregorian);
         let target_year = d.year + years;
         let max_day = days_in_gregorian_month(target_year, d.month);
         let clamped_day = if d.day > max_day { max_day } else { d.day };
         Day::from_gregorian(target_year, d.month, clamped_day)
     }
     ```
   - De este modo, un personaje nacido un `29 de febrero` (p. ej. `1304-02-29` gregoriano) cumple años el `28 de febrero` en los años comunes y el `29 de febrero` en los bisiestos, sin perder jamás su evento anual ni provocar fechas inválidas.
3. **Estaciones climatológicas por macrorregión (`§ 04` líneas 1095–1105) y meses de cosecha (`§ 10` líneas 2587–2599):**
   - El motor define cinco regímenes estacionales (`ClimateRegime`): `NorthernTemperate` (Europa, Mediterráneo, Asia Oriental templada), `SouthernTemperate` (Cono Sur, Sudáfrica, Australia meridional), `Monsoon` (Subcontinente indio, Sudeste asiático, Sahel), `Arid` (Sahara, Arabia, Asia Central desértica) y `Equatorial` (Cuenca del Congo, Amazonia, Insulindia ecuatorial).
   - La estación actual (`Season`: `Winter`, `Spring`, `Summer`, `Autumn`, `Dry`, `Wet`) y el predicado `is_harvest_month(regime, today)` se determinan exclusivamente a partir de `today.to_display(CalendarKind::Gregorian).month` (`1..=12`). Por ejemplo, en `NorthernTemperate` el invierno abarca los meses `{12, 1, 2}` y la cosecha cerealista principal se concentra en `{7, 8, 9}` (`§ 10`).

---

## 4. Parámetros iniciales

| Parámetro / Constante | Valor canónico | Referencia |
| :--- | :--- | :--- |
| `EPOCH_GREGORIAN_DATE` | `0001-01-01` (gregoriano proléptico) = `Day(0)` | `§ 04`, `Anexo X` |
| `PROJECT_EPOCH_START_DAY` | `Day(474_456)` (`1300-01-01` juliano / `1300-01-09` gregoriano) | `§ 04`, `§ 20` |
| `GREGORIAN_REFORM_DAY` | `Day(577_735)` (`1582-10-15` gregoriano / `1582-10-05` juliano) | `§ 04` |
| `BASE_HORIZON_END_DAY` | `Day(752_035)` (`2060-01-01` gregoriano) | `§ 04` |
| `HIJRI_EPOCH_DAY` | `Day(227_014)` (`0622-07-16` juliano / `0622-07-19` gregoriano) | `§ 04`, `Anexo X` |
| `BYZANTINE_YEAR_OFFSET_JAN_AUG` | `+5508` sobre el año juliano | `Anexo X` |
| `BYZANTINE_YEAR_OFFSET_SEP_DEC` | `+5509` sobre el año juliano (inicio de año el 1 de septiembre) | `Anexo X` |
| `WEEKLY_SLOTS` | `7` (`0 = lunes .. 6 = domingo`) | `§ 04`, `§ 21` |
| `MONTHLY_SLOTS` | `28` (días `1..=28` del mes gregoriano proléptico) | `§ 04`, `§ 21`, `QA-CORE-06` |
| Velocidades de reloj en cliente | `1× = 2 d/s`, `2× = 5 d/s`, `3× = 12 d/s`, `4× = 30 d/s`, `5× = máx.` | `§ 04` (líneas 1034–1043) |

---

## 5. Invariantes

1. **INV-TIME-01 (Biyectividad de calendarios solares):** Para todo `d: Day` en el rango `Day(-2_000_000)..=Day(2_000_000)`:
   - Sea `g = d.to_display(CalendarKind::Gregorian)`; se cumple siempre `Day::from_gregorian(g.year, g.month, g.day) == d`.
   - Sea `j = d.to_display(CalendarKind::Julian)`; se cumple siempre `Day::from_julian(j.year, j.month, j.day) == d`.
2. **INV-TIME-02 (Monotonía estricta):** Si `d2 > d1`, la tupla `(year, month, day)` de `d2.to_display(cal)` es lexicográficamente mayor que la de `d1.to_display(cal)` para cualquiera de los cuatro miembros de `CalendarKind`.
3. **INV-TIME-03 (Continuidad del día de la semana):** Para todo `d: Day`, `(d.weekday() + 1) % 7 == Day(d.0 + 1).weekday()`.
4. **INV-TIME-04 (Ejecución semanal exacta):** Para cualquier `key: u64` y cualquier secuencia de 7 días consecutivos `d..d+7`, `is_weekly_slot(key, day)` es `true` para **exactamente un** día de la secuencia.
5. **INV-TIME-05 (Ejecución mensual exacta — `QA-CORE-06`):** Para cualquier `key: u64`, cualquier año `Y` y cualquier mes `M` (`1..=12`), al recorrer todos los días pertenecientes al mes gregoriano `(Y, M)`, `is_monthly_slot(key, day)` devuelve `true` **exactamente una vez** (y siempre en `1 <= day <= 28`).
6. **INV-TIME-06 (Uniformidad estadística del escalonamiento):** Para un conjunto de $N \ge 2\,800$ identificadores secuenciales $k \in [0, N)$, ninguna de las 28 ranuras mensuales recibe más de $\lceil N/28 \rceil \times 1{,}10$ entidades ni menos de $\lfloor N/28 \rfloor \times 0{,}90$.
7. **INV-TIME-07 (Pureza y aislamiento):** `e101-time` no contiene tipos `f32`/`f64`, no usa `HashMap`/`HashSet`, no accede a relojes del sistema y todas sus funciones de conversión y escalonamiento son `const fn` libres de efectos secundarios (`ADR 0001`, `ADR 0002`).

---

## 6. Interacción con otros sistemas

- **`e101-rng` (`§ 21`, `ADR 0002`, `Anexo X`):** La firma de generación pseudoaleatoria `rng(seed: u64, system: SystemId, entity: u64, day: Day)` recibe `Day` como cuarto parámetro, garantizando flujos estadísticamente independientes entre días distintos.
- **`e101-commands` (`§ 21`, `ADR 0004`):** Todo `StampedCommand` sella el comando con `day: Day`. La cola de comandos se ordena por `(day, issuer, seq)`.
- **`e101-ledger` (`§ 21`, `Anexo X`):** Cada `CauseEntry` almacena `day: Day` para acotar la ventana circular de los últimos 12 meses (365 días) o 12 cierres mensuales mostrada al jugador en los desgloses causales.
- **`e101-sim` (`§ 04`, `§ 21`, `ADR 0004`):**
  - El bucle diario incrementa `state.today = Day(state.today.0 + 1)` al concluir la Fase 17.
  - Las Fases 0 a 4 (comandos, clima, movimiento, suministro, combate y asedios) se ejecutan todos los días para todas las unidades activas.
  - Las Fases 5 y 6 filtran por `is_weekly_slot(entity.stagger_key(), state.today)`.
  - Las Fases 7 a 14 filtran por `is_monthly_slot(entity.stagger_key(), state.today)`.
- **`e101-content` y `data-build` (`Anexo P`, `Anexo T`):** El compilador de datos convierte fechas literales en archivos RON (`Julian(1300, 1, 1)` o `Gregorian(1582, 10, 15)`) a `Day(i32)` durante `cargo xtask data`, validando que no existan fechas inexistentes (p. ej. `1301-02-29`).
- **`e101-save` (`§ 21`):** La cabecera del archivo `.e101save` incluye `start_day: Day`, `current_day: Day` y el `DisplayCalendarPolicy` preferido por el jugador.

---

## 7. Registro causal

El avance del tiempo en sí no es una variable contable con deltas aditivos, pero `e101-time` interviene en el registro causal (`e101-ledger`) y en la explicabilidad (`§ 22`, `Anexo AM`) de tres formas:

1. **Sello temporal de toda entrada causal:** Cada llamada a `ledger.record(target, source, amount, day)` queda indexada por `day: Day`. Al consultar el desglose de un indicador (p. ej., saldo del tesoro o precio del trigo), el agregador filtra las entradas cuyo `entry.day` cae dentro de la ventana solicitada (`último mes = [today - 30, today]`, `último año = [today - 365, today]`).
2. **Transparencia de la ranura mensual en la UI:** Dado que las entidades se actualizan en su día asignado `monthly_slot_day(key) ∈ 1..=28`, el panel de provincia o de entidad política expone explícitamente el día de cierre mensual (p. ej. *"Cierre contable mensual: día 14 de cada mes | Próximo cierre en 5 días"*) para que el jugador comprenda por qué un cambio en aranceles o impuestos se materializa en esa fecha exacta.
3. **Modificadores estacionales explícitos:** Cuando el clima o la estación (`Season`) alteran la velocidad de movimiento, el desgaste por suministro o el rendimiento agrícola, el sistema correspondiente registra en `e101-ledger` una causa explícita (`CauseSource::Season(Season::Winter)`), nunca un factor oculto.

---

## 8. Interfaz de usuario

De acuerdo con `§ 04` (líneas 1029–1043) y `§ 22`:

1. **Reloj de la barra superior:**
   - Muestra la fecha actual formateada mediante `today.to_display(active_calendar)`, el indicador del calendario activo (`[Jul.]`, `[Greg.]`, `[Hég.]`, `[Biz.]`), la estación climática de la capital del jugador y el selector de velocidad (`Pausa`, `1×`..`5×`).
   - Al pasar el cursor sobre la fecha (*tooltip*), se despliega la equivalencia simultánea en los demás calendarios históricos (`Juliano`, `Gregoriano`, `Hégira`, `Bizantino`), el día absoluto (`Día 474.456`) y el tick de partida (`Tick 0`).
2. **Opciones de preferencia del jugador (`DisplayCalendarPolicy`):**
   - **Histórico dinámico (por defecto):** Muestra el calendario juliano desde 1300 y conmuta al gregoriano cuando la entidad del jugador (o la tradición confesional/cultural de su capital) adopta la reforma a partir de octubre de 1582; permite además mostrar entre paréntesis el calendario cultural (`Hijri` o `Byzantine`) para entidades islámicas u ortodoxas orientales.
   - **Siempre gregoriano (proléptico):** Muestra `CalendarKind::Gregorian` durante toda la campaña.
   - **Siempre juliano:** Muestra `CalendarKind::Julian` durante toda la campaña.
3. **Pausa automática configurable:** El cliente consulta los eventos emitidos en el `Day` actual para pausar automáticamente ante declaraciones de guerra, batallas iniciadas, muerte del gobernante o decisiones críticas de situaciones históricas (`§ 04`, línea 1043).

---

## 9. Pruebas y escenarios

Las pruebas del crate `e101-time` (`cargo xtask test e101-time`, tarea `T-102` del `Anexo W`) son bloqueantes en CI y comprenden:

1. **Pruebas unitarias de vectores históricos conocidos (`Anexo X`):**
   - `Day::from_gregorian(1, 1, 1) == Day(0)` y `Day(0).weekday() == 0` (lunes).
   - `Day::from_gregorian(1300, 1, 1) == Day(474_448)`.
   - `Day::from_julian(1300, 1, 1) == Day(474_456)` y `Day(474_456).to_display(CalendarKind::Gregorian) == DisplayDate { year: 1300, month: 1, day: 9, calendar: CalendarKind::Gregorian }`.
   - Verificar que `1300-02-29` juliano (`Day::from_julian(1300, 2, 29)`) equivale a `1300-03-08` gregoriano (`Day(474_514)`).
   - Continuidad de la reforma de 1582:
     `Day::from_julian(1582, 10, 4) + 1 == Day::from_gregorian(1582, 10, 15)` (`Day(577_734)` jueves -> `Day(577_735)` viernes).
   - `Day::from_gregorian(2060, 1, 1) == Day(752_035)`.
   - Verificación de épocas culturales: `Day(227_014).to_display(CalendarKind::Hijri) == (1, 1, 1)` y `Day::from_julian(1300, 9, 1).to_display(CalendarKind::Byzantine) == (6809, 9, 1)`.
2. **Pruebas de propiedades (*property-based tests* con `proptest`):**
   - Ida y vuelta (`round-trip`) exhaustiva de `from_gregorian <-> to_display(Gregorian)` y `from_julian <-> to_display(Julian)` en el intervalo de años `-5000..=5000` (más de $3{,}65 \times 10^6$ días).
   - Monotonía estricta de `to_display` para los cuatro calendarios en días consecutivos `d` y `d + 1`.
3. **Pruebas del invariante `QA-CORE-06` (escalonamiento sin omisiones ni duplicados):**
   - Para $10\,000$ claves `key` generadas (tanto secuenciales `0..10_000` como aleatorias con semilla fija) y para todos los meses entre `1300-01` y `1600-12` (incluyendo años bisiestos y seculares como 1300, 1400, 1500 y 1600), comprobar que cada clave activa `is_monthly_slot(key, day)` **exactamente 1 vez por mes** y que `is_weekly_slot(key, day)` se activa **exactamente 1 vez por cada bloque de 7 días**.
   - Prueba $\chi^2$ / cotas de dispersión sobre las 28 ranuras mensuales y 7 semanales para garantizar que el desvío máximo respecto a la media teórica es $< 5\,\%$ con $N = 3\,500$ provincias (`§ 04`).

---

## 10. Preguntas abiertas

- **Abierto (`TIME-Q1` — Transición del calendario de presentación tras 1582):** Cuando el jugador elige la política de visualización *"Histórico dinámico"*, ¿el cambio visual del reloj de la interfaz de juliano a gregoriano a partir de octubre de 1582 debe activarse automáticamente según una tabla de fechas históricas por cultura/confesión, o debe vincularse a una decisión/evento de la situación *Reforma del calendario* en `101 History` (permitiendo que una potencia católica u ortodoxa alternativa acepte o rechace la bula en su partida)?
  - *Comportamiento provisional en Fase 0–2:* En la vertical de Tesalia (1300–1350) todas las fechas son previas a 1582, por lo que la política histórica muestra el calendario juliano (con opción bizantina en el *tooltip*). Para escenarios posteriores a 1582 se aplicará inicialmente una fecha de corte por tradición confesional de la entidad, sujeta a sustitución por un disparador de `e101-history` cuando se especifique el contenido de la Edad Moderna.
