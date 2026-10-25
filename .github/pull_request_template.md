## Resumen

<!-- Qué cambia y por qué, en 2–4 frases. -->

## Tarea y diario

- Tarea: #<issue>
- Diario: `docs/agents/journal/<issue>.md`
- Rol: <rol>

## Cambios

- …

## Verificación

- [ ] `cargo xtask check`
- [ ] `cargo xtask golden` (sin cambios de hash, o etiqueta `golden-change` justificada)
- [ ] `cargo xtask bench` (si toca simulación o rendimiento)
- [ ] `cargo xtask data` (si toca contenido)
- [ ] `CONTEXT.md` actualizado (si cambió el propósito o los invariantes del crate)

## Determinismo y contabilidad

- [ ] Sin `f32`/`f64` en estado persistente
- [ ] Sin iteración de `HashMap`/`HashSet`
- [ ] Aleatoriedad solo mediante `e101-rng`
- [ ] Cambios visibles registrados en el ledger

## Aprobaciones necesarias

<!-- Marca las que apliquen y añade la etiqueta correspondiente. -->

- [ ] Nueva dependencia (`new-dependency`)
- [ ] Cambio de interfaz pública (`api-change` + ADR)
- [ ] Cambio de hashes dorados (`golden-change`)
- [ ] Datos históricos A/B (`needs-history-review`)
- [ ] Contenido sensible (`needs-sensitive-review`)

## No incluido / pendiente

- …
