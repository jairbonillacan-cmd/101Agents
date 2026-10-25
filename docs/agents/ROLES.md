# Roles de agentes

Cada tarea se asigna a **un rol**. El rol define qué rutas puede modificar el agente sin pedir permiso, qué debe entregar y quién revisa.

| Rol | Rutas propias | Entrega típica | Revisa |
| --- | --- | --- | --- |
| Arquitectura (`role:architecture`) | `docs/adr/`, `docs/specs/`, interfaces públicas (`lib.rs`) de todos los crates | ADR, contratos de interfaz, revisiones de diseño | Persona responsable |
| Motor (`role:engine`) | `crates/e101-time`, `e101-store`, `e101-commands`, `e101-ledger`, `e101-rng`, `e101-save` | Scheduler, almacenamiento, guardado, rendimiento | Arquitectura |
| Simulación (`role:sim`) | `crates/e101-sim` | Sistemas de población, economía, política, diplomacia, guerra, ciencia | Arquitectura + QA |
| Historia (`role:history`) | `crates/e101-history`, `games/epoch/data/history/`, `games/epoch/data/entities/` | Situaciones, entidades, personajes, fuentes | Persona responsable (datos A/B) |
| IA de juego (`role:ai`) | `crates/e101-ai` | Planificadores, utilidades, personalidades | Simulación + QA |
| Mapa y datos (`role:data`) | `crates/e101-map`, `crates/e101-content`, `data-build/`, `games/epoch/data/map/` | Pipeline geográfico, validadores, contenido | Arquitectura |
| Cliente (`role:client`) | `crates/e101-client`, `games/epoch/assets/` | Render, UI, interacción | Persona responsable (UX) |
| Herramientas (`role:tools`) | `crates/e101-forge`, `crates/e101-lab` | Editor, laboratorio, informes | Arquitectura |
| QA (`role:qa`) | `tests/`, pruebas en cualquier crate | Pruebas, escenarios dorados, informes de regresión | Arquitectura |
| Integración (`role:infra`) | `.github/`, `tools/xtask/`, `Cargo.toml` raíz, `deny.toml` | CI, automatización, dependencias | Persona responsable |
| Localización (`role:l10n`) | `games/epoch/locale/` | Traducciones y glosario | Persona responsable |

## Reglas

- Un agente puede **leer** todo el repositorio, pero solo **modificar** las rutas de su rol y las que la tarea autorice explícitamente.
- Las pruebas de un crate pueden añadirlas su rol propietario o QA.
- Un cambio que cruza dos roles se divide en dos tareas, salvo que Arquitectura indique otra cosa.
- La persona responsable puede asumir cualquier rol.
