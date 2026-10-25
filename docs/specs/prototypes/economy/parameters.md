# Parámetros del prototipo económico (T-008)

Extracción de todos los parámetros relevantes para un prototipo económico del slice 1300–1600, a partir del **documento maestro `docs/master/101_Agents_Games_Documento_Maestro_v0.7.md`**. Fecha de extracción: **2026-10-24**. Secciones de origen: 09 (Población y sociedad), 10 (Economía, producción y finanzas, incluida la "Especificación detallada de economía (v0.7, propuesto)"), Anexo F (Objetivos de calibración de 101 Lab), Anexo K (Catálogo de bienes y edificios) y Anexo AI (Tabla de parámetros globales).

Notas de lectura:

- Todo valor es de **confianza D (diseño)** salvo indicación explícita (A/B/C). La calibración final corresponde a 101 Lab (Anexo F).
- La **unidad de cuenta (uc)** es el valor de 3,5 g de oro fino (≈ ducado veneciano de 1284); no es una moneda del juego y no se devalúa.
- Los ID entre acentos graves son los del Anexo AI; viven en `games/epoch/data/rules/*.ron` y los mods pueden sobrescribirlos.
- Conversión anual→mensual de tasas: `r_mes = 1 − (1 − r_año)^(1/12)`, con tabla precalculada en punto fijo (nunca potencias de flotantes).

## TABLA 1 — Parámetros del Anexo AI relevantes a economía y población

| ID | Parámetro | Valor | Unidad | Nota |
| --- | --- | --- | --- | --- |
| `eco.unit_of_account` | Unidad de cuenta | 3,5 g de oro fino | uc | ≈ ducado veneciano de 1284; fija, no devalúa. |
| `eco.price.k` | Amortiguación del ajuste de precios | 0,10 | por semana | Coeficiente sobre la presión. |
| `eco.price.max_change` | Límite de cambio de precio | ±10 % | por semana | Impide saltos absurdos. |
| `eco.price.stock_weight` | Peso de las existencias en la presión | 0,25 | — | Multiplica el término `(existencias_obj − existencias)/existencias_obj`. |
| `eco.price.min_max` | Precio mínimo y máximo | 0,2× / 10× el precio base | — | Cotas del precio de mercado. |
| `eco.stock.grain_weeks` | Semanas de reserva objetivo de grano | 26 | semanas de consumo tras la cosecha | Define `existencias_obj` del grano. |
| `eco.trade.partial_adjust` | Ajuste parcial del comercio | 20 % | por semana | Fracción del desequilibrio de existencias que se mueve por la ruta. |
| `eco.transport.sea` | Coste de transporte por mar | 0,0008 | uc por t·km | Mar abierto, nave redonda. |
| `eco.transport.river` | Coste de transporte por río | 0,0032 | uc por t·km | Danubio, Nilo; caudal estacional. |
| `eco.transport.road` | Coste de transporte por camino | 0,012 | uc por t·km | Carros. |
| `eco.transport.pack` | Coste de transporte con animales de carga | 0,020 | uc por t·km | Montaña, estepa, desierto. |
| `eco.invest.hurdle` | Umbral de inversión privada | interés + riesgo + 3 % | anual | Rentabilidad mínima exigida. |
| `eco.invest.max_share` | Máximo capital invertible por cohorte | 30 % del capital | trimestral | Se invierte en el proyecto de mayor rentabilidad. |
| `eco.tax_farm.price` | Precio de subasta del arrendamiento fiscal | 0,70–0,85 × recaudación esperada | — | F-ECO-15. |
| `eco.tax_farm.extra_pressure` | Presión extra del arrendatario | 1,10–1,40 | — | Genera agravio adicional. |
| `eco.debt.risk_per_debt_ratio` | Prima de riesgo por ratio deuda/ingresos | 2 % por unidad | anual | `prima = 2 % × (deuda/ingresos_anuales)`. |
| `eco.debt.risk_per_default` | Prima por impago recordado | 6 % por impago | anual | Cada impago pesa 1,0. |
| `eco.debt.default_half_life` | Semivida de un impago recordado | 15 | años | El recuerdo decae a la mitad cada 15 años. |
| `eco.coin.detection.urban` | Velocidad de detección de devaluación (urbano) | 1/6 | fracción mensual | ≈ semivida de 4 meses con cambistas y ensayadores. |
| `eco.coin.detection.rural` | Velocidad de detección de devaluación (rural) | 1/18 | fracción mensual | Mercados rurales o aislados. |
| `eco.coin.gresham_outflow` | Salida de moneda buena (Gresham) | 5 % | mensual | Existencias de moneda buena hacia el exterior. |
| `eco.price_level.adjust` | Ajuste del nivel de precios por mercado | 1/36 | fracción mensual | Hacia `(masa_monetaria × velocidad)/producción_real`. |
| `eco.gold_silver_ratio.start` | Relación oro/plata inicial | 11 | — | Precio de mercado; rango 1:9 a 1:14 (confianza B). |
| `pop.birth_rate_per_adult` | Natalidad por adulto | 72,7 | ‰ anual por adulto | ≈ natalidad bruta de 40 ‰ anual (rango orientativo 35–45 ‰). |
| `pop.mortality.children` | Mortalidad base de niños (0–14) | 55 | ‰ anual | Años normales, 1300. |
| `pop.mortality.adults` | Mortalidad base de adultos (15–49) | 16 | ‰ anual | Años normales, 1300. |
| `pop.mortality.elders` | Mortalidad base de mayores (50+) | 85 | ‰ anual | Años normales, 1300. |
| `pop.aging.child_to_adult` | Paso de niños a adultos | 1/180 | fracción mensual | 15 años × 12 meses. |
| `pop.aging.adult_to_elder` | Paso de adultos a mayores | 1/420 | fracción mensual | 35 años × 12 meses. |
| `pop.cohort.create_threshold` | Umbral de creación de cohorte (`U_crear`) | 50 | personas | Flujos menores esperan en `pending_flows`. |
| `pop.cohort.merge_threshold` | Umbral de fusión (`U_fusion`) | max(100; 0,3 % de la provincia) | personas | Fusión en el cierre mensual. |
| `pop.cohort.max_per_province.S/M/L` | Máximo de cohortes por provincia | 70 / 50 / 40 | cohortes | Escalas S / M / L. |
| `pop.migration.alpha` | α de migración | 0,02 | fracción mensual | Fracción máxima teórica por mes antes del límite. |
| `pop.migration.threshold` | Umbral de atractivo migratorio | 0,10 | atractivo | Diferencias menores no mueven a nadie (arraigo). |
| `pop.migration.cap_free` | Límite de migración de población libre | 1 % | mensual por cohorte | Refugiados sin límite. |
| `pop.migration.max_days` | Radio de destinos candidatos | 30 | días de viaje | Más ciudad principal del mercado y hasta 3 provincias de diáspora. |
| `pop.refugees.security_trigger` | Umbral de seguridad para refugiados | 0,30 | seguridad | Devastación, asedio, persecución. |
| `pop.refugees.cap` | Límite de desplazamiento de refugiados | 10 % | mensual | De cada cohorte afectada. |
| `pop.refugees.return_chance` | Probabilidad de retorno de refugiados | 2 % | mensual | Si su provincia recupera seguridad > 0,6. |
| `pop.refugees.productivity_malus` | Penalización de productividad del refugiado | −30 % durante 12 meses | — | — |
| `pop.mobility.cap` | Límite de movilidad social por cohorte | 0,5 % | mensual | Tope de la v0.6, se mantiene. |
| `pop.literacy.convergence` | Convergencia de alfabetización | 1/240 | fracción mensual | ≈ 20 años. |
| `pop.urban.threshold` | Umbral de provincia urbana | 30 % no agrario o 10.000 hab. | — | — |
| `pop.urban.overcap_mortality` | Mortalidad por exceso sobre el techo urbano | +10 % por cada 10 % de exceso | — | — |
| `cul.assimilation.base` | Tasa base de asimilación | 0,0012 | fracción mensual | Sección 06; contexto para cohortes. |
| `rel.conversion.base` | Tasa base de conversión religiosa | 0,0003 | fracción mensual | Sección 06. |

## TABLA 2 — Parámetros de la sección 10 sin ID en el Anexo AI

| Nombre | Valor | Unidad | Fuente exacta (sección y encabezado) |
| --- | --- | --- | --- |
| Precio base grano | 9 | uc/tonelada | 10 · "Especificación detallada de economía (v0.7, propuesto)" · "Precios base del slice (1300–1600)" |
| Precio base arroz | 11 | uc/tonelada | 10 · "Precios base del slice (1300–1600)" |
| Precio base legumbres | 8 | uc/tonelada | 10 · "Precios base del slice (1300–1600)" |
| Precio base carne (y ganado en pie) | 30 | uc/tonelada de carne | 10 · "Precios base del slice (1300–1600)" |
| Precio base pescado fresco / salado | 15 / 25 | uc/tonelada | 10 · "Precios base del slice (1300–1600)" |
| Precio base sal | 20 | uc/tonelada | 10 · "Precios base del slice (1300–1600)" |
| Precio base aceite de oliva | 3 | uc/hectolitro | 10 · "Precios base del slice (1300–1600)" |
| Precio base vino | 2 | uc/hectolitro | 10 · "Precios base del slice (1300–1600)" |
| Precio base azúcar | 25 | uc/quintal (50 kg) | 10 · "Precios base del slice (1300–1600)" |
| Precio base especias (mezcla) | 100 | uc/quintal | 10 · "Precios base del slice (1300–1600)" |
| Precio base seda en bruto | 250 | uc/quintal | 10 · "Precios base del slice (1300–1600)" |
| Precio base lana | 4 | uc/quintal | 10 · "Precios base del slice (1300–1600)" |
| Precio base paño común / fino | 6 / 25 | uc/pieza (~30 m) | 10 · "Precios base del slice (1300–1600)" |
| Precio base tejido basto (unidad de cesta) | 0,2 | uc/unidad (~1 m²) | 10 · "Precios base del slice (1300–1600)" |
| Precio base alumbre | 3 | uc/quintal | 10 · "Precios base del slice (1300–1600)" |
| Precio base hierro en barras | 2,5 | uc/quintal | 10 · "Precios base del slice (1300–1600)" |
| Precio base cobre | 6 | uc/quintal | 10 · "Precios base del slice (1300–1600)" |
| Precio base plata | 10 | uc/kg | 10 · "Precios base del slice (1300–1600)" |
| Precio base madera de construcción | 1,5 | uc/tonelada | 10 · "Precios base del slice (1300–1600)" |
| Precio base leña | 1,2 | uc/tonelada | 10 · "Precios base del slice (1300–1600)" |
| Precio base pertrechos navales | 120 | uc/lote (equipo de una galera durante un año) | 10 · "Precios base del slice (1300–1600)" |
| Precio base caballo de silla / de guerra | 12 / 45 | uc/cabeza | 10 · "Precios base del slice (1300–1600)" |
| Precio base equipo de infantería | 3 | uc/lote por soldado | 10 · "Precios base del slice (1300–1600)" |
| Precio base equipo de caballería pesada | 40 | uc/lote por jinete | 10 · "Precios base del slice (1300–1600)" |
| Precio base pólvora (desde su adopción) | 8 | uc/quintal | 10 · "Precios base del slice (1300–1600)" |
| Pérdida mensual en almacén — grano, arroz, legumbres | 1 % | mensual | 10 · "Precios base del slice (1300–1600)" |
| Pérdida mensual en almacén — carne | 15 % | mensual | Perecedero (ganado vivo: almacenable). |
| Pérdida mensual en almacén — pescado fresco / salado | 20 % / 2 % | mensual | 10 · "Precios base del slice (1300–1600)" |
| Pérdida mensual en almacén — sal | 0 % | mensual | 10 · "Precios base del slice (1300–1600)" |
| Pérdida mensual en almacén — aceite | 0,5 % | mensual | 10 · "Precios base del slice (1300–1600)" |
| Pérdida mensual en almacén — vino | 1 % | mensual | 10 · "Precios base del slice (1300–1600)" |
| Pérdida mensual en almacén — lana | 0,5 % | mensual | 10 · "Precios base del slice (1300–1600)" |
| Pérdida mensual en almacén — paño, tejido basto | 0,2 % | mensual | 10 · "Precios base del slice (1300–1600)" |
| Pérdida mensual en almacén — hierro | 0,1 % | mensual | 10 · "Precios base del slice (1300–1600)" |
| Pérdida mensual en almacén — madera, leña | 0,5 % | mensual | 10 · "Precios base del slice (1300–1600)" |
| Peso para transporte — grano, arroz, legumbres, carne, pescado, sal, madera, leña | 1 t | por unidad de bien | 10 · "Precios base del slice (1300–1600)" |
| Peso para transporte — aceite / vino | 0,09 / 0,1 t | por hectolitro | 10 · "Precios base del slice (1300–1600)" |
| Peso para transporte — bienes en quintal (lana, hierro, alumbre, cobre, azúcar, especias, seda, pólvora) | 0,05 t | por quintal | 10 · "Precios base del slice (1300–1600)" |
| Peso para transporte — paño | 0,03 t | por pieza | 10 · "Precios base del slice (1300–1600)" |
| Peso para transporte — tejido basto | 0,001 t | por unidad | 10 · "Precios base del slice (1300–1600)" |
| Peso para transporte — pertrechos navales | 2 t | por lote | 10 · "Precios base del slice (1300–1600)" |
| Cosecha de cereal — Mediterráneo costero (Grecia, Tracia, Egeo, Chipre) | Junio–julio | meses | 10 · "Calendario agrícola" |
| Cosecha de vid — Mediterráneo costero | Septiembre–octubre | meses | 10 · "Calendario agrícola" |
| Cosecha de oliva — Mediterráneo costero | Noviembre–enero | meses | 10 · "Calendario agrícola" |
| Hortalizas — Mediterráneo costero | Marzo–octubre, 1/8 de la producción cada mes | meses y fracción | 10 · "Calendario agrícola" |
| Cosecha de cereal — Meseta anatolia | Julio–agosto | meses | 10 · "Calendario agrícola" |
| Cosecha de vid — Meseta anatolia | Septiembre | mes | 10 · "Calendario agrícola" |
| Ganado — Meseta anatolia | Partos en primavera; venta en otoño | meses | 10 · "Calendario agrícola" |
| Cosecha de cereal — Llanura panónica y Danubio | Julio–agosto | meses | 10 · "Calendario agrícola" |
| Cosecha de vid — Llanura panónica y Danubio | Septiembre–octubre | meses | 10 · "Calendario agrícola" |
| Mijo y avena — Llanura panónica y Danubio | Agosto | mes | 10 · "Calendario agrícola" |
| Cosecha de cereal — Costa del mar Negro y Crimea | Julio | mes | 10 · "Calendario agrícola" |
| Pesca — Costa del mar Negro y Crimea | Abril–noviembre | meses | 10 · "Calendario agrícola" |
| Cosecha de cereal — Delta del Nilo (externo) | Abril–mayo | meses | 10 · "Calendario agrícola" |
| Crecida del Nilo | Agosto–septiembre | meses | 10 · "Calendario agrícola" |
| Campos de cereal (100 ha, año y vez): plazas | 25 campesinos | personas por nivel | 10 · "Edificios de referencia del slice" |
| Campos de cereal (año y vez): insumos anuales | 13 t grano (semilla) | t/año | 10 · "Edificios de referencia del slice" |
| Campos de cereal (año y vez): productos anuales | 39 t grano | t/año | 10 · "Edificios de referencia del slice" |
| Campos de cereal (año y vez): coste y mantenimiento | 150 uc + 2 años de construcción; 3 uc | uc | 10 · "Edificios de referencia del slice" |
| Campos de cereal (rotación trienal, tierras húmedas): plazas | 25 campesinos | personas por nivel | 10 · "Edificios de referencia del slice" |
| Campos de cereal (rotación trienal): insumos y productos | 15 t grano (semilla) → 56 t grano | t/año | Requiere arado pesado; mejora de 80 uc; mantenimiento 4 uc. |
| Olivar (50 ha): plazas | 12 campesinos | personas por nivel | 10 · "Edificios de referencia del slice" |
| Olivar: insumos y productos | 1 t equivalentes de herramientas (0,4 uc) → 45 hl aceite | hl/año | 200 uc + 8 años hasta plena producción; mantenimiento 2 uc. |
| Viñedo (30 ha): plazas | 15 campesinos | personas por nivel | 10 · "Edificios de referencia del slice" |
| Viñedo: insumos y productos | 2 uc en toneles → 150 hl vino | hl/año | 180 uc + 4 años; mantenimiento 3 uc. |
| Pastos (500 ha): plazas y productos | 6 pastores → 4 t carne, 30 quintales de lana, 60 cueros | t y quintales/año | 20 uc; mantenimiento 1 uc. |
| Pesquería costera: plazas y productos | 15 pescadores → 25 t pescado | t/año | Insumo: 0,5 lotes de pertrechos (60 uc) cada 5 años; 60 uc; mantenimiento 4 uc. |
| Salina: plazas y productos | 10 trabajadores → 120 t sal (julio–septiembre) | t/año | 120 uc; mantenimiento 3 uc. |
| Molino de agua: plazas, insumos y productos | 3 artesanos; grano → harina (95 % del grano) con productividad 2,5 | — | 90 uc; mantenimiento 4 uc. |
| Taller textil: plazas, insumos y productos | 20 artesanos; 60 quintales de lana, 6 quintales de alumbre, tintes → 50 piezas de paño común | piezas/año | 100 uc; mantenimiento 5 uc. |
| Forja: plazas, insumos y productos | 6 artesanos; 30 quintales de hierro, 20 t leña o carbón vegetal → herramientas (40 uc) o 60 lotes de equipo de infantería | — | 70 uc; mantenimiento 3 uc. |
| Astillero (galeras): plazas, insumos y productos | 60 artesanos; 300 t madera, 3 lotes de pertrechos → 1 galera ligera cada 8 meses | galeras/año | 600 uc; mantenimiento 30 uc. |
| Mina de plata: plazas, insumos y productos | 80 mineros; 200 t madera, 40 quintales de hierro → 120 kg plata | kg/año | 1.200 uc; mantenimiento 40 uc. |
| Mina de alumbre (Focea): plazas, insumos y productos | 50 mineros; 400 t leña → 1.500 quintales de alumbre | quintales/año | 800 uc; mantenimiento 30 uc. |
| Ingenio de azúcar: plazas, insumos y productos | 40 trabajadores; 300 t caña, 150 t leña → 60 quintales de azúcar | quintales/año | 900 uc; mantenimiento 35 uc. |
| Rendimiento agrario de referencia | 26 t netas (39 t − 13 t de semilla) alimentan a ≈ 135 personas/año (192 kg/persona) | t y kg | 10 · "Edificios de referencia del slice" (comprobación de la explotación agraria); con rotación trienal la neta pasa a 41 t (+58 %). |
| Algoritmo de precios: presión | `presión = (demanda − oferta)/max(oferta, mínimo) + 0,25 × (existencias_obj − existencias)/existencias_obj` | — | 10 · "Algoritmo de precios con existencias" (y 10 · "Precios" para la forma base sin existencias) |
| Algoritmo de precios: actualización | `precio(t+1) = precio(t) × (1 + acotar(0,10 × presión, −10 %, +10 %))` | — | 10 · "Algoritmo de precios con existencias" |
| Existencias objetivo | `existencias_obj = consumo_semanal_medio × semanas_de_reserva(bien)`; grano: 26 semanas tras la cosecha | semanas | 10 · "Algoritmo de precios con existencias" |
| Compra/liberación de existencias por mercaderes y graneros públicos | Compran si precio < media de 52 semanas; liberan si precio > media; límite del 10 % de las existencias por semana | % por semana | 10 · "Algoritmo de precios con existencias" |
| Comercio entre mercados: margen | `margen = precio_destino − precio_origen − coste_transporte − peajes − prima_de_riesgo` | uc | 10 · "Comercio entre mercados" |
| Comercio entre mercados: flujo | Si margen > 0: `flujo = min(capacidad_ruta_libre, capital_mercantil/precio_origen, 0,2 × diferencia_de_existencias_necesaria_para_igualar_precios)` | unidades/semana | 10 · "Comercio entre mercados" |
| Comercio entre mercados: ajuste parcial | 20 % por semana | fracción semanal | 10 · "Comercio entre mercados" |
| Coste de transporte — mar abierto (nave redonda) | 0,0008 (relativo 1) | uc por t·km | 10 · "Transporte: costes por medio"; velocidad 80–120 km/día; de noviembre a febrero: −50 % capacidad y +100 % riesgo. |
| Coste de transporte — galera mercante | 0,0016 (relativo 2) | uc por t·km | 10 · "Transporte: costes por medio"; velocidad 60–100 km/día. |
| Coste de transporte — río navegable | 0,0032 (relativo 4) | uc por t·km | 10 · "Transporte: costes por medio"; 30–50 km/día aguas abajo, 15–25 aguas arriba. |
| Coste de transporte — camino con carros | 0,012 (relativo 15) | uc por t·km | 10 · "Transporte: costes por medio"; 20–30 km/día. |
| Coste de transporte — animales de carga | 0,020 (relativo 25) | uc por t·km | 10 · "Transporte: costes por medio"; 25–35 km/día. |
| Coste de transporte — caravana del desierto | 0,016 (relativo 20) | uc por t·km | 10 · "Transporte: costes por medio"; 30–40 km/día. |
| Prima de riesgo de transporte | `valor_carga × (riesgo_piratería + riesgo_guerra + riesgo_meteorológico)`; piratería 1–4 % por viaje en el Egeo; guerra 5–25 % en zonas en guerra; meteorológico 1 % (verano) a 6 % (invierno) | % del valor de la carga | 10 · "Transporte: costes por medio" |
| Cesta de subsistencia — estrato bajo | 16 GE de alimento básico; 0,5 kg sal; 0,8 l aceite o grasa; 0,15 unidades de tejido; 25 kg leña (× 1,6 en invierno) | por persona y mes | 09 · "Nivel de vida y cestas" · "Cestas del periodo 1300–1600" |
| Cesta de comodidad — estrato bajo (adicional) | 4 GE (carne, pescado, legumbres); 3 l vino o cerveza; 0,1 unidades de tejido | por persona y mes | 09 · "Cestas del periodo 1300–1600" |
| Cesta de lujo — estrato bajo (adicional) | Raro; 0,05 unidades de paño fino | por persona y mes | 09 · "Cestas del periodo 1300–1600" |
| Cesta de subsistencia — estrato medio | Igual que el bajo + 0,2 unidades de tejido | por persona y mes | 09 · "Cestas del periodo 1300–1600" |
| Cesta de comodidad — estrato medio | 8 GE variados; 6 l vino; 0,3 unidades de paño; servicios urbanos 0,3 uc | por persona y mes | 09 · "Cestas del periodo 1300–1600" |
| Cesta de lujo — estrato medio | 0,1 unidades de seda o paño fino; 10 g especias; 0,5 uc en servicios | por persona y mes | 09 · "Cestas del periodo 1300–1600" |
| Cesta de subsistencia — estrato alto | Igual que el medio | por persona y mes | 09 · "Cestas del periodo 1300–1600" |
| Cesta de comodidad — estrato alto | 15 GE variados; 10 l vino; 0,6 unidades de paño; 1,5 uc en servicios | por persona y mes | 09 · "Cestas del periodo 1300–1600" |
| Cesta de lujo — estrato alto | 0,4 unidades de seda; 60 g especias; 0,2 kg azúcar; 4 uc en servicios y objetos | por persona y mes | 09 · "Cestas del periodo 1300–1600" |
| Cesta — élite | Subsistencia: igual que el alto; comodidad: igual que el alto × 1,5; lujo: 1,5 unidades de seda; 200 g especias; 1 kg azúcar; 20 uc en servicios, joyas y patronazgo | por persona y mes | 09 · "Cestas del periodo 1300–1600" |
| GE (grano equivalente) | 1 GE = aporte calórico de 1 kg de trigo; equivalencias: 1 kg pescado = 0,45 GE; 1 kg carne = 0,70 GE; 1 kg arroz = 1,05 GE; 1 kg legumbres = 0,95 GE | kg por GE | 09 · "Nivel de vida y cestas" y nota de "Sustitución dentro de una categoría" |
| Cuota de sustitución de alimento | Proporcional a `preferencia_cultural × (1/precio_por_GE)²` | — | 09 · "Sustitución dentro de una categoría" |
| Nivel de vida (NV) | `NV = cobertura_subsistencia + cobertura_comodidad + cobertura_lujo`, cada una 0–1; rango almacenado 0–3,00 | — | 09 · "Nivel de vida y cestas"; campo `living_standard` 0–30.000 pb. |
| Gasto mensual de riqueza para sostener subsistencia | Bajo 20 %, Medio 10 %, Alto 5 %, Élite 5 % | de la riqueza al mes | 09 · "Ingresos y gasto de una cohorte" |
| Propensión a ahorrar el excedente | Bajo 10 %, Medio 25 %, Alto 40 %, Élite 30 % | del excedente | 09 · "Ingresos y gasto de una cohorte" |
| Coste de la cesta de subsistencia del estrato bajo | ≈ 0,23 uc/persona/mes (≈ 0,14 alimento + 0,01 sal + 0,024 aceite + 0,03 tejido + 0,03 leña); ≈ 2,8 uc/año por persona; 12–14 uc por hogar campesino | uc | 10 · "Precios base del slice (1300–1600)" (comprobación de órdenes de magnitud) |
| Salario de referencia del jornalero urbano | 1,2–1,8 | uc/mes | 10 · "Precios base del slice (1300–1600)" (comprobación de órdenes de magnitud) |
| Mortalidad bruta en años normales | 30–40 ‰ anual (media ponderada de franjas ≈ 36,5 ‰; base mensual ≈ 3,0 ‰) | ‰ | 09 · "Modelo demográfico (propuesto)" y "Estructura de edad" |
| Natalidad bruta orientativa | 35–45 ‰ anual (≈ 40 ‰) | ‰ | 09 · "Modelo demográfico (propuesto)" |
| Fracción de adultos | ~55 % | de la población | 09 · "Modelo demográfico (propuesto)" |
| `f_vida` (natalidad) por NV | NV 0,50→0,80; 0,80→0,95; 1,00→1,00; 1,50→1,04; 2,00→1,02; 3,00→0,95 | multiplicador | 09 · "Funciones de modificación (tablas por tramos)" |
| `g_alimentos` (mortalidad) por cobertura alimentaria | 1,00→1,00; 0,90→1,15; 0,80→1,50; 0,70→2,20; 0,60→3,50; 0,50→5,50; ≤0,40→8,00 | multiplicador | 09 · "Funciones de modificación (tablas por tramos)" |
| `f_paz` (natalidad) por seguridad | 1,00→1,00; 0,70→0,95; 0,40→0,85; 0,10→0,70 | multiplicador | 09 · "Funciones de modificación (tablas por tramos)" |
| Factores de salud sobre mortalidad | Ciudad > 20.000 hab. sin saneamiento ×1,15; acueducto y cloacas ×1,05; saneamiento moderno ×0,85; medicina básica ×0,80 (niños); vacunación ×0,60 (niños); antibióticos ×0,70 | multiplicador | 09 · "Funciones de modificación (tablas por tramos)" |
| Regla de hambruna de referencia | Cobertura del 70 % durante 6 meses ⇒ mortalidad mensual de ≈ 3,0 ‰ a ≈ 6,7 ‰ (exceso ≈ 22 ‰, un 2,2 % de población en medio año) | — | 09 · "Funciones de modificación" (comprobación de la regla de hambruna de la v0.6) |
| Atractivo migratorio | `0,40 × salario_real/salario_real_ref + 0,25 × seguridad + 0,20 × tolerancia + 0,15 × tierra_libre` | — | 09 · "Migración detallada" |
| Fricción y β de movilidad social | Campesino→jornalero β 0,010, fricción 0,15; jornalero→artesano β 0,004, fricción 0,30 (capital 2 uc/persona); artesano→mercader β 0,002, fricción 0,40 (capital 20 uc/persona, alfabetización ≥ 20 %); →clero β 0,001, fricción 0,20; mercader→banquero β 0,0005, fricción 0,50 (capital 200 uc/persona) | mensual | 09 · "Movilidad social detallada" |
| Huida (dependientes o esclavizados) | Probabilidad mensual 0,2–2 % según agravio, control efectivo y cercanía de refugio | mensual | 09 · "Migración detallada" |

## TABLA 3 — Criterios de validación (Anexo F) y datos de mercado (Anexo AK)

### Anexo F · Objetivos de calibración aplicables al prototipo económico

| Métrica | Objetivo | Grupo |
| --- | --- | --- |
| Variación anual del precio del grano en años sin crisis | ≤ ±25 % | Salud del mundo |
| Bancarrotas por Estado y siglo (mediana) | ≤ 1,5 | Salud del mundo |
| Población total del slice tras la peste respecto a antes | 50–80 % | Salud del mundo |
| Recuperación de la población anterior a la peste | Entre 80 y 200 años | Salud del mundo |
| Guerras activas por década en el slice (mediana) | 3–8 | Salud del mundo |
| Duración media de una guerra | 1–6 años | Salud del mundo |
| Estados destruidos que se restauran alguna vez | 5–25 % | Salud del mundo |
| IA bloqueadas (sin acciones válidas durante un año) | 0 | Salud del mundo |
| Violaciones de invariantes | 0 | Salud del mundo |

Pruebas económicas específicas definidas en la sección 10 ("Invariantes y pruebas específicas"), usables como criterios del prototipo:

| Prueba | Criterio |
| --- | --- |
| `economy_closed_100y` | Conservación exacta de bienes y dinero en un escenario cerrado sin comercio externo. |
| `harvest_shock` | Una cosecha −40 % en un mercado aislado sube el precio entre +40 % y +90 % en 20 semanas y vuelve al ±15 % del base en dos cosechas normales. |
| `transport_gradient` | Con una sola fuente de grano, el precio aumenta con la distancia según la tabla de costes (±5 %). |
| `debasement_detection` | Una devaluación del 20 % se refleja en precios en 12 ± 4 meses en un mercado con cambistas. |
| `tax_farm_tradeoff` | El arrendamiento aumenta la liquidez inmediata y reduce la recaudación anual entre un 15 % y un 30 %. |
| `default_creditors` | Un impago reduce exactamente la riqueza de los acreedores registrados por el importe impagado. |
| `investment_response` | Si el precio de un bien sube un 50 % durante dos años, la capacidad de producción privada aumenta en el mercado sin intervención del Estado. |

Pruebas de población relacionadas (sección 09): `pop_stability_200y` (sin crisis, la población varía entre −10 % y +40 % en 200 años) y `famine_response` (cobertura 0,6 durante 6 meses produce un exceso de mortalidad del 3 % al 6 %).

### Anexo AK · Mercados de la vertical (datos de partida, 1300)

| Mercado | Controlador en 1300 | Población urbana (miles) | Exporta | Importa | Grano inicial (uc/t) | Conexiones principales |
| --- | --- | --- | --- | --- | --- | --- |
| Constantinopla | Bizancio | 100 (confianza B) | Seda, manufacturas de lujo, servicios | Grano, pescado, sal, pieles, esclavos (sistema de población) | 10,5 | Pera, Tesalónica, Bursa, Caffa, Venecia (ext.), Génova (ext.) |
| Tesalónica | Bizancio | 40 | Grano de Macedonia, vino, paño | Especias, sal | 8,5 | Constantinopla, Skopie, Negroponte, Ragusa |
| Caffa | Génova | 20 | Grano, pescado salado, pieles, cera, personas esclavizadas (sistema de población) | Paño, vino, sal | 6,5 | Tana, Sarai (ext.), Constantinopla, Trebisonda |
| Bursa (Prusa) | Bizancio (hasta su posible caída) | 15 | Seda en bruto, fruta | Grano | 9,0 | Constantinopla, Nicea, Konya |
| Candía | Venecia | 25 | Vino, grano, queso | Paño, madera | 8,5 | Venecia (ext.), Negroponte, Modón-Corón, Alejandría (ext.) |

Otros mercados del Anexo AK útiles para rutas del prototipo: Pera (15 miles, grano 10,5 compartido con Constantinopla), Konya (25; grano 7,5), Esmirna-Focea (20; 8,5), Antalya (10; 8,0), Trebisonda (40; 9,5), Sinope (10; 9,0), Tana (8; 6,0), Tarnovo (15; 7,0), Skopie (15; 7,5), Ragusa (8; 10,0), Buda (10; 6,0), Negroponte (10; 8,5), Modón-Corón (6; 9,0), Famagusta (30; 9,0), Ayas (15; 8,5). Externos: Tabriz (200, C), Alejandría (100, C), Sarai (75, C), Venecia (100, B), Génova (60, B) — con precios de recorrido aleatorio acotado y capacidad de absorción por bien.

## HUECOS

Valores necesarios para el prototipo que **no aparecen en el documento maestro** y deben tratarse como supuestos explícitos (registrarlos como confianza D y anotarlos en el diario):

1. **Existencias iniciales por bien y mercado.** El Anexo AK da el precio inicial del grano pero no el nivel de almacenes de partida; el ejemplo numérico asume existencias al 100 % del objetivo (semana 0). No hay valores para ningún bien ni mercado.
2. **`semanas_de_reserva` para bienes distintos del grano.** `eco.stock.grain_weeks = 26` es el único valor; pescado salado, sal, aceite, vino, lana, paño, hierro, madera y leña carecen de objetivo de existencias.
3. **El "mínimo" de la fórmula de presión** `(demanda − oferta) / max(oferta, mínimo)` no tiene valor numérico definido.
4. **Equivalencia explícita GE→kg de grano de consumo.** La cesta pide 16 GE/mes y la comprobación agraria implica 192 kg/persona/año (= 16 kg/mes con 1 GE = 1 kg de trigo), pero no está declarado como parámetro de consumo mensual por estrato en unidades de bien.
5. **Distribución de la cosecha dentro de los meses de cosecha** (p. ej. junio–julio: ¿mitad y mitad? ¿proporción fija por semana?) y el reparto mensual exacto de la producción anual por edificio.
6. **Salarios por ocupación y edificio.** Solo existe el rango del jornalero urbano (1,2–1,8 uc/mes); faltan salarios de campesinos, artesanos, mineros, pescadores y el reparto del valor añadido entre salarios, renta e impuestos (se dice "según las leyes y la propiedad" sin coeficientes).
7. **Producción de edificios sin tabla de referencia:** aserradero/madera, mina de hierro, producción de leña (carbones), huertas de regadío (hortalizas), cueros y queso; el Anexo K lista los edificios pero sin rendimientos por nivel.
8. **Capacidad de almacenamiento física** (graneros, depósitos) por mercado o edificio: no hay parámetro; las existencias solo tienen objetivo en semanas.
9. **Consumo de forraje del ganado** y la relación entre el bien "ganado" (Anexo K) y la cesta (el estrato bajo pide 4 GE de "carne, pescado, legumbres"); no hay conversión cabeza de ganado → t de carne para el bien del slice.
10. **Elasticidad precio de la demanda** como tal no existe: solo la sustitución dentro de categoría con `(1/precio_por_GE)²`; falta cómo responde el consumo total cuando cambia el ingreso real o el precio de toda la categoría.
11. **Capacidad de las rutas** (`capacidad_ruta_libre`), peajes concretos por estrecho/puerto y prima de riesgo por ruta concreta de partida (solo hay rangos genéricos para el Egeo).
12. **Capital mercantil inicial por mercado** y su composición (riqueza de cohortes + crédito): sin valores de partida.
13. **Masa monetaria inicial por Estado o mercado y velocidad de circulación** (`velocidad` en `nivel_objetivo = masa_monetaria × velocidad / producción_real` no tiene valor de partida).
14. **Demanda semanal agregada por mercado:** la fórmula usa `demanda_semana`, pero no se define cómo se desagrega el consumo mensual de las cohortes a semanas ni cómo se suman exportaciones y compras para existencias.
15. **Población total del hinterland de cada mercado** (el Anexo AK da solo población urbana): el consumo que presiona los precios es el de la región económica, no solo el de la ciudad.
16. **Escala del estrato (reparto de la población entre bajo/medio/alto/élite)** por provincia o mercado en 1300.
17. **Equivalencia entre "unidades de paño" de las cestas y "piezas (~30 m)" del precio base** (la cesta del estrato medio pide 0,3 "unidades de paño" sin definir cuántos metros son).
18. **Precio base de la cerveza** (la cesta admite "vino o cerveza"; la cerveza está en el Anexo K pero no en la tabla de precios base).
19. **Pérdidas o deterioro de bienes durante el transporte** (además del coste monetario y del riesgo de pérdida total por piratería/guerra).
20. **Tipo de interés local base** para el umbral de inversión (`interés + riesgo + 3 %`): falta el valor de partida por mercado/época (los intereses de deuda pública sí tienen tabla, pero no el interés mercantil local).
21. **`preferencia_cultural` inicial por cultura** para la sustitución de alimentos.
22. **`productividad` de partida y sus modificadores** (tecnología, infraestructura, rasgos culturales, control efectivo, daño de guerra) en forma numérica.
23. **Dotación inicial de riqueza por cohorte/estrato** y dinero en efectivo por mercado (afecta a la demanda efectiva y al capital invertible).
24. **Precio base del pescado en GE** para la cesta: la equivalencia 0,45 GE/kg existe, pero no qué fracción del confort la cubre pescado frente a carne y legumbres por defecto.
25. **Rendimiento de la pesca fuera de la temporada del mar Negro** (abril–noviembre) y calendario pesquero del Egeo/Mediterráneo oriental.
