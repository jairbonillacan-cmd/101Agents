# Backlog de tareas para agentes de 101 Engine

Este directorio contiene los archivos formales de tarea para el desarrollo de **101 Engine** y el juego *Project Epoch*, organizados a partir de las especificaciones del **Anexo P** y el calendario del **Anexo AF** del documento maestro (`docs/master/101_Agents_Games_Documento_Maestro_v0.7.md`).

## Ciclo de vida y flujo de trabajo

Cada tarea sigue estrictamente el ciclo definido en [WORKFLOW.md](../WORKFLOW.md) y se rige por las reglas universales de [AGENTS.md](../../../AGENTS.md) y [ROLES.md](../ROLES.md):

1. **Estados de tarea:**
   - `status:draft`: En redacción preliminar.
   - `status:ready`: Lista para ser tomada por un agente o persona.
   - `status:in-progress`: Reclamada y en desarrollo activo en una rama aislada (`agent/<rol>/<tarea>-<descripcion>`).
   - `status:review`: Pull request abierto pendiente de revisión del rol revisor.
   - `status:done`: Fusionada en `main` tras superar verificaciones y aprobación humana obligatoria si aplica.
   - Estados laterales: `needs-human` (bloqueo que requiere decisión humana), `status:blocked` (dependiente de otra tarea en curso).

2. **Reglas operativas esenciales:**
   - **Una sola tarea por agente** a la vez en su propia rama/worktree.
   - **Respeto estricto de rutas permitidas:** Ningún agente puede modificar archivos fuera de los designados en la sección `Archivos permitidos` de su tarea.
   - **Verificación continua:** `cargo xtask check` obligatorio antes de abrir cualquier PR.

---

## Índice general de tareas (Fases 0 y 1)

| ID | Título | Rol | Fase | Ola sugerida | Dependencias | Estado |
| --- | --- | --- | --- | --- | --- | --- |
| [T-001](T-001.md) | Crear el repositorio con el kit `101-engine-starter` | `infra` | Fase 0 | Ola 1 | — | `status:done` |
| [T-002](T-002.md) | Workspace vacío con `rust-toolchain.toml`, lints compartidos y `deny.toml` | `infra` | Fase 0 | Ola 1 | T-001 | `status:ready` |
| [T-003](T-003.md) | `tools/xtask` con subcomando `check` (fmt, clippy, test) | `infra` | Fase 0 | Ola 1 | T-002 | `status:ready` |
| [T-004](T-004.md) | Flujo `ci.yml` que ejecuta `cargo xtask check` | `infra` | Fase 0 | Ola 1 | T-003 | `status:ready` |
| [T-005](T-005.md) | ADR 0001: monorepo y prefijo `e101-` | `architecture` | Fase 0 | Ola 1 | T-001 | `status:ready` |
| [T-006](T-006.md) | ADR 0002: reglas de determinismo | `architecture` | Fase 0 | Ola 1 | T-001 | `status:ready` |
| [T-007](T-007.md) | ADR 0003: tipos de punto fijo | `architecture` | Fase 0 | Ola 1 | T-006 | `status:ready` |
| [T-008](T-008.md) | Prototipo económico en hoja de cálculo o script (fuera del motor) | `sim` | Fase 0 | Ola 1 | T-001 | `status:ready` |
| [T-009](T-009.md) | Prueba del pipeline: costas y ríos de la región en una textura de IDs | `data` | Fase 0 | Ola 3 | T-001 | `status:ready` |
| [T-010](T-010.md) | Lista verificada de entidades y gobernantes de 1300 en la región | `history` | Fase 0 | Ola 1 | T-001 | `status:ready` |
| [T-101](T-101.md) | Crate `e101-time`: día absoluto y conversión juliana/gregoriana | `engine` | Fase 1 | Ola 2 | T-002, T-006 | `status:ready` |
| [T-102](T-102.md) | Escalonamiento mensual por ID en `e101-time` | `engine` | Fase 1 | Ola 2 | T-101 | `status:ready` |
| [T-103](T-103.md) | Crate `e101-rng` con generador basado en contador | `engine` | Fase 1 | Ola 2 | T-002, T-006 | `status:ready` |
| [T-104](T-104.md) | Tipos `Money`, `Qty`, `Ratio` en `e101-store::fixed` | `engine` | Fase 1 | Ola 2 | T-002, T-007 | `status:ready` |
| [T-105](T-105.md) | Tablas SoA con IDs estables y slotmaps en `e101-store` | `engine` | Fase 1 | Ola 2 | T-104 | `status:ready` |
| [T-106](T-106.md) | Lint de determinismo (flotantes y `HashMap` en crates de simulación) | `infra` | Fase 1 | Ola 2 | T-003, T-006 | `status:ready` |
| [T-107](T-107.md) | Lint del grafo de dependencias entre crates | `infra` | Fase 1 | Ola 2 | T-003, T-005 | `status:ready` |
| [T-108](T-108.md) | Crate `e101-commands`: bus y diario de comandos | `engine` | Fase 1 | Ola 3 | T-101, T-105 | `status:ready` |
| [T-109](T-109.md) | Fase de aplicación de deltas con orden estable en `e101-sim` | `engine` | Fase 1 | Ola 3 | T-108 | `status:ready` |
| [T-110](T-110.md) | Hash de estado por tick en `e101-save` | `engine` | Fase 1 | Ola 3 | T-105, T-109 | `status:ready` |
| [T-111](T-111.md) | Primer escenario dorado: 300 años vacíos en `tests/golden/empty_300y` | `qa` | Fase 1 | Ola 3 | T-110 | `status:ready` |
| [T-112](T-112.md) | Guardado y carga con postcard o bitcode y zstd en `e101-save` | `engine` | Fase 1 | Ola 3 | T-110 | `status:ready` |
| [T-113](T-113.md) | Modelo de territorios en `e101-map`: localizaciones, provincias, adyacencias | `data` | Fase 1 | Ola 3 | T-009, T-105 | `status:ready` |
| [T-114](T-114.md) | Carga y validación de entidades desde RON en `e101-content` | `data` | Fase 1 | Ola 3 | T-010, T-105 | `status:ready` |
| [T-115](T-115.md) | Soberanía y control efectivo básicos en `e101-sim::politics` | `sim` | Fase 1 | Ola 3 | T-109, T-113, T-114 | `status:ready` |
| [T-116](T-116.md) | `e101-headless` ejecuta N años y escribe un resumen | `tools` | Fase 1 | Ola 3 | T-109, T-110 | `status:ready` |
| [T-117](T-117.md) | Spike A: mapa con textura de IDs y tres modos wgpu | `client` | Fase 1 | Ola 3 | T-009 | `status:ready` |
| [T-118](T-118.md) | Spike D: mismo mapa y panel en Godot con Rust | `client` | Fase 1 | Ola 3 | T-009 | `status:ready` |
| [T-119](T-119.md) | Spike G: mismo mapa con UI web embebida | `client` | Fase 1 | Ola 3 | T-117 | `status:ready` |
| [T-120](T-120.md) | ADR 0004: elección del cliente con métricas de spikes | `architecture` | Fase 1 | Ola 4 | T-117, T-118, T-119 | `status:ready` |
