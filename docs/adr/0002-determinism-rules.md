# ADR 0002: Reglas de determinismo estricto y lints de verificación en el núcleo de simulación

- **Estado:** propuesto
- **Fecha:** 2026-10-24
- **Autoría:** Agente de Arquitectura (`role:architecture`) — tarea T-006
- **Relacionado con:** Documento maestro v0.7 §§ 21, 22, 23, 40, 41, 45, 46; Anexo B (D-008, D-017, D-018, D-019); Anexo P (T-006, T-106); Anexo T (QA-CORE-01 a QA-CORE-06); Anexo AC; ADR 0001, ADR 0003, ADR 0004

## Contexto

El primer principio inquebrantable de **101 Engine** (`AGENTS.md` § 2.1; Documento maestro v0.7 § 23) establece que la simulación histórica y sistémica debe ser **estrictamente determinista bit a bit**. Esta propiedad no es una optimización opcional, sino un pilar arquitectónico del que dependen directamente cuatro capacidades críticas del motor y del flujo de trabajo con agentes autónomos:

1. **Reproducibilidad y regresión con ejecuciones doradas (*golden runs*, § 23, § 45):** Toda solicitud de cambio (PR) generada por un agente o una persona se valida comparando el hash criptográfico del estado de simulación contra escenarios de referencia de hasta 300 años de duración. Una discrepancia de un solo bit en el año 50 invalida la comparación si el motor no es determinista.
2. **Depuración por bisección automática (`cargo xtask golden --bisect`, § 23, § 45):** Localizar el primer tick y el subsistema responsable de una divergencia requiere que reejecutar una partida con los mismos insumos reproduzca exactamente la misma trayectoria de estado.
3. **Simulación masiva y paralelismo de datos en 101 Lab (§ 21, § 39):** El motor ejecuta fases de cálculo en paralelo mediante Rayon. El resultado de un tick debe ser idéntico tanto si se ejecuta en 1 hilo como en 16 hilos (`QA-CORE-02`), y debe preparar el camino hacia el determinismo multiplataforma entre arquitecturas (`x86_64` y `aarch64`) y sistemas operativos (Windows, Linux, macOS; Documento maestro § 23 y Anexo B, riesgo A-08).
4. **Guardado, repetición de comandos y futuro multijugador por *lockstep* (§ 21, § 22, D-008):** La validación de partidas guardadas y la reproducción de diarios de comandos (`Vec<StampedCommand>`) exigen que el estado resultante tras aplicar la misma secuencia sobre la misma semilla sea idéntico al estado previo a serializar (`QA-CORE-03`).

En Rust estándar existen múltiples fuentes de no determinismo implícito: diferencias de redondeo o contracción de instrucciones FMA (`fused multiply-add`) en números de punto flotante (`f32`, `f64`), implementaciones dependientes de la biblioteca matemática del sistema (`libm`) para funciones trascendentes, aleatorización de semillas por proceso en `std::collections::{HashMap, HashSet}` (`RandomState`), orden de reducción no determinista en iteradores paralelos, lecturas del reloj del sistema o del entorno, y generadores de números aleatorios con estado compartido mutable entre hilos.

Dado que el desarrollo en `101Agents` se realiza de forma distribuida entre múltiples agentes de IA con contexto acotado (§ 41, § 46), no basta con documentar buenas prácticas: las reglas de determinismo deben estar formalizadas contractualmente y aplicadas de manera automática en compilación y en CI mediante lints de Clippy y analizadores estáticos en `cargo xtask check`.

## Decisión

### 1. Definición contractual de determinismo y ámbito de aplicación

Se define formalmente el contrato de determinismo del núcleo de **101 Engine** (`AGENTS.md` § 2.1, Documento maestro § 23):

$$\text{Misma versión del binario} + \text{mismos datos compilados} + \text{misma semilla } (\texttt{u64}) + \text{mismo diario de comandos } (\texttt{Vec<StampedCommand>}) \implies \text{mismo estado bit a bit } (\texttt{state\_hash} \text{ idéntico en cada tick})$$

Este contrato se cumple con independencia del número de hilos de ejecución de Rayon (p. ej., 1 hilo frente a 16 hilos) y sienta las bases para la equivalencia bit a bit entre plataformas (`x86_64` y `aarch64` en Windows, Linux y macOS; § 23, Anexo B A-08).

**Ámbito estricto de aplicación (`AGENTS.md` § 3, ADR 0001):** Las reglas de este ADR son de cumplimiento obligatorio y sin excepción en los **12 crates de simulación y núcleo**:

- `e101-time`
- `e101-store`
- `e101-commands`
- `e101-ledger`
- `e101-rng`
- `e101-sim`
- `e101-history`
- `e101-map`
- `e101-content`
- `e101-script`
- `e101-save`
- `e101-ai`

---

### 2. Catálogo exhaustivo de prohibiciones en los crates del núcleo

De acuerdo con `AGENTS.md` § 3 y el Documento maestro (§ 23, Anexo X y Anexo AC), se establecen las siguientes siete prohibiciones (P-01 a P-07) en los 12 crates del núcleo:

#### P-01 · Prohibición absoluta de punto flotante (`f32`, `f64`)
Queda **prohibido** el uso de los tipos primitivos `f32` y `f64` en el estado persistente (`State`), en la contabilidad (`e101-ledger`), en las firmas públicas o privadas y en **cualquier cálculo intermedio** dentro de los crates de simulación (Documento maestro § 23, `AGENTS.md` § 3 y Anexo AC: *"¿Puedo usar `f64` en un cálculo intermedio si el resultado es entero? No en los crates de simulación"*).
- **Sustituto obligatorio:** Enteros con tamaño explícito (`i32`, `u32`, `i64`, `u64`, `i128`) y los tipos de punto fijo de `e101-store::fixed` (`Money`, `Qty`, `Ratio`) con aritmética saturada o comprobada e intermedios en `i128`, definidos en el **ADR 0003** (D-017).

#### P-02 · Prohibición de funciones trascendentes o matemáticas de plataforma
Queda **prohibido** invocar funciones matemáticas en punto flotante o dependientes de la implementación de `libm` del sistema operativo o de la arquitectura de CPU: `sin`, `cos`, `tan`, `asin`, `acos`, `atan`, `atan2`, `exp`, `exp2`, `ln`, `log2`, `log10`, `powf`, `powi` sobre flotantes y `sqrt` en punto flotante (§ 23).
- **Sustituto obligatorio:** Toda relación no lineal (rendimientos decrecientes, logística, decaimiento, mortalidad, modificadores climáticos) se resuelve mediante tablas precalculadas en punto fijo con interpolación lineal determinista en `e101-store::fixed` o curvas por tramos definidas en los archivos de datos RON (D-019, ADR 0003). Si se requiere raíz cuadrada entera, se emplea `isqrt` determinista sobre enteros/punto fijo.

#### P-03 · Prohibición de colecciones con orden de almacenamiento o iteración no determinista
Queda **prohibido** usar o iterar `std::collections::HashMap` y `std::collections::HashSet`, así como `std::hash::RandomState`, dado que su semilla aleatoria cambia en cada proceso y altera el orden de iteración (§ 23, `AGENTS.md` § 3).
- **Sustituto obligatorio:**
  - Almacenamiento primario en `Table<T>` / `Vec<T>` indexados por identificadores tipados densos `Id<T>` (`u32`), iterando siempre en orden ascendente de `Id<T>` (Anexo X, Anexo AC).
  - Cuando se requiera un mapa o conjunto asociativo dinámico, se utilizarán exclusivamente `std::collections::BTreeMap`, `std::collections::BTreeSet` o `indexmap::IndexMap` / `IndexSet` (sin `RandomState` o con ordenación explícita por clave antes de iterar).

#### P-04 · Prohibición de reloj del sistema, E/S, red, entorno y direcciones de memoria
Queda **prohibido** dentro de la lógica de simulación (`AGENTS.md` § 3, § 23):
- Leer el reloj del sistema (`std::time::Instant`, `std::time::SystemTime`). El único tiempo válido en la simulación es `Tick` / `Date` de `e101-time`.
- Acceder a la red (`std::net::*`), a variables de entorno (`std::env::*`), a procesos (`std::process::*`) o al sistema de archivos (`std::fs::*`) desde los sistemas de simulación (con la única excepción de las funciones de frontera de compilación/carga de datos en `e101-content` y serialización de partidas en `e101-save`, detalladas en la sección 3.3).
- Consultar el identificador del hilo del sistema operativo (`std::thread::current().id()`) o convertir punteros/referencias a enteros (`as usize`) para ordenar, comparar o calcular hashes de entidades.

#### P-05 · Prohibición de aleatoriedad externa o con estado compartido mutable
Queda **prohibido** el uso de `rand::thread_rng()`, `rand::random()`, `OsRng`, generadores globales con mutex o cualquier PRNG secuencial compartido entre hilos cuyo resultado dependa del orden en que Rayon planifique las tareas (`AGENTS.md` § 3, § 22, § 23).
- **Sustituto obligatorio:** Toda decisión estocástica debe obtener su generador exclusivamente mediante la función pura basada en contador (ChaCha8 de 8 rondas o SplitMix64/Philox, D-018):
  ```rust
  let mut r = e101_rng::rng(state.seed, SystemId::Disease, settlement_id.raw(), state.tick.raw());
  ```
  De este modo, la secuencia pseudoaleatoria de cualquier entidad en cualquier día es una función pura de `(seed, system_id, entity_id, tick)` e inmune al número de hilos (Anexo X).

#### P-06 · Prohibición de mutación directa del estado y de reducciones paralelas sin clave estable
Los sistemas de simulación tienen obligatoriamente la firma `fn run(&self, state: &State, deltas: &mut Deltas)` (`AGENTS.md` § 3, Anexo X).
- Ningún sistema recibe `&mut State`.
- Cuando un sistema emplea Rayon (`par_iter`) para evaluar entidades en paralelo, solo lee `&State` de forma inmutable y emite `Deltas` en búferes locales por tarea.
- Al concluir la fase de cálculo, `e101-sim::apply` recolecta todos los `Deltas` y **los ordena canónicamente por clave estable** `(TargetTable, TargetEntityId, CauseId, SourceEntityId)` antes de fusionarlos y mutar `State` en un único hilo (§ 21, § 23, ADR 0004). Queda prohibido usar `par_bridge()` o reducciones paralelas asociativas no conmutativas sin ordenación previa por `Id<T>`.

#### P-07 · Prohibición de código `unsafe` y de silenciamiento de lints
Queda **prohibido** el bloque o atributo `unsafe` en los crates del núcleo sin un ADR específico aprobado por Arquitectura (`AGENTS.md` § 3, § 10). Asimismo, queda **prohibido** silenciar los lints de determinismo mediante atributos locales `#[allow(...)]` o `#![allow(...)]` en cualquiera de los 12 crates del núcleo (§ 46).

---

### 3. Lints de compilación y verificación estática (`cargo xtask check`)

Para garantizar que ningún agente ni colaborador viole las reglas P-01 a P-07, la verificación se automatiza en tres capas complementarias (§§ 40, 45, 46; tarea T-106):

#### 3.1. Configuración de `[workspace.lints]` en el `Cargo.toml` raíz
Todos los crates del workspace heredan (`[lints] workspace = true`) la siguiente política estricta:

```toml
[workspace.lints.rust]
unsafe_code = "forbid"

[workspace.lints.clippy]
float_arithmetic = "deny"
float_cmp = "deny"
float_cmp_const = "deny"
lossy_float_literal = "deny"
imprecise_flops = "deny"
suboptimal_flops = "deny"
disallowed_types = "deny"
disallowed_methods = "deny"
```

#### 3.2. Catálogo de tipos y métodos prohibidos en `clippy.toml`
En la raíz del repositorio se declara el archivo `clippy.toml` con las listas negras auditables por Clippy:

```toml
disallowed-types = [
    { path = "std::collections::HashMap", reason = "Orden de iteración no determinista (P-03, ADR 0002). Usa Table<T>, BTreeMap o IndexMap." },
    { path = "std::collections::HashSet", reason = "Orden de iteración no determinista (P-03, ADR 0002). Usa BTreeSet o IndexSet." },
    { path = "std::hash::RandomState", reason = "Semilla aleatoria por ejecución prohibida en simulación (P-03, ADR 0002)." },
    { path = "std::time::Instant", reason = "Reloj del sistema prohibido en simulación (P-04, ADR 0002). Usa e101-time::Tick." },
    { path = "std::time::SystemTime", reason = "Reloj del sistema prohibido en simulación (P-04, ADR 0002). Usa e101-time::Date." },
    { path = "rand::rngs::ThreadRng", reason = "RNG dependiente del hilo prohibido (P-05, ADR 0002). Usa e101_rng::rng(seed, system, entity, day)." },
    { path = "rand::rngs::OsRng", reason = "Entropía del SO prohibida en simulación (P-05, ADR 0002). Usa e101_rng::rng(seed, system, entity, day)." },
]

disallowed-methods = [
    { path = "std::time::Instant::now", reason = "Reloj del sistema prohibido en simulación (P-04, ADR 0002)." },
    { path = "std::time::SystemTime::now", reason = "Reloj del sistema prohibido en simulación (P-04, ADR 0002)." },
    { path = "std::env::var", reason = "Variables de entorno prohibidas en simulación (P-04, ADR 0002)." },
    { path = "std::env::var_os", reason = "Variables de entorno prohibidas en simulación (P-04, ADR 0002)." },
    { path = "std::env::vars", reason = "Variables de entorno prohibidas en simulación (P-04, ADR 0002)." },
    { path = "rand::thread_rng", reason = "Usa e101_rng::rng(seed, system, entity, day) (P-05, ADR 0002)." },
    { path = "rand::random", reason = "Usa e101_rng::rng(seed, system, entity, day) (P-05, ADR 0002)." },
]
```

#### 3.3. Escaneo estático propio en `tools/xtask` (`cargo xtask check`, tarea T-106)
Dado que `clippy::float_arithmetic` solo detecta operaciones aritméticas pero no impide declarar campos `f32`/`f64` en estructuras o firmas, el subcomando `cargo xtask check` incluye un analizador léxico/sintáctico sobre todos los archivos `crates/e101-{time,store,commands,ledger,rng,sim,history,map,content,script,save,ai}/src/**/*.rs` que falla inmediatamente si detecta:

1. **Aparición de tokens de tipo `f32` o `f64`:** En cualquier definición de `struct`, `enum`, firma de función, constante o conversión `as f32` / `as f64`.
2. **Intento de evasión de lints (P-07):** Cualquier directiva `#[allow(clippy::float_arithmetic)]`, `#[allow(clippy::float_cmp)]`, `#[allow(clippy::disallowed_types)]`, `#[allow(clippy::disallowed_methods)]` o `#![allow(...)]` equivalente.
3. **Uso de E/S o red en crates de lógica de simulación (P-04):** Cualquier referencia a `std::fs`, `std::net` o `std::process` en los crates del núcleo, con la única excepción explícitamente registrada en la lista blanca de `xtask` para las funciones de frontera de carga/compilación de paquetes en `e101-content` y lectura/escritura de archivos `.e101save` en `e101-save` (cuyas interfaces de núcleo operan siempre sobre `&[u8]` / `Vec<u8>` en memoria para las pruebas de simulación).

---

### 4. Excepciones documentadas: cliente gráfico y herramientas

De conformidad con el principio 5 (`AGENTS.md` § 2.5: *"El núcleo no conoce el cliente"*) y el Documento maestro (§§ 21, 22, 23, 40), las restricciones sobre punto flotante, reloj del sistema y E/S **no se aplican** a los binarios y crates periféricos que quedan fuera del bucle determinista del estado:

- **`e101-client`** (cliente gráfico y de audio)
- **`e101-forge`** (editor visual de mapas y contenido)
- **`e101-lab`** (únicamente en su capa de agregación estadística, exportación Parquet y generación de informes HTML/Markdown; la ejecución de cada campaña invoca `e101-sim` bajo las reglas estrictas del núcleo)
- **`tools/xtask`** y **`data-build`** (herramientas de automatización y pipeline offline de datos)

Estos crates están autorizados a declarar `#![allow(clippy::float_arithmetic, clippy::float_cmp)]` en su raíz (`lib.rs` o `main.rs`) y a emplear `f32`/`f64` y `std::time::Instant` exclusivamente para:
1. Renderizado de cámara, sombreadores, audio y diseño de interfaz a 60 FPS (§ 21).
2. Interpolación visual de posiciones de ejércitos y animaciones entre ticks discretos (§ 21).
3. Cronometraje de rendimiento de frame y de tick para telemetría local y benchmarks (`cargo xtask bench`).

**Frontera inquebrantable cliente-núcleo (Anexo X):** `e101-client` solo accede al estado del motor a través de vistas inmutables (`View<'a>` / `Snapshot`) y solo se comunica hacia el motor emitiendo valores `Command` tipados (`e101-commands`) que contienen identificadores (`Id<T>`) y tipos de punto fijo (`Money`, `Qty`, `Ratio`). Ningún valor en punto flotante calculado en el cliente o en las herramientas puede cruzar jamás hacia `e101-commands` ni hacia `e101-sim`.

## Alternativas consideradas

| Alternativa | Ventajas | Inconvenientes |
| --- | --- | --- |
| **1. Punto fijo (`e101-store::fixed`) + prohibición total de `f32`/`f64` en el núcleo + RNG por contador + lints en Clippy/`xtask` (Elegida)** | Garantiza determinismo bit a bit entre 1 y $N$ hilos y entre arquitecturas (`x86_64`/`aarch64`); impide regresiones accidentales de agentes de IA en compilación; permite bisección exacta (`--bisect`). | Requiere escribir funciones de utilidad y tablas por tramos en punto fijo (ADR 0003) y cuidar el rango de desbordamiento con intermedios `i128`. |
| **2. Permitir `f32`/`f64` IEEE 754 en el núcleo desactivando optimizaciones (`-C target-feature=-fma`)** | Menor fricción inicial al escribir fórmulas matemáticas continuas; uso directo de operadores nativos. | Las funciones trascendentes (`exp`, `ln`, `powf`, `sin`) siguen dependiendo de la `libm` del SO; diferencias sutiles de redondeo entre `x86_64` y `aarch64` o futuras versiones de LLVM rompen los hashes dorados; alto riesgo de sumas no asociativas en paralelo. |
| **3. Permitir `f64` solo en cálculos intermedios convirtiendo a entero al guardar en `State`** | Facilita prototipar fórmulas complejas antes de truncar al tipo de almacenamiento. | Pequeñas diferencias de redondeo cerca de un umbral entero producen un salto de $\pm 1$ unidad que diverge exponencialmente por efecto mariposa; explícitamente rechazado en el Documento maestro (Anexo AC). |
| **4. Confiar solo en revisiones de código humanas o prompts sin lints estáticos en `xtask`** | Cero mantenimiento de reglas en `clippy.toml` y `tools/xtask`. | Inviable en un flujo con decenas de tareas ejecutadas por agentes de IA: los errores se descubrirían tarde (en ejecuciones doradas lentas o tras un cambio de plataforma) en lugar de en milisegundos durante `cargo xtask check`. |

## Consecuencias

### Positivas
- **Detección inmediata en compilación:** Cualquier intento de un agente de introducir un `f64`, un `HashMap`, un `Instant::now()` o un `thread_rng()` en los crates de simulación falla en pocos segundos al ejecutar `cargo xtask check`, con un mensaje de error que indica el sustituto exacto (`Money`/`Qty`/`Ratio`, `BTreeMap`/`Table<T>`, `Tick`, `e101_rng::rng`).
- **Invarianza al paralelismo (`QA-CORE-02`):** La combinación de P-03 (orden de iteración por `Id<T>`), P-05 (RNG por contador) y P-06 (fusión de `Deltas` ordenada por clave estable) garantiza por construcción que `threads_1_vs_16` produzca exactamente el mismo `state_hash`.
- **Auditoría y bisección fiables:** Los escenarios dorados (`tests/golden/`) y la herramienta `cargo xtask golden --bisect` operan sobre una base determinista sólida (ADR 0004).

### Negativas y costes asumidos
- **Esfuerzo de expresividad matemática:** Los agentes del rol de Simulación (`role:sim`) deben expresar todas las ecuaciones económicas, demográficas y militares mediante `Money`, `Qty`, `Ratio` y tablas de consulta por tramos (ADR 0003), sin recurrir a flotantes.
- **Mantenimiento del escáner en `tools/xtask`:** El verificador de T-106 debe mantenerse sincronizado con la lista de los 12 crates del núcleo si en el futuro se añade un nuevo crate de simulación (lo cual requeriría a su vez un nuevo ADR).

## Cómo se verifica

El cumplimiento de este ADR se verifica de forma continua y automatizada mediante tres mecanismos (§ 23, § 45, Anexo T):

1. **Verificación estática obligatoria (`cargo xtask check`, `QA-CORE-04` y tarea T-106):**
   - Ejecuta `cargo clippy --workspace --all-targets -- -D warnings` aplicando `[workspace.lints]` y `clippy.toml`.
   - Ejecuta el pase de análisis estático de `tools/xtask` sobre los 12 crates del núcleo para verificar la ausencia total de `f32`/`f64`, de directivas `#[allow(...)]` prohibidas y de llamadas a `std::fs`/`std::net`/`std::env`.
   - Incluye una **prueba automatizada negativa** en `tools/xtask` (criterio de aceptación de T-106) que inyecta un archivo temporal o caso de prueba con `f64` y `HashMap` en un crate del núcleo y comprueba que el verificador lo rechaza con código de salida distinto de cero.
2. **Pruebas de determinismo y ejecuciones doradas (`cargo xtask golden`, `QA-CORE-01` a `QA-CORE-03`):**
   - Ejecuta los **7 escenarios dorados iniciales** definidos en el Documento maestro (§ 23):
     1. `empty_300y` (mundo mínimo durante 300 años sin pánico ni deriva).
     2. `economy_closed_100y` (conservación monetaria y de bienes en economía cerrada durante 100 años).
     3. `slice_ai_only_50y` (escenario del *vertical slice* Tesalia 1300 gobernado por IA durante 50 años).
     4. `war_two_states_10y` (guerra entre dos entidades políticas durante 10 años).
     5. `plague_1347` (propagación epidémica en una red comercial).
     6. `save_load_roundtrip` (`QA-CORE-03`: guardar en el año 5, recargar y continuar hasta el año 10 produce el mismo `state_hash` que ejecutar 10 años seguidos).
     7. `threads_1_vs_16` (`QA-CORE-02`: ejecutar el escenario completo con 1 hilo y con 16 hilos de Rayon produce un `state_hash` BLAKE3 idéntico bit a bit).
3. **Bisección automática de divergencias (`cargo xtask golden --bisect <escenario>`):**
   - Cuando una ejecución difiere del hash esperado o entre dos configuraciones, realiza búsqueda binaria por ticks y compara los hashes por tabla (`population`, `economy`, `polities`, `military`, etc., definidos en el ADR 0004) para aislar el primer tick y el sistema exacto donde se produjo la divergencia.
