# Modelo del prototipo económico T-008 (MODEL.md)

Diseño del modelo mínimo de validación del modelo económico del documento maestro
(`docs/master/101_Agents_Games_Documento_Maestro_v0.7.md`, sección 10), para implementar en
**Python 3.12 (solo stdlib + matplotlib)** por un subagente de código, sin releer el maestro.

Fuente numérica única: `docs/specs/prototypes/economy/parameters.md` (extracción del maestro).
Todo valor que ese archivo no traiga se declara como **SUPUESTO** en la sección 12, con su valor
elegido y su justificación. Confianza global D (diseño); la calibración final es de 101 Lab (Anexo F).

Este documento **no** es especificación del motor: es el contrato de un prototipo desechable cuyo
único objetivo es comprobar que la sección 10 del maestro produce un sistema cerrado, estable y
capaz de pasar los criterios numéricos del Anexo F (`economy_closed_100y`, `harvest_shock`,
variación anual ≤ ±25 %).

## 0. Qué modela y qué no

Modela: 5 mercados, 10 bienes, producción estacional con edificios de referencia, consumo por
estratos, algoritmo de precios con existencias de la sección 10, comercio entre los 5 mercados con
coste de transporte, masa monetaria conservada, deterioro en almacén y perturbaciones de cosecha.

No modela (fuera de alcance, documentado como simplificación): demografía (población constante),
Estado e impuestos, crédito e interés, devaluación monetaria, mercados externos (Venecia, Génova,
Alejandría…), salarios por ocupación, inversión privada, nivel de vida (NV) y migración.

---

## 1. Entidades

### 1.1 Bienes (10)

Unidad natural, precio base de la sección 10, peso para transporte y pérdida mensual en almacén
(Tabla 2 de parameters.md). `pb` = puntos básicos (sección 2).

| Bien | ID | Unidad | Precio base | Peso (t/unidad) | Pérdida mensual |
| --- | --- | --- | --- | --- | --- |
| Grano | `grano` | tonelada (t) | 9 uc/t | 1 | 1 % |
| Pescado (salado) | `pescado` | tonelada (t) | 25 uc/t | 1 | 2 % |
| Sal | `sal` | tonelada (t) | 20 uc/t | 1 | 0 % |
| Aceite de oliva | `aceite` | hectolitro (hl) | 3 uc/hl | 0,09 | 0,5 % |
| Vino | `vino` | hectolitro (hl) | 2 uc/hl | 0,1 | 1 % |
| Lana | `lana` | quintal (q = 50 kg) | 4 uc/q | 0,05 | 0,5 % |
| Paño común | `pano` | pieza (~30 m) | 6 uc/pieza | 0,03 | 0,2 % |
| Hierro en barras | `hierro` | quintal (q) | 2,5 uc/q | 0,05 | 0,1 % |
| Madera | `madera` | tonelada (t) | 1,5 uc/t | 1 | 0,5 % |
| Leña | `lena` | tonelada (t) | 1,2 uc/t | 1 | 0,5 % |

Decisiones: (a) "pescado" es el **pescado salado** (25 uc/t, pérdida 2 %/mes): el fresco (15 uc/t,
20 %/mes) exige consumo intrasemanal y rompería el paso mensual; Caffa exporta pescado salado
(Anexo AK). (b) El bien de cesta "tejido basto" (0,2 uc/unidad ≈ 1 m²) se representa con `pano`:
**1 pieza = 30 unidades de tejido** (SUPUESTO S4; verificado contra la comprobación del maestro:
0,15 unidades/mes × 6 uc/30 = 0,03 uc/mes, exactamente el valor que el maestro atribuye al tejido
en la cesta de 0,23 uc). (c) El alumbre y los tintes del taller textil se ignoran (S22).

### 1.2 Mercados (5)

Población (Anexo AK), reparto por estratos (SUPUESTO S1: 80 % bajo / 15 % medio / 4,5 % alto /
0,5 % élite) y precio inicial del grano (Anexo AK). El resto de bienes arranca al precio base.

| Mercado | Población | Bajo | Medio | Alto | Élite | Grano inicial | Grano base (cotas) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Constantinopla | 100.000 | 80.000 | 15.000 | 4.500 | 500 | 10,5 uc/t | 9 uc/t |
| Tesalónica | 40.000 | 32.000 | 6.000 | 1.800 | 200 | 8,5 uc/t | 9 uc/t |
| Caffa | 20.000 | 16.000 | 3.000 | 900 | 100 | 6,5 uc/t | 9 uc/t |
| Bursa | 15.000 | 12.000 | 2.250 | 675 | 75 | 9,0 uc/t | 9 uc/t |
| Candía | 25.000 | 20.000 | 3.750 | 1.125 | 125 | 8,5 uc/t | 9 uc/t |

Todas las poblaciones y todos los estratos son enteros; con las tasas de consumo por persona de la
sección 5 (todas enteras en pb) **toda demanda mensual es un entero exacto en pb**. El código lo
comprueba con `assert` al inicializar.

Cada mercado es un nodo con: `stock[good]` (pb), `precio[good]` (m/u), `dinero_hogares` (m),
`dinero_mercado` (m), `carry_demanda[good]` (pb, para semanalizar la demanda, sección 6).

### 1.3 Rutas (5)

Grafo conexo. Distancias y medios (SUPUESTO S12; "mixto" = tramo marítimo + tramo de carretera):

| Ruta | Km por medio | Coste grano (1 t) |
| --- | --- | --- |
| Constantinopla – Tesalónica | 500 mar | 0,40 uc/t |
| Constantinopla – Caffa | 700 mar | 0,56 uc/t |
| Constantinopla – Candía | 700 mar | 0,56 uc/t |
| Tesalónica – Candía | 900 mar | 0,72 uc/t |
| Constantinopla – Bursa | 200 mar + 100 carretera | 0,16 + 1,20 = 1,36 uc/t |

Costes por medio (Anexo AI): mar 0,0008 uc/t·km, carretera 0,012 uc/t·km, río 0,0032, animales
0,020 (definidos en CONSTANTES por si se añaden rutas). El coste de una ruta se calcula por tramo:
`coste = Σ (km_tramo × coste_medio) × peso_t(unidad_del_bien)`, en m.

Capacidad (SUPUESTO S13): 250 t de carga/semana por ruta marítima, 50 t/semana por carretera;
de noviembre a febrero la capacidad marítima se reduce a la mitad (maestro: −50 % nov–feb).
Capital mercantil por ruta y semana: 5.000 uc (S14).

Prima de riesgo (maestro: `valor_carga × (piratería + meteorológico)`, SUPUESTO S15): piratería
2 % del valor por tramo marítimo (Egeo, rango del maestro 1–4 %), ×2 en noviembre–febrero;
meteorológico 1 % (abril–septiembre) o 6 % (octubre–marzo), todos los tramos. La ruta mixta aplica
la piratería solo a la fracción marítima de los km (Constantinopla–Bursa: 2/3).

---

## 2. Aritmética entera y redondeos

Igual que el motor: **ningún float en el estado**. Todos los importes, cantidades y precios son
`int`. Los floats solo aparecen como variables locales sin persistir, en dos sitios: la presión y
la cantidad que iguala precios (secciones 6 y 7).

- **Dinero**: en **milésimas de uc** (m). 1 uc = 1000 m.
- **Cantidades**: en **puntos básicos** (pb) = milésimas de la unidad natural. 1 t = 1000 pb,
  1 hl = 1000 pb, 1 quintal = 1000 pb, 1 pieza = 1000 pb. Para los bienes en toneladas 1 pb = 1 kg,
  lo que hace enteras las tasas de consumo (16 kg = 16 pb, 0,5 kg sal = 0,5 pb…).
- **Precios**: en **m por unidad natural** (m/u), NO por pb. Motivo: los precios base 1,2 / 1,5 /
  2,5 uc no dan enteros en m/pb (1,2 m/pb), mientras que en m/u todos los base son enteros:
  `precio_m_u = precio_uc × 1000`. Un cambio de 1 m/t en el grano es un 0,011 %: resolución de
  sobra para pasos semanales del ±10 % máximo. La equivalencia m/pb pedida en la tarea sería 1000
  veces más gruesa (1 m/pb = 11 % de salto en el grano) y rompería la suavidad del algoritmo.

### 2.1 Conversión de precios base a m/u

| Bien | m/u base | Cotas (0,2× / 10×) |
| --- | --- | --- |
| grano | 9000 | 1800 – 90000 |
| pescado | 25000 | 5000 – 250000 |
| sal | 20000 | 4000 – 200000 |
| aceite | 3000 | 600 – 30000 |
| vino | 2000 | 400 – 20000 |
| lana | 4000 | 800 – 40000 |
| pano | 6000 | 1200 – 60000 |
| hierro | 2500 | 500 – 25000 |
| madera | 1500 | 300 – 15000 |
| lena | 1200 | 240 – 12000 |

Precios iniciales del grano (Anexo AK) en m/u: Constantinopla 10500, Tesalónica 8500, Caffa 6500,
Bursa 9000, Candía 8500 (todos enteros). Resto de bienes: precio base en los 5 mercados.

### 2.2 Reglas de redondeo (únicas en todo el modelo)

1. **Valor de un lote**: `pago_m = (q_pb × precio_m_u) // 1000` — división entera truncada por
   suelo (// de Python). El comprador paga `pago_m` y el vendedor recibe exactamente `pago_m`: el
   polvo de redondeo es un artefacto del **precio**, nunca una pérdida de dinero.
2. **Producción con factor de cosecha**: `q = q_base × (10000 + δ) // 10000` con δ entero
   (sección 9). Truncamiento por suelo.
3. **Deterioro**: `podrido = stock × pct // 100` (pct entero: 1, 2, 20→no aplica, 0,5→… véase
   2.3). Truncamiento por suelo; lo no podrido sigue en stock.
4. **Ajuste de precio** (única excepción con redondeo al más cercano): δ_i =
   `round(0,10 × presión × 10000)` acotado a [−1000, +1000]; luego
   `precio' = (precio × (10000 + δ_i)) // 10000` (suelo) y acotado a las cotas de la tabla 2.1.
5. **Demanda semanal**: `demanda_sem = (demanda_mensual + carry) // 4`, `carry = (demanda_mensual
   + carry) % 4` — el residuo se acumula en `carry_demanda[good]` y se cobra en las semanas
   siguientes: la suma de las 4 semanas de demanda es exactamente la mensual (necesario para el
   vino de Bursa/Candía, p. ej. 213.750 pb/mes no es divisible entre 4).
6. **Compra parcial por presupuesto**: `q = dinero_restante × 1000 // precio_m_u` (suelo).
   Lo no comprado **permanece en stock**: no viola la conservación (es demanda insatisfecha).
7. **Flujo de comercio**: `q_pb = floor(…)` de cada término del mínimo (sección 7), y además
   `q = min(q, stock_origen)`.

### 2.3 Tasa de deterioro como entero

`pct` mensual entero en **centésimas de %** para permitir 0,5 % y 0,1 %:
`podrido = stock × pct // 10000`, con pct = 100 (1 %) grano y vino, 200 pescado, 50 aceite, lana,
madera y leña, 20 paño, 10 hierro, 0 sal. El truncamiento por suelo puede devolver 0 para stocks
pequeños (< 100 pb con pct 100): aceptable, el stock es grande en el objetivo.

### 2.4 Invariantes que el código comprueba con `assert`

- **Dinero, en cada paso**: `Σ hogares + Σ mercados == MASA_INICIAL` (exacto).
- **Bienes, al cierre de cada año (y de cada paso si se quiere)**, por bien y en el total:
  `producido == consumido + podrido + Δ(Σ stocks) + Δ(en_tránsito)`, con `en_tránsito == 0`
  siempre (sección 7, SUPUESTO S16: tránsito instantáneo). `consumido` incluye consumo de hogares
  e insumos de edificios (lana de los talleres).
- Todo movimiento de dinero es una **transferencia entre carteras** (5 hogares + 5 mercados):
  prohibido sumar o restar de una sola cartera.
- Iteración siempre sobre listas con orden fijo (bienes en el orden de la tabla 1.1, mercados y
  rutas en el orden de las tablas 1.2/1.3); prohibido iterar `set` (los `dict` solo en orden de
  inserción fijo). Sin `random` global: solo `random.Random(semilla_entera)` (sección 9).

---

## 3. Calendario

**SUPUESTO S2 (documentar en el código): el año tiene 12 meses × 4 semanas = 48 semanas.** El
maestro habla de semanas de reserva y pasos semanales/mensuales sin fijar la longitud del año;
48 uniformiza mes = 4 semanas y evita semanas 53. Todas las conversiones anuales usan /48.

Dos pasos por semana y un bloque de cierre mensual:

- **Paso semanal** (todas las semanas): 1) comercio, 2) actualización de precios.
- **Cierre mensual** (tras la 4.ª semana del mes, `semana % 4 == 3`): 1) producción del mes y pago
  a los hogares, 2) consumo de insumos por los edificios, 3) consumo de los hogares y pago,
  4) deterioro en almacén, 5) tarifa de almacenaje, 6) comprobaciones de conservación.

Meses 1–12 = enero–diciembre. Invierno (leña ×1,6 y capacidad marítima −50 %): noviembre–febrero
para la navegación, diciembre–febrero para la leña. Verano meteorológico: abril–septiembre.

Los años se numeran 1..200. El shock de sequía se aplica a la cosecha de grano de Tesalónica del
año 100 (meses 6–7).

---

## 4. Producción

### 4.1 Edificios de referencia y rendimientos

De la sección 10 del maestro ("Edificios de referencia del slice"). El grano es **neto**: el
edificio produce 39 t/año brutos y 13 t/año se reservan como semilla dentro del propio edificio
(sin pasar por el mercado), de modo que al mercado entran **26 t/año netas** por unidad — el
propio maestro usa 26 t netas en su comprobación agraria. Con rotación trienal serían 41 t; no se
usa (una sola tecnología, minimismo).

Edificios sin tabla de rendimiento en el maestro (HUECO 7 de parameters.md) — mina de hierro,
aserradero de madera y carbonería de leña — reciben rendimientos inventados (SUPUESTO S8):
mina de hierro 60 q/año, aserradero 60 t/año, carbonería 300 t/año. La pesquería se aplica a todos
los mercados con la temporada abril–noviembre del mar Negro (HUECO 25, SUPUESTO S9).

| Edificio | Rendimiento anual | Plazas (no se usan, referencia) |
| --- | --- | --- |
| Campos de cereal (100 ha, año y vez) | 26 t grano netas | 25 campesinos |
| Olivar (50 ha) | 45 hl aceite | 12 campesinos |
| Viñedo (30 ha) | 150 hl vino | 15 campesinos |
| Pesquería costera | 25 t pescado | 15 pescadores |
| Salina | 120 t sal | 10 trabajadores |
| Pastos (500 ha) | 30 q lana | 6 pastores |
| Taller textil | 50 piezas paño (consume 60 q lana) | 20 artesanos |
| Mina de hierro (inventado) | 60 q hierro | — |
| Aserradero (inventado) | 60 t madera | — |
| Carbonería (inventado) | 300 t leña | — |

### 4.2 Número de edificios por mercado

Dimensionado para que el **sistema cerrado cuadre bien a bien**: producción ≈ consumo +
deterioro de equilibrio. Para el grano, el deterioro (1 %/mes sobre un stock que oscila alrededor
del objetivo) absorbe un excedente anual de `0,12 × existencias_objetivo`; con
`existencias_obj = 26 × consumo semanal medio = 26 × 38400/48 = 20800 t`, el objetivo de
producción es `38400 + 0,12 × 20800 ≈ 40896 t/año → 1573 edificios de 26 t` (40.898 t). Los
repartos por mercado siguen los roles del Anexo AK (Tesalónica y Caffa exportan grano,
Constantinopla y Bursa importan, Candía exporta poco). En los demás bienes el redondeo deja
desajustes ≤ 1 %, absorbidos por el deterioro o aceptados (solo el grano está calibrado).

| Bien | Constantinopla | Tesalónica | Caffa | Bursa | Candía | Total sistema (año) |
| --- | --- | --- | --- | --- | --- | --- |
| grano (26 t) | 400 | 600 | 260 | 90 | 223 | 1573 ed. → 40.898 t |
| pescado (25 t) | 40 | 20 | 91 | 5 | 22 | 178 ed. → 4.450 t |
| sal (120 t) | 2 | 0 | 7 | 0 | 1 | 10 ed. → 1.200 t (exacto) |
| aceite (45 hl) | 100 | 120 | 21 | 40 | 150 | 431 ed. → 19.395 hl |
| vino (150 hl) | 40 | 60 | 8 | 25 | 100 | 233 ed. → 34.950 hl |
| lana (30 q) | 130 | 240 | 190 | 80 | 95 | 735 ed. → 22.050 q |
| paño (50 piezas) | 175 | 72 | 33 | 36 | 48 | 364 ed. → 18.200 piezas |
| hierro (60 q) | 30 | 20 | 0 | 30 | 0 | 80 ed. → 4.800 q |
| madera (60 t) | 20 | 40 | 20 | 60 | 22 | 162 ed. → 9.720 t |
| leña (300 t) | 30 | 70 | 32 | 60 | 40 | 232 ed. → 69.600 t |

Consumo del sistema (anual, para comparar): grano 38.400 t, pescado 4.272 t, sal 1.200 t, aceite
19.200 hl, vino 34.200 hl, lana 21.840 q (insumo de los talleres), paño 18.120 piezas, hierro
4.800 q, madera 9.600 t, leña 69.000 t. Sal y hierro se producen exactamente lo consumido (sin
deterioro el stock no tiene amortiguador); el resto lleva el margen de deterioro.

### 4.3 Calendario de entrega y reparto dentro de la cosecha

La producción anual de cada edificio se entrega al mercado en **mensualidades fijas** (el maestro
da los meses; el reparto dentro de ellos es SUPUESTO S5: **reparto uniforme entre los meses de
cosecha**, entregado íntegro al final de cada mes):

| Bien | Meses de entrega | Reparto | Base (Anexo AK / maestro) |
| --- | --- | --- | --- |
| grano, Constantinopla/Tesalónica/Candía | jun–jul | 50 % / 50 % | Mediterráneo costero |
| grano, Bursa | jul–ago | 50 % / 50 % | Meseta anatolia |
| grano, Caffa | jul | 100 % | costa del mar Negro |
| aceite | nov, dic, ene | 1/3 cada uno | olivar nov–ene |
| vino | sep, oct | 50 % / 50 % | vid sep–oct |
| pescado | abr–nov | 1/8 cada uno | pesca mar Negro (S9) |
| sal | jul, ago, sep | 1/3 cada uno | salina jul–sep |
| lana | may | 100 % | esquila de primavera (S10) |
| paño | mar, jun, sep, dic | 12,5 piezas (12.500 pb) | continuo, trimestral para dar enteros |
| hierro, madera, leña | todos | 1/12 mensual | continuo |

Todas las mensualidades resultan enteras en pb (comprobar con `assert`): p. ej. Tesalónica grano
junio = 600 × 26.000 pb × 0,5 = 7.800.000 pb; paño trimestral = 12.500 pb por taller.

### 4.4 Pago de la producción y pagos netos

En el cierre mensual, el mercado **paga a sus hogares** la producción entregada:
`pago = Σ_bienes entregado_pb × precio_m_u // 1000`. Los insumos consumidos por los edificios del
mercado (lana de los talleres) se descuentan del pago del edificio correspondiente: el mercado
paga al taller `valor_paño − valor_lana_consumida` (pago **neto**, acotado por debajo a 0). Así el
fondo del mercado no pierde el valor de la lana dos veces y el circuito hogares→mercado→hogares
cierra. Si algún pago neto individual resultara negativo (no ocurre con los precios base: 50
piezas × 6 uc = 300 uc > 60 q × 4 uc = 240 uc), se paga 0 y se anota.

Los fondos de mercado **pueden quedar negativos** (crédito implícito de los hogares al mercado);
la masa monetaria total se conserva igualmente (S18).

### 4.5 Ruido de cosecha

Sección 9: un único factor por mercado y año, aplicado a los bienes biológicos (grano, aceite,
vino, lana, pescado), no a sal, hierro, madera, leña ni paño. Ver sección 9 para la generación.

---

## 5. Consumo

### 5.1 Cestas (por persona y mes, de la sección 09)

**Subsistencia (todos los estratos)**: 16 GE de alimento básico, 0,5 kg sal, 0,8 l aceite,
25 kg leña, 0,15 unidades de tejido. **Comodidad (solo medio, alto y élite)**: 4 GE de pescado,
vino (6/10/15 l para medio/alto/élite), paño (0,3/0,6/0,9 unidades). El estrato bajo no consume
comodidad (S6): comprar comodidad solo si sobra dinero añadiría un feedback no necesario.

Conversiones GE→bien (sección 09):
- grano: 1 GE = 1 kg → **16 kg grano/mes** (el maestro lo confirma: 192 kg/persona/año).
- pescado: 0,45 GE/kg → las 4 GE de comodidad son **8,9 kg pescado/mes** (80/9 = 8,89, redondeado;
  SUPUESTO S7: todo el bloque de comodidad alimentaria del estrato medio se asigna a pescado;
  carne y legumbres no están entre los 10 bienes).
- tejido: 0,15 unidades = **5 pb de paño** (1/30 de pieza, S4); comodidad: medio 10 pb, alto 20 pb,
  élite 30 pb por persona y mes.
- sal 0,5 kg = 0,5 pb; aceite 0,8 l = 8 pb; leña 25 kg = 25 pb (todas las tasas enteras en pb).
- Leña de invierno ×1,6 (maestro): diciembre–febrero 40 kg = 40 pb por persona (S11).
- Los "servicios urbanos" de las cestas medias/altas se ignoran (S6): no hay sector servicios
  salvo la renta de la capital (sección 8), y añadirlos obligaría a definir a quién se pagan.

Cesta mensual por mercado (suma de población × tasas), en unidades naturales:

| Mercado | grano (t) | pescado (t) | sal (t) | aceite (hl) | vino (hl) | leña (t, inv) | paño (piezas) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Constantinopla | 1600 | 178,0 | 50,0 | 800 | 1425,00 | 2500 (4000) | 755,00 |
| Tesalónica | 640 | 71,2 | 20,0 | 320 | 570,00 | 1000 (1600) | 302,00 |
| Caffa | 320 | 35,6 | 10,0 | 160 | 285,00 | 500 (800) | 151,00 |
| Bursa | 240 | 26,7 | 7,5 | 120 | 213,75 | 375 (600) | 113,25 |
| Candía | 400 | 44,5 | 12,5 | 200 | 356,25 | 625 (1000) | 188,75 |

Coste de la cesta a precios base: 0,238 uc/persona/mes para el estrato bajo (el maestro dice
≈ 0,23 ✓), ≈ 0,68 para medio/alto/élite; total del sistema ≈ 65.260 uc/mes. El código calcula la
cesta en m con la regla 2.2.1 y la usa para dimensionar el dinero (sección 8).

### 5.2 Compra mensual con presupuesto (elasticidad mínima)

En el cierre mensual, los hogares de cada mercado compran al mercado local, con su cartera común
`dinero_hogares`, en **orden de prioridad fijo**:

1. grano (subsistencia) → 2. sal → 3. aceite → 4. leña → 5. paño (subsistencia + comodidad
   juntos) → 6. pescado (comodidad) → 7. vino (comodidad) → 8. hierro → 9. madera (demanda
   artesanal, 5.3).

Para cada bien, en orden: `q_deseado` (pb); `q = min(q_deseado, stock, (dinero_restante × 1000)
// precio)`; se transfiere el bien y el dinero; `dinero_restante -= pago`. Si el dinero se agota,
los bienes siguientes quedan sin comprar (cobertura < 1). Lo no comprado permanece en el stock del
mercado. Esto da al modelo su única elasticidad demanda–precio y es la válvula que evita tanto la
hambruna runaway como el drenaje infinito de dinero.

Cobertura (métrica): `cobertura(g, m) = comprado / deseado` del mes; se registra la de grano.

### 5.3 Demanda artesanal de hierro y madera

El hierro y la madera no aparecen en las cestas de la sección 09, pero deben tener demanda final
para que sus precios no caigan al suelo (SUPUESTO S28, rendimientos y consumos inventados,
confianza D): cada mercado consume **0,1 kg de hierro** (herramientas, clavos, herraduras) y
**4 kg de madera** (construcción y mobiliario) por persona y mes — 0,1 pb y 4 pb respectivamente.
Se añaden a la compra mensual como los bienes de cesta, con la **prioridad más baja** (tras el
vino): orden completo de compra = grano → sal → aceite → leña → paño → pescado → vino → hierro →
madera. Con las poblaciones de 1.2 las cantidades mensuales son enteras en pb
(200.000 × 0,1 = 20.000 pb de hierro en Constantinopla) y cuadran con la producción de 4.2.

---

## 6. Precios (algoritmo semanal exacto de la sección 10)

```
presión = (demanda − oferta) / max(oferta, mínimo) + 0,25 × (existencias_obj − existencias) / existencias_obj
precio(t+1) = precio(t) × (1 + acotar(0,10 × presión, −10 %, +10 %))        # cotas absolutas 0,2×–10× del base
```

Parámetros del Anexo AI: `eco.price.k = 0,10`, `eco.price.max_change = ±10 %`,
`eco.price.stock_weight = 0,25`, `eco.price.min_max = 0,2×/10×`,
`eco.stock.grain_weeks = 26` (grano). Para los demás bienes `semanas_de_reserva = 8`
(SUPUESTO S3; el maestro solo define el 26 del grano).

**Interpretación de demanda y oferta en el prototipo** (los flujos puros estallan estacionalmente:
con la cosecha concentrada en 2 meses, un término de flujo sin almacén subiría el precio +10 %
semanal todo el otoño; por eso las ventas desde existencias forman parte de la oferta — S20):

- `demanda_semana(g, m)` = consumo deseado del mes / 4 (con `carry`, regla 2.2.5)
  **+ exportaciones servidas esta semana** (registradas en el paso de comercio).
  Los insumos de edificios (lana) NO entran: se consumen en el cierre mensual (S21).
- `oferta_semana(g, m)` = producción local de la semana (0 salvo la semana de entrega, que ocurre
  en el cierre mensual) + importaciones recibidas esta semana
  + `ventas_desde_existencias = min(max(0, demanda − producción − importaciones), stock)`.
  Si el almacén cubre la demanda, `oferta == demanda` y el término de flujo es exactamente 0; el
  precio lo gobierna el término de existencias. Solo cuando el stock se agota aparece presión de
  flujo positiva (precios de hambruna). Con superávit de importaciones el término de flujo es
  negativo y abarata.
- `mínimo` (hueco 3): **1 pb/semana** (S17). Solo evita el 0 en el denominador; con oferta 0 y
  demanda grande la presión dispara el precio al tope del +10 % semanal, que es el comportamiento
  deseado en hambruna.
- `existencias` = stock actual (tras el comercio de la semana). `existencias_obj(g, m)` =
  `consumo_mensual_m(g) × semanas(g) // 4` (grano 26, resto 8), constante en toda la ejecución.
- `existencias` iniciales = `existencias_obj` (100 % del objetivo, semana 0; SUPUESTO S19, el
  propio maestro lo asume en su ejemplo numérico).

**Versión entera del paso de precio** (regla 2.2.4):

```python
presion = (demanda - oferta) / max(oferta, 1) + STOCK_WEIGHT * (obj - stock) / obj   # float local
delta = round(PRICE_K * presion * 10000)          # única división con redondeo al más cercano
delta = max(-1000, min(1000, delta))              # ±10 % semanal
precio = (precio * (10000 + delta)) // 10000      # suelo
precio = max(precio_min, min(precio_max, precio)) # cotas 0,2× / 10× del base
```

El orden semanal es: 1) comercio (con los precios vigentes), 2) actualización de precios con la
demanda/oferta resultantes. Así el comercio de esta semana ya se refleja en el precio de la
siguiente, y la conservación no se ve afectada (el precio no mueve dinero por sí solo).

---

## 7. Comercio entre mercados

Cada semana, para cada ruta (orden fijo de la tabla 1.3) y cada bien (orden fijo de la tabla 1.1):

1. **Coste de transporte** por unidad: `coste_m_u = Σ_tramos (km × coste_medio_uc_tkm) ×
   peso_t(unidad) × 1000` (regla 2.2.1 aplicada por unidad: para 1 t de grano por mar,
   700 × 0,0008 × 1 × 1000 = 560 m/u).
2. **Prima de riesgo** por unidad: `prima_m_u = precio_origen × tasa_riesgo`, con
   `tasa = meteo + piratería × fracción_mar` (sección 1.3). Float local, redondeado hacia abajo.
3. **Margen**: `margen = precio_dest − precio_orig − coste − prima` (m/u). Si `margen ≤ 0`, no hay
   flujo.
4. **Cantidad que iguala precios** (`0,2 ×` de esto es el ajuste parcial del maestro,
   `eco.trade.partial_adjust = 20 %`): linealización del término de existencias — mover q unidades
   sube el precio de origen `q × 0,10 × 0,25 × p_orig/obj_orig` y baja el de destino lo simétrico,
   luego `q_iguala = margen / (0,025 × (p_orig/obj_orig + p_dest/obj_dest))` en unidades
   (float local, truncado a pb). El 0,025 = `eco.price.k × eco.price.stock_weight`. Esta es la
   interpretación de "diferencia de existencias necesaria para igualar precios" (S23); en la
   práctica casi siempre liga un tope, no este término.
5. **Flujo**: `q = min(capacidad_ruta, capital/precio_orig, 0,2 × q_iguala, stock_origen)`:
   - capacidad: `capacidad_t_semana × 1000 // peso_t(unidad)` pb, con −50 % marítimo en
     noviembre–febrero; la capacidad de la ruta es **compartida entre bienes** (se descuenta en el
     orden fijo de bienes dentro de la semana);
   - capital: `capital_m × 1000 // precio_orig` pb, con `capital_m = 5.000 uc` por ruta y semana.
6. **Asientos** (todo por transferencias, conservación exacta):
   - bienes: `stock_orig -= q`; `stock_dest += q` (tránsito instantáneo, S16);
   - dinero: el mercado de destino paga `valor + flete + prima` donde
     `valor = q × p_orig // 1000`, `flete = q × coste_m_u // 1000`,
     `prima = q × prima_m_u // 1000`: `dinero_mercado[dest] -= todo`;
     `dinero_mercado[orig] += valor`; **`dinero_hogares[orig] += flete + prima`** (los porteadores
     son hogares del mercado de origen; así el coste de transporte permanece dentro del sistema
     cerrado). 
   - registrar `exportado[orig][g] += q` e `importado[dest][g] += q` para la demanda/oferta semanal.

Con los precios iniciales del Anexo AK el comercio arranca solo: Caffa (6.500 m/t) vende grano a
Constantinopla (10.500 m/t) con margen ≈ 10.500 − 6.500 − 560 − 195 ≈ 3.245 m/t, y Bursa importa
por Constantinopla cuando su precio supera 10.500 + 1.360 + prima.

---

## 8. Dinero

### 8.1 Carteras y masa inicial

Dos carteras por mercado: `dinero_hogares` (todos los hogares del mercado, agregados) y
`dinero_mercado` (fondo municipal que compra producción y vende consumo). Masas iniciales
(SUPUESTO S24, la tarea sugiere ~6 meses de cestas):

- `dinero_hogares[m] = 6 × cesta_mensual_m(precios base)`
- `dinero_mercado[m] = 2 × cesta_mensual_m(precios base)`

Con las cestas de 5.1: hogares ≈ 195.780 uc en Constantinopla, 78.312 Tesalónica, 39.156 Caffa,
29.367 Bursa, 48.945 Candía; mercados ≈ 1/3 de eso. Masa total ≈ 522.000 uc. El código la calcula
exacta en m a partir de las tablas (no a mano).

### 8.2 Renta de la capital (cierra el circuito monetario)

Constantinopla consume ≈ 385.000 uc/año y produce ≈ 215.000 uc con los 10 bienes a granel: sin
más flujos, su dinero se agota en ~1 año y el sistema entero se deflaciona detrás. El Anexo AK
dice que Constantinopla exporta "seda, manufacturas de lujo y servicios" — la seda no está entre
los 10 bienes del prototipo. Por eso (SUPUESTO S25, el supuesto estructural más importante):

> **Renta de la capital**: cada mes, los hogares de cada mercado no Constantinopla pagan a los
> hogares de Constantinopla `150 m por habitante` (0,15 uc/persona/mes), en concepto de rentas
> imperiales, fletes, seguros y servicios de la capital. Importe mensual exacto: se calcula por el
> código como `T = cesta_anual_Constantinopla − producción_neta_anual_Constantinopla` (a precios
> base, pagos netos), prorrateado entre los demás mercados por población; el valor queda ≈
> 0,15–0,17 uc/persona/mes con los edificios de 4.2. Es una transferencia entre carteras de
> hogares: masa monetaria intacta.

Con esto el balance monetario anual de cada mercado queda ≈ 0 (Constantinopla por construcción;
los exportadores porque su superávit de producción ≈ su pago de renta) y solo el valor del
deterioro queda sin cerrar; lo cierra la tarifa siguiente.

### 8.3 Flujos mensuales (en el cierre de mes, en este orden)

1. **Producción y pago**: mercado → hogares por lo entregado (4.4, pagos netos de insumos).
2. **Insumos**: los talleres toman lana del stock (sin dinero; ya descontada del pago neto).
3. **Consumo**: hogares → mercado por la cesta comprada (5.2, con prioridad y presupuesto).
4. **Deterioro**: `podrido = stock × pct // 10000` (2.3); se registra.
5. **Tarifa de almacenaje** (SUPUESTO S26): el mercado cobra a sus hogares el valor del deterioro
   del mes (`Σ podrido × precio // 1000`): hogares → mercado. Sin ella, los hogares acumularían
   cada año el valor de lo podrido (lo cobraron al producirlo y nunca se lo vendieron) y los
   fondos de mercado se hundirían de forma estable; con ella, ambos lados quedan ≈ estables.
6. **Renta de la capital** (8.2).
7. `assert` de conservación de dinero.

### 8.4 Identidades de conservación

- Dinero (cada paso): `Σ hogares + Σ mercados = MASA_INICIAL`. Flujos posibles y su asiento:
  consumo (hogares→mercado local), producción (mercado→hogares local), comercio
  (mercado dest → mercado orig + hogares orig), almacenaje (hogares→mercado local), renta
  (hogares↔hogares). Nada más.
- Bienes (por bien, al cierre de cada año):
  `producido == consumido(hogares + insumos) + podrido + Δstock_total` con tránsito 0.

---

## 9. Aleatoriedad

- Nada de `random` global. Un generador por mercado y año: `rnd = random.Random(BASE_SEED *
  1_000_000 + anio * 10 + indice_mercado)` — **semilla entera** (las de cadena dependen de
  `PYTHONHASHSEED` y romperían la reproducibilidad).
- Un único factor de cosecha por mercado y año, entero: `δ = rnd.randint(-1000, 1000)` (±10 %,
  S27); `q = q_base × (10000 + δ) // 10000`. Se aplica a las entregas del año de grano, aceite,
  vino, lana y pescado de ese mercado; no a sal, hierro, madera, leña ni paño.
- El shock de sequía no usa azar: es un factor fijo ×0,6 sobre la cosecha de grano de Tesalónica
  del año 100 (sección 10).
- Con ±10 % de ruido y existencias de 26 semanas, la respuesta del precio queda dentro del ±25 %
  anual exigido en años normales; si no, ver calibración (sección 15).

---

## 10. Escenarios y CLI

```
python prototype.py [--anos 200] [--semilla 42] [--shock] [--csv RUTA] [--plot RUTA.png]
```

- **(a) Base**: 200 años, sin shock. `--shock` no presente.
- **(b) Shock**: idéntico salvo que la cosecha de grano de Tesalónica del año 100 (jun–jul) se
  multiplica por 0,6 (−40 %). El resto de mercados y bienes ese año son normales. El factor de
  ruido aleatorio de Tesalónica-año-100 se genera igual (determinismo) y el shock se aplica
  encima.
- Salidas: CSV con el precio semanal del grano por mercado (48 × años filas), resumen de métricas
  de la sección 11 con PASS/FAIL por criterio, y PNG opcional (matplotlib) con la serie semanal
  completa y un zoom a los años 99–103.
- Determinismo: mismo `--semilla` → mismos CSV bit a bit. Nada de red, ni reloj del sistema, ni
  floats en el estado.

---

## 11. Métricas y criterios de aceptación

Todas las métricas sobre el **grano** (el único bien calibrado; el resto solo debe conservarse y
no desbocarse). Precio base = 9.000 m/t en los cinco mercados.

| # | Métrica | Definición exacta | Criterio |
| --- | --- | --- | --- |
| M1 | Precio semanal del grano | serie por mercado (CSV) | siempre dentro de [1.800, 90.000] m/t |
| M2 | Media anual | media de las 48 semanas, por mercado y año | `\|media − 9000\| / 9000 ≤ 0,25` en **todos** los mercados y años salvo 100 y 101 (años con crisis; el shock de la cosecha del año 100 mantiene precios altos hasta la cosecha del 101) |
| M3 | Pico tras el shock (solo `--shock`) | referencia = media de las semanas 16–19 del año 100 de Tesalónica (índice 0; las 4 semanas previas a la cosecha shockeada); pico = máximo semanal de Tesalónica en las semanas 20–39 del año 100 (las 20 semanas desde el inicio del shock, mes 6) | `1,40 ≤ pico/referencia ≤ 1,90` |
| M4 | Vuelta tras dos cosechas (solo `--shock`) | media móvil de 8 semanas de Tesalónica al cierre del año 102 | dentro de `±15 %` del precio base (9.000 m/t) |
| M5 | Conservación de dinero | `assert` en cada paso | 0 violaciones |
| M6 | Conservación de bienes | identidad anual por bien (8.4) | 0 violaciones |
| M7 | Cobertura | cobertura mensual de grano por mercado | media > 0,95 en el escenario base (indicador de sanidad, sin umbral duro) |

El resumen imprime una línea por criterio: `PASS`/`FAIL` + valor numérico.

---

## 12. Supuestos introducidos por este diseño

Solo los huecos de parameters.md que el diseño rellena. Confianza D en todos.

| # | Supuesto | Valor elegido | Por qué |
| --- | --- | --- | --- |
| S1 | Reparto por estratos (hueco 16) | 80 / 15 / 4,5 / 0,5 % | El sugerido por la tarea; da enteros exactos con las 5 poblaciones. |
| S2 | Longitud del año | 12 × 4 = 48 semanas | Uniformiza mes = 4 semanas; el maestro no fija el calendario del prototipo. |
| S3 | `semanas_de_reserva` de los 9 bienes sin objetivo (hueco 2) | 8 | La tarea lo sugiere; 8 semanas ≈ 2 meses, menor que las 26 del grano por ser bienes menos estratégicos. |
| S4 | 1 unidad de tejido de cesta = 1/30 de pieza (hueco 17) | 0,15 unidades = 5 pb | Reproduce exactamente los 0,03 uc/mes de tejido de la comprobación del maestro. |
| S5 | Reparto de la cosecha dentro de sus meses (hueco 5) | uniforme (1/n meses) | Lo más simple; el paso es mensual. |
| S6 | Comodidad del estrato bajo y servicios urbanos | fuera del modelo | Minimiza feedbacks; los criterios no los usan. |
| S7 | Las 4 GE de comodidad alimentaria (huecos 9, 24) | 100 % pescado: 8,9 kg/mes para medio/alto/élite | Da demanda final al pescado con la equivalencia 0,45 GE/kg del maestro. |
| S8 | Rendimientos sin tabla (hueco 7) | hierro 60 q/año, madera 60 t/año, leña 300 t/año por edificio | Inventados para cerrar los mercados de esos bienes; solo el grano está calibrado. |
| S9 | Temporada pesquera en Egeo/Mediterráneo (hueco 25) | abr–nov, 1/8 por mes | La del mar Negro del maestro, extendida a todos los mercados. |
| S10 | Calendario de la lana | esquila en mayo, 100 % | Único mes de esquila razonable; el maestro calla. |
| S11 | Leña de invierno ×1,6 | dic–feb, 40 kg/persona | Textual del maestro ("×1,6 en invierno"). |
| S12 | Distancias y medios de las rutas (hueco 11) | tabla 1.3 | Las 5 de la tarea; "mixto" = 200 km mar + 100 km carretera. |
| S13 | Capacidad de las rutas (hueco 11) | 250 t/sem mar (−50 % nov–feb), 50 t/sem carretera, compartida entre bienes | Una nave redonda por semana; el −50 % es textual del maestro. |
| S14 | Capital mercantil (hueco 12) | 5.000 uc por ruta y semana | Liga el flujo para bienes baratos (leña) y no liga para el grano. |
| S15 | Prima de riesgo por ruta (hueco 11) | piratería 2 % mar (×2 nov–feb), meteo 1 % verano / 6 % invierno | Centro del rango del maestro (1–4 %) + sus valores de meteo. |
| S16 | Tránsito | instantáneo (`en_tránsito = 0`) | Las rutas duran < 2 semanas; evita estado intermedio. La identidad de conservación lo contempla. |
| S17 | `mínimo` de la fórmula de presión (hueco 3) | 1 pb/semana | Evita dividir por 0; solo actúa con oferta nula (hambruna). |
| S18 | Fondos de mercado negativos | permitidos | Crédito implícito; conserva la masa y evita lógica de suspensión de pagos. |
| S19 | Existencias iniciales (hueco 1) | 100 % del objetivo (semana 0) | Es lo que el propio maestro asume en su ejemplo numérico. |
| S20 | `oferta_semana` incluye ventas desde existencias; `demanda_semana` incluye exportaciones servidas | según sección 6 | Sin ello el término de flujo puro sube el precio +10 %/semana todo el otoño (la cosecha dura 2 meses); con ello el término de flujo mide escasez real y el de existencias gobierna el ciclo estacional. |
| S21 | Insumos de edificios fuera de la demanda semanal | consumidos en el cierre mensual | La lana llega en mayo y se consume por trimestres; semanalizarla daría picos artificiales de presión. |
| S22 | Alumbre y tintes del taller | ignorados | Bien fuera de los 10; su coste es marginal frente al de la lana. |
| S23 | "0,2 × diferencia de existencias para igualar precios" | linealización de la sección 7.4 | Da una cantidad concreta y monótona en el margen; casi siempre liga un tope (capacidad/capital). |
| S24 | Masa monetaria inicial (huecos 13, 23) | hogares 6 meses de cesta + mercado 2 meses, a precios base | Sugerido por la tarea (~0,23 uc/persona/mes de subsistencia como orden de magnitud). |
| S25 | Renta de la capital (huecos 6, 12, 13, 15) | transferencia mensual de los hogares no-Constantinopla a los de Constantinopla, dimensionada por el código (≈ 0,15 uc/persona/mes) | Sin ella la capital quiebra en ~1 año: consume 385k uc/año y produce 215k con bienes a granel; el AK la financia con seda/servicios que no están en los 10 bienes. Es el supuesto estructural mayor del prototipo. |
| S26 | Tarifa de almacenaje | los hogares pagan el valor del deterioro mensual de su mercado | Cierra el último agujero monetario: lo cobrado al producir y luego podrido volvería a drenar los fondos de mercado para siempre. |
| S27 | Varianza de la cosecha | ±10 % uniforme entero, un factor por mercado y año | Sugerido por la tarea; suficiente para estabilidad del escenario base. |
| S28 | Demanda final de hierro y madera (huecos 7, 9) | 0,1 kg de hierro y 4 kg de madera por persona y mes, prioridad de compra más baja | El maestro no define quién consume estos bienes; sin demanda final sus precios caerían al suelo. Magnitudes plausibles y redondas; solo el grano está calibrado. |

---

## 13. Pseudocódigo del bucle

```python
BIENES = ["grano", "pescado", "sal", "aceite", "vino", "lana", "pano", "hierro", "madera", "lena"]

def iniciar(semilla):
    mercados = []                      # orden fijo: Con, Tes, Caffa, Bursa, Candía
    for m in MERCADOS:                 # tablas 1.2, 4.2, 5.1
        m.stock      = {g: obj(m, g) for g in BIENES}          # S19: 100 % del objetivo
        m.obj        = dict(m.stock)                           # objetivo de existencias, fijo
        m.precio     = {g: base_m_u(g) for g in BIENES}
        m.precio["grano"] = grano_inicial_ak(m)                # 10500/8500/6500/9000/8500
        m.carry      = {g: 0 for g in BIENES}
        m.cesta_m    = cesta_mensual_pb(m)                     # sección 5.1, entera
        m.din_hog    = 6 * valor_cesta_m(m)                    # sección 8.1, en m
        m.din_merc   = 2 * valor_cesta_m(m)
    MASA0 = sum(m.din_hog + m.din_merc for m in mercados)
    renta_capital_mensual = calcular_renta(mercados)           # sección 8.2, en m
    return mercados, MASA0, renta_capital_mensual

def ejecutar(mercados, anos, shock):
    for anio in range(1, anos + 1):
        factores = {m: factor_cosecha(m, anio) for m in mercados}   # sección 9: entero ±10 %
        for mes in range(1, 13):
            for sem in range(4):
                comercio(mercados, mes)                    # orden fijo de rutas y bienes
                actualizar_precios(mercados)               # sección 6, orden fijo
                if sem == 3:
                    cierre_mes(mercados, mes, anio, factores, shock)

def cierre_mes(mercados, mes, anio, factores, shock):
    for m in mercados:                                     # 1) producción + pago (4.4, 4.5)
        for (g, q_pb) in entrega_del_mes(m, mes):          # tabla 4.3, enteros en pb
            if g in BIOLOGICOS: q_pb = q_pb * (10000 + factores[m]) // 10000
            if shock and m == TESALONICA and g == "grano" and anio == SHOCK_ANIO:
                q_pb = q_pb * 6000 // 10000
            m.stock[g] += q_pb
            pago = q_pb * m.precio[g] // 1000 - insumos_netos(m, g, mes)   # pago neto, ≥ 0
            m.din_merc -= pago; m.din_hog += pago
    for m in mercados:                                     # 2) insumos (S21)
        for (g, q_pb) in insumos_del_mes(m, mes):          # lana de los talleres
            q_pb = min(q_pb, m.stock[g]); m.stock[g] -= q_pb; registrar_consumo(m, g, q_pb)
    for m in mercados:                                     # 3) consumo con presupuesto (5.2)
        restante = m.din_hog
        for g in ORDEN_PRIORIDAD:                          # grano, sal, aceite, lena, pano,
                                                           # pescado, vino, hierro, madera
            q_deseada = cesta_bien_pb(m, g, mes)           # leña ×1,6 en dic–feb
            q = min(q_deseada, m.stock[g], restante * 1000 // m.precio[g])
            pago = q * m.precio[g] // 1000
            m.stock[g] -= q; registrar_consumo(m, g, q)
            restante -= pago; m.din_merc += pago
        m.din_hog = restante
        registrar_cobertura(m, mes)
    for m in mercados:                                     # 4) deterioro + 5) tarifa (2.3, S26)
        podrido_total = 0
        for g in BIENES:
            podrido = m.stock[g] * PCT_MERMA[g] // 10000
            m.stock[g] -= podrido; registrar_merma(m, g, podrido); podrido_total += podrido
        tarifa = valor(m, podrido_total); m.din_hog -= tarifa; m.din_merc += tarifa
    for m in mercados if m != CONSTANTINOPLA:              # 6) renta de la capital (S25)
        cuota = renta_capital_mensual[m]; m.din_hog -= cuota; CONSTANTINOPLA.din_hog += cuota
    assert sum(dinero de todos) == MASA0                   # 7) conservación

def comercio(mercados, mes):
    for ruta in RUTAS:                                     # orden fijo tabla 1.3
        cap_restante_t = capacidad(ruta, mes)              # mar ×0,5 en nov–feb
        for g in BIENES:                                   # orden fijo tabla 1.1
            a, b = ruta.origen, ruta.destino
            coste  = coste_m_u(ruta, g)                    # sección 7.1
            prima  = int(a.precio[g] * tasa_riesgo(ruta, mes))     # 7.2
            margen = b.precio[g] - a.precio[g] - coste - prima
            if margen <= 0 or a.stock[g] == 0: continue
            q_iguala = margen / (0.025 * (a.precio[g]/a.obj[g] + b.precio[g]/b.obj[g]))  # float
            q = min(cap_restante_t * 1000 // PESO_T[g],                 # capacidad compartida
                    CAPITAL_RUTA_M * 1000 // a.precio[g],               # capital
                    int(0.2 * q_iguala),                                # ajuste parcial 20 %
                    a.stock[g])
            if q <= 0: continue
            cap_restante_t -= q * PESO_T[g] // 1000
            valor, flete = q * a.precio[g] // 1000, q * coste // 1000
            prim   = q * prima // 1000
            a.stock[g] -= q; b.stock[g] += q                     # tránsito 0 (S16)
            b.din_merc -= valor + flete + prim
            a.din_merc += valor; a.din_hog += flete + prim       # porteadores: hogares origen
            a.exportado_semana[g] += q; b.importado_semana[g] += q

def actualizar_precios(mercados):
    for m in mercados:
        for g in BIENES:
            demanda = (m.cesta_m[g] + m.carry[g]) // 4 + m.exportado_semana[g]   # 6, regla 2.2.5
            m.carry[g] = (m.cesta_m[g] + m.carry[g]) % 4
            ventas_stock = min(max(0, demanda - m.produccion_semana[g] - m.importado_semana[g]),
                               m.stock[g])
            oferta = m.produccion_semana[g] + m.importado_semana[g] + ventas_stock
            presion = (demanda - oferta) / max(oferta, 1) \
                      + STOCK_WEIGHT * (m.obj[g] - m.stock[g]) / m.obj[g]        # float local
            delta = max(-1000, min(1000, round(PRICE_K * presion * 10000)))
            m.precio[g] = clamp((m.precio[g] * (10000 + delta)) // 10000, m.pmin[g], m.pmax[g])
            m.exportado_semana[g] = m.importado_semana[g] = m.produccion_semana[g] = 0
```

Notas: `produccion_semana` solo es no nula si se decidiera entregar producción semanal (aquí no:
la entrega es mensual, luego vale 0); se mantiene en el pseudocódigo para que la fórmula de la
sección 6 sea literal. La demanda semanal no descuenta lo ya comprado en el cierre mensual del
mismo mes: es la tasa deseada, que es lo que la fórmula del maestro necesita.

---

## 14. Tabla de constantes (nombres Python sugeridos)

| Constante | Valor | Origen |
| --- | --- | --- |
| `SCALE` | 1000 | m por uc; pb por unidad natural |
| `PRICE_K` | 0.10 | Anexo AI `eco.price.k` |
| `PRICE_MAX_CHANGE` | 0.10 (±10 % semanal, δ ∈ [−1000, 1000] en diezmilésimas) | `eco.price.max_change` |
| `STOCK_WEIGHT` | 0.25 | `eco.price.stock_weight` |
| `PRICE_FLOOR_MULT` / `PRICE_CEIL_MULT` | 0.2 / 10.0 | `eco.price.min_max` |
| `GRAIN_RESERVE_WEEKS` | 26 | `eco.stock.grain_weeks` |
| `OTHER_RESERVE_WEEKS` | 8 | S3 |
| `PRESSURE_MIN_OFFER_PB` | 1 | S17 |
| `WEEKS_PER_YEAR` | 48 (12 meses × 4) | S2 |
| `WINTER_LENA_MONTHS` / `WINTER_LENA_MULT` | {12, 1, 2} / 1.6 → 40 pb | maestro, S11 |
| `NAV_WINTER_MONTHS` | {11, 12, 1, 2} | maestro (−50 % cap marítima, piratería ×2) |
| `TRADE_PARTIAL` | 0.20 | `eco.trade.partial_adjust` |
| `COST_SEA_UC_TKM` / `COST_RIVER_…` / `COST_ROAD_…` / `COST_PACK_…` | 0.0008 / 0.0032 / 0.012 / 0.020 | Anexo AI `eco.transport.*` |
| `CAP_SEA_T_WEEK` / `CAP_ROAD_T_WEEK` | 250 / 50 | S13 |
| `CAPITAL_ROUTE_UC` | 5000 | S14 |
| `RISK_PIRACY` / `RISK_WEATHER_SUMMER` / `RISK_WEATHER_WINTER` | 0.02 / 0.01 / 0.06 | S15 |
| `PESO_T` | grano/pescado/sal/madera/lena 1; aceite 0.09; vino 0.1; lana/hierro 0.05; pano 0.03 | maestro |
| `PCT_MERMA` | en centésimas de %: grano/vino 100, pescado 200, aceite/lana/madera/lena 50, pano 20, hierro 10, sal 0 | maestro |
| `STRATAS` | (0.80, 0.15, 0.045, 0.005) | S1 |
| `CESTA_PB_PERSONA_MES` | grano 16; sal 0,5; aceite 8; lena 25 (40 inv); pano 5 (+10/20/30 comodidad); pescado 8,9; vino 0/60/100/150; hierro 0,1; madera 4 | secciones 5.1 y 5.3 |
| `EDIFICIOS` | tabla 4.2 | sección 4 |
| `MONEY_MONTHS_HOGARES` / `MONEY_MONTHS_MERCADO` | 6 / 2 | S24 |
| `RENTA_CAPITAL_M_PERSONA_MES` | ≈ 150 (la fija el código con la fórmula de 8.2) | S25 |
| `HARVEST_NOISE` | 1000 (±10 % en diezmilésimas) | S27 |
| `BASE_SEED` | 42 (CLI) | — |
| `SHOCK_YEAR` / `SHOCK_FACTOR` | 100 / 0.6 (`q × 6000 // 10000`) | sección 10 |
| `YEARS_DEFAULT` | 200 | sección 10 |
| `CRIT_ANNUAL_BAND` | 0.25 | Anexo F |
| `CRIT_SHOCK_MIN` / `CRIT_SHOCK_MAX` | 1.40 / 1.90 | Anexo F `harvest_shock` |
| `CRIT_RECOVERY_BAND` | 0.15 | Anexo F `harvest_shock` |

Knobs de calibración (sección 15): `AJUSTE_COSECHA_GRANO_T` (t/año extra de grano repartidos
proporcionalmente a los edificios, 0 por defecto), `MONEY_MONTHS_HOGARES`, `CAP_SEA_T_WEEK`.

---

## 15. Guía de calibración y riesgos conocidos

El modelo es cerrado y con población fija, así que el nivel de precios a largo plazo depende de un
punto fijo débil: producción − consumo = deterioro de equilibrio, y el ciclo estacional del stock
debe cruzar el objetivo (sube antes de la cosecha, baja después). Tres riesgos numéricos y su
manejo:

1. **Deriva lenta de la media anual (criterio M2).** La respuesta del precio es multiplicativa y
   el ciclo del stock no es perfectamente simétrico alrededor del objetivo: puede aparecer una
   deriva de unos pocos ‰ al año que en 50–100 años saque la media fuera del ±25 %. Detección:
   comparar la media de los años 40–50 con la base. Corrección: `AJUSTE_COSECHA_GRANO_T` en pasos
   de ±100 t/año (más producción → ciclo más alto → presión media más negativa). Repetir hasta
   `|media(40–50) − 9000| ≤ 5 %`. Es calibración de prototipo, no cambio de modelo.
2. **Amplitud del pico del shock (criterio M3, +40 %…+90 % en 20 semanas).** Si el pico se queda
   corto (+< 40 %), los hogares están amortiguando demasiado: bajar `MONEY_MONTHS_HOGARES` (6 → 4)
   o la capacidad marítima. Si se pasa (+> 90 %), subirlos. El mecanismo es el correcto (el stock
   de Constantinopla se vacía al cortarse las exportaciones de Tesalónica y el término de flujo
   empuja al +10 %/semana con tope); lo que se ajusta es cuánto puede seguir comprando la gente.
3. **Oscilación intraanual.** La variación estacional del precio del grano puede superar ±25 %
   (pico pre-cosecha, valle post-cosecha): el criterio M2 es sobre la **media anual**, y así debe
   medirse. Si el valle post-cosecha toca el suelo 0,2× de forma sistemática, subir
   `AJUSTE_COSECHA_GRANO_T` (menos superávit estacional) o bajar `OTHER_RESERVE_WEEKS`… del grano
   no: bajar el superávit.

Riesgos menores aceptados y documentados: los bienes no calibrados (hierro, madera, paño…) pueden
derivar hacia sus cotas a muy largo plazo sin violar criterios; los fondos de mercado pueden ser
negativos (S18); el polvo de redondeo de los pagos (regla 2.2.1) es un artefacto de precio, no de
conservación.

Orden de trabajo sugerido para el subagente de código: (1) tablas y aritmética con `assert` de
enteros, (2) cierre mensual sin comercio ni precios, comprobar M5/M6 en 5 años, (3) precios,
comprobar el ciclo estacional en 10 años, (4) comercio, comprobar el gradiente Caffa→Constantinopla,
(5) 200 años + calibración fina, (6) shock + métricas M3/M4, (7) gráficos.

---

## 16. Rev. 1 (2026-10-24): ajustes tras la primera implementación

La primera implementación fiel de este documento cumplió M1/M5/M6 (conservación exacta, cotas de
precio) pero falló M2/M3/M4/M7: el nivel de precios deriva sin ancla hasta una cota en ~5–10 años.
Diagnóstico con cifras en el informe de la tarea T-008 (rev. 1). Tres cambios, dos de ellos
nuevos supuestos (S29–S31) y uno de calibración:

### S29 — Granero público (recupera un mecanismo de la sección 10 del maestro)

parameters.md (TABLA 2, «Algoritmo de precios con existencias») recoge: «Compra/liberación de
existencias por mercaderes y graneros públicos: compran si precio < media de 52 semanas; liberan
si precio > media; límite del 10 % de las existencias por semana». MODEL.md lo omitió en §6.

- **Estado**: stock de granero por mercado y bien, empieza en 0. Tamaño máximo: una cosecha anual
  local del bien (`EDIFICIOS × RENDIMIENTO_PB`). El granero es stock del mercado: cuenta en la
  conservación de bienes y se deteriora con el mismo pct.
- **Compra** (precio < media móvil de 52 semanas, mínimo 8 semanas de historial): hasta el 10 % de
  las existencias comerciales de la semana, sin rebasar el tamaño máximo.
- **Liberación** (precio > media): hasta el 10 % del stock del granero, sin pasar de cubrir el
  déficit bajo el objetivo de existencias.
- **Dinero**: no mueve. La consignación es stock propio del mercado; una compra con efectivo no
  tiene contraparte coherente en el sistema cerrado (el fondo se compraría a sí mismo) y una
  transferencia a hogares convierte el granero en una bomba unidireccional que se apaga cuando el
  fondo toca 0, justo en los mercados exportadores cuyos fondos son estructuralmente negativos
  (S18). Los hogares pagan el precio vigente cuando consumen el bien liberado en el cierre mensual.
- **Resultado empírico**: el granero amortigua los desplomes de cosecha pero su compra es
  asimétrica (frena las caídas, no las subidas) y el nivel pasa de derivar a la baja (sin granero:
  −25 %/año hasta el suelo) a derivar al alza (+30 %/año hasta el techo, grano a 90.000 m/t en el
  año 15). La media móvil de 52 semanas es autorreferencial: no ancla el nivel, solo elige el
  sentido de la deriva. Se conserva implementado por fidelidad al maestro; no resuelve M2.

### S30 — Objetivos de existencias puente (sustituye el valor plano de S3 para no-grano)

El objetivo de S3 (8 semanas para los 9 bienes sin objetivo) no cubre los huecos entre entregas
del calendario de §4.3: la sal (entrega jul–sep) agotaba sus 2 meses de existencias iniciales en
febrero y pasaba ~20 semanas al año en hambruna sistémica (precio ×6,9 en el año 1: 20.000 →
138.039 m/t); el vino tocaba el techo 10×; el paño (entrega trimestral) tocaba el suelo del stock
cada trimestre. La sal y el aceite son prioritarios en la cesta: la explosión destruía los
presupuestos de los hogares y arrastraba al grano.

`semanas_de_reserva(bien) = máx(8, mayor hueco entre entregas del calendario, contando el mes de
entrega, cuyo pago llega al cierre)`. El grano conserva las 26 de `eco.stock.grain_weeks`.

| Bien | Semanas | Calendario de entrega (§4.3) |
| --- | --- | --- |
| grano | 26 | jun–jul / jul–ago / jul según mercado (maestro) |
| pescado | 20 | abr–nov: hueco dic–mar (4 meses) + mes de entrega |
| sal | 40 | jul–sep: hueco oct–jun (9 meses) + mes de entrega |
| aceite | 40 | nov–ene: hueco feb–oct (9 meses) + mes de entrega |
| vino | 44 | sep–oct: hueco nov–ago (10 meses) + mes de entrega |
| lana | 48 | may: hueco jun–abr (11 meses) + mes de entrega |
| paño | 13 | mar/jun/sep/dic: entrega a entrega (13 semanas) |
| hierro, madera, leña | 8 | entrega mensual: queda el valor de S3 |

Con esto desaparecen las hambrunas estructurales de la cesta. Los bienes de entrega mensual
conservan las 8 semanas de S3.

### S31 — Renta de la capital reindexada anualmente (refina S25)

S25 fijaba el importe «a precios base» (constante nominal). Con cualquier deriva del nivel de
precios la cuota quiebra a los mercados pagadores (Tesalónica entra en bancarrota de hogares con
una deriva de −16 %) y la cobertura colapsa en cascada. La propiedad que §8.2 promete («el balance
monetario anual de cada mercado queda ≈ 0») solo se sostiene si el importe sigue al nivel de
precios: **el importe se recalcula al inicio de cada año con la misma fórmula de S25 valorada a
precios corrientes de Constantinopla** (cesta anual − producción neta, con el pago neto del paño),
prorrateado por población. Acotado por debajo a 0.

### Calibración de capacidades (knobs de §15, valores finales)

Las importaciones estructurales de Constantinopla suman ≈ 800 t/semana (leña 490, grano 170,
madera 75, vino 21, pescado 22, resto ~20): la capacidad de S13 (3 rutas marítimas × 250 + la mixta
50 = 800 t/sem) estaba saturada al 100 % y el orden fijo de bienes de §7.5 (la leña es el último)
la estrangulaba: la leña de Con encadenaba hambrunas invernales hasta su techo (12.000 m/t), lo que
disparaba la cesta, la renta reindexada y la bancarrota de Bursa. Además la ruta mixta a 50 t/sem
no podía llevar a la vez el grano que Bursa importa (≈105 t/sem) ni su excedente de leña
(≈250 t/sem).

- `CAP_SEA_T_WEEK` = **400** t/semana (S13 traía 250).
- `CAP_CARRETERA_T_WEEK` = **400** t/semana (S13 traía 50; la mixta queda en el mínimo de tramos).

### Resultado de la rev. 1 (cifras en el informe de la tarea)

M1 PASS (cotas), M5 PASS (12.000 comprobaciones de conservación de dinero, 0 violaciones), M6 PASS
(2.000 identidades anuales de bienes, 0 violaciones), determinismo byte a byte verificado,
200 años en ~1,9 s. M2/M3/M4/M7 siguen FAIL por causas estructurales documentadas: (a) el nivel de
precios no tiene ancla estable en un prototipo de cantidades rígidas — sin granero deriva a la
baja, con granero (S29) deriva al alza; (b) M3 es inalcanzable con el factor ×0,6 sobre
Tesalónica, cuya producción shockeada (9.360 t) sigue superando su consumo (7.680 t): no hay
hambruna local dentro de la ventana de 20 semanas aunque las exportaciones sigan a tope (el stock
se vacía en la semana ~45–54, fuera de la ventana). La calibración definitiva corresponde a 101
Lab (Anexo F) sobre el motor, no a este prototipo desechable.

---

## 17. Rev. 2 (2026-10-24): ancla de nivel de precios y Tesalónica modesta

### S32 — Ancla de nivel de precios por mercado (maestro §10, «Nivel de precios por mercado» +
Anexo AI `eco.price_level.adjust` = 1/36 mensual)

Cada mercado lleva un escalar `nivel` (empieza en 1,0). El precio real de transacción es el precio
relativo × nivel; todo lo que usa precios (hogares, comercio, granario, renta, métricas, CSV, PNG)
usa el precio real, y la MA-52 del granario opera sobre precios reales.

- `producción_real_m` = valor anual de la producción local a **precios base** (referencia fija;
  valorarla a precios corrientes haría el objetivo autorreferente).
- `velocidad_m` = producción_real_m / masa_monetaria_inicial_m, de modo que el nivel objetivo
  arranque exactamente en 1,0.
- `masa_monetaria_m` = efectivo de hogares + efectivo del mercado del propio mercado, **acotada a
  ≥ 0** (los fondos pueden ser negativos por S18 y una masa negativa daría un nivel objetivo sin
  sentido económico).
- Actualización mensual: `nivel += (nivel_objetivo − nivel) × 1/36`. El reescalado de los precios
  reales no se aplica de un golpe: se reparte en las 4 semanas del mes (raíz cuarta del ratio
  mensual) y el cambio total de cada semana (presión + reescalado) se acota al ±10 % de
  `eco.price.max_change` sobre el precio de entrada de la semana, de modo que el ancla nunca añada
  un salto semanal por encima del tope de spec. No toca la conservación (solo reescala precios).

**Hallazgo empírico (documentado, no maquillado)**: el ancla por masa monetaria **polariza** la
distribución de dinero en un sistema cerrado con mercados estructuralmente desequilibrados. La
masa de cada mercado deriva a las esquinas (Caffa/Candía acumulan por superávit comercial;
Tesalónica/Bursa quedan en 0 por la renta de la capital y el drenaje de sus fondos), el nivel
sigue a la masa (niveles observados 0,00–12,97 al año 25) y los precios reales acaban entre
1.800 y 3.500 m/t (−72 %): el comercio se bloquea porque las cotas (0,2×) impiden que el mercado
barato caiga lo suficiente para exportar a un mercado caro. Dos atenuantes probados: (i) la cuota
de la renta se escala con el nivel del pagador respecto al de la capital (carga real constante;
sin ella el drenaje es exponencial); (ii) la masa se acota a ≥ 0. Con ambos, M7 pasa (0,956) pero
M2 sigue FAIL. Conclusión: en un sistema de dinero de suma cero con balanzas comerciales
estructurales, ningún ancla de nivel por masa estabiliza el nivel mientras la **distribución** de
la masa derive a las esquinas; estabilizar esa distribución (el tamaño de la renta, el saldo
comercial por mercado) es un problema del motor, no de este prototipo.

### S33 — Asignación de Tesalónica como exportador modesto de grano

El shock −40 % de Anexo F no mordía: con 600 edificios de cereal, la producción shockeada de
Tesalónica (9.360 t) seguía superando su consumo (7.680 t) y no había hambruna local dentro de la
ventana de M3. Nueva asignación (el total de grano no cambia: 1.573 ed → 40.898 t/año):

| Mercado | Ed. de cereal (rev. 1) | Ed. de cereal (S33) | Producción t/año | Consumo t/año | Margen |
| --- | --- | --- | --- | --- | --- |
| Constantinopla | 400 | 400 | 10.400 | 19.200 | −8.800 |
| Tesalónica | 600 | **340** | **8.840** | 7.680 | **+1.160 (1,15×)** |
| Caffa | 260 | **390** | 10.140 | 3.840 | +6.300 |
| Bursa | 90 | 90 | 2.340 | 3.600 | −1.260 |
| Candía | 223 | **353** | 9.178 | 4.800 | +4.378 |
| **Total** | **1.573** | **1.573** | **40.898** | 38.400 + merma | ≈ 0 ✓ |

Con S33 la cosecha shockeada de Tesalónica (5.304 t) queda un 31 % por debajo de su consumo: el
shock muerde. Aun así M3 no llega a +40 % en 20 semanas (medido 1,05 con comercio): el déficit
local (≈46 t/semana) vacía el objetivo de 26 semanas en ~90 semanas, fuera de la ventana, y el
granario amortigua el resto. La ventana de M3 del Anexo F implica un objetivo de existencias muy
inferior a 26 semanas o un shock más profundo; es una inconsistencia entre Anexo F y los
parámetros de §10 que este prototipo documenta.

### Knobs finales (rev. 2)

- `CAP_SEA_T_WEEK` = 400; `CAP_CARRETERA_T_WEEK` = 400 (rev. 1).
- Tope del granario S29 = **una reserva objetivo** por mercado y bien (rev. 2; rev. 1 usaba una
  cosecha anual local: el granario bloqueaba tanto grano que el mercado se vaciaba y el precio
  encadenaba ratchets alcistas hasta el techo; con el tope de reserva objetivo el sistema
  platea a ~5× el precio base en lugar de ×10, y M7 pasa).
- `AJUSTE_COSECHA_GRANO_T` = 0. `MONEY_MONTHS_HOGARES/MERCADO` = 6/2 (sin cambios).

### Resultado de la rev. 2 (cifras en el informe de la tarea)

M1 PASS; M5 PASS (0/12.000); M6 PASS (0/2.000); **M7 PASS por primera vez (0,9564 conectado /
0,9565 shock)**; determinismo byte a byte; 200 años en ~2,4–4,0 s. M2 FAIL (deriva del nivel hasta
×10 en algunos tramos: el granario plaquea a ~5× el base y el ancla S32 polariza la masa entre
mercados), M3 FAIL (1,05 con comercio; 1,00 sin comercio — en el régimen sin comercio el sistema
colapsa a las cotas y la métrica pierde significado), M4 FAIL. Los tres fallos comparten la causa
raíz ya documentada en la rev. 1: la ley de precios de §10 en cantidades rígidas no tiene un punto
fijo estable del nivel — el granario y el ancla de masa la desplazan, no la eliminan. Escalar a
Arquitectura: la estabilidad del nivel requiere o bien demanda elástica (sustitución/level of
living), o bien un mercado externo que absorba emisiones, o bien una revisión del objetivo de
existencias del grano (26 semanas) frente a la respuesta ±10 %/semana.

### Resultado de la rev. 3 (cifras en el informe de la tarea)

M1 PASS; M5 PASS (0/12.000); M6 PASS (0/2.000); M7 PASS (0,9576 conectado / 0,9580 shock);
determinismo byte a byte; 200 años en ~1,9–3,9 s. M2a FAIL (peor desvío intra-anual 121,0 % en
Caffa, año 34, base; 123,9 % en Caffa, año 178, shock). M2b FAIL (peor desvío de nivel 899,8 % en
Constantinopla, año 100, base; 898,6 %, año 102, shock). M3 FAIL (1,05 con comercio; 1,00 sin
comercio — en el régimen sin comercio el sistema colapsa a las cotas y la métrica pierde
significado). M4 FAIL (+311 % / +645 %). Las causas de cada lectura están en «Lecturas de M2».

### Lecturas de M2 (rev. 3)

El encargo y el Anexo F describen M2 como «variación anual del precio del grano en años sin crisis
≤ ±25 %» sin citar el precio base (a diferencia de M3/M4, que citan «del precio base»
expresamente). La lectura literal es, por tanto, **intra-anual**: cada precio semanal dentro de
±25 % de la media de SU año. Existe una segunda lectura, más estricta, que mide la desviación de
la media anual de cada mercado respecto al precio base (9.000 m/t) y que es la que el prototipo
reportó hasta la rev. 2. El prototipo calcula e imprime **ambas**:

- **M2a (intra-anual, literal)**: para cada mercado y año sin crisis (base: todos; shock: todos
  salvo el año del shock y el siguiente), máximo |p_semana − media_año| / media_año ≤ 0,25.
- **M2b (nivel, estricta)**: |media_año − 9.000| / 9.000 ≤ 0,25 por mercado y año sin crisis.

Resultados (200 años, semilla 20261024): M2a FAIL — peor desvío intra-anual 121,0 % en Caffa
(año 34) en el escenario base y 123,9 % en Caffa (año 178) con shock: el ciclo estacional de los
mercados productores (el desplome post-cosecha frente a la escalada previa a la cosecha) supera
ampliamente ±25 %, coherente con el diagnóstico de la rev. 1 sobre la amplitud del ciclo de
existencias frente a un objetivo de 26 semanas. M2b FAIL — 899,8 % (Con, año 100) / 898,6 %
(Con, año 102): la deriva del nivel documentada arriba. Las dos lecturas fallan por causas
distintas y complementarias: M2a por la amplitud del ciclo estacional, M2b por la deriva del
nivel. Ninguna de las dos se soluciona con calibración dentro de los parámetros de §10 (ver el
diagnóstico de las rev. 1–2).
