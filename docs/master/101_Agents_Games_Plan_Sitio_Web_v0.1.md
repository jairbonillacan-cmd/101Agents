# 101 Agents Games — Plan del sitio web

> **Versión:** 0.1  
> **Fecha:** 24 de octubre de 2026  
> **Ámbito:** sitio público del estudio y del primer juego (nombre de trabajo *Project Epoch*)  
> **Relación con el documento maestro:** desarrolla las secciones 19 (dirección de arte), 20 (comunidad), 28 (calendario) y 30 (publicación, negocio y marca), y el Anexo H (hoja de ruta posterior al lanzamiento).  
> **Estado:** documento de planificación. Usa las mismas etiquetas que el documento maestro: **Definido**, **Propuesto**, **Objetivo**, **Abierto**.

**Propósito.** Un único sitio donde vive todo lo público del proyecto: la presentación del juego y del estudio, los diarios de desarrollo, el registro de cambios, la hoja de ruta, los materiales de prensa y, más adelante, la documentación para modders.

---

## 1. Objetivos y principios

### Objetivos

| # | Objetivo | Indicador (Objetivo) |
| --- | --- | --- |
| O-1 | Explicar en menos de 30 segundos qué es el juego y por qué es distinto. | En pruebas con 5 personas, 4 lo resumen con sus palabras tras ver la portada. |
| O-2 | Construir audiencia antes de Steam: suscriptores al boletín y seguidores. | Lista de correo activa antes de la Fase 5; después, conversión a lista de deseos de Steam. |
| O-3 | Ser la fuente oficial y honesta del estado del proyecto. | Hoja de ruta y registro de cambios actualizados como máximo 30 días después de cada hito. |
| O-4 | Facilitar el trabajo de prensa y creadores. | Kit de prensa descargable completo antes de la página de Steam. |
| O-5 | Preparar la casa de los modders. | Documentación pública de formatos lista para la 1.0 (F-PLT-02). |

### Principios

- **Honestidad del estado.** El sitio refleja la regla del documento maestro: las fechas son estimaciones, no compromisos. Cada elemento de la hoja de ruta muestra su estado real y nada se presenta como terminado si no lo está.
- **Mostrar el “¿por qué?”.** El diferenciador del juego es la causalidad explicable; el sitio lo demuestra con ejemplos concretos (como “un año de partida” de la sección 01), no con adjetivos.
- **Misma estética que el juego.** Sobriedad, el mapa como protagonista y la época visible (sección 19). Se evita la estética genérica de IA: gradientes neón, cubos 3D, brillos, redes neuronales.
- **El nombre del juego puede cambiar.** La arquitectura del sitio no depende del título provisional (ver sección 4).
- **Privacidad por defecto.** Coherente con la política de telemetría (sección 30): sin cookies de seguimiento, analítica agregada y anónima.
- **Bilingüe desde el primer día.** Español e inglés, como el vertical slice.
- **Contenido como datos.** Hoja de ruta, registro de cambios y fichas se escriben como archivos estructurados en el repositorio; las páginas se generan a partir de ellos.

---

## 2. Públicos y qué busca cada uno en el sitio

Deriva del público objetivo de la sección 01.

| Público | Qué viene a buscar | Secciones clave |
| --- | --- | --- |
| Jugadores veteranos de gran estrategia | Profundidad, sistemas, ritmo de desarrollo, fecha de acceso. | El juego, Sistemas, Hoja de ruta, Diarios. |
| Aficionados a la historia | Plausibilidad, el mundo en 1300, “¿qué habría pasado si…?”. | El mundo, Situaciones históricas, Diarios. |
| Modders y comunidad técnica | Formatos, determinismo, herramientas. | 101 Engine, Modding (desde 1.0), Registro de cambios. |
| Docentes y divulgadores | Uso en clase o en vídeo, modo observador. | El juego, Prensa y creadores. |
| Prensa, creadores y festivales | Datos, capturas, tráiler, contacto. | Prensa (kit), Contacto. |
| Personas curiosas por el desarrollo con IA | Cómo trabaja un estudio con agentes de IA. | Estudio, Diarios técnicos. |

---

## 3. Mapa del sitio

Las secciones se activan por etapas (ver sección 7). La columna **Etapa** indica cuándo se publica cada una.

| Ruta | Sección | Contenido | Etapa |
| --- | --- | --- | --- |
| `/` | Inicio | Pitch, fantasía del jugador, recorrido visual por las épocas, estado actual del proyecto, último diario, suscripción (después, lista de deseos de Steam). | W1 |
| `/juego/` | El juego | Presentación completa: pitch, pilares, diferenciadores, bucles de juego, “un año de partida”, qué *no* es (no es un sandbox sin reglas). | W1 |
| `/juego/sistemas/` | Sistemas | Una ficha por gran sistema: población, economía, gobierno, diplomacia, guerra, ciencia, clima y epidemias, personajes, IA. Cada una con un ejemplo resuelto del documento maestro. | W2 |
| `/juego/epocas/` | Épocas | Las seis épocas de la Parte VII (1300 → más allá de 2060): identidad, qué pesa más, estilo cartográfico. Marcadas como “en la vertical” o “futuras”. | W2 |
| `/juego/mundo/` | El mundo en 1300 | Panorama por regiones; fichas de las 18 entidades jugables del vertical slice (Anexo I). | W3 |
| `/juego/situaciones/` | Situaciones históricas | Muestra del catálogo (p. ej. la caída de Constantinopla) explicando causas, variantes y divergencia. | W3 |
| `/motor/` | 101 Engine | Determinismo, registro causal, simulación sin render, 101 Lab, 101 Forge. Nivel divulgativo con enlaces a diarios técnicos. | W2 |
| `/diarios/` | Diarios de desarrollo | Blog: técnicos (determinismo, registro causal, mapa) desde la Fase 2; de diseño e historia después. Etiquetas por sistema y fase. RSS. | W1 |
| `/cambios/` | Registro de cambios | Versiones del juego (internas, demo, acceso anticipado, parches), del documento de diseño público y del propio sitio. Filtros por canal y tipo. RSS. | W1 |
| `/hoja-de-ruta/` | Hoja de ruta | Fases 0–7 con estado, entregable y “puerta de salida”; después del lanzamiento, los bloques del Anexo H. | W1 |
| `/prensa/` | Prensa y creadores | Ficha técnica, descripción corta y larga, logotipos, capturas, tráiler, fotos, contacto de prensa, política para creadores de contenido. | W2 |
| `/comunidad/` | Comunidad | Discord, boletín, redes, normas de conducta, cómo enviar comentarios. | W1 |
| `/modding/` | Modding | Documentación de formatos de datos y del lenguaje de condiciones; guías; versiones compatibles. | W4 |
| `/estudio/` | Estudio | Quiénes somos, cómo se desarrolla con agentes de IA y revisión humana, principios (historia con inercia, contenido sensible, uso responsable de IA). | W1 |
| `/faq/` | Preguntas frecuentes | Plataformas, precio orientativo, fecha, idiomas, requisitos, multijugador, uso de IA. | W2 |
| `/legal/…` | Legal | Aviso legal, privacidad, cookies (si las hubiera), términos, declaración de uso de IA en recursos. | W1 |
| `/en/…` | Versión en inglés | Espejo completo de todas las rutas. | W1 |

### Navegación

- **Barra principal (5 entradas como máximo):** El juego · Diarios · Hoja de ruta · Cambios · Comunidad.
- **Botón de llamada a la acción fijo:** “Suscríbete” hasta que exista la página de Steam; después, “Añadir a la lista de deseos”; con la demo, “Prueba la demo”.
- **Pie de página:** Estudio, 101 Engine, Prensa, FAQ, Legal, RSS, idioma, redes.

---

## 4. Dominio, marca y nombre del juego

| Elemento | Propuesta | Estado |
| --- | --- | --- |
| Dominio principal | Dominio del estudio (p. ej. `101agentsgames.com`). Todo el contenido del juego cuelga de él. | **Abierto** — verificar disponibilidad (sección 30: reservar dominio y cuentas antes de la presencia pública). |
| Dominio del juego | Se reserva cuando exista el título comercial y redirige a la sección del juego. | **Abierto** — depende del nombre. |
| Rutas | Neutras respecto al título: `/juego/`, no `/epoch/`. Así el cambio de nombre no rompe enlaces ni posicionamiento. | **Propuesto** |
| Nombre visible | “Project Epoch (nombre provisional)” en todas las páginas hasta el anuncio del título. | **Propuesto** |
| Registro de marca | Verificar y registrar *101 Agents Games* y *101 Engine* antes de lanzar W1. | **Definido** en el documento maestro como requisito previo. |
| Identidad | Logotipo final, variantes, favicon, tipografías y paleta de la guía de identidad (sección 30). El sitio usa esa guía; si no está lista en W1, se lanza con un logotipo tipográfico provisional. | **Propuesto** |

---

## 5. Dirección de arte del sitio

Aplica la sección 19 del documento maestro al medio web.

### Idea central: el sitio viaja en el tiempo

El elemento distintivo de la portada es un **recorrido por las épocas**: al desplazarse, el mismo fragmento de mapa (el Mediterráneo oriental del vertical slice) cambia de estilo cartográfico y de tipografía, siguiendo la tabla de la sección 19:

| Tramo de la portada | Estilo |
| --- | --- |
| 1300–1500 | Pergamino, tintas sepia, rotulación caligráfica. |
| 1500–1750 | Grabado en cobre, cartelas, acuarela. |
| 1750–1900 | Cartografía topográfica, colores planos, tipografía de periódico. |
| 1900–1990 | Mapa de estado mayor, atlas escolar, informe técnico. |
| 1990+ | Cartografía digital limpia con datos superpuestos. |

En cada tramo, un texto breve cuenta una cadena causal (“la guarnición llevaba cinco meses sin cobrar…”), para que el diferenciador se entienda sin explicarlo.

**Requisitos:** funciona sin JavaScript (las épocas se muestran en secuencia estática), respeta `prefers-reduced-motion` y las imágenes se cargan de forma diferida. Al principio se usan ilustraciones estáticas; cuando el render de mapa del juego exista (Fase 1), se sustituyen por capturas reales.

### Sistema visual

- **Tipografía:** una serif con carácter histórico para títulos y una sans muy legible para el texto. Las dos con soporte completo de español y licencia web clara.
- **Color:** paleta sobria derivada del pergamino y la tinta para el modo claro; modo oscuro tipo “mesa de mapas nocturna”. Contraste AA como mínimo.
- **Componentes propios:** tarjeta de estado (Definido / Propuesto / Objetivo / Abierto), cronología de fases, ficha de entidad, bloque “cadena causal”, nota de versión.
- **Imágenes:** solo capturas reales cuando existan; las ilustraciones conceptuales se etiquetan como tales. Los recursos generados con IA, si se usan, se revisan por licencia y calidad y se declaran (sección 19).

---

## 6. Secciones clave en detalle

### 6.1 Presentación del juego (`/juego/`)

Estructura de la página, en este orden:

1. **Pitch** (sección 01) y una imagen dominante del mapa.
2. **Fantasía del jugador:** “Guío a mi pueblo a lo largo de siete siglos y entiendo exactamente por qué el mundo terminó siendo como es.”
3. **Cinco diferenciadores**, cada uno con un ejemplo de una línea.
4. **Un año de partida:** el ejemplo bizantino de 1303 como historia ilustrada, terminando en el registro causal.
5. **Los bucles de juego** (inmediata, operativa, estratégica, histórica) como diagrama.
6. **Lo que no es:** no es un sandbox sin reglas; la historia tiene inercia, no guion.
7. **Estado del proyecto** (componente compartido con la portada) y llamada a la acción.

### 6.2 Diarios de desarrollo (`/diarios/`)

- **Ritmo (Objetivo):** uno al mes desde la Fase 2; cada dos semanas desde la página de Steam.
- **Tipos:** técnico, diseño, historia, arte, estudio. Cada diario lleva fase, sistemas relacionados y tiempo de lectura.
- **Primeros temas propuestos**, alineados con la sección 30:
  1. Por qué una sola partida de 1300 a 2060.
  2. La historia tiene inercia, no guion: así funciona 101 History.
  3. Determinismo: la misma semilla, la misma historia.
  4. El registro causal: preguntarle “¿por qué?” a un precio.
  5. Un estudio con agentes de IA: reglas, revisión humana y límites.
  6. Dibujar el mapa: de la textura de IDs al pergamino.
- **Reutilización:** cada diario genera un resumen para el boletín, Steam (cuando exista) y redes.

### 6.3 Registro de cambios (`/cambios/`)

Un único registro con **canales** filtrables:

| Canal | Qué registra | Desde |
| --- | --- | --- |
| `juego` | Builds: internas (resumen público opcional), demo, acceso anticipado, parches. Versionado semántico. | Fase 1 (resúmenes de hitos) |
| `diseño` | Versiones públicas del documento de diseño (resumen de cambios, como la sección “Cambios en la versión 0.6”). | W1 |
| `sitio` | Cambios relevantes del propio sitio. | W1 |

**Formato de cada entrada:** versión, fecha, canal, resumen de una línea y cambios agrupados en *Añadido*, *Cambiado*, *Corregido*, *Eliminado* y *Rendimiento*. Las entradas de juego enlazan con el diario correspondiente si existe.

**Origen de los datos (Propuesto):**

- El monorepo `101-engine` mantiene un `CHANGELOG.md` interno a partir de los commits y PR (sección 44).
- Un script genera un **borrador público** al etiquetar una versión; una persona lo edita (se eliminan detalles internos, se reescribe para jugadores) y lo publica como archivo en el repositorio del sitio.
- Nada pasa del registro interno al público sin revisión humana. El repositorio del juego es privado hasta el acceso anticipado (sección 39).

### 6.4 Hoja de ruta (`/hoja-de-ruta/`)

- **Antes del lanzamiento:** cronología de las fases 0–7 de la sección 28. Cada fase muestra periodo orientativo, entregable resumido para jugadores, puerta de salida en lenguaje claro y estado.
- **Estados:** *Completado*, *En curso*, *Siguiente*, *Planificado*, *En revisión* (cuando una fase se retrasa más de un 50 % y se revisa el alcance, como dicta la sección 28).
- **Después del lanzamiento:** tablero por bloques del Anexo H (actualizaciones gratuitas, expansiones regionales y temporales, multijugador, Forge público), sin fechas hasta que estén confirmadas.
- **Aviso fijo:** “Las fechas son orientativas y pueden cambiar. Cuando cambien, lo explicaremos en un diario.”
- **Historial:** cada modificación de la hoja de ruta queda en el canal `diseño` del registro de cambios, para que los cambios de plan sean visibles.
- **Origen de los datos:** un archivo `roadmap.yaml` en el repositorio del sitio, editado por una persona.

### 6.5 Prensa y creadores (`/prensa/`)

Ficha técnica (estudio, motor, plataformas, fecha orientativa, precio orientativo cuando se anuncie, idiomas), descripciones de 50 y 200 palabras, historia del proyecto, logotipos en todas sus variantes, capturas en alta resolución, tráiler, contacto y permiso explícito para que los creadores moneticen vídeos del juego. Todo descargable en un ZIP.

### 6.6 Estudio (`/estudio/`)

Explica sin rodeos que el juego se desarrolla con agentes de IA bajo revisión humana obligatoria: qué hacen los agentes, qué decide siempre una persona (sección 10 de `AGENTS.md`), cómo se revisa el contenido histórico y el sensible, y la política de recursos generados con IA. La transparencia aquí evita polémicas y además es un tema de interés propio.

---

## 7. Etapas del sitio, alineadas con las fases del juego

| Etapa | Periodo orientativo | Fase del juego | Qué se publica | Puerta de salida |
| --- | --- | --- | --- | --- |
| **W0 — Preparación** | Nov–dic 2026 | 0 | Nada público. Verificar y reservar dominio, cuentas y marca; repositorio del sitio; diseño base; textos de El juego y Estudio. | Dominio y cuentas reservados; marca verificada; prototipo navegable en local. |
| **W1 — Presentación** | Ene–mar 2027 | 1 | Inicio, El juego, Estudio, Hoja de ruta, Registro de cambios (canal `diseño` y `sitio`), Comunidad, Legal, boletín, ES/EN. | Las 5 pruebas de O-1 superadas; Lighthouse ≥ 95 en todas las categorías; sin cookies de seguimiento. |
| **W2 — Diarios y sistemas** | Abr 2027 – dic 2027 | 2–4 | Diarios mensuales (empezando por los técnicos), Sistemas, Épocas, 101 Engine, FAQ, Prensa básica, Discord. | Seis diarios publicados; hoja de ruta actualizada en cada puerta de fase. |
| **W3 — Steam y vertical** | Ene–abr 2028 | 5 | Página de Steam enlazada, botón de lista de deseos, tráiler, capturas reales, El mundo en 1300, Situaciones, kit de prensa completo. | Kit de prensa completo; tráfico del sitio medido hacia Steam. |
| **W4 — Demo y acceso anticipado** | Tras el slice / 2029 | 6–7 | Página de la demo y festivales, registro de cambios por parche, hoja de ruta pública con bloques posteriores, Modding, wiki o enciclopedia (por decidir). | Registro de cambios publicado el mismo día de cada parche. |

---

## 8. Arquitectura técnica (Propuesto)

### Decisión recomendada

| Pieza | Recomendación | Motivo |
| --- | --- | --- |
| Generador | **Astro** (sitio estático) | Contenido en Markdown/MDX con colecciones tipadas, rutas multilingües integradas, cero JavaScript por defecto y componentes interactivos solo donde hacen falta (recorrido por épocas, filtros). |
| Contenido | Archivos en el repositorio: `src/content/diarios/*.mdx`, `cambios/*.md`, `roadmap.yaml`, `entidades/*.md`, `prensa/*.yaml`. | Se versiona con git, se revisa en PR y los agentes pueden trabajar con él igual que con el resto del proyecto. |
| Esquemas | Validación con esquemas de las colecciones (campos obligatorios, fechas, estados, canales). | Una entrada mal formada rompe la build, no la página publicada. |
| Alojamiento | **Cloudflare Pages** (alternativas: Netlify, GitHub Pages). | Gratuito o casi para un sitio estático, CDN global, vistas previas por PR. |
| Repositorio | `101-agents-games/website`, separado del monorepo. | El monorepo es privado y tiene reglas de determinismo que no aplican a la web; el sitio puede hacerse público antes. |
| Boletín | Proveedor con doble confirmación y alojamiento de datos compatible con el RGPD (p. ej. Buttondown). | Exportable, sin seguimiento invasivo. **Abierto.** |
| Analítica | Sin cookies (Cloudflare Web Analytics, Plausible o Umami). | Permite no mostrar banner de cookies y es coherente con la sección 30. |
| Búsqueda | Índice estático (p. ej. Pagefind) desde W2. | Sin servidor ni servicios externos. |
| RSS | Para diarios y registro de cambios. | Lo espera el público técnico y de estrategia. |
| Formularios | Solo suscripción al boletín y contacto de prensa por correo. | Superficie mínima: menos datos personales y menos mantenimiento. |

### Estructura del repositorio del sitio

```text
website/
├── AGENTS.md                 reglas para agentes en este repositorio
├── astro.config.mjs          i18n es/en, sitemap, integración MDX
├── public/                   favicon, imágenes optimizadas, kit de prensa
├── src/
│   ├── content/
│   │   ├── diarios/          es/ y en/
│   │   ├── cambios/          una entrada por versión y canal
│   │   ├── entidades/        fichas del vertical slice (desde W3)
│   │   └── config.ts         esquemas de las colecciones
│   ├── data/
│   │   ├── roadmap.yaml      fases, estados y bloques posteriores
│   │   └── estado.yaml       estado actual del proyecto (portada)
│   ├── components/           EraJourney, StatusBadge, PhaseTimeline,
│   │                         CausalChain, ChangelogEntry, EntityCard
│   ├── layouts/
│   ├── i18n/                 textos de interfaz es/en
│   └── pages/                rutas (espejo en /en/)
├── scripts/
│   └── changelog-draft.ts    borrador público a partir del CHANGELOG interno
└── .github/workflows/
    └── ci.yml                build, validación de contenido, enlaces, Lighthouse
```

### Calidad y rendimiento (Objetivo)

- Lighthouse ≥ 95 en rendimiento, accesibilidad, buenas prácticas y SEO.
- Portada con menos de 200 KB de JavaScript y LCP por debajo de 2,5 s en móvil.
- **WCAG 2.2 AA**: contraste, navegación por teclado, textos alternativos, movimiento reducido. Coherente con el compromiso de accesibilidad del juego (sección 18).
- CI: comprobación de enlaces rotos, validación de esquemas, que cada página exista en los dos idiomas (o esté marcada como pendiente de traducción) y Lighthouse en cada PR.
- SEO: metadatos y Open Graph por página, `hreflang` es/en, sitemap y datos estructurados `VideoGame` cuando haya título y plataforma.

---

## 9. Flujo de trabajo y gobierno del contenido

- **Agentes de IA:** pueden programar componentes, maquetar, redactar borradores y traducir. Siguen un `AGENTS.md` propio del repositorio del sitio, con el mismo espíritu que el del motor: tareas acotadas, PR con vista previa y nunca hacer merge de su propio PR.
- **Revisión humana obligatoria** (CODEOWNERS) para: todo texto público nuevo, hoja de ruta, registro de cambios, contenido histórico y sensible, páginas legales y cualquier afirmación sobre fechas, precio o plataformas.
- **Contenido histórico:** los datos del documento maestro son material de trabajo; antes de publicarse en El mundo o Situaciones se verifican en la Biblia histórica, igual que para el juego.
- **Traducción:** se escribe en español y la traducción al inglés la revisa una persona antes de publicar. Un diario solo se publica cuando están las dos versiones.
- **Fuente única:** si el documento maestro cambia una fase o un dato de presentación, la tarea que lo cambia incluye actualizar `roadmap.yaml` o el texto del sitio.

---

## 10. Legal y privacidad

| Elemento | Contenido |
| --- | --- |
| Aviso legal | Titular, contacto, jurisdicción. |
| Privacidad | Qué datos se recogen (solo el correo del boletín), base legal, proveedor, conservación, cómo darse de baja y pedir el borrado. |
| Cookies | Si la analítica no usa cookies, se declara que no hay cookies de seguimiento y no hace falta banner. Si se añade algún servicio que las use, banner con rechazo tan fácil como aceptar. |
| Términos | Uso del sitio y de los materiales de prensa. |
| Uso de IA | Declaración de cómo se usa la IA en el desarrollo y en los recursos, alineada con las normas de Steam. |
| Licencias | Créditos de tipografías, mapas base (p. ej. Natural Earth) y bibliotecas. |

---

## 11. Riesgos

| Riesgo | Mitigación |
| --- | --- |
| Prometer de más con la hoja de ruta. | Fechas solo como periodos orientativos; estados honestos; cada cambio de plan se explica en un diario. |
| Cambio de nombre del juego. | Rutas neutras, título provisional marcado, dominio del estudio como principal. |
| Conflicto de marca o dominio. | Verificación y registro en W0, antes de cualquier publicación. |
| Mantener el sitio quita tiempo al juego (una persona, 20–30 h/semana). | Sitio estático sin servidor; contenido como datos; agentes para maquetación y borradores; ritmo de diarios realista (mensual). |
| Rechazo por desarrollo con IA. | Transparencia en Estudio y en los diarios; arte y textos finales con autoría y licencias claras. |
| Capturas que no representan el juego. | Ilustraciones conceptuales etiquetadas; capturas reales en cuanto existan. |
| Contenido histórico erróneo o sensible publicado sin revisar. | Revisión humana obligatoria y verificación en la Biblia histórica. |

---

## 12. Preguntas abiertas

| # | Pregunta | Resolver en |
| --- | --- | --- |
| A-W1 | Dominio definitivo y extensiones a reservar. | W0 |
| A-W2 | Proveedor del boletín y de la analítica. | W0 |
| A-W3 | ¿Se crea el Discord en W1 o se espera a tener diarios regulares (W2)? | W1 |
| A-W4 | ¿Wiki o enciclopedia propia en el sitio, o wiki comunitaria externa? | W4 |
| A-W5 | ¿Se publica la versión pública del documento de diseño completa o solo resúmenes? | W1 |
| A-W6 | Tipografías y paleta definitivas (dependen de la guía de identidad). | W0–W1 |
| A-W7 | ¿Las builds internas aparecen en el registro de cambios público o solo los hitos de fase? | W1 |

---

## 13. Backlog inicial (W0–W1)

Formato de tarea compatible con el flujo de agentes del documento maestro (sección 43).

| ID | Tarea | Rol | Depende de |
| --- | --- | --- | --- |
| W-01 | Verificar disponibilidad de dominio, cuentas en redes y marca; documentar el resultado. | Humano | — |
| W-02 | Crear el repositorio `website` con Astro, i18n es/en, `AGENTS.md`, CODEOWNERS y CI básico. | Agente | W-01 |
| W-03 | Definir esquemas de colecciones: diarios, cambios, roadmap, estado. | Agente | W-02 |
| W-04 | Sistema visual base: tokens de color claro/oscuro, tipografías, componentes `StatusBadge` y `PhaseTimeline`. | Agente + revisión humana | W-02 |
| W-05 | Redactar textos de El juego y Estudio a partir de las secciones 01 y 27 del documento maestro. | Agente (borrador) + humano | — |
| W-06 | Cargar `roadmap.yaml` con las fases 0–7 de la sección 28. | Agente | W-03 |
| W-07 | Página de registro de cambios con filtros por canal y RSS; primera entrada: v0.7 del documento de diseño. | Agente | W-03 |
| W-08 | Componente `EraJourney` de la portada, versión estática con ilustraciones provisionales y `prefers-reduced-motion`. | Agente + revisión humana | W-04 |
| W-09 | Integrar el boletín con doble confirmación y redactar la política de privacidad. | Agente + humano | A-W2 |
| W-10 | Traducción al inglés de todas las páginas de W1. | Agente + revisión humana | W-05 |
| W-11 | Prueba de comprensión de la portada con 5 personas (O-1) y ajustes. | Humano | W-08 |
| W-12 | Configurar alojamiento, dominio, analítica sin cookies y vistas previas por PR; publicar W1. | Agente + humano | W-01, W-11 |
