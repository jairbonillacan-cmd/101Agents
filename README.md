# 101Agents

Monorepo de **101 Agents Games**: el motor **101 Engine**, el contenido del primer juego (nombre de trabajo *Project Epoch*), sus herramientas y el sitio web del estudio.

> **Estado: preproducción.** El repositorio contiene el documento maestro, las reglas para agentes de IA y el prototipo del sitio web. El código del motor, `tools/xtask` y las guías de estilo (`docs/style/`) se añadirán en las Fases 0 y 1; hasta entonces, los comandos `cargo xtask` descritos en `AGENTS.md` son la especificación de lo que debe existir.

## Empezar

- **Personas:** lee el documento maestro en `docs/master/` y las decisiones en `docs/adr/`.
- **Agentes de IA:** lee **`AGENTS.md`** antes de cualquier tarea. Para el sitio web, lee además `website/AGENTS.md`.

## Estructura

| Ruta | Contenido |
| --- | --- |
| `docs/master/` | Documento maestro (v0.7) y plan del sitio web (v0.1). |
| `docs/adr/` | Decisiones de arquitectura (plantilla incluida). |
| `docs/agents/` | Roles, flujo de trabajo, prompts, preguntas frecuentes y plantilla de diario. |
| `crates/` | Crates de Rust con prefijo `e101-` (por ahora, la plantilla de `CONTEXT.md`). |
| `website/` | Sitio web del estudio (Astro, estático, ES/EN). |
| `.github/` | Plantillas de tareas y PR, `CODEOWNERS` y workflows de CI. |
| `AGENTS.md` | Reglas para agentes de IA (fuente única). |
| `CLAUDE.md` | Remite a `AGENTS.md`. |

## Sitio web

```sh
cd website
npm ci
npm run dev      # http://127.0.0.1:4321
npm run build
npm run check
```

El CI del sitio (`.github/workflows/website.yml`) se ejecuta solo cuando cambia `website/`.

## Seguridad

No se suben secretos, claves, tokens, archivos `.env`, dependencias instaladas ni resultados de compilación (ver `.gitignore`). Si encuentras un secreto en el historial, avisa al responsable para rotarlo de inmediato.

## Licencia

**Propietaria, código visible solo como referencia** (ver [`LICENSE`](LICENSE)). Todos los derechos reservados: que el repositorio sea público permite leerlo, pero **no se concede permiso de uso, copia, modificación ni redistribución** sin autorización escrita. Las dependencias de terceros conservan sus propias licencias. Las contribuciones se aceptan solo por invitación.
