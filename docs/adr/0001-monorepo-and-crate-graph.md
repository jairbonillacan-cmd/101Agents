# ADR 0001: Organización en monorepo, convención `e101-` y grafo de dependencias entre crates

- **Estado:** propuesto
- **Fecha:** 2026-10-24
- **Autoría:** Agente de Arquitectura (`role:architecture`) — tarea T-005
- **Relacionado con:** Documento maestro (`docs/master/101_Agents_Games_Documento_Maestro_v0.7.md`) §§ 21, 22, 39, 40, 41, 42, 45; Anexo B (D-001, D-002, D-006, D-007, D-014, D-022, D-023, D-024); Anexo P (T-001, T-002, T-005, T-107)

## Contexto

**101 Engine** es un motor propio de simulación de gran estrategia histórica desarrollado en Rust mediante un flujo coordinado de agentes de inteligencia artificial con supervisión humana (`docs/master/101_Agents_Games_Documento_Maestro_v0.7.md`, §§ 1, 21, 22, D-001, D-002, D-014). Para que múltiples agentes de IA (`role:engine`, `role:sim`, `role:data`, `role:history`, `role:ai`, `role:client`, `role:tools`, `role:qa`, `role:integration`, `role:architecture`, § 42) trabajen en paralelo sin degradar el determinismo ni acoplar la simulación a la capa gráfica, necesitamos fijar formalmente desde el inicio de la Etapa 0 (§ 22, Anexo P T-005):

1. **La topología de repositorios y directorios** donde conviven el motor en Rust, los datos históricos de *Project Epoch*, las herramientas de construcción (`tools/xtask`, `data-build`), las pruebas doradas (`tests/golden`), la documentación técnica (`docs/`) y el sitio web del estudio (`website/`) (§§ 39, 40, D-023, D-024).
2. **La convención de nombres de los paquetes Cargo**, habida cuenta de que el gestor de paquetes de Rust no permite identificadores de crate que comiencen por un dígito (`101-...` es inválido en Cargo) y de que el documento maestro unificó la nomenclatura bajo la marca *101 Engine* (§§ 21, 39, 40, D-022).
3. **La partición modular en crates y su grafo acíclico dirigido (DAG) de dependencias**, garantizando que los crates del núcleo determinista no dependan jamás de bibliotecas gráficas, de ventana, de audio ni del ejecutable cliente (`AGENTS.md` § 2.5, Documento maestro §§ 21, 40, D-007).

## Decisión

### 1. Organización en monorepo (`101Agents`)

Adoptamos una arquitectura de **monorepo único** para todo el código fuente del motor, los datos de *Project Epoch*, las herramientas de validación, la documentación de diseño y el sitio web del estudio (`docs/master/101_Agents_Games_Documento_Maestro_v0.7.md`, §§ 39, 40, D-023, D-024):

- **Justificación operativa para agentes de IA (§ 39):**
  - Un agente de IA tiene a su alcance el código del motor, los esquemas de datos, las pruebas y la documentación dentro de un mismo árbol de directorios sin necesidad de sincronizar submódulos ni múltiples repositorios.
  - Un cambio en una interfaz interna y la actualización de todos sus consumidores se revisan y aprueban en un único *pull request* atómico.
  - La integración continua ejecuta `cargo xtask check`, `cargo xtask golden`, `cargo xtask data` y `cargo xtask bench` sobre una misma instantánea coherente del repositorio (§§ 39, 45).
- **Alojamiento, visibilidad y licencia (D-023, D-024, § 39):**
  - El repositorio se aloja inicialmente en `https://github.com/jairbonillacan-cmd/101Agents` (incluyendo la carpeta `website/` del sitio estático en Astro) y es **público** desde el primer día para aprovechar los minutos gratuitos de GitHub Actions en repositorios públicos (D-023).
  - Cuando se constituya la cuenta de organización del estudio, el repositorio se transferirá a `101-agents-games/101-engine` conservando íntegro el historial de commits, issues y PRs (§ 39, D-023).
  - Aunque el repositorio sea público, el código y los datos son propietarios (**código visible como referencia**, `LicenseRef-101-Agents-Games-Proprietary`, D-024), auditado en CI con `cargo-deny` (`deny.toml`, § 40).
  - Si en etapas posteriores los activos binarios pesados de arte o audio crecen de forma significativa, podrán segregarse en un repositorio `101-engine-assets` con Git LFS sin alterar la estructura del monorepo de código y datos tabulares (§ 39).
- **Configuración del workspace de Rust (§ 40, D-006):**
  - Toolchain fijado en Rust estable con `edition = "2024"` y `resolver = "3"` en el `Cargo.toml` raíz (`rust-toolchain.toml`, § 40, T-001).
  - Miembros del workspace: `members = ["crates/*", "tools/xtask"]` (§ 40).
- **Estructura canónica de directorios (§ 40):**

```text
101Agents/
├── AGENTS.md
├── Cargo.toml
├── Cargo.lock
├── rust-toolchain.toml
├── clippy.toml
├── rustfmt.toml
├── deny.toml
├── .github/workflows/
├── crates/                  # Los 16 crates de Rust con prefijo e101-
├── games/epoch/             # Contenido de Project Epoch (data/, locale/, assets/)
├── data-build/              # Pipeline offline geográfico e histórico
├── tests/golden/            # Escenarios y hashes de determinismo
├── tools/xtask/             # Automatización (check, golden, data, bench, lab, docs)
├── docs/                    # master/, adr/, specs/, agents/, style/
└── website/                 # Sitio web del estudio (Astro)
```

### 2. Convención de nombres `e101-` y catálogo de los 16 crates

Todos los crates del motor dentro de `crates/` utilizan obligatoriamente el prefijo **`e101-`** (`e` de *engine* + `101`, `docs/master/101_Agents_Games_Documento_Maestro_v0.7.md`, §§ 21, 39, 40, D-022):

- **Motivo técnico y de marca (D-022, § 39):** Cargo rechaza nombres de paquete que empiecen por un número (`101-sim` no es válido). El prefijo `e101-` cumple las reglas de Cargo, preserva la identidad de marca de **101 Engine** en `Cargo.toml`, `crates/`, la documentación generada y los binarios, y reemplaza definitivamente cualquier nombre provisional previo (`sim-core`, `map-data`, etc., § 21). En código Rust, los nombres de crate se importan con guion bajo (`e101_time`, `e101_store`, etc.).
- **Partición en 16 crates (§§ 21, 22, 40, 42):** El workspace se divide en **12 crates de núcleo determinista** (librerías puras sin dependencias gráficas) y **4 crates de ejecutables y herramientas**:

#### A. Crates del núcleo determinista (12 crates)

| Crate | Rol propietario (§ 42) | Responsabilidad principal (§§ 21, 22, 40) |
| --- | --- | --- |
| `e101-time` | `role:engine` | Calendario histórico, tipos `Tick`/`Date` y planificador de fases (horaria, diaria, semanal, mensual, estacional, anual). |
| `e101-rng` | `role:engine` | Generador pseudoaleatorio determinista con subsemillas explícitas `rng(seed, system, entity, day)` y pruebas estadísticas. |
| `e101-store` | `role:engine` | Almacén columnar por tipo de entidad, IDs tipados con generación (`EntityId`), aritmética de punto fijo (`Money`, `Qty`, `Ratio`) y doble búfer (`State` + `Deltas`). |
| `e101-commands` | `role:engine` | Tipos de comando emitidos por jugador, IA o eventos, validación previa, cola determinista y registro de comandos para repetición y multijugador. |
| `e101-ledger` | `role:engine` | Registro causal de contribuciones (`ledger.record(...)`), invariantes contables y explicaciones desglosadas para la interfaz y la IA. |
| `e101-map` | `role:data` | Grafo de celdas (tierra, costa, mar, río), vecindades, distancias y búsqueda de caminos determinista (A* / Dijkstra con desempate por ID). |
| `e101-content` | `role:data` | Esquemas tipados, carga desde RON/CSV, compilación a binario y validadores de integridad referencial e histórica. |
| `e101-script` | `role:engine` | Lenguaje declarativo de condiciones, efectos y pesos con tipos estáticos y límite de pasos de evaluación. |
| `e101-sim` | `role:sim` | Sistemas de simulación (demografía, producción, mercados, comercio, fiscalidad, logística, combate, diplomacia, caracteres, conocimiento e instituciones). |
| `e101-history` | `role:history` | Motor de situaciones históricas emergentes, desastres, enfermedades y mecánicas asimétricas por tipo de entidad política. |
| `e101-ai` | `role:ai` | IA jerárquica determinista (postura estratégica, presupuesto, teatros operativos y evaluación táctica) que actúa exclusivamente emitiendo `e101-commands`. |
| `e101-save` | `role:engine` | Serialización canónica (Postcard + Zstd), sumas de verificación (BLAKE3), instantáneas de estado y migración de versiones de guardado. |

#### B. Crates de ejecutables y herramientas (4 crates)

| Crate | Rol propietario (§ 42) | Responsabilidad principal (§§ 21, 22, 40) |
| --- | --- | --- |
| `e101-headless` | `role:tools` | Ejecutor por línea de comandos sin gráficos para pruebas doradas, benchmarks de rendimiento y servidores dedicados. |
| `e101-lab` | `role:qa` / `role:tools` | **101 Lab**: arnés de simulación masiva sin cabeza para ejecutar decenas o cientos de campañas en paralelo y auditar invariantes y equilibrio. |
| `e101-client` | `role:client` | Cliente gráfico del juego (mapa por modos, paneles de inspección con datos de `e101-ledger`, audio y localización). |
| `e101-forge` | `role:tools` | **101 Forge**: editor visual de mapa, entidades, árboles de situaciones y depurador de ticks conectado a los validadores de `e101-content`. |

### 3. Grafo de dependencias entre crates (DAG estricto)

Las dependencias internas entre los crates `e101-*` forman un **grafo acíclico dirigido (DAG) estricto** donde las flechas solo apuntan hacia abajo (`docs/master/101_Agents_Games_Documento_Maestro_v0.7.md`, §§ 21, 40, D-007):

```text
e101-time      e101-rng
    \            /
     v          v
      e101-store
      /    |    \
     v     v     v
e101-commands e101-map
     \     |
      v    v
    e101-ledger
         |
         v
    e101-content
         |
         v
    e101-script
         |
         v
     e101-sim
         |
         v
   e101-history
         |
         v
     e101-ai
         |
         v
    e101-save
   /    |    \
  v     v     v
e101-headless  e101-lab  e101-client  e101-forge
```

#### Matriz de niveles y dependencias internas permitidas

Un crate situado en el nivel $N$ solo puede depender de los crates explícitamente autorizados en los niveles $< N$ según la siguiente tabla normativa (§§ 21, 40):

| Nivel | Crate | Dependencias internas `e101-*` permitidas | Restricciones clave |
| --- | --- | --- | --- |
| **0** | `e101-time` | *(ninguna)* | Hoja pura; sin dependencias internas ni de I/O. |
| **0** | `e101-rng` | *(ninguna)* | Hoja pura; sin `rand::thread_rng` ni entropía del SO. |
| **1** | `e101-store` | `e101-time`, `e101-rng` | Base de datos en memoria y tipos `Money`, `Qty`, `Ratio`. |
| **2** | `e101-commands` | `e101-time`, `e101-store` | Define comandos e identificadores; no ejecuta lógica de simulación. |
| **2** | `e101-map` | `e101-store` | Topología y pathfinding sobre tipos de `e101-store`. |
| **3** | `e101-ledger` | `e101-time`, `e101-store`, `e101-commands` | Contabilidad causal de deltas y explicaciones. |
| **4** | `e101-content` | `e101-store`, `e101-commands`, `e101-ledger` | Esquemas de datos y validación estática/referencial. |
| **5** | `e101-script` | `e101-store`, `e101-commands`, `e101-ledger`, `e101-content` | Evaluación acotada de condiciones y efectos declarativos. |
| **6** | `e101-sim` | `e101-time`, `e101-rng`, `e101-store`, `e101-commands`, `e101-ledger`, `e101-map`, `e101-content`, `e101-script` | Sistemas puros `fn run(state: &State, deltas: &mut Deltas)`. No conoce a `e101-ai` ni a `e101-client`. |
| **7** | `e101-history` | `e101-time`, `e101-rng`, `e101-store`, `e101-commands`, `e101-ledger`, `e101-map`, `e101-content`, `e101-script`, `e101-sim` | Situaciones históricas condicionales construidas sobre `e101-sim`. |
| **8** | `e101-ai` | `e101-time`, `e101-rng`, `e101-store`, `e101-commands`, `e101-ledger`, `e101-map`, `e101-content`, `e101-script`, `e101-sim`, `e101-history` | Lee el estado y emite `e101-commands`; nunca muta `State` directamente. |
| **9** | `e101-save` | `e101-time`, `e101-rng`, `e101-store`, `e101-commands`, `e101-ledger`, `e101-map`, `e101-content`, `e101-script`, `e101-sim`, `e101-history`, `e101-ai` | Punto de cierre del núcleo determinista para serialización y hashing. |
| **10** | `e101-headless` | `e101-save` y cualquier crate de los niveles 0–8 | Binario CLI sin dependencias de ventana ni GPU. |
| **10** | `e101-lab` | `e101-save` y cualquier crate de los niveles 0–8 | Ejecutor paralelo de campañas; el paralelismo ocurre entre campañas o por partición determinista, sin alterar hashes. |
| **10** | `e101-client` | `e101-save` y cualquier crate de los niveles 0–8 | Único crate del juego autorizado a depender del motor de renderizado/audio/ventana. |
| **10** | `e101-forge` | `e101-save` y cualquier crate de los niveles 0–8 | Único crate de herramientas autorizado a depender de UI gráfica de edición. |

#### Invariantes arquitectónicos de aislamiento (D-007, `AGENTS.md` §§ 2.5, 3)

1. **El núcleo no conoce el cliente (D-007):** Ninguno de los 12 crates del núcleo (niveles 0–9) puede depender directa ni transitivamente de `e101-client`, `e101-forge` ni de crates externos de gráficos, ventanas, interfaz o sonido (`wgpu`, `winit`, `egui`, `bevy`, `macroquad`, `godot`, `rodio`, `cpal`, etc.).
2. **Prohibición de ciclos y saltos invertidos:** Ningún crate de nivel inferior puede depender de un crate de nivel superior (por ejemplo, `e101-sim` no puede depender de `e101-history` ni de `e101-ai`; `e101-store` no puede depender de `e101-commands`).
3. **Documentación local por crate (§ 41):** Todo crate en `crates/e101-*/` debe incluir un archivo `CONTEXT.md` de menos de 120 líneas que declare su propósito, lo que **no** hace, sus invariantes y sus dependencias internas y externas autorizadas.

## Alternativas consideradas

| Alternativa | Ventajas | Inconvenientes |
| --- | --- | --- |
| **1. Monorepo único con 16 crates `e101-*` y DAG por capas (Decisión elegida)** | Contexto completo para los agentes de IA en una sola clonación (§ 39); PRs atómicos entre motor, datos y pruebas; compilación incremental por crate; aislamiento estricto entre simulación headless y cliente gráfico (D-007). | Requiere disciplina en CI (`cargo xtask check`) para impedir dependencias cruzadas no autorizadas y evitar que crezcan binarios pesados en Git. |
| **2. Multirepo (repositorios separados para motor, datos de *Project Epoch*, herramientas y web)** | Permisos de acceso granulares por repositorio; historiales de Git más pequeños. | Rompe la atomicidad de los cambios realizados por agentes de IA (§ 39); obliga a sincronizar versiones y submódulos constantemente; dificulta ejecutar `golden` y `data` en cada PR del motor. |
| **3. Monolito en un único crate (`e101-engine`) con módulos internos** | Configuración inicial de `Cargo.toml` más simple. | Tiempos de recompilación elevados al tocar cualquier módulo; los agentes pueden introducir acoplamientos circulares entre `sim`, `ai` y `client` sin que Cargo lo impida a nivel de grafo de paquetes (§§ 21, 40). |
| **4. Nombres de crate genéricos sin prefijo (`sim-core`, `map-data`, `ledger`)** | Nombres más cortos al importar. | Descartado en D-022 (§§ 21, 39): diluye la identidad de **101 Engine**, complica distinguir crates propios de dependencias externas en `Cargo.lock` y `cargo metadata`, e impide aplicar reglas simples de prefijo en `xtask`. |

## Consecuencias

### Positivas

- **Compilación y pruebas sin GPU en cualquier entorno:** Los 12 crates del núcleo, `e101-headless` y `e101-lab` compilan y pasan todas las pruebas en contenedores de CI estándar sin tarjeta gráfica ni servidor de ventanas (§§ 21, 39, D-007).
- **Fronteras claras por rol de agente:** Cada rol de agente (`role:engine`, `role:sim`, `role:data`, `role:history`, `role:ai`, `role:client`, `role:tools`) tiene asignados crates específicos con interfaces públicas acotadas (§ 42), reduciendo conflictos de merge y facilitando la exigencia de un ADR ante cualquier `api-change` (`AGENTS.md` §§ 5, 10).
- **Sustitución limpia de la capa visual:** Como `e101-client` está en la hoja inferior del DAG (nivel 10), la tecnología de presentación puede evolucionar sin tocar ni una sola línea de `e101-sim`, `e101-history` o `e101-ai` (D-007).

### Negativas y compromisos

- **Coste de mantenimiento del grafo:** Añadir una dependencia entre dos crates `e101-*` que no esté contemplada en la matriz de este ADR requiere revisión del rol de Arquitectura (`api-change`) y actualizar tanto este documento como el verificador de `tools/xtask`.
- **Conversión de identificadores en Rust:** El prefijo con guion en Cargo (`e101-store`) se escribe con guion bajo en código Rust (`use e101_store::...`), convención estándar de Rust que queda documentada en la guía de estilo (`docs/style/rust.md`, T-004).

## Cómo se verifica

1. **Verificador automático del grafo de dependencias (`cargo xtask check` / T-107, § 45):**
   - El subcomando `cargo xtask check` invoca `cargo metadata --no-deps --format-version 1` y comprueba automáticamente:
     - Que todos los paquetes ubicados bajo `crates/` tienen el prefijo `e101-`.
     - Que para cada paquete `e101-*`, el conjunto de sus dependencias internas es un subconjunto estricto de las permitidas en la tabla de niveles de este ADR (ausencia total de ciclos y de aristas invertidas).
     - Que ninguno de los 12 crates del núcleo depende de `e101-client`, `e101-forge` ni de la lista negra de crates gráficos, de ventana o de audio.
2. **Andamiaje estandarizado de crates (`cargo xtask new-crate`, § 45):**
   - La creación de cualquier crate se realiza mediante `cargo xtask new-crate`, que genera la estructura con el prefijo `e101-`, las reglas de lints de determinismo y la plantilla obligatoria de `CONTEXT.md` (§ 41).
3. **Auditoría de licencias y dependencias externas (`cargo deny check`):**
   - Ejecutada en CI sobre el `Cargo.lock` del monorepo conforme a `deny.toml` (§ 40, D-024).
