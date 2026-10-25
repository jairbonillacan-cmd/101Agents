# ADR 0004: Orden fijo de fases del tick, diferimiento de comandos de IA y hash canónico de estado BLAKE3

- **Estado:** propuesto
- **Fecha:** 2026-10-24
- **Autoría:** Agente de Arquitectura (`role:architecture`) — tareas T-109, T-110 (Fase 0/1)
- **Relacionado con:** Documento maestro v0.7 §§ 17, 21, 23, 25, 45; Anexo B (D-017, D-018); Anexo P (T-109, T-110, T-111); Anexo T (QA-CORE-01 a QA-CORE-04); Anexo X; Anexo AM; Anexo AR; ADR 0002; `docs/specs/apply-and-invariants.md`

## Contexto

El motor **101 Engine** tiene como principio innegociable el **determinismo estricto bit a bit** (Documento maestro v0.7 § 2.1, § 23 y Anexo B, D-017/D-018): el mismo binario compilado con los mismos datos base (`content_hash`), la misma semilla (`seed: u64`) y la misma secuencia de comandos (`StampedCommand`) debe producir exactamente el mismo estado en cualquier plataforma (`x86_64` o `ARM64`, Windows, Linux o macOS), con cualquier número de hilos de trabajo (1, 2, 4, 8 o 16) y tras guardar y recargar la partida en cualquier día $d$ (§ 23, líneas 4954–4961; § 25).

Para que `e101-sim` (T-109) y `e101-save` (T-110) garanticen este contrato sin condiciones de carrera ni dependencias del entorno de ejecución, necesitamos fijar formalmente tres piezas arquitectónicas:

1. **El calendario de ejecución interna del tick diario (§ 21, D-017, Anexo AM):** En qué orden exacto se ejecutan los sistemas de simulación durante un día (`Day`), qué datos lee y escribe cada fase y cómo se sincronizan la lectura paralela inmutable (`&State`) y la aplicación determinista de cambios (`Deltas` → `&mut State`).
2. **El acoplamiento temporal de la inteligencia artificial (§ 17, § 21 línea 4730, D-017, Anexo AM línea 9583):** Cómo interactúa la evaluación de `e101-ai` con el estado del mundo sin introducir efectos instantáneos intratick, dependencias del orden de iteración de países ni bloqueos en el paralelismo por lotes.
3. **La función de resumen criptográfico del estado (`state_hash`, § 23 líneas 4943–4952, D-018, Anexo X, Anexo AM, Anexo AR):** Qué algoritmo se emplea, cómo se serializa canónicamente cada tabla persistente con independencia de `#[repr(Rust)]` y de la arquitectura de CPU, qué datos derivados se excluyen expresamente y cómo se estructura el hash en dos niveles (por tabla y global) para permitir el diagnóstico inmediato de divergencias (`cargo xtask golden --bisect`).

---

## Decisión

### 1. Orden fijo de sistemas dentro del tick diario (18 fases, `Fase 0` a `Fase 17`)

El bucle de simulación (`e101_sim::run_tick`) avanza el mundo de `Day(d)` a `Day(d + 1)` ejecutando una secuencia estricta de **18 fases numeradas de `0` a `17`** (Documento maestro v0.7 § 21, líneas 4705–4728; Anexo B, D-017; Anexo AM, líneas 9573–9585).

**Este orden es fijo y forma parte del contrato de determinismo del motor (§ 21, línea 4707):** alterar el orden de dos fases, dividir una fase o mover un sistema de una fase a otra modifica los hashes dorados y requiere obligatoriamente un nuevo ADR aprobado por el rol de Arquitectura y la etiqueta `golden-change` en el PR.

#### 1.1. Tabla canónica de las 18 fases del tick diario (§ 21, líneas 4709–4728)

| Fase | Sistema | Frecuencia | Lee | Escribe |
| --- | --- | --- | --- | --- |
| **0** | **Comandos** | Diaria | Diario de comandos | Validación; deltas de órdenes |
| **1** | **Clima y estación** | Diaria (cambio de estación); anual (anomalías) | Calendario, semilla | Estado climático |
| **2** | **Movimiento militar y naval** | Diaria | Ejércitos, grafo de viaje | Posiciones, llegadas |
| **3** | **Batallas y asedios** | Diaria | Ejércitos en contacto, fortificaciones | Bajas, moral, progreso de asedio |
| **4** | **Suministro militar** | Diaria | Ejércitos, provincias | Consumo, desgaste |
| **5** | **Epidemias** | Semanal escalonada por provincia | Población, tráfico | $S, I, R$, fallecidos |
| **6** | **Mercados y comercio** | Semanal escalonada por mercado | Oferta, demanda, rutas | Precios, flujos, existencias |
| **7** | **Producción y consumo** | Mensual escalonada por provincia; cosechas en su mes | Edificios, cohortes, precios | Bienes, ingresos, NV |
| **8** | **Demografía y migración** | Mensual escalonada por provincia | Cohortes, NV, seguridad | Nacimientos, muertes, flujos |
| **9** | **Finanzas públicas** | Mensual escalonada por Estado | Recaudación, gastos | Tesoro, deuda |
| **10** | **Política** | Mensual escalonada por Estado | Grupos, leyes, legitimidad | Presión, demandas, etapas de reformas |
| **11** | **Diplomacia** | Mensual escalonada por Estado; tratados al vencer | Relaciones, tratados | Relaciones, vencimientos |
| **12** | **Tecnología** | Mensual escalonada por Estado; adopción trimestral | Instituciones, contactos | Progreso, cuotas |
| **13** | **Personajes** | Mensual (salud y edad); diaria para muertes | Personajes | Muertes, nacimientos, sucesiones |
| **14** | **101 History** | Mensual escalonada por situación; divergencia anual | Estado agregado | Activación, etapas, sesgos |
| **15** | **IA** | Según capas (§ 17) | Mundo estimado | Comandos para el día siguiente |
| **16** | **Registro causal e índices** | Diaria | Deltas aplicados | Contribuciones, agregados |
| **17** | **Invariantes y hash** | Diaria en pruebas; mensual en partida | Estado | Informe, hash |

#### 1.2. Semántica de lectura inmutable paralela y aplicación determinista entre fases (§ 21, § 23, `docs/specs/apply-and-invariants.md`)

Cada fase $k \in \{0, \dots, 15\}$ se ejecuta en dos subetapas separadas por una barrera de sincronización explícita (§ 21, líneas 4705–4707 y 4730; § 23, líneas 4935–4941):

1. **Subetapa de cálculo (`run`):**
   - Los sistemas registrados en la fase $k$ tienen la firma obligatoria `fn run(state: &State, deltas: &mut Deltas)`.
   - Ningún sistema puede mutar `State` directamente. Si la fase procesa lotes de entidades independientes (provincias en las Fases 5, 7 y 8; mercados en la Fase 6; Estados en las Fases 9 a 12; situaciones en la Fase 14), el planificador de hilos evalúa en paralelo las entidades cuyo predicado de escalonamiento temporal (`should_run_weekly`, `should_run_monthly`, `should_run_quarterly`, `should_run_yearly`, definidos en `e101-time` según ADR 0002) sea verdadero en `state.time.day`.
   - Cada hilo de trabajo recibe una referencia compartida `&State` y escribe sus propuestas de cambio en un búfer local `LocalDeltas`.
   - Toda extracción pseudoaleatoria dentro de una fase utiliza exclusivamente `e101_rng::rng(state.seed, system_id, entity_id, state.time.day)` (§ 23, línea 4932), garantizando secuencias idénticas con independencia del hilo que procese la entidad.
2. **Subetapa de reducción y aplicación (`apply`):**
   - Al concluir el cálculo paralelo de la fase $k$, el recolector fusiona todos los `LocalDeltas` en el contenedor `Deltas` de la fase y los **ordena por clave canónica total**: `(TargetId, DeltaKind, SourceOrder)` (§ 23, líneas 4935–4940; `docs/specs/apply-and-invariants.md`).
   - La función `apply_phase_deltas(state: &mut State, phase: PhaseId, deltas: &Deltas, ledger: &mut LedgerCollector)` aplica secuencialmente los deltas ordenados sobre `state`, utilizando aritmética saturada/verificada de punto fijo (`Money`, `Qty`, `Ratio`) y emitiendo las entradas correspondientes para `e101-ledger`.
   - Solo cuando `apply_phase_deltas` termina queda consolidado el nuevo `State` que leerá de forma inmutable la fase $k + 1$.

Las **Fases 16 y 17** cierran el tick:
- En la **Fase 16**, `e101-ledger` consolida las contribuciones causales (`ContributionEntry`) generadas por las Fases 0 a 14 y actualiza los índices agregados de lectura.
- En la **Fase 17**, el verificador ejecuta las comprobaciones de invariantes contables y de dominio (`check_invariants(state)`, Anexo X y `docs/specs/apply-and-invariants.md`) y, cuando corresponde según la frecuencia configurada, calcula el `StateHashReport`.

---

### 2. Regla de la IA: «la IA del día $d$ se aplica en $d + 1$» (§ 21 línea 4730, D-017, Anexo AM línea 9583)

Para integrar `e101-ai` sin comprometer el determinismo ni la arquitectura orientada a comandos (Principio 2 de `AGENTS.md`: *Comandos, no mutaciones*), se establece la regla estricta de diferimiento de un día (**Anexo B, D-017; § 21, línea 4730; Anexo AM, línea 9583**):

1. **Evaluación sobre estado consolidado del día $d$:**
   - La Fase 15 (`IA`) se ejecuta después de que todas las fases de simulación física, económica, demográfica, política, diplomática, militar, de personajes e histórica del día $d$ (Fases 0 a 14) hayan aplicado sus deltas.
   - Cada país controlado por la IA recibe únicamente su vista estimada e inmutable del mundo (`View` proyectada desde `&State` en el día $d$, respetando niebla de guerra e información imperfecta según § 17) y un presupuesto de cómputo acotado (`ai.budget.share_of_tick <= 25 %`, Anexo AI).
2. **Emisión exclusiva de comandos sellados para `Day(d.0 + 1)`:**
   - La Fase 15 **no emite `Deltas` sobre `State`** ni modifica ninguna tabla de simulación del mundo (salvo la memoria interna persistente `ai_memory` del propio agente, actualizada por clave estable de `PolityId`).
   - Todas las decisiones operativas, diplomáticas, económicas o militares tomadas por la IA en el día $d$ se emiten como comandos tipados `StampedCommand` cuya marca temporal es obligatoriamente:
     $$\text{cmd.day} = \text{Day}(d + 1)$$
   - Dichos comandos se insertan en la cola de comandos pendientes (`CommandLog`) ordenados canónicamente por `(Day(d + 1), ActorId, SequenceNumber)`.
3. **Validación y aplicación en la Fase 0 del día $d + 1$:**
   - Al comenzar el tick del día $d + 1$, la **Fase 0 (`Comandos`)** extrae todos los `StampedCommand` con `cmd.day == Day(d + 1)` —tanto los emitidos por jugadores humanos como los generados por la IA en la Fase 15 del día $d$—, los valida contra las precondiciones de `State` y emite los `Deltas` de órdenes correspondientes.

**Justificación y garantías arquitectónicas (§ 17, § 21, D-017):**
- **Ausencia de reacción instantánea intratick:** Ningún país controlado por la IA puede observar ni reaccionar en el mismo día $d$ a los efectos de sus propias órdenes ni a las órdenes emitidas por otros países en ese mismo instante.
- **Paralelismo 100 % libre de carreras en la Fase 15:** Como ningún agente de IA muta el estado del mundo que leen los demás agentes durante la Fase 15, la evaluación de todos los Estados del mapa es completamente independiente y paralelizable por `PolityId`.
- **Invarianza respecto al orden de evaluación:** El resultado del tick es idéntico bit a bit sin importar en qué orden el planificador de hilos evalúe los países en la Fase 15, ya que los comandos emitidos se ordenan por `(Day(d + 1), ActorId, SequenceNumber)` antes de entrar en la Fase 0 del día siguiente.
- **Simetría con el sistema de guardado y repetición (`replay`):** Un archivo de guardado o un registro de `replay` que capture la secuencia de `StampedCommand` reproduce exactamente el mismo comportamiento que la partida original (§ 25).

---

### 3. Hash de estado BLAKE3 global y por tabla (§ 23 líneas 4943–4952, D-018, Anexo X, Anexo AM, Anexo AR)

Para verificar el determinismo en pruebas, ejecuciones doradas (`cargo xtask golden`), partidas multijugador/laboratorio y archivos de guardado (`e101-save`), se define el sistema de resumen criptográfico canónico `state_hash` (**§ 23, líneas 4943–4952; Anexo B, D-018; Anexo X; Anexo AM; Anexo AR**).

#### 3.1. Algoritmo criptográfico: BLAKE3 de 256 bits

Se elige **BLAKE3** con salida estándar de 256 bits (`[u8; 32]`) por tres motivos técnicos (§ 23, línea 4945; D-018):
1. **Rendimiento:** Su estructura en árbol de Merkle permite alcanzar varios GB/s con instrucciones SIMD modernas sin comprometer la seguridad criptográfica frente a colisiones.
2. **Determinismo y pureza de compilación:** Implementación 100 % en Rust seguro (`blake3` crate sin dependencias de C/C++), garantizando salidas idénticas en `x86_64` y `ARM64`.
3. **Composición jerárquica nativa:** Permite calcular en paralelo el hash de cada tabla de estado y combinarlos de forma determinista en un único hash raíz.

#### 3.2. Estructura en dos niveles: `TableHashes` y `state_hash` global

El cálculo del hash de estado (`compute_state_hash(state: &State) -> StateHashReport`) se organiza en dos niveles jerárquicos (§ 23, líneas 4947–4951; Anexo X; Anexo AM, línea 9585; Anexo AR, línea 9787):

1. **Nivel 1 — Hashes independientes por tabla (`TableHashes`):**
   Se calcula un hash BLAKE3 de 32 bytes (`[u8; 32]`) para cada una de las **12 secciones persistentes** que componen `State` (alineadas exactamente con el formato de guardado del Anexo AR, línea 9787, y el verificador del Anexo X):

   | Índice | Nombre canónico de sección | Contenido persistente resumido |
   | --- | --- | --- |
   | 0 | `time` | Día actual (`Day`), contador de ticks y estado de calendario (`e101-time`) |
   | 1 | `map_dynamic` | Estado dinámico de celdas/provincias, clima activo, uso del suelo e infraestructura mutable (`e101-map`, `e101-sim`) |
   | 2 | `entities` | Tabla maestra de entidades políticas (`Polity`), asentamientos e identificadores activos (`e101-store`) |
   | 3 | `population` | Tablas SoA de cohortes demográficas (`CohortTables`), alfabetización, nivel de vida (`NV`) y flujos migratorios |
   | 4 | `economy` | Mercados, precios (`Money`), inventarios (`Qty`), edificios productivos y rutas comerciales |
   | 5 | `politics` | Grupos de interés, leyes vigentes, legitimidad, estabilidad y progreso de reformas |
   | 6 | `diplomacy` | Relaciones bilaterales, tratados activos, treguas, alianzas y fechas de vencimiento |
   | 7 | `military` | Ejércitos, armadas, guarniciones (`MilitaryTables`), posiciones, moral, suministro y asedios en curso |
   | 8 | `characters` | Personajes activos, atributos, salud, edad, cargos y líneas de sucesión |
   | 9 | `history` | Estado de situaciones históricas (`e101-history`), etapas activas, banderas de disparo único y puntaje de divergencia |
   | 10 | `ledger_summary` | Resumen agregado determinista de contabilidad causal (`e101-ledger`) necesario para invariantes y continuidad |
   | 11 | `ai_memory` | Memoria persistente de planes, intenciones y compromisos de los agentes de IA (`e101-ai`) |

2. **Nivel 2 — Hash global (`state_hash: [u8; 32]`):**
   El hash global del estado se obtiene aplicando `blake3::hash` sobre un bloque maestro de tamaño fijo (**408 bytes**) construido exactamente en este orden (§ 23, línea 4948):
   - `canonical_format_version: u32` en little-endian (4 bytes; versión del esquema de serialización canónica),
   - `day: i32` en little-endian (4 bytes; valor interno de `state.time.day.0`),
   - `seed: u64` en little-endian (8 bytes; semilla maestra de la partida `state.seed`),
   - `command_count: u64` en little-endian (8 bytes; contador acumulado de `StampedCommand` aplicados desde el inicio de la partida hasta el tick actual inclusive),
   - seguido de la concatenación en el orden fijo `0..12` de los 12 hashes de 32 bytes de `TableHashes` ($12 \times 32 = 384\text{ bytes}$).

```rust
pub struct TableHashes {
    pub time: [u8; 32],
    pub map_dynamic: [u8; 32],
    pub entities: [u8; 32],
    pub population: [u8; 32],
    pub economy: [u8; 32],
    pub politics: [u8; 32],
    pub diplomacy: [u8; 32],
    pub military: [u8; 32],
    pub characters: [u8; 32],
    pub history: [u8; 32],
    pub ledger_summary: [u8; 32],
    pub ai_memory: [u8; 32],
}

pub struct StateHashReport {
    pub day: Day,
    pub command_count: u64,
    pub state_hash: [u8; 32],
    pub tables: TableHashes,
}
```

#### 3.3. Exclusiones expresas del `state_hash` (§ 23, línea 4949)

Para garantizar que el hash dependa única y exclusivamente de la verdad lógica persistente de la simulación y sea invariante tras guardar/recargar (`save` / `load`), **se excluyen expresamente** del cálculo de `TableHashes` y de `state_hash` (§ 23, línea 4949; Anexo AR):

1. **Índices derivados y cachés reconstruibles:** Cachés de caminos mínimos Dijkstra/A* de `e101-map`, tablas espaciales auxiliares, índices invertidos de consulta rápida y proyecciones `View` generadas para el cliente o la IA. Todos ellos se reconstruyen de manera determinista a partir de las 12 tablas persistentes al cargar una partida.
2. **Búfer circular detallado de los últimos meses del registro causal (`e101-ledger`):** El historial pormenorizado de explicaciones de UI de los últimos meses puede recortarse o configurarse sin afectar a la evolución futura del mundo; en el hash entra únicamente la sección `ledger_summary` (totales acumulados y balances necesarios para la verificación de invariantes contables).
3. **Estado efímero del cliente o del ejecutor:** Número de hilos de trabajo, tiempos de reloj de pared (`std::time::Instant`), telemetría de rendimiento, estado de cámara o selección de interfaz.

#### 3.4. Formato binario canónico de serialización hacia el hasher (§ 23, línea 4948)

Nunca se vuelca memoria cruda (`std::slice::from_raw_parts`) ni se depende del layout en memoria de Rust (`#[repr(Rust)]`). Cada tabla implementa el trait interno `CanonicalHashWrite`, que escribe bytes en el `blake3::Hasher` siguiendo estas reglas estrictas (§ 23, línea 4948):

- **Orden de bytes (*endianness*) y ausencia de relleno (*padding*):** Todos los enteros primitivos (`u8`, `u16`, `u32`, `u64`, `i8`, `i16`, `i32`, `i64`) y los tipos de punto fijo de `e101-store::fixed` (`Money(i64)`, `Qty(i64)`, `Ratio(i32)`) se escriben en **little-endian** (`to_le_bytes()`), contiguos y sin bytes de alineación.
- **Booleanos y enumerados:** `bool` se codifica como un único `u8` (`0x00` para `false`, `0x01` para `true`). Todo `enum` se codifica escribiendo primero su discriminante entero explícito (`u16` o `u32` en little-endian) seguido de los campos canónicos de la variante activa.
- **Identificadores tipados (`Id<T>` y `GenId<T>`):** `Id<T>(u32)` escribe su `u32` en little-endian; `GenId<T> { index: u32, generation: u32 }` escribe `index.to_le_bytes()` seguido de `generation.to_le_bytes()`. `Option<T>` escribe una etiqueta `u8` (`0x00` = `None`, `0x01` = `Some`) seguida del valor canónico cuando es `Some`.
- **Recorrido determinista de tablas SoA (`0..len`):** Toda columna o tabla indexada por `Id<T>` se recorre estrictamente en **orden ascendente de identificador** (`0..len`), precedida por la longitud `len as u64` en little-endian.
- **Recorrido canónico de `SlotMap` generacionales (`CohortTables`, `MilitaryTables`):** En las tablas dinámicas con alta rotación respaldadas por slotmaps generacionales (ADR 0002), se escribe primero la capacidad/longitud lógica de slots (`u64` LE) y la cabeza de la lista libre determinista, y a continuación se recorren **todos los slots en orden de índice `0..capacity`**, escribiendo para cada slot `(occupied: u8, generation: u32 LE, payload_canónico_si_ocupado)`. De este modo, las generaciones de slots libres y ocupados quedan reflejadas en el hash y se preservan intactas tras guardar y cargar.
- **Colecciones asociativas permitidas:** Cualquier `BTreeMap<K, V>` o `BTreeSet<K>` se precede de su número de elementos (`u64` LE) y se recorre en el orden ascendente natural de su clave `K`. (`HashMap` y `HashSet` están prohibidos en los crates de simulación por `AGENTS.md` § 3).

#### 3.5. Frecuencia de cálculo y uso en guardado/carga (§ 23, línea 4950; § 25)

La Fase 17 (`Invariantes y hash`) calcula `StateHashReport` con la siguiente cadencia (§ 23, línea 4950):
- **En pruebas unitarias/integración, CI y ejecuciones doradas (`cargo xtask golden`):** **Cada tick diario** (todos los días $d$).
- **En partida normal del jugador:** **En el cierre mensual** (cuando `is_month_end(state.time.day)` es verdadero) para minimizar el coste por fotograma manteniendo detección temprana de anomalías.
- **En guardado y carga (`e101-save`, § 25, Anexo AR):** **Siempre.** Al guardar una partida, se calcula `state_hash` y se almacena en `SaveHeader.state_hash`; al cargar un archivo `.e101save`, `e101-save` reconstruye `State`, recalcula `compute_state_hash(&state)` y verifica que coincide bit a bit con `SaveHeader.state_hash` antes de reanudar la simulación.

---

## Alternativas consideradas

| Alternativa | Ventajas | Inconvenientes |
| --- | --- | --- |
| **1. Orden fijo de 18 fases + IA diferida a $d + 1$ + BLAKE3 canónico en dos niveles (Elegida)** | Determinismo bit a bit independiente del número de hilos y de la CPU; paralelismo completo en la Fase 15 de IA; localización inmediata de divergencias por día y por tabla (`TableHashes`); verificación instantánea al guardar/cargar. | Requiere mantener implementaciones de escritura canónica (`CanonicalHashWrite`) sincronizadas con el esquema de las 12 tablas de `State`; las órdenes de la IA tienen una latencia mínima de 1 tick diario (imperceptible a escala histórica). |
| **2. Grafo dinámico de sistemas resuelto en tiempo de ejecución (estilo ECS generalista con planificación automática)** | Flexibilidad para insertar sistemas sin asignarles un número de fase explícito. | El orden efectivo de aplicación de deltas puede cambiar sutilmente al añadir sistemas nuevos, rompiendo hashes dorados y dificultando la auditoría causal y la bisección de fallos. Descartada (§ 21, D-017). |
| **3. Aplicar las decisiones de la IA dentro del mismo día $d$ en la Fase 15** | Los países controlados por la IA reaccionan en el mismo tick en que se produce un suceso. | Rompe la separación entre fase de comandos (Fase 0) y fases de simulación; obliga a evaluar los países secuencialmente o introduce condiciones de carrera cuando dos IA modifican el mismo mercado o frente en el día $d$; complica la reproducción por diario de comandos. Descartada (§ 21 línea 4730, D-017). |
| **4. Calcular el hash sobre el volcado directo de memoria (`#[repr(C)]`) o sobre el flujo comprimido de `postcard` usando `SipHash`/`xxHash`** | Menor código de serialización específica para el hash. | `#[repr(C)]` puede incluir bytes de relleno (*padding*) no inicializados y depende del *endianness* de la arquitectura; `SipHash`/`xxHash` de 64 bits tienen mayor riesgo de colisión en miles de campañas de `101 Lab`; un único hash plano sobre todo el archivo impide saber qué subsistema divergió sin inspeccionar todo el estado. Descartada (§ 23, D-018). |

---

## Consecuencias

### Positivas
- **Contrato de determinismo auditable y biseccionable:** Si dos ejecuciones divergen en el tick $d$, la herramienta `cargo xtask golden --bisect <escenario>` compara los 12 campos de `TableHashes` en el día $d$ e identifica de inmediato qué subsistema (`economy`, `military`, `population`, etc.) y qué fase introdujeron la discrepancia (§ 23, línea 4951; Anexo X).
- **Escalabilidad multinúcleo segura:** Tantísimas fases escalonadas (Fases 5 a 14) como la Fase 15 de IA pueden repartirse entre todos los núcleos disponibles sabiendo que la barrera `apply` de cada fase y el diferimiento de comandos a $d + 1$ eliminan cualquier dependencia del orden de planificación de hilos.
- **Integridad de guardado garantizada (`QA-CORE-03`):** El mismo `state_hash` que certifica las ejecuciones doradas se incrusta en `SaveHeader` (Anexo AR), asegurando que guardar en el día $k$, recargar y simular hasta $N$ produce exactamente el mismo estado que simular de 0 a $N$ de corrido (§ 25).

### Negativas y compromisos asumidos
- **Disciplina estricta al evolucionar el estado:** Añadir un campo persistente a cualquiera de las 12 tablas de `State` exige actualizar simultáneamente su serializador canónico (`CanonicalHashWrite`), el esquema de `e101-save` (`canonical_format_version` / `save_format_version`) y, con aprobación humana (`golden-change`), los hashes de referencia de `tests/golden/`.
- **Prohibición de efectos colaterales fuera de fase:** Ningún sistema puede saltarse la cola de `Deltas` ni emitir comandos para el día en curso ($d$); el validador de la Fase 0 rechaza cualquier `StampedCommand` de IA cuyo `day` no coincida con el tick que se está abriendo.

---

## Cómo se verifica

1. **Pruebas de determinismo multi-hilo (`QA-CORE-01`, Anexo T):**
   - `cargo xtask test e101-sim` ejecuta el mismo escenario con 1, 2, 4, 8 y 16 hilos durante 3.650 ticks (10 años) y comprueba que tanto `state_hash` como los 12 `TableHashes` coinciden bit a bit en cada tick.
2. **Pruebas de independencia de orden de la IA y diferimiento a $d + 1$ (`T-109`, § 21):**
   - Prueba unitaria en `e101-sim` que permuta aleatoriamente el orden de evaluación de los países en la Fase 15 y verifica que los `StampedCommand` encolados para `Day(d + 1)` y el `state_hash` de los días $d$ y $d + 1$ son idénticos.
   - Prueba que verifica que ningún comando emitido en la Fase 15 del día $d$ tiene `cmd.day <= Day(d)`.
3. **Pruebas de ida y vuelta de guardado/carga (`QA-CORE-03`, `T-110`, § 25):**
   - `cargo xtask test e101-save` simula de `Day(0)` a `Day(k)`, guarda la partida, la recarga en una instancia limpia de `State`, comprueba que `compute_state_hash(&reloaded) == SaveHeader.state_hash` y continúa hasta `Day(N)`, verificando igualdad bit a bit con una ejecución continua `0..N`.
4. **Suite de escenarios dorados y bisección (`T-111`, § 23):**
   - `cargo xtask golden` ejecuta los escenarios deterministas de `tests/golden/` y valida los `StateHashReport` contra las referencias aprobadas.
   - Prueba de mutación controlada que altera 1 unidad de `Money` en `economy` en un tick intermedio y verifica que `cargo xtask golden --bisect` señala exactamente el día del fallo y la tabla `economy` sin falsos positivos en las 11 tablas restantes.
