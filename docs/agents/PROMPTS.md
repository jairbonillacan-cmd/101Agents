# Biblioteca de prompts

Prompts base para encargar tareas a agentes. Sustituye lo que está entre `< >`.

## Prompt general de tarea

```text
Trabajas en el repositorio 101-engine con el rol <rol>.
Lee AGENTS.md completo, después la tarea <enlace o ruta> y los CONTEXT.md de <crates>.
Objetivo: <objetivo en una frase>.
Solo puedes modificar: <rutas>.
Criterios de aceptación: <lista>.
Antes de escribir código, escribe tu plan en docs/agents/journal/<issue>.md.
Termina con cargo xtask check y cargo xtask golden en verde y abre un PR con la plantilla.
Si algo no está claro o necesitas tocar otras rutas, pregunta antes.
```

## Arquitectura: nuevo contrato entre crates

```text
Rol: architecture. Redacta un ADR en docs/adr/ y la interfaz pública (solo firmas y tipos,
con documentación) para <funcionalidad> entre <crate A> y <crate B>.
Incluye: responsabilidades de cada lado, tipos compartidos, invariantes, cómo se prueba,
alternativas descartadas. No implementes la lógica.
```

## Simulación: nuevo sistema

```text
Rol: sim. Implementa el sistema <nombre> en crates/e101-sim/src/<ruta> según la especificación
de la sección <n> del documento maestro y el ADR <id>.
Firma obligatoria: fn run(state: &State, deltas: &mut Deltas).
Registra en el ledger todo cambio visible. Añade pruebas de propiedad para los invariantes
<lista> y un escenario dorado en tests/golden/<nombre>.
```

## Historia: nueva entidad o situación

```text
Rol: history. Añade <entidad o situación> en games/epoch/data/<ruta> siguiendo el formato
del Anexo E. Cada dato lleva fuente y confianza. No inventes datos: si no estás seguro,
usa confianza C o D y explícalo en el diario. Ejecuta cargo xtask data.
Etiqueta el PR con needs-history-review.
```

## QA: investigar una desincronización

```text
Rol: qa. Las ejecuciones doradas <escenario> difieren a partir del tick <n> entre <commit A>
y <commit B>. Usa cargo xtask golden --bisect para localizar el primer tick y el sistema
responsable. Documenta la causa en el diario y propón una corrección mínima con prueba.
```

## Rendimiento: optimizar un sistema

```text
Rol: engine. El sistema <nombre> supera su presupuesto (<medido> frente a <objetivo>).
Perfila con Tracy usando cargo xtask bench --profile <escenario>. Propón y aplica una
optimización que no cambie los hashes dorados. Adjunta antes y después en el PR.
```

## Revisión de un PR

```text
Revisa el PR <enlace> como rol <rol revisor>. Comprueba:
1. Cumple los criterios de aceptación de la tarea.
2. Respeta AGENTS.md §3 (determinismo) y §10 (aprobaciones).
3. Las pruebas cubren los invariantes afectados.
4. No modifica rutas fuera de la tarea.
5. El registro causal se actualiza donde corresponde.
Responde con: aprobar, aprobar con cambios menores o solicitar cambios, y una lista concreta.
```
