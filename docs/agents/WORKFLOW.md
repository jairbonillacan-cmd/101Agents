# Flujo de trabajo de una tarea

## Estados

`status:draft` → `status:ready` → `status:in-progress` → `status:review` → `status:done`

Estados laterales: `needs-human` (bloqueada), `status:blocked` (depende de otra tarea).

## Pasos

1. **Preparación (persona o Arquitectura).** La tarea se redacta con la plantilla, incluyendo archivos permitidos y criterios de aceptación. Pasa a `status:ready`.
2. **Reclamo.** El agente se asigna la tarea y la pasa a `status:in-progress`. Solo un agente por tarea.
3. **Contexto.** Lee `AGENTS.md`, la tarea, los `CONTEXT.md` de los crates afectados y las secciones del documento maestro citadas.
4. **Plan.** Escribe en su diario un plan breve: pasos, pruebas, riesgos. Si el plan contradice la tarea, pregunta.
5. **Implementación.** Cambios pequeños con pruebas; `cargo xtask check` frecuente.
6. **Verificación.** `check`, `golden`, y según el caso `bench`, `data` o `lab`.
7. **PR.** Plantilla completa, enlaces a tarea y diario, lista de pendientes.
8. **Revisión.** El rol revisor comenta. El agente corrige en la misma rama.
9. **Aprobación humana** si alguna etiqueta la exige (ver AGENTS.md §10).
10. **Merge** por la persona responsable o por el rol revisor con permiso. El agente nunca hace merge de su propio PR.
11. **Cierre.** La tarea pasa a `status:done`; el diario queda en el repositorio como registro.

## Tamaño de las tareas

- Ideal: entre 2 y 6 horas de trabajo de agente.
- Máximo: ~400 líneas cambiadas sin contar pruebas ni datos generados.
- Si una tarea crece más, se divide.

## Trabajo en paralelo

- Cada agente trabaja en su propia rama y, si la herramienta lo permite, en su propio *worktree*.
- Dos agentes no pueden modificar el mismo crate a la vez salvo que la tarea lo indique.
- Las interfaces entre crates se acuerdan primero (tarea de Arquitectura con ADR) y después se implementan en paralelo detrás de esa interfaz.
- Si un agente necesita algo de otra tarea en curso, marca `status:blocked` y enlaza la dependencia.
