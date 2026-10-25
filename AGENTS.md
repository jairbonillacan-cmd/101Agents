# AGENTS.md — Instrucciones para agentes de IA en `101Agents`

Este archivo es la **fuente única de reglas** para cualquier agente de IA que trabaje en este repositorio. Léelo completo antes de cualquier tarea. Si otra instrucción del repositorio lo contradice, este archivo manda, salvo que la persona responsable diga otra cosa en la tarea.

## 1. Qué es este repositorio

`101Agents` es el monorepo de **101 Agents Games**. Es **público**: todo lo que subas lo puede leer cualquiera. Contiene:

- **101 Engine**: un motor de simulación de gran estrategia histórica escrito en Rust.
- El contenido del primer juego (nombre de trabajo *Project Epoch*), en `games/epoch/`.
- Herramientas: 101 Forge (editor), 101 Lab (simulación masiva), pipeline de datos.
- El sitio web del estudio, en `website/`, con sus propias reglas en `website/AGENTS.md` (las de este archivo también se aplican).

El documento de diseño completo está en `docs/master/`. Las decisiones están en `docs/adr/`. Ante cualquier duda de diseño, **consulta primero esos documentos** y no inventes reglas nuevas.

## 2. Principios que nunca se rompen

1. **Determinismo.** Mismo binario + mismos datos + misma semilla + mismos comandos ⇒ mismo estado bit a bit.
2. **Comandos, no mutaciones.** El cliente, la IA y los eventos emiten comandos; solo la fase de aplicación modifica el estado.
3. **Contabilidad exacta.** Ningún bien, persona o unidad de dinero aparece ni desaparece sin una regla registrada.
4. **Registro causal.** Todo cambio en una variable visible para el jugador registra su origen.
5. **El núcleo no conoce el cliente.** Los crates de simulación no dependen de ninguna biblioteca gráfica.
6. **Historia condicional.** Nada histórico ocurre por fecha; todo ocurre por condiciones.

## 3. Reglas de código en los crates de simulación

Se aplican a `e101-time`, `e101-store`, `e101-commands`, `e101-ledger`, `e101-rng`, `e101-sim`, `e101-history`, `e101-map`, `e101-content`, `e101-script`, `e101-save` y `e101-ai`.

- **Prohibido** `f32`/`f64` en el estado persistente y en la contabilidad. Usa los tipos de punto fijo de `e101-store::fixed` (`Money`, `Qty`, `Ratio`).
- **Prohibido** iterar `std::collections::HashMap` o `HashSet`. Usa vectores indexados por ID, `BTreeMap` o `IndexMap`.
- **Prohibido** leer el reloj del sistema, la red, el sistema de archivos o variables de entorno desde la lógica de simulación.
- **Prohibida** cualquier aleatoriedad que no venga de `e101-rng::rng(seed, system, entity, day)`.
- **Prohibido** `unsafe` sin un ADR aprobado.
- Los sistemas tienen la firma `fn run(state: &State, deltas: &mut Deltas)`; nunca escriben en `State` directamente.
- Todo delta que afecte a una variable visible llama a `ledger.record(...)` con su origen.

El CI tiene lints que comprueban estas reglas. Si un lint falla, corrige el código: no desactives el lint.

## 4. Antes de empezar una tarea

1. Lee la tarea completa (issue o archivo en `docs/agents/tasks/`).
2. Lee el `CONTEXT.md` de cada crate que vayas a tocar.
3. Confirma que la tarea indica: objetivo, archivos permitidos, criterios de aceptación y pruebas requeridas. Si falta algo esencial, **pregunta** en la tarea antes de escribir código.
4. Crea una rama: `agent/<rol>/<issue>-<descripcion-corta>`.
5. Crea tu diario: `docs/agents/journal/<issue>.md` a partir de la plantilla.

## 5. Durante la tarea

- Trabaja **solo** en los archivos que permite la tarea. Si necesitas tocar otro, anótalo en el diario y pregunta.
- Haz cambios pequeños y verificables. Un PR no debería superar ~400 líneas cambiadas, sin contar pruebas ni datos generados.
- Escribe las pruebas **antes o junto** al código, nunca después de abrir el PR.
- Ejecuta `cargo xtask check` con frecuencia.
- Si cambias una interfaz pública de un crate, detente: hace falta un ADR y revisión del rol de Arquitectura.
- Registra en el diario las decisiones que tomes y por qué.

## 6. Comandos

| Comando | Qué hace |
| --- | --- |
| `cargo xtask check` | Formato, clippy, lints de determinismo y pruebas. Obligatorio antes de abrir un PR. |
| `cargo xtask test <crate>` | Pruebas de un crate. |
| `cargo xtask golden` | Ejecuta los escenarios de determinismo y compara hashes. |
| `cargo xtask golden --bless` | Actualiza los hashes. **Solo** con la etiqueta `golden-change` aprobada por una persona. |
| `cargo xtask golden --bisect <escenario>` | Localiza el primer tick en el que dos versiones divergen y el sistema responsable. |
| `cargo xtask bench` | Benchmarks; compara con la rama principal. |
| `cargo xtask data` | Compila el contenido de `games/epoch/data` y ejecuta los validadores. |
| `cargo xtask lab --campaigns 20` | Ejecuta campañas cortas de 101 Lab y genera un informe local. |
| `cargo xtask docs` | Genera la documentación de los crates. |

## 7. Al terminar

1. `cargo xtask check` y `cargo xtask golden` en verde.
2. Si tocaste rendimiento o sistemas de simulación: `cargo xtask bench` sin regresiones mayores del 5 %.
3. Si tocaste datos: `cargo xtask data` sin errores ni advertencias nuevas.
4. Actualiza el `CONTEXT.md` del crate si cambiaste su propósito, sus invariantes o sus límites.
5. Abre el PR con la plantilla completa. Enlaza la tarea y el diario.
6. En el PR, enumera lo que **no** hiciste y lo que queda pendiente.

## 8. Mensajes de commit

Formato *Conventional Commits* en inglés:

```text
feat(sim): add weekly price adjustment with damping
fix(save): keep command log order on reload
test(ledger): property tests for contribution totals
docs(adr): 0007 choose postcard for save files
data(epoch): add Thessaly 1300 entity with sources
```

## 9. Datos históricos

- Todo dato histórico nuevo lleva **fuente** y **nivel de confianza** (A, B, C o D).
- Los datos A y B requieren verificación humana antes del merge: añade la etiqueta `needs-history-review`.
- No inventes gobernantes, fechas ni cifras. Si no sabes algo, usa nivel C o D y dilo en el diario.
- El contenido sensible (esclavitud, violencia masiva, persecuciones) sigue `docs/style/sensitive-content.md` y lleva la etiqueta `needs-sensitive-review`.
- No copies texto de libros, artículos ni juegos. Resume con tus palabras y cita la fuente.

## 10. Lo que requiere aprobación humana

| Cambio | Etiqueta |
| --- | --- |
| Nueva dependencia externa | `new-dependency` (incluye licencia y motivo) |
| Cambio de interfaz pública entre crates | `api-change` + ADR |
| Actualizar hashes de ejecuciones doradas | `golden-change` |
| Regresión de rendimiento > 5 % | `perf-regression` |
| Datos históricos de confianza A o B | `needs-history-review` |
| Contenido sensible | `needs-sensitive-review` |
| Cambios en CI, permisos o secretos | `infra` |

Nunca hagas merge de tu propio PR.

## 11. Seguridad

- No añadas secretos, claves ni tokens al repositorio.
- No subas conversaciones con agentes, notas personales ni datos personales. Los diarios de `docs/agents/journal/` recogen solo decisiones técnicas de la tarea.
- No subas `node_modules/`, resultados de compilación, archivos `.env` ni la identidad privada de alojamiento del sitio (`website/.openai/`).
- No ejecutes scripts descargados de Internet.
- Las pruebas no acceden a la red.
- No modifiques `.github/workflows/` salvo en tareas del rol de Integración.

## 12. Si te bloqueas

1. Describe el bloqueo en el diario: qué intentaste, qué falló, qué necesitas.
2. Añade la etiqueta `needs-human` a la tarea.
3. No hagas cambios grandes para “rodear” el problema.

## 13. Dónde está cada cosa

| Ruta | Contenido |
| --- | --- |
| `crates/` | Crates de Rust con prefijo `e101-`. |
| `games/epoch/data/` | Contenido del juego en RON y CSV. |
| `games/epoch/locale/` | Traducciones (Fluent). |
| `data-build/` | Pipeline geográfico e histórico. |
| `tests/golden/` | Escenarios de determinismo. |
| `tools/xtask/` | Automatización del repositorio. |
| `docs/master/` | Documento maestro. |
| `docs/adr/` | Decisiones de arquitectura. |
| `docs/specs/` | Especificaciones por sistema. |
| `docs/agents/` | Roles, flujo, prompts, tareas y diarios. |
| `docs/style/` | Guía de estilo de código y de contenido. |
| `website/` | Sitio web del estudio (Astro). |
