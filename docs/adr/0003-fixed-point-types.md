# ADR 0003: Aritmética en punto fijo decimal (`Money`, `Qty`, `Ratio`), redondeo y funciones tabuladas

- **Estado:** propuesto
- **Fecha:** 2026-10-24
- **Autoría:** Agente de Arquitectura (`role:architecture`) — tarea T-007
- **Relacionado con:** Documento maestro v0.7 §§ 09, 10, 22, 23, 46; Anexo B (D-008, D-016, D-019); Anexo P (T-007, T-104); Anexo W; Anexo X; Anexo AC; Anexo AI; ADR 0002; `docs/specs/fixed-point.md`

## Contexto

El primer principio innegociable de **101 Engine** es el **determinismo bit a bit** entre plataformas (`x86_64` y `aarch64`, Windows, Linux y macOS), complementado por el principio de **contabilidad exacta**, según el cual ningún bien, persona o unidad monetaria aparece ni desaparece sin una regla registrada (Documento maestro v0.7 §§ 09, 10, 22, 23; Anexo B D-008).

El uso de tipos en coma flotante IEEE 754 (`f32`, `f64`) en el estado persistente o en la lógica de simulación compromete ambos principios:

1. **Divergencia entre arquitecturas y compiladores:** diferencias en instrucciones FMA (*fused multiply-add*), ancho de registros intermedios, reordenamiento algebraico o implementaciones de la biblioteca matemática estándar (`libm` para `powf`, `exp`, `ln`) pueden alterar el bit menos significativo y amplificarse exponencialmente a lo largo de cientos de años de simulación (§ 22, § 23).
2. **Inexactitud contable en base 2:** fracciones decimales omnipresentes en el diseño económico y demográfico ($0{,}10$, $0{,}01$, $0{,}001$, $0{,}0008$) no tienen representación finita en coma flotante binaria, provocando deriva acumulada en balances de tesorería, existencias de mercados y sumas de cuotas que deben conservar invariantes exactos (§ 09, § 10).
3. **Riesgo de errores dimensionales:** operar con un único tipo numérico genérico permite errores semánticos como sumar unidades monetarias con toneladas de grano o interpretar un porcentaje como cantidad absoluta.

Por ello, el Documento maestro (§ 22; Anexo B D-008; Anexo X) y el ADR 0002 prohíben `f32` y `f64` en todos los crates de simulación y delegan en `e101-store::fixed` la provisión de tipos de punto fijo decimal con reglas de redondeo, desbordamiento y evaluación no lineal completamente especificadas.

## Decisión

Se adopta en el módulo `e101_store::fixed` una aritmética propia en **punto fijo decimal (base 10)** compuesta por tres *newtypes* con semántica de dominio (`Money`, `Qty`, `Ratio`), redondeo bancario (*half-to-even*) sobre intermedios `i128`, política explícita de desbordamiento y funciones no lineales basadas en tablas deterministas.

### 1. Los tres tipos de punto fijo en `e101-store::fixed`

Siguiendo las secciones §§ 09, 10, 22, las decisiones D-008 y D-016 (Anexo B) y el contrato del Anexo X, se definen tres tipos con representación transparente (`#[repr(transparent)]`) y orden total determinista:

| Tipo | Representación interna | Factor de escala ($S$) | Decimales implícitos | Unidad base ($1{,}0$) | Resolución mínima ($1\text{ ulp}$) | Rango representable |
| --- | --- | --- | --- | --- | --- | --- |
| `Money(i64)` | `i64` | $S_{\text{Money}} = 10\,000$ | 4 | $1\text{ uc}$ ($10\,000$) | $0{,}0001\text{ uc}$ | $\pm 922\,337\,203\,685\,477{,}5807\text{ uc}$ ($\approx \pm 9{,}22 \times 10^{14}\text{ uc}$) |
| `Qty(i64)` | `i64` | $S_{\text{Qty}} = 1\,000$ | 3 | $1\text{ ud.}$ ($1\,000$) | $0{,}001\text{ ud.}$ | $\pm 9\,223\,372\,036\,854\,775{,}807\text{ ud.}$ ($\approx \pm 9{,}22 \times 10^{15}\text{ ud.}$) |
| `Ratio(i32)` | `i32` | $S_{\text{Ratio}} = 10\,000$ | 4 ($1\text{ pb}$) | $100\,\%$ ($10\,000\text{ pb}$) | $0{,}0001$ ($1\text{ pb} = 0{,}01\,\%$) | $\pm 214\,748{,}3647$ ($\pm 2\,147\,483\,647\text{ pb}$) |

#### 1.1. `Money(i64)` — Valor monetario (4 decimales implícitos)
- **Definición de dominio:** $1\text{ unidad} = 1\text{ uc}$ (unidad de cuenta interna del motor, equivalente a $3{,}5\text{ g}$ de oro fino al inicio de 1300 según D-016 y § 10). La conversión a monedas históricas visibles para el jugador (ducados, florines, dinares, libras esterlinas) ocurre exclusivamente en la capa de presentación.
- **Justificación de los 4 decimales ($S_{\text{Money}} = 10\,000$):** Permite representar sin pérdida de precisión costes unitarios fraccionarios por unidad-kilómetro definidos en el catálogo de parámetros (Anexo AI), como el coste de transporte marítimo `eco.transport.sea = 0,0008 uc/(ud.·km)` ($8\text{ ulp}$), fluvial `eco.transport.river = 0,0032 uc/(ud.·km)` ($32\text{ ulp}$), por calzada `eco.transport.road = 0,0120 uc/(ud.·km)` ($120\text{ ulp}$) y por acémila `eco.transport.pack = 0,0200 uc/(ud.·km)` ($200\text{ ulp}$), así como salarios e impuestos sobre cohortes pequeñas.
- **Justificación de `i64`:** El rango de $\pm 9{,}22 \times 10^{14}\text{ uc}$ previene desbordamientos en tesorerías imperiales, deuda soberana acumulada y agregados de PIB mundial desde 1300 hasta 2060+. El signo permite representar saldos netos, déficits y deltas contables (`Deltas`).

#### 1.2. `Qty(i64)` — Cantidades físicas y demográficas (3 decimales implícitos)
- **Definición de dominio:** Representa existencias y flujos físicos de los 28 bienes del motor (toneladas, quintales, hectolitros, lotes; § 10) y tamaños de población por cohorte (personas; § 09).
- **Justificación de los 3 decimales ($S_{\text{Qty}} = 1\,000$):** Cumple la especificación demográfica de § 09 (*«una cohorte puede tener 1.234,567 personas internamente, aunque la interfaz redondee»*), evitando que cohortes minoritarias o flujos mensuales de migración, nacimientos y consumo per cápita se trunquen a cero en asentamientos pequeños.
- **Justificación de `i64`:** Soporta desde mili-unidades hasta $\approx 9{,}22 \times 10^{15}$ unidades, holgadamente por encima de la población mundial o el volumen global de cualquier mercancía.

#### 1.3. `Ratio(i32)` — Tasas, proporciones y multiplicadores en puntos básicos (4 decimales implícitos)
- **Definición de dominio:** Expresa proporciones adimensionales en **puntos básicos** ($\text{pb}$), donde $10\,000\text{ pb} = 1{,}0 = 100\,\%$ y $1\text{ pb} = 0{,}01\,\% = 0{,}0001$ (Anexo X).
- **Casos de uso principales:**
  - Cuotas que forman particiones de la unidad, como las tres franjas de edad de cada cohorte (`age_share: [Ratio; 3]`, cuya suma invariante es $10\,000\text{ pb}$, § 09) o el poder relativo de los grupos de interés ($\sum_g \text{poder}_g = 10\,000\text{ pb}$, § 11).
  - Índices acotados, como el nivel de vida (`living_standard: Ratio` en el rango $0\text{–}30\,000\text{ pb}$, donde $10\,000\text{ pb}$ es subsistencia digna, § 09).
  - Multiplicadores de precios y límites de mercado, como `MAX_FACTOR = Ratio::from_bp(100_000)` ($10\times$ el precio base) y `MIN_FACTOR = Ratio::from_bp(2_000)` ($0{,}2\times$) en el Anexo W.
  - Tasas pequeñas del Anexo AI, como la tasa base de conversión religiosa `rel.conversion.base = 0,0003` ($3\text{ pb}$ mensuales), el coeficiente de fuego en combate `war.fire.coefficient = 0,0008` ($8\text{ pb}$) o el desgaste militar base `war.attrition.base = 0,02` ($200\text{ pb}$).
- **Justificación de `i32`:** Con $\pm 2\,147\,483\,647\text{ pb}$ ($\approx \pm 214\,748\times$), ofrece rango de sobra para cualquier multiplicador o tasa manteniendo una huella de 4 bytes en componentes densos (`Cohort`, `MarketState`).

---

### 2. Regla de redondeo: *half-to-even* (redondeo bancario) y conservación en repartos

Para evitar el sesgo sistemático al alza o a la baja a lo largo de miles de ticks semanales y mensuales, **toda operación que divide o reduce factor de escala utiliza redondeo al par más cercano (*round half-to-even* / redondeo bancario)** sobre aritmética entera de 128 bits (Anexo X).

#### 2.1. Algoritmo general de escalado y división
En operaciones cruzadas como:
- `Money::scale(self, r: Ratio) -> Money`: $\text{round\_hte}\!\left(\frac{\text{self.0 as i128} \times \text{r.0 as i128}}{10\,000}\right)$
- `Qty::scale(self, r: Ratio) -> Qty`: $\text{round\_hte}\!\left(\frac{\text{self.0 as i128} \times \text{r.0 as i128}}{10\,000}\right)$
- `Ratio::mul_ratio(self, other: Ratio) -> Ratio`: $\text{round\_hte}\!\left(\frac{\text{self.0 as i128} \times \text{other.0 as i128}}{10\,000}\right)$
- Valoración monetaria `Qty::valuation(self, unit_price: Money) -> Option<Money>`: dado que `Qty` tiene escala $1\,000$ y `Money` tiene escala $10\,000$, el importe total es $\text{round\_hte}\!\left(\frac{\text{qty.0 as i128} \times \text{price.0 as i128}}{1\,000}\right)$.

Sea $N \in \texttt{i128}$ el numerador y $D > 0$ el divisor ($D \in \texttt{i128}$). Se calculan el cociente truncado hacia cero $q = N / D$ y el resto $rem = N \bmod D$:

1. Si $|rem| \times 2 < D$: el resultado es $q$.
2. Si $|rem| \times 2 > D$: el resultado se aleja de cero ($q + \operatorname{sgn}(rem)$).
3. Si $|rem| \times 2 == D$ (empate exacto en $,5$): se elige el entero par más cercano; si $q \bmod 2 == 0$ se devuelve $q$, y en caso contrario $q + \operatorname{sgn}(rem)$.

#### 2.2. Conservación exacta en repartos de suma fija
El redondeo independiente de cada término en un reparto proporcional puede dejar un residuo de $\pm 1\text{–}k\text{ ulp}$. En virtud del principio de contabilidad exacta (§§ 09, 10, 11), cuando un total $T$ debe repartirse entre $n$ partidas según pesos o cuotas $(w_0, w_1, \dots, w_{n-1})$ cuya suma debe igualar exactamente $T$ (por ejemplo: normalización de `age_share` a $10\,000\text{ pb}$ en § 09, normalización de poder político a $10\,000\text{ pb}$ en § 11, o distribución de recaudación/valor añadido entre salarios, rentas de élite e impuestos en § 10):

1. Se calcula cada parte inicial $p_i$ mediante redondeo *half-to-even*.
2. Se calcula el residuo $\Delta = T - \sum_{i=0}^{n-1} p_i$.
3. Si $\Delta \neq 0$, se asigna deterministamente al componente de mayor peso bruto $w_i$ (y en caso de empate en peso bruto, al de **menor índice o `EntityId`**).

---

### 3. Política de desbordamiento

Siguiendo la tarea T-104 (Anexo P), el Anexo X y la especificación de pruebas de propiedades (§ 46):

1. **Prohibición absoluta de desbordamiento silencioso (`wrapping`):** Ningún tipo de `e101-store::fixed` implementa aritmética modular (`wrapping_add`, `wrapping_mul`). Los operadores aritméticos estándar (`+`, `-`, `*`, `/`) no se exponen de forma que puedan ocultar un desbordamiento en compilaciones `release`.
2. **APIs públicas `checked_*` por defecto para contabilidad y estado:**
   - Las operaciones de suma, resta y multiplicación/división por escalar (`checked_add`, `checked_sub`, `checked_mul_i64`, `checked_div_i64`, `checked_valuation`) devuelven `Option<Self>` (o `Result<Self, FixedPointError>`).
   - Los sistemas que registran asientos en `e101-ledger` o acumulan deltas en `State` deben propagar o manejar explícitamente cualquier condición de fuera de rango; en invariantes internos donde un desbordamiento indique un defecto de programación o datos corruptos, el fallo es ruidoso y determinista.
3. **Promoción obligatoria a `i128` en productos y cocientes:**
   - `Money::scale(Ratio)`, `Qty::scale(Ratio)`, `Ratio::mul_ratio(Ratio)`, `Qty::valuation(Money)` y `Ratio::from_quotient(Qty, Qty)` promocionan ambos operandos a `i128` antes de multiplicar, garantizando que nunca ocurra desbordamiento en el producto intermedio mientras el resultado final quepa en el tipo de destino (`checked_scale` devuelve `None` si el cociente redondeado excede `i64::MAX`/`i64::MIN`).
4. **APIs `saturating_*` y `clamp` restringidas y documentadas:**
   - Solo se permiten operaciones saturantes o acotadas allí donde el modelo matemático del documento maestro define explícitamente un techo o suelo:
     - `Ratio::from_quotient(num: Qty, den: Qty) -> Ratio`: marcado explícitamente como `// saturating` en el Anexo X; calcula $\text{round\_hte}((\text{num} \times 10\,000) / \text{den})$ y satura en `Ratio::MAX` / `Ratio::MIN` (combinado en economía con un denominador mínimo `supply.max(Qty::ONE)`, Anexo W).
     - `clamp(min, max)`: utilizado en el ajuste semanal de precios para limitar el cambio semanal a $\pm 10\,\%$ y el factor de precio al intervalo $[0{,}2\times, 10\times]$ (`MIN_FACTOR..=MAX_FACTOR`, Anexo W), así como en índices acotados (`living_standard` en $[0, 30\,000]\text{ pb}$, § 09).

---

### 4. Tablas para funciones no lineales (`e101-store::fixed::tables`)

Queda prohibido invocar funciones trascendentes o irracionales en coma flotante (`f32::powf`, `f64::exp`, `f64::ln`, `f64::sqrt`). Todas las relaciones no lineales del motor se resuelven en `e101-store::fixed::tables` mediante cuatro mecanismos deterministas con interpolación lineal entera y redondeo *half-to-even* (§ 09, § 23, Anexo B D-019, Anexo AC):

#### 4.1. Conversión de tasa anual a tasa mensual ($1 - (1 - r_{\text{año}})^{1/12}$)
- **Uso en el dominio:** Demografía mensual (§ 09, línea 2192), para aplicar natalidad y mortalidad anuales sin error de capitalización: $r_{\text{mes}} = 1 - (1 - r_{\text{año}})^{1/12}$.
- **Mecanismo:** Tabla estática `ANNUAL_TO_MONTHLY_TABLE` precalculada en tiempo de compilación para $r_{\text{año}} \in [0, 10\,000]\text{ pb}$ con paso uniforme de $10\text{ pb}$ ($1\,001$ nodos almacenados en unidades de $10^{-7}$, es decir, milésimas de punto básico, en `i32`). Para cualquier `r_annual: Ratio` intermedio, se interpola linealmente entre los dos nodos adyacentes con redondeo *half-to-even*.

#### 4.2. Decaimiento exponencial por semivida ($2^{-\Delta t / t_{1/2}}$)
- **Uso en el dominio:** Decaimiento temporal de agravios diplomáticos y treguas rotas (semividas de 10 y 20 años, § 12), memoria de impagos soberanos (semivida de 15 años, § 10), prestigio por victorias/derrotas y penalización de legitimidad por usurpación (§ 11), y agravios de cohortes por represión (semivida de 10 años, § 11).
- **Mecanismo:** Dado el tiempo transcurrido $\Delta t \ge 0$ y la semivida $t_{1/2} > 0$ (en las mismas unidades temporales, días o meses):
  1. Se descompone el exponente en parte entera $k = \lfloor \Delta t / t_{1/2} \rfloor$ y resto $r = \Delta t \bmod t_{1/2}$. Si $k \ge 63$, el factor es $0$.
  2. La fracción $u = r / t_{1/2} \in [0, 1)$ se proyecta al índice fraccionario de una tabla estática `EXP2_NEG_TABLE: [i32; 257]` que almacena $2^{-i/256} \times 10\,000$ redondeado al entero más cercano para $i \in 0..=256$.
  3. Se obtiene el factor fraccionario $f \in [5\,000, 10\,000]\text{ pb}$ por interpolación lineal *half-to-even* en la tabla y se aplica la reducción exacta de las $k$ semividas completas dividiendo por $2^k$ con redondeo *half-to-even* ($\text{round\_hte}(f, 2^k)$).

#### 4.3. Raíz cuadrada entera y en punto fijo (`isqrt` / `sqrt_ratio`)
- **Uso en el dominio:** Cálculos de distancia euclídea sobre el grafo espacial cuando se requieren en preprocesado o heurísticas, y normalizaciones sublineales.
- **Mecanismo:** Basado exclusivamente en la raíz cuadrada entera determinista `u128::isqrt()` / `i128::isqrt()` de la biblioteca estándar de Rust. Para `sqrt_ratio(r: Ratio) -> Ratio` (con $r \ge 0$), dado que $\sqrt{r / 10\,000} = \sqrt{r \times 10\,000} / 10\,000$, se evalúa sobre `u128` con escalado previo para obtener el resultado en puntos básicos con redondeo *half-to-even*.

#### 4.4. Tablas por tramos definidas en datos (`PiecewiseTable`, D-019)
- **Uso en el dominio:** Todas las curvas empíricas de respuesta de los sistemas de simulación, incluyendo en demografía (§ 09) `f_vida(nivel_vida)`, `g_alimentos(acceso_alimentos)`, `f_paz(en_guerra)` y `h_crianza(nivel_vida)`, así como curvas de eficiencia administrativa, fatiga bélica y precios en `games/epoch/data/rules/*.ron`.
- **Mecanismo:** Estructura `PiecewiseTable` compuesta por una lista estrictamente creciente de nodos `(x_i: Ratio, y_i: Ratio)` validada al compilar los datos (`cargo xtask data`). Para una entrada $x$:
  - Si $x \le x_0$, devuelve $y_0$ (*clamp* inferior).
  - Si $x \ge x_{n-1}$, devuelve $y_{n-1}$ (*clamp* superior).
  - Si $x_i \le x \le x_{i+1}$, devuelve $y_i + \text{round\_hte}((y_{i+1} - y_i) \times (x - x_i), x_{i+1} - x_i)$ usando intermedios `i128`.

---

### 5. Por qué se descarta el crate externo `fixed`

De acuerdo con la justificación arquitectónica de § 22 (línea 4898 del Documento maestro):

1. **Base 2 frente a base 10:** El crate `fixed` utiliza escalas binarias ($2^{-k}$). En base 2, constantes centrales del diseño como $0{,}10$ ($10\,\%$), $0{,}01$ ($1\,\%$), $0{,}001$ ($1\text{ kg}$ en toneladas) o $0{,}0008\text{ uc}$ son fracciones periódicas inexactas. Esto dificulta la verificación manual de los ejemplos numéricos resueltos del documento maestro (como el mercado de trigo de Tesalia en el Anexo W o el ciclo demográfico en § 09) y complica la auditoría de invariantes contables en base 10.
2. **Seguridad de tipos por dominio:** Un tipo genérico `FixedI64<Frac>` no distingue entre dinero, masa física y tasas adimensionales si comparten número de bits fraccionarios (por ejemplo, `Money` y `Ratio` tienen ambos 4 decimales implícitos). Tres *newtypes* distintos (`Money`, `Qty`, `Ratio`) hacen imposible en tiempo de compilación sumar dinero con población o multiplicar dos precios sin pasar por las firmas semánticas (`Qty::valuation(Money) -> Money`, `Money::scale(Ratio) -> Money`).
3. **Cero dependencias externas y control total:** La implementación completa de `e101-store::fixed` requiere ~300 líneas de Rust puro sin `unsafe`, evita introducir una dependencia externa (sujeta a aprobación `new-dependency`), garantiza serialización trivial en little-endian (`to_le_bytes()`) para el hash canónico BLAKE3 (ADR 0004) y asegura que el redondeo *half-to-even* sea idéntico en todas las operaciones.

## Alternativas consideradas

| Alternativa | Ventajas | Inconvenientes |
| --- | --- | --- |
| **1. Tres *newtypes* decimales propios (`Money(i64)`, `Qty(i64)`, `Ratio(i32)`) con intermedios `i128` y tablas (Elegida)** | Exactitud en base 10; seguridad dimensional en compilación; determinismo bit a bit; correspondencia 1:1 con fórmulas y ejemplos del documento maestro; cero dependencias externas (~300 líneas). | Requiere escribir las operaciones aritméticas, el redondeo *half-to-even* y las tablas de interpolación en `e101-store::fixed`. |
| **2. Crate externo `fixed` (punto fijo binario $2^{-k}$)** | Implementación madura de operadores y rasgos numéricos en el ecosistema Rust. | Fracciones decimales ($0{,}1$, $0{,}01$, $0{,}0008$) inexactas en base 2; no distingue semánticamente `Money`, `Qty` y `Ratio`; añade dependencia externa innecesaria (§ 22). |
| **3. Coma flotante IEEE 754 (`f32` / `f64`) con flags estrictos del compilador** | Escritura directa de expresiones algebraicas y funciones `powf`/`exp` estándar. | Viola la regla de determinismo multiplataforma (§ 22, § 23) y el principio de contabilidad exacta por errores de representación binaria y diferencias en `libm`/FMA. |
| **4. Punto fijo de 128 bits (`i128`) para todos los campos almacenados** | Rango prácticamente infinito sin necesidad de promociones al multiplicar. | Duplica el tamaño en memoria de componentes críticos (`Cohort`, `MarketState`), degradando la localidad de caché (SoA) y el presupuesto de rendimiento del tick (§ 24). |
| **5. Redondeo por truncamiento hacia cero o *half-away-from-zero*** | Implementación ligeramente más simple (una comparación menos en el caso de empate $,5$). | El truncamiento introduce sesgo sistemático hacia cero (pérdida continua de valor/población); *half-away-from-zero* introduce deriva positiva en empates frecuentes en escala decimal. |

## Consecuencias

### Positivas
- **Determinismo garantizado:** Toda la aritmética del núcleo utiliza exclusivamente enteros con signo (`i32`, `i64`, `i128`) y desplazamientos/divisiones enteras, produciendo el mismo resultado bit a bit en cualquier CPU y sistema operativo.
- **Trazabilidad y auditoría:** Los valores almacenados en memoria, volcados en el *ledger* causal (`e101-ledger`) o inspeccionados en pruebas doradas son directamente legibles en base 10 ($12\,345$ en `Qty` es exactamente $12{,}345$; $10\,000$ en `Ratio` es exactamente $100{,}00\,\%$).
- **Imposibilidad de errores dimensionales:** El sistema de tipos de Rust impide mezclar accidentalmente unidades monetarias, cantidades físicas y razones adimensionales.
- **Curvas modificables por diseño de contenido:** Las funciones empíricas (`PiecewiseTable`, D-019) viven en archivos RON validados, permitiendo calibrar la simulación en 101 Lab sin recompilar el motor.

### Negativas y compromisos
- **Verbosidad en las fórmulas de simulación:** Los sistemas en `e101-sim` no pueden escribir expresiones infijas libres con literales flotantes; deben encadenar métodos explícitos (`qty.scale(ratio)`, `qty.checked_valuation(price)`, `checked_add`) y gestionar el retorno `Option`/`Result`.
- **Mantenimiento de constructores y pruebas exhaustivas:** Cualquier nueva función no lineal que se incorpore en fases posteriores deberá formularse como tabla precalculada o `PiecewiseTable` y documentarse en `docs/specs/fixed-point.md`.

## Cómo se verifica

1. **Lints estáticos en CI (`cargo xtask check`):**
   - `clippy::float_arithmetic` denegado (`#[deny(clippy::float_arithmetic)]`) en todos los crates de simulación (ADR 0002).
   - Verificación en el AST de `tools/xtask` de que no existen ocurrencias de `f32` ni `f64` en los tipos de estado ni llamadas a métodos `wrapping_*` en `e101-store::fixed`.
2. **Pruebas unitarias de casos límite (`cargo xtask test e101-store`):**
   - Verificación del redondeo *half-to-even* en empates exactos ($,5$ con cociente par e impar, tanto para valores positivos como negativos).
   - Verificación de que `Money::MAX.checked_add(Money::from_raw(1))` devuelve `None` y de que `Money::scale(Money::MAX, Ratio::ONE)` no desborda en el producto intermedio `i128`.
   - Verificación del ejemplo resuelto del mercado de trigo de Tesalia (Anexo W) bit a bit.
3. **Pruebas de propiedades con `proptest` (§ 46, Anexo P T-104):**
   - Conmutatividad de `checked_add`.
   - Identidad multiplicativa: `m.scale(Ratio::ONE) == m` para todo `m: Money` y `q.scale(Ratio::ONE) == q` para todo `q: Qty`.
   - Conservación exacta en repartos: para cualquier total $T$ y vector de pesos positivos, la suma de las partes devueltas por el repartidor con ajuste de residuo es exactamente igual a $T$.
   - Monotonía y acotación de `ANNUAL_TO_MONTHLY_TABLE`, `EXP2_NEG_TABLE`, `sqrt_ratio` y `PiecewiseTable::eval`.
4. **Escenarios dorados (`cargo xtask golden`):**
   - Coincidencia exacta de hashes BLAKE3 entre Linux, Windows y macOS tras 360 días de simulación en los escenarios `01_single_province_economy` y `02_two_province_trade`.
