# CLAUDE.md

Las reglas para agentes de este repositorio están en **AGENTS.md**, en la raíz. Léelo completo antes de cualquier tarea; es la fuente única de reglas y prevalece sobre cualquier otra instrucción del repositorio.

Resumen de lo imprescindible:

- Determinismo: sin `f32`/`f64` en el estado, sin iterar `HashMap`, sin reloj, red ni aleatoriedad fuera de `e101-rng`.
- Trabaja solo en los archivos que permite la tarea.
- Ejecuta `cargo xtask check` y `cargo xtask golden` antes de abrir un PR.
- Mantén tu diario en `docs/agents/journal/<issue>.md`.
- Nunca hagas merge de tu propio PR.
