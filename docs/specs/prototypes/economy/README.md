# Prototipo económico T-008 (Anexo P)

Simulación económica **fuera del motor** (Python 3.12, stdlib + matplotlib) que valida el modelo de
la sección 10 del documento maestro (v0.7) antes de escribirlo en Rust: 10 bienes, 5 mercados,
200 años, precios semanales con existencias, comercio con ajuste parcial del 20 %, cosechas por
calendario y consumo por estratos con cesta de subsistencia.

**Veredicto en una frase:** la contabilidad, las cotas y el determinismo del algoritmo de la
sección 10 se sostienen (conservación exacta, sin caos explosivo), pero **el nivel de precios no
tiene punto fijo estable** con cantidades rígidas y el criterio `harvest_shock` del Anexo F es
incompatible con los parámetros de la sección 10: tres incumplimientos cuantificados, con causa
raíz, en la tabla de resultados.

## Cómo ejecutarlo

```bash
# Dependencias (matplotlib solo para las gráficas; el resto es stdlib)
python -m pip install -r requirements.txt

# Escenario base: 200 años
python economy.py --anos 200 --semilla 20261024 --csv out/base.csv --plot out/base

# Escenario con sequía: cosecha de grano −40 % en Tesalónica durante el año 100
python economy.py --anos 200 --semilla 20261024 --shock --csv out/shock.csv --plot out/shock

# Pruebas (desde este directorio, o con discover desde la raíz del repo)
python -m unittest
python -m unittest discover -s docs/specs/prototypes/economy
```

- CLI completa: `--anos` (200), `--semilla` (20261024), `--shock`, `--shock-anio` (100),
  `--csv RUTA`, `--plot DIR`, `--sin-comercio` (diagnóstico).
- Un run de 200 años tarda ~2–4 s. Al terminar imprime el resumen de métricas M1–M7.
- Las gráficas (precio del grano, existencias, dinero y zoom del shock) se escriben en `out/`,
  que está en el `.gitignore` local y **no se sube al repositorio**.
- Determinismo: toda la aleatoriedad sale de `random.Random(semilla)` (una por mercado y año,
  S27); dos ejecuciones con la misma semilla producen CSV idénticos byte a byte.

## Parámetros usados

Valores tomados del documento maestro v0.7. Extracción completa con fuentes línea a línea en
[`parameters.md`](parameters.md); diseño del modelo en [`MODEL.md`](MODEL.md).

| ID (Anexo AI) | Valor | Uso en el prototipo |
| --- | --- | --- |
| `eco.price.k` | 0,10 / semana | ganancia del algoritmo de precios |
| `eco.price.max_change` | ±10 % / semana | tope semanal de variación |
| `eco.price.stock_weight` | 0,25 | peso del término de existencias en la presión |
| `eco.price.min_max` | 0,2× / 10× del precio base | cotas absolutas por bien |
| `eco.stock.grain_weeks` | 26 semanas | objetivo de existencias del grano |
| `eco.trade.partial_adjust` | 20 % / semana | ajuste parcial del flujo comercial |
| `eco.transport.sea` | 0,0008 uc/t·km | coste marítimo (rutas de la tabla 1.3) |
| `eco.transport.road` | 0,012 uc/t·km | coste por carretera (ruta mixta a Bursa) |
| `eco.price_level.adjust` | 1/36 mensual | ancla del nivel de precios por masa monetaria (§10) |
| `eco.unit_of_account` | 3,5 g de oro | unidad de cuenta (dinero en milésimas de uc) |
| — (sección 10, sin ID) | grano 9 uc/t; pescado 15; sal 20; aceite 3/hl; vino 2/hl; lana 4/q; paño 6/pieza; hierro 2,5/q; madera 1,5/t; leña 1,2/t | precios base del slice |
| — (sección 10) | cereal jun–jul (Egeo/Tracia), jul–ago (Anatolia), jul ( mar Negro); pesca abr–nov; sal jul–sep; vino sep–oct; aceite nov–ene | calendario de cosechas y entregas |
| — (sección 10) | campos de cereal 39 t/año; olivar 45 hl; viñedo 150 hl; pesquería 25 t; salina 120 t; textil 50 piezas | edificios de referencia |
| — (Anexo AK) | Constantinopla 100k, Tesalónica 40k, Caffa 20k, Bursa 15k, Candía 25k | población y roles comerciales de los 5 mercados |
| — (sección 09) | cesta de subsistencia del estrato bajo: 16 GE alimento (≈16 kg de grano), 0,5 kg sal, 0,8 l aceite, 25 kg leña (×1,6 en invierno), 0,15 tejidos | consumo mensual por persona |

No se usan los parámetros demográficos (`pop.*`): la población es fija en este prototipo
(supuesto S-scope; ver «Fuera de alcance» de la tarea T-008).

## Supuestos

El modelo introdujo 33 supuestos etiquetados **S1–S33** (justificación individual en
`MODEL.md` §13–§17; los 25 huecos detectados en el maestro están listados en `parameters.md`).
Los que condicionan los resultados:

- **S2** — Año de 12 meses × 4 semanas = 48 semanas (semanas enteras por mes).
- **S1** — Reparto de estratos 80 % bajo / 15 % medio / 4,5 % alto / 0,5 % élite en todos los mercados.
- **S30** — Objetivo de existencias de los bienes no agrícolas: el mayor hueco entre entregas de su
  calendario (sal 40, vino 44, aceite 40, lana 48, pescado 20, paño 13, hierro/madera/leña 8 semanas);
  el grano conserva las 26 de `eco.stock.grain_weeks`. Sin esto, la sal y el vino pasan ~20 semanas al
  año en escasez estructural y la cesta encarece el resto.
- **S29** — Granero público de la sección 10 (compra por debajo de la media móvil de 52 semanas,
  libera por encima, 10 %/semana), con tope de una reserva objetivo por mercado y bien.
- **S32** — Normalización del ancla de nivel: `velocidad_m = producción_real_m / masa_inicial_m`
  (producción valorada a precios base) para que el nivel arranque exactamente en 1,0.
- **S31/S25** — Renta de la capital (el pago por los servicios no modelados de Constantinopla,
  ≈ 0,15 uc/persona/mes) reindexada anualmente al coste corriente de su cesta.
- **S33** — Tesalónica como exportador modesto de grano (producción ≈ 1,15 × consumo), para que el
  shock de la sequía pueda morder; el excedente retirado se reubicó en Caffa y Candía.
- **S12–S14** — Distancias y medios de las 5 rutas, capacidades (400 t/semana por ruta y sentido,
  −50 % en invierno) y capital mercantil (5.000 uc/ruta).
- **S24** — Masa monetaria inicial: 6 meses de cesta en hogares + 2 meses en el fondo de mercado
  (522.080.000 m en total).
- **S18** — Los fondos de mercado pueden ser negativos (crédito implícito); sin esto el comercio
  y la renta quiebran el circuito en el primer año.
- **S27** — Ruido de rendimiento ±10 % por mercado y año, con semilla derivada
  `Random(base·10⁶ + año·10 + mercado)`.
- **S5** — La cosecha se reparte uniforme entre sus meses de cosecha.

## Resultados

Semilla 20261024, 200 años, escenario conectado (con comercio). La suite `unittest` (10 pruebas)
está en verde y el determinismo se verificó byte a byte.

| # | Criterio (fuente) | Estado | Cifras |
| --- | --- | --- | --- |
| 1 | Base: el precio del grano se mantiene dentro de ±25 % de su media anual en años sin crisis (Anexo F) | **NO CUMPLE** | peor variación intra-anual **121,0 %** (Caffa, año 34); lectura estricta de nivel (media anual vs 9.000 ±25 %) tampoco cumple: peor **+899,8 %** (Constantinopla, año 100) |
| 2 | Shock: el grano de Tesalónica sube +40…+90 % en 20 semanas (harvest_shock, sección 10) | **NO CUMPLE** | pico/referencia **1,00** (pico 90.000 m/t = cota superior; referencia 89.688 m/t: el sistema ya está clavado en la cota cuando llega el shock) |
| 3 | Shock: vuelta a ±15 % del precio base tras dos cosechas normales | **NO CUMPLE** | media de 8 semanas al cierre del año 102: **67.074 m/t (+645 %)** |
| 4 | Conservación exacta de bienes y dinero | **CUMPLE** | **0 violaciones**: 12.000 comprobaciones de dinero (una por paso) y 2.000 identidades anuales de bienes; masa monetaria 522.080.000 m constante |
| 5 | `python -m unittest` en verde | **CUMPLE** | 10/10 en 0,3 s (conservación, límites ±10 % semanal y cotas 0,2×–10×, determinismo, CLI) |
| 6 | Tarea T-008: 200 años ejecutables (código 0), sin hiperinflación exponencial ni deflación irreversible | **CUMPLE CON MATIZ** | runs completos en ~2–4 s; las cotas aguantan siempre (M1 PASS, rango observado 3.659–90.000 m/t) y no hay divergencia monótona, pero el nivel **oscila entre cotas en un ciclo de ~60 años** en lugar de estabilizarse |
| 7 | Tarea T-008: gráficas de series temporales (PNG) y CSV exportable | **CUMPLE** | `out/{base,shock}/` con 7 PNG y 2 CSV de 9.600 semanas (generados localmente, no se suben) |
| 8 | Tarea T-008: informe técnico con ecuaciones validadas y recomendaciones | **CUMPLE** | este documento + `MODEL.md` (ecuaciones y pseudocódigo) |

**Lectura visual de las gráficas** (requisito del encargo, verificada sobre los 7 PNG):
el precio del grano forma un ciclo límite acotado de periodo ~60 años entre las cotas 0,2× y 10×,
con una sierra estacional profunda dentro de cada año; las existencias están acotadas (Constantinopla
acumula el grueso: el granario se llena y deja de operar); el dinero total se conserva pero
**se polariza** (Bursa deriva a ≈ −2,9 M uc de crédito implícito, Constantinopla a ≈ +2 M uc);
en el zoom del shock, el nivel ya está en 50.000–90.000 m/t antes del año 100, por lo que el efecto
de la sequía es invisible sobre ese nivel.

### Causas de los incumplimientos (documentadas en MODEL.md §16–§17)

1. **El nivel de precios no tiene punto fijo (criterios 1 y 3).** Con producción y consumo rígidos,
   la ley de precios semanal es multiplicativa y homogénea: el precio del año siguiente es el de este
   por una función de las existencias, y la trayectoria de existencias no depende del nivel. Cualquier
   desviación sistemática de cobertura (los stockouts de los productores exportadores) integra una
   deriva que nada frena. Probados tres regímenes: sin granero deriva a la baja (−25 %/año); con
   granero de tope alto, ratchet alcista (+30 %/año hasta la cota); con granero de tope = reserva
   objetivo, platea a ~5× el base. El ancla de la propia sección 10 (`eco.price_level.adjust = 1/36`
   por masa monetaria, S32) **polariza**: el dinero migra a las esquinas (niveles 0,00–12,97) porque
   el dinero no sale del sistema y las transferencias indexadas al nivel amplifican el desequilibrio.
2. **El ciclo estacional supera ±25 % intra-anual (criterio 1, lectura literal).** El objetivo de 26
   semanas con peso de existencias 0,25 y cosecha concentrada produce oscilaciones anuales de ±121 %
   en los mercados productores (desplome post-cosecha frente a escalada previa).
3. **`harvest_shock` es estructuralmente incompatible con los parámetros (criterios 2 y 3).** Con un
   mercado de superávit modesto (S33, producción shockeada 5.304 t < consumo 7.680 t), el déficit de
   ~46 t/semana tarda ~90 semanas en drenar el objetivo de 26 semanas (4.160 t), fuera de la ventana
   de 20 semanas del criterio; y al llegar el shock el sistema ya circula por la cota superior.
   En modo aislado (`--sin-comercio`, lectura literal de Anexo F) el sistema colapsa a cotas en ~3
   años (cobertura 0,58) y la métrica pierde significado. El criterio +40…+90 % en 20 semanas exige
   reservas de ~4–8 semanas o un shock mayor: **es una inconsistencia entre Anexo F y la sección 10,
   ahora cifrada**.

## Recomendaciones de ajuste para la sección 10

1. **Conectar la elasticidad de demanda al bucle de precios antes de portar a Rust.** La sustitución
   de §9 (consumo ∝ preferencia_cultural × (1/precio_por_GE)²) y la respuesta de inversión
   (`investment_response`) son los estabilizadores que la sección 10 asume pero que este prototipo,
   de cantidades rígidas, no tiene. Sin ellos, el nivel de precios no tiene punto fijo: no porter
   el algoritmo semanal tal cual.
2. **Reformular `harvest_shock` (Anexo F) para que sea alcanzable**: (a) mercado de prueba con
   reservas iniciales de 4–8 semanas en lugar de 26, (b) ventana de 52 semanas en lugar de 20,
   (c) shock ≥ −60 %, o (d) medir el pico sobre el importador cuya existencia se vacía, no sobre el
   mercado shockeado. Cualquiera de las cuatro exige un cambio de texto en Anexo F o de parámetro
   en §10 (`eco.stock.grain_weeks`).
3. **Revisar la amplitud del ciclo estacional** si Anexo F quiere ≤ ±25 % intra-anual: reducir
   `eco.price.stock_weight` (0,25), suavizar el reparto de la cosecha (supuesto S5) o acotar el
   término de flujo cuando hay existencias positivas.
4. **El granero público amortigua, no ancla.** Mantenerlo (subió la cobertura media a 0,9576 y
   eliminó las hambrunas de la cesta), con tope de una reserva objetivo; un tope mayor produce
   ratchets alcistas al bloquear existencias por encima del objetivo.
5. **El ancla por masa monetaria (`eco.price_level.adjust`) necesita contrapesos fiscales.** En un
   sistema cerrado sin Estado, el dinero migra a los exportadores estructurales y los fondos de
   mercado negativos (crédito implícito, S18) crecen sin límite (Bursa: −2,9 M uc). Para el motor:
   o prohibir fondos negativos con quiebra de mercado, o incluir los flujos fiscales de §10
   (presupuesto bizantino ≈ 465.000 uc/año) que devuelvan dinero a los mercados pagadores.
6. **Las transferencias indexadas al nivel de precios amplifican la polarización** (S31): si el
   motor indexa rentas o salarios al nivel, hacerlo parcial y lentamente, y compensar los
   superávits comerciales con salida de dinero (o con la prima de riesgo y el consumo de servicios
   de los exportadores).

## Archivos

| Archivo | Contenido |
| --- | --- |
| `parameters.md` | Extracción de parámetros de las secciones 09/10 y anexos AI/F/K/AK, con los 25 huecos detectados |
| `MODEL.md` | Diseño del modelo: aritmética entera, calendario, fórmulas, supuestos S1–S33, revisiones 1–3 |
| `economy.py` | Implementación (Python 3.12: stdlib + matplotlib solo para gráficas) |
| `test_economy.py` | Suite `unittest`: conservación, límites de precio, determinismo, CLI |
| `requirements.txt` | `matplotlib==3.11.2` (el resto es stdlib) |
| `.gitignore` | Excluye `out/` (resultados generados) |
| `README.md` | Este informe |
