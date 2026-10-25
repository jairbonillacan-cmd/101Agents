# 101 Agents Games — Documento maestro del proyecto

> **Versión:** 0.7  
> **Fecha:** 24 de octubre de 2026  
> **Estudio:** 101 Agents Games  
> **Motor:** 101 Engine  
> **Videojuego:** título definitivo pendiente (nombre de trabajo: *Project Epoch*)  
> **Periodo de simulación:** 1300–2060+, con continuación abierta  
> **Estado:** documento de planificación; no representa un producto terminado.

**Historia en movimiento.** Simulador de gran estrategia histórica que integra guerra, economía, diplomacia, política, sociedad, cultura y tecnología en una sola partida continua de más de siete siglos.

---

## Presentación

Este documento reúne las decisiones y propuestas para el estudio **101 Agents Games**, su plataforma tecnológica **101 Engine** y un primer videojuego de gran estrategia histórica. Sirve como base de trabajo para la dirección creativa, la implementación con agentes de IA, la producción de contenido histórico y las revisiones futuras.

| Confirmado | Propuesto / pendiente |
| --- | --- |
| Estudio: **101 Agents Games** | Nombre comercial del juego: **pendiente**. “Project Epoch” es un nombre de trabajo. |
| La familia tecnológica usa el prefijo **101**; motor: **101 Engine**. | Nombres de módulos: 101 Sim, 101 History, 101 Map, 101 Forge, 101 Lab, 101 Script. |
| Gran estrategia continua desde **1300** hasta **2060**, ampliable. | Stack técnico detallado en la Parte V; validación en la Fase 0. |
| La historia real es una trayectoria plausible, no un guion. | Región de la vertical: propuesta Mediterráneo oriental y Balcanes (Parte VI). |

> **PRINCIPIO RECTOR**  
> **La historia tiene inercia, no un guion obligatorio.** El mundo sigue trayectorias reconocibles mientras se mantienen sus causas y produce alternativas coherentes cuando el jugador cambia esas causas.

### Cómo leer el documento

| Etiqueta | Significado |
| --- | --- |
| **Definido** | Acuerdo tomado. Cambiarlo requiere una entrada nueva en el registro de decisiones (Anexo B). |
| **Propuesto** | Recomendación que debe validarse con un prototipo, una medición o una revisión. |
| **Objetivo** | Meta medible, no resultado garantizado. |
| **Abierto** | Pregunta sin respuesta, con la fase en la que debe resolverse. |

Las fechas del plan son estimaciones, no compromisos. Los datos históricos de este documento son **material de trabajo**: deben verificarse en la Biblia histórica antes de convertirse en contenido del juego. Los términos técnicos se definen en el glosario (Anexo C).

### Tiers de alcance

Todas las features llevan uno de estos niveles:

| Tier | Significado |
| --- | --- |
| **MVP** | Necesario para que el núcleo funcione (Fases 1–3). |
| **Slice** | Necesario para la vertical jugable 1300–1600 (Fases 4–5). |
| **1.0** | Necesario para el lanzamiento comercial. |
| **Post** | Expansiones, actualizaciones o ideas para después del lanzamiento. |

## Cambios en la versión 0.7

La v0.7 pasa de **describir** los sistemas a **especificarlos**: cada sistema tiene ahora estructuras de datos, fórmulas con parámetros numéricos, tablas de valores iniciales, un ejemplo resuelto con cifras comprobadas y una lista de pruebas con nombre. El objetivo es que un agente de IA pueda redactar `docs/specs/<sistema>.md` y empezar a implementar sin inventar números.

- **Especificaciones detalladas (secciones 04, 06–18):** mapa y grafo de tiempos de viaje (04); asimilación, conversión, políticas religiosas y emergencia de reformas (06); algoritmo de 101 History, plausibilidad e índice de divergencia (07); ciclo de vida de identidades y proclamación de entidades formables (08); cohortes, fusión, edad, cestas, migración, refugiados, alfabetización y movilización (09); unidad de cuenta, precios base, calendario agrícola, edificios, existencias, transporte, inversión, fiscalidad, deuda y moneda (10); primitivas, poder de los grupos, reformas por etapas, legitimidad, control, corrupción y rebeliones (11); relaciones, cláusulas, vasallaje, amenaza, casus belli, puntuación bélica e inteligencia (12); unidades, terreno, movimiento, suministro, batalla, asedios, guerra naval, agotamiento y mercenarios (13); capacidad de investigación, difusión, adopción y límite de adelanto (14); clima, enfermedades, peste negra, medidas sanitarias y exploración (15); personajes, sucesión, regencias e institucionalización (16); canal de decisión y utilidades de la IA (17); panel “¿por qué?”, tooltips, composición, atajos y formato de cifras (18).
- **Ejemplos resueltos con números:** un mes en Bitinia (09), el presupuesto bizantino de 1300 y una crisis del grano en Tesalónica (10), gravar las tierras monásticas (11), el tratado veneciano-bizantino (12), una batalla de frontera y un bloqueo (13), la imprenta en Venecia (14), la sucesión húngara de 1301 (16), la decisión otomana ante Bursa (17).
- **Motor:** calendario de sistemas dentro del tick (21), especificación del hash de estado y escenarios dorados iniciales (23), mods con parches y orden de carga e informe nocturno de 101 Lab (20/26).
- **Nuevos anexos AI–AW:** tabla de parámetros globales (AI), estado inicial cuantitativo de la vertical (AJ), mercados de la vertical (AK), lenguaje 101 Script (AL), traza de un día de simulación (AM), partida comentada de Bizancio 1300–1330 (AN), catálogo de alertas (AO), matriz de interacción entre sistemas (AP), protocolo de pruebas con jugadores (AQ), formato de guardado (AR), esfuerzo y presupuesto (AS), indicadores de riesgo (AT), trazabilidad features → especificación → pruebas (AU), escenarios de aprendizaje (AV) y objetivos de balance por entidad (AW).
- **Parte VII:** tabla de cómo cambian los parámetros clave entre 1300 y 2025 según la tecnología.
- **Corregido:** los nombres de crates de la sección 21 (`sim-core`, `map-data`…) se sustituyen por los definitivos de prefijo `e101-` de la Parte VIII; la estructura de repositorio de la sección 27 remite a la sección 40; las reglas globales de agentes están en `AGENTS.md`, no en un `CONTEXT.md` raíz; los lints de determinismo se refieren a los crates del núcleo.
- **Decisiones:** nuevas decisiones propuestas D-016 a D-022 y propuesta de resolución de A-11 (Anexo B); glosario ampliado (Anexo C); índice de especificaciones actualizado (Anexo AG).

## Cambios en la versión 0.6

- **Repositorio y agentes de IA (Parte VIII, secciones 39–48):** nombre del repositorio (`101-agents-games/101-engine`), prefijo de crates `e101-`, estructura completa, grafo de dependencias, `AGENTS.md` completo, roles y propiedad del código, ciclo de vida de una tarea, ramas, commits, PR, etiquetas, comandos `cargo xtask`, reglas de código y datos, coordinación en paralelo, prompts y métricas. Todo se entrega también como kit de archivos listo para el primer commit.
- **Diseño por épocas (Parte VII, secciones 33–38):** cómo se juega cada periodo de 1300 a más allá de 2060, qué sistemas pesan más, crisis características, tecnologías, fuerzas armadas, condiciones de transición y contenido mínimo.
- **Más features:** más de 300 en total, con nuevas categorías por época, herramientas, laboratorio, depuración, accesibilidad y localización.
- **Más países:** fichas completas de las 18 entidades jugables de la vertical (Anexo I), más de 60 entidades de la primera expansión (Anexo J) y unas 45 de las expansiones de Asia, África y las Américas (Anexo S).
- **Más culturas:** 39 fichas culturales adicionales (Anexo N).
- **Catálogos:** bienes y edificios por época (K), leyes (L), unidades de tierra, mar y aire (M), bocetos de pantallas (O), backlog de las Fases 0–2 en formato de tareas para agentes (P), unas 60 situaciones históricas adicionales (Q), unas 130 tecnologías por época (R), plan de pruebas por sistema (T), glosario histórico (U) y bibliografía de trabajo (V).
- **Para los agentes, además:** un ejemplo completo de una tarea resuelta de principio a fin, con código y pruebas (W), un borrador de la interfaz del núcleo en Rust (X), el plan de producción de contenido dimensionado por la capacidad de revisión (Y) y el catálogo de escenarios de prueba con nombre estable (Z), quince eventos de ejemplo escritos con la guía de estilo (AA), rasgos de personajes y personalidades de la IA (AB) preguntas frecuentes para agentes (AC), fichas de 24 religiones y confesiones (AD), potencias de referencia por época (AE) el plan día a día de las primeras cuatro semanas del repositorio (AF), el índice de especificaciones por sistema (AG) y la lista de comprobación para cerrar la vertical (AH).
- **Corregido:** en la fórmula de precios de la sección 10, el límite de ±10 % se aplica ahora al cambio semanal completo, como indican sus parámetros.
- La conclusión pasa a la sección 49.
- Versiones anteriores: la v0.5 especificó los modelos con fórmulas y añadió los anexos E–H; la v0.4 sustituyó los nombres de juegos por patrones de diseño; la v0.3 añadió el mundo en 1300 y la vertical; la v0.2, determinismo y registro causal.

## Índice

**Parte I · Visión y producto**
- [01. Visión de producto](#01-visión-de-producto)
- [02. Patrones de diseño del género](#02-patrones-de-diseño-del-género)
- [03. Catálogo de features](#03-catálogo-de-features)

**Parte II · Mundo y contenido histórico**
- [04. Mundo, mapa y tiempo](#04-mundo-mapa-y-tiempo)
- [05. El mundo en 1300](#05-el-mundo-en-1300)
- [06. Culturas, idiomas y religiones](#06-culturas-idiomas-y-religiones)
- [07. Historia guiada y divergencia causal](#07-historia-guiada-y-divergencia-causal)
- [08. Estados dinámicos y entidades formables](#08-estados-dinámicos-y-entidades-formables)

**Parte III · Sistemas de juego**
- [09. Población y sociedad](#09-población-y-sociedad)
- [10. Economía, producción y finanzas](#10-economía-producción-y-finanzas)
- [11. Gobierno, instituciones y política](#11-gobierno-instituciones-y-política)
- [12. Diplomacia, alianzas e inteligencia](#12-diplomacia-alianzas-e-inteligencia)
- [13. Guerra, logística y mando militar](#13-guerra-logística-y-mando-militar)
- [14. Ciencia y tecnología](#14-ciencia-y-tecnología)
- [15. Clima, epidemias y exploración](#15-clima-epidemias-y-exploración)
- [16. Personajes y dinastías](#16-personajes-y-dinastías)
- [17. IA de países](#17-ia-de-países)

**Parte IV · Experiencia**
- [18. Interfaz, mapa y accesibilidad](#18-interfaz-mapa-y-accesibilidad)
- [19. Dirección de arte y audio](#19-dirección-de-arte-y-audio)
- [20. Modding y comunidad](#20-modding-y-comunidad)

**Parte V · Tecnología**
- [21. Arquitectura de 101 Engine](#21-arquitectura-de-101-engine)
- [22. Stack tecnológico recomendado](#22-stack-tecnológico-recomendado)
- [23. Determinismo y reproducibilidad](#23-determinismo-y-reproducibilidad)
- [24. Datos históricos y pipeline](#24-datos-históricos-y-pipeline)
- [25. Rendimiento y pruebas](#25-rendimiento-y-pruebas)
- [26. Herramientas: 101 Forge y 101 Lab](#26-herramientas-101-forge-y-101-lab)

**Parte VI · Producción y negocio**
- [27. Desarrollo mediante agentes de IA](#27-desarrollo-mediante-agentes-de-ia)
- [28. Plan de desarrollo y calendario](#28-plan-de-desarrollo-y-calendario)
- [29. Vertical slice: Mediterráneo oriental 1300–1600](#29-vertical-slice-mediterráneo-oriental-13001600)
- [30. Publicación, negocio y marca](#30-publicación-negocio-y-marca)
- [31. Riesgos](#31-riesgos)
- [32. Backlog inicial](#32-backlog-inicial)

**Parte VII · Diseño por épocas**
- [33. Baja Edad Media (1300–1500)](#33-baja-edad-media-13001500)
- [34. Edad Moderna temprana (1500–1750)](#34-edad-moderna-temprana-15001750)
- [35. Era de las revoluciones e industrialización (1750–1914)](#35-era-de-las-revoluciones-e-industrialización-17501914)
- [36. Era de las guerras mundiales y los bloques (1914–1991)](#36-era-de-las-guerras-mundiales-y-los-bloques-19141991)
- [37. Era digital y globalización (1991–2060)](#37-era-digital-y-globalización-19912060)
- [38. Más allá de 2060](#38-más-allá-de-2060)

**Parte VIII · Repositorio y agentes de IA**
- [39. Nombre y organización del repositorio](#39-nombre-y-organización-del-repositorio)
- [40. Estructura del repositorio](#40-estructura-del-repositorio)
- [41. Archivos de instrucciones para agentes](#41-archivos-de-instrucciones-para-agentes)
- [42. Roles de agentes y propiedad del código](#42-roles-de-agentes-y-propiedad-del-código)
- [43. Ciclo de vida de una tarea](#43-ciclo-de-vida-de-una-tarea)
- [44. Ramas, commits, PR y revisión](#44-ramas-commits-pr-y-revisión)
- [45. Comandos y automatización](#45-comandos-y-automatización)
- [46. Reglas de código y de datos para agentes](#46-reglas-de-código-y-de-datos-para-agentes)
- [47. Coordinación de varios agentes en paralelo](#47-coordinación-de-varios-agentes-en-paralelo)
- [48. Plantillas, prompts y métricas](#48-plantillas-prompts-y-métricas)

**Cierre**
- [49. Conclusión y definición de éxito](#49-conclusión-y-definición-de-éxito)

**Anexos**
- [Anexo A · Inventario de entregables](#anexo-a--inventario-de-entregables)
- [Anexo B · Registro de decisiones](#anexo-b--registro-de-decisiones)
- [Anexo C · Glosario](#anexo-c--glosario)
- [Anexo D · Referencias, fuentes de datos y comprobaciones](#anexo-d--referencias-fuentes-de-datos-y-comprobaciones)
- [Anexo E · Formatos de datos (ejemplos)](#anexo-e--formatos-de-datos-ejemplos)
- [Anexo F · Objetivos de calibración de 101 Lab](#anexo-f--objetivos-de-calibración-de-101-lab)
- [Anexo G · Guía de estilo del contenido](#anexo-g--guía-de-estilo-del-contenido)
- [Anexo H · Hoja de ruta posterior al lanzamiento](#anexo-h--hoja-de-ruta-posterior-al-lanzamiento)
- [Anexo I · Fichas de las entidades jugables de la vertical](#anexo-i--fichas-de-las-entidades-jugables-de-la-vertical)
- [Anexo J · Entidades de la primera expansión](#anexo-j--entidades-de-la-primera-expansión)
- [Anexo K · Catálogo de bienes y edificios por época](#anexo-k--catálogo-de-bienes-y-edificios-por-época)
- [Anexo L · Catálogo de leyes](#anexo-l--catálogo-de-leyes)
- [Anexo M · Catálogo de unidades por época](#anexo-m--catálogo-de-unidades-por-época)
- [Anexo N · Fichas culturales de la primera expansión](#anexo-n--fichas-culturales-de-la-primera-expansión)
- [Anexo O · Especificación de pantallas (bocetos)](#anexo-o--especificación-de-pantallas-bocetos)
- [Anexo P · Backlog de las Fases 0–2 en formato de tareas](#anexo-p--backlog-de-las-fases-02-en-formato-de-tareas)
- [Anexo Q · Catálogo ampliado de situaciones históricas](#anexo-q--catálogo-ampliado-de-situaciones-históricas)
- [Anexo R · Catálogo de tecnologías por época](#anexo-r--catálogo-de-tecnologías-por-época)
- [Anexo S · Entidades de las expansiones mundiales](#anexo-s--entidades-de-las-expansiones-mundiales)
- [Anexo T · Plan de pruebas por sistema](#anexo-t--plan-de-pruebas-por-sistema)
- [Anexo U · Glosario histórico](#anexo-u--glosario-histórico)
- [Anexo V · Bibliografía de trabajo](#anexo-v--bibliografía-de-trabajo)
- [Anexo W · Ejemplo completo de una tarea resuelta por un agente](#anexo-w--ejemplo-completo-de-una-tarea-resuelta-por-un-agente)
- [Anexo X · Referencia de la interfaz del núcleo (borrador)](#anexo-x--referencia-de-la-interfaz-del-núcleo-borrador)
- [Anexo Y · Plan de producción de contenido](#anexo-y--plan-de-producción-de-contenido)
- [Anexo Z · Catálogo de escenarios de prueba y de laboratorio](#anexo-z--catálogo-de-escenarios-de-prueba-y-de-laboratorio)
- [Anexo AA · Eventos de ejemplo de la vertical](#anexo-aa--eventos-de-ejemplo-de-la-vertical)
- [Anexo AB · Rasgos de personajes y personalidades de la IA](#anexo-ab--rasgos-de-personajes-y-personalidades-de-la-ia)
- [Anexo AC · Preguntas frecuentes para agentes](#anexo-ac--preguntas-frecuentes-para-agentes)
- [Anexo AD · Fichas de religiones y confesiones](#anexo-ad--fichas-de-religiones-y-confesiones)
- [Anexo AE · Potencias de referencia por época](#anexo-ae--potencias-de-referencia-por-época)
- [Anexo AF · Las primeras cuatro semanas del repositorio](#anexo-af--las-primeras-cuatro-semanas-del-repositorio)
- [Anexo AG · Índice de especificaciones por sistema](#anexo-ag--índice-de-especificaciones-por-sistema)
- [Anexo AH · Lista de comprobación para cerrar la vertical](#anexo-ah--lista-de-comprobación-para-cerrar-la-vertical)
- [Anexo AI · Tabla de parámetros globales](#anexo-ai--tabla-de-parámetros-globales)
- [Anexo AJ · Estado inicial cuantitativo de la vertical (1300)](#anexo-aj--estado-inicial-cuantitativo-de-la-vertical-1300)
- [Anexo AK · Mercados de la vertical](#anexo-ak--mercados-de-la-vertical)
- [Anexo AL · Especificación de 101 Script: condiciones y efectos (borrador)](#anexo-al--especificación-de-101-script-condiciones-y-efectos-borrador)
- [Anexo AM · Traza de un día de simulación](#anexo-am--traza-de-un-día-de-simulación)
- [Anexo AN · Partida de ejemplo comentada: Bizancio, 1300–1330](#anexo-an--partida-de-ejemplo-comentada-bizancio-13001330)
- [Anexo AO · Catálogo de alertas y notificaciones](#anexo-ao--catálogo-de-alertas-y-notificaciones)
- [Anexo AP · Matriz de interacción entre sistemas](#anexo-ap--matriz-de-interacción-entre-sistemas)
- [Anexo AQ · Protocolo de pruebas con jugadores](#anexo-aq--protocolo-de-pruebas-con-jugadores)
- [Anexo AR · Formato de guardado (borrador)](#anexo-ar--formato-de-guardado-borrador)
- [Anexo AS · Esfuerzo y presupuesto estimados hasta la vertical](#anexo-as--esfuerzo-y-presupuesto-estimados-hasta-la-vertical)
- [Anexo AT · Riesgos con indicadores de alerta temprana](#anexo-at--riesgos-con-indicadores-de-alerta-temprana)
- [Anexo AU · Trazabilidad: features → especificación → pruebas](#anexo-au--trazabilidad-features--especificación--pruebas)
- [Anexo AV · Escenarios de aprendizaje](#anexo-av--escenarios-de-aprendizaje)
- [Anexo AW · Objetivos de balance por entidad de la vertical](#anexo-aw--objetivos-de-balance-por-entidad-de-la-vertical)

---

# Parte I · Visión y producto

## 01. Visión de producto

### Pitch

> Dirige a un pueblo desde 1300 hasta más allá de 2060 en una sola partida. Cada guerra cuesta grano, hombres y deuda; cada reforma cambia quién manda; cada invento necesita sus precursores. La historia real sigue ocurriendo mientras sus causas existan. Cuando cambias las causas, el mundo escribe otra historia, y siempre puedes preguntar por qué.

### Fantasía del jugador

> *“Guío a mi pueblo a lo largo de siete siglos y entiendo exactamente por qué el mundo terminó siendo como es.”*

La recompensa central no es pintar el mapa, sino **ver cómo las propias decisiones reescriben la historia de forma creíble** y poder rastrear esas consecuencias hasta su origen.

### Público objetivo (propuesto)

| Segmento | Qué busca | Implicación de diseño |
| --- | --- | --- |
| Primario: jugadores veteranos de gran estrategia | Profundidad sistémica, partidas largas, alternativas históricas. | La complejidad es aceptable si es legible y tiene consecuencias. |
| Secundario: aficionados a la historia | Plausibilidad, contexto, “¿qué habría pasado si…?”. | Crónicas, líneas de tiempo comparadas, enciclopedia integrada. |
| Terciario: modders y comunidad técnica | Herramientas, datos documentados, escenarios propios. | Separación motor/contenido; formatos abiertos desde el inicio. |
| Cuarto: docentes y divulgadores | Explorar causas históricas en clase o en vídeo. | Modo observador, repeticiones, exportación de gráficas (Post). |

### Diferenciadores buscados

1. **Una sola partida continua** de 1300 a 2060+, sin cambio de juego ni conversión de partidas.
2. **Causalidad explicable:** toda variable importante puede responder “¿por qué?”.
3. **Historia condicional:** los grandes acontecimientos ocurren porque se dan sus causas, no por fecha.
4. **El Estado como proceso:** los países nacen, se fragmentan, se fusionan y se restauran con identidades persistentes.
5. **Simulación verificable:** 101 Lab mide cómo se comporta el mundo en cientos de partidas, y esos datos guían el diseño.

### Pilares del diseño

- **Continuidad:** no hay transiciones artificiales entre épocas; las instituciones y fuerzas cambian mediante procesos simulados.
- **Plausibilidad:** las trayectorias históricas son referentes sujetos a restricciones tecnológicas, políticas y geográficas.
- **Agencia:** intervenir en alianzas, guerras, comercio, ciencia y política tiene efectos explicables.
- **Profundidad sistémica:** cada sistema afecta a otros; una guerra consume recursos y transforma sociedades.
- **Legibilidad:** la interfaz explica causas, restricciones y consecuencias; el jugador puede delegar tareas.
- **Escala:** mundo grande, avance rápido del tiempo, simulación sin renderizar y arquitectura medible.

### Bucles de juego

| Escala | Ritmo | Qué hace el jugador |
| --- | --- | --- |
| Inmediata | Segundos a minutos | Lee una alerta → consulta su causa → decide (ley, presupuesto, orden, tratado) → reanuda el tiempo. |
| Operativa | Meses a años de juego | Gestiona una guerra, una crisis fiscal, una reforma o una negociación; ajusta producción y diplomacia. |
| Estratégica | Décadas | Fija objetivos nacionales, transforma instituciones, cambia de aliados y rivales. |
| Histórica | Siglos | Su Estado se transforma, se fragmenta o se reinventa; compara su crónica con la historia real. |

**Cierre del bucle:** cada decisión importante debe producir al menos una consecuencia observable en el plazo de su escala, y el registro causal (sección 21) debe poder mostrar la conexión.

### Un año de partida, como ejemplo

*Imperio bizantino, primavera de 1303.* El tesoro no alcanza para pagar a la flota, y una alerta avisa de que los beyliks turcos han tomado dos fortalezas en Bitinia. El jugador abre la causa: la guarnición llevaba cinco meses sin cobrar y las aldeas cercanas habían huido a la costa. Puede devaluar el *hiperpirón*, que es rápido pero eleva los precios y enfada a los mercaderes; subir impuestos a los monasterios, lo que provoca un conflicto con la Iglesia; o contratar a la Compañía Catalana, mercenarios veteranos que llegan pidiendo un pago adelantado. Elige a los catalanes. Dos años después vencen en Anatolia, pero el pago se retrasa y la Compañía se vuelve contra el imperio. El jugador puede rastrear cada paso de esa cadena en el registro causal.

### Objetivos de partida (abierto)

El calendario no impone un final. Propuesta para la Fase 5:

- **Ambiciones nacionales** generadas a partir de la identidad y la situación (“restaurar el Imperio”, “dominar el comercio del mar Negro”). Son opcionales y cambian con el tiempo.
- **Hitos de época** que reconocen logros sin otorgar bonificaciones desequilibrantes.
- **Crónica de la partida:** un libro generado con los sucesos principales, comparado con la historia real y exportable.
- **Puntuación opcional** para quien quiera compararse con otros jugadores.

### Fechas de inicio (abierto)

| Opción | Ventaja | Coste |
| --- | --- | --- |
| Solo 1300 | Coherencia total; un único estado histórico que mantener. | Partidas muy largas para quien quiere jugar el siglo XX. |
| Inicios históricos adicionales (p. ej. 1444, 1700, 1836, 1914, 1936) | Acceso directo a cada época. | Cada fecha exige un estado completo y documentado del mundo: el contenido se multiplica. |
| Inicios generados por simulación | Se simula desde 1300 hasta la fecha elegida en modo histórico estricto. | El resultado puede no coincidir con la historia; requiere una simulación muy calibrada. |

Recomendación: lanzar con 1300 y añadir inicios históricos como contenido posterior, empezando por los de mayor demanda.

> **NO ES UN SANDBOX SIN REGLAS**  
> No es posible investigar tecnología de 2060 en 1450 acumulando puntos. Toda capacidad requiere precursores científicos, materiales, instituciones, infraestructura, conocimiento disponible y una madurez temporal razonable.

## 02. Patrones de diseño del género

La gran estrategia histórica ha desarrollado durante más de dos décadas un repertorio de mecánicas que los jugadores ya conocen y valoran. Este proyecto **no copia títulos concretos**: identifica patrones de diseño, entiende por qué funcionan y los reinterpreta para una partida continua de 760 años con causalidad explicable. No se reproducirá código, datos, textos, interfaces ni recursos de ningún juego comercial.

Cada patrón se describe con el mismo esquema:

- **Qué es:** la mecánica tal como suele aparecer en el género.
- **Por qué funciona:** qué experiencia produce en el jugador.
- **Problemas habituales:** dónde suele fallar.
- **Cómo lo adaptamos:** la versión de 101, con sus diferencias.
- **Features:** IDs del catálogo (sección 03).

### Sociedad y economía

#### P-01 · Población por grupos sociales

- **Qué es:** en lugar de un número de habitantes por provincia, la población se divide en grupos con ocupación, cultura, religión, ingresos y opinión política. Los grupos trabajan, consumen, migran y apoyan o rechazan al gobierno.
- **Por qué funciona:** convierte la economía y la política en algo que les pasa a personas concretas. El jugador ve quién gana y quién pierde con cada decisión.
- **Problemas habituales:** el número de grupos crece sin control y degrada el rendimiento; la información se vuelve ilegible cuando hay miles de grupos.
- **Cómo lo adaptamos:** cohortes con fusión automática por debajo de un umbral (30–70 por provincia en la escala S), almacenamiento por columnas y paneles que agregan por estrato, cultura o religión. Las cohortes existen desde 1300; sus categorías cambian con la época.
- **Features:** F-POP-01, F-POP-02, F-POP-03, F-POP-08.

#### P-02 · Edificios con modos de producción

- **Qué es:** la producción ocurre en edificios que transforman insumos en productos empleando a ciertos grupos. Cada edificio puede usar distintos métodos que cambian la proporción de insumos, trabajo y producto.
- **Por qué funciona:** la tecnología se nota en la economía real: un nuevo método despide a unos trabajadores, contrata a otros y cambia la demanda de materias primas.
- **Problemas habituales:** optimización en hoja de cálculo; bucles de retroalimentación que inflan o hunden precios; microgestión de cada edificio.
- **Cómo lo adaptamos:** modos de producción ligados al grafo tecnológico y a la disponibilidad real de insumos; invariantes contables; inversión privada simulada para que el jugador no tenga que construirlo todo; asesor económico delegable.
- **Features:** F-ECO-01, F-ECO-04, F-ECO-09.

#### P-03 · Mercados con precios por oferta y demanda

- **Qué es:** cada mercado fija precios según lo que se produce y se consume; el comercio mueve bienes entre mercados.
- **Por qué funciona:** las escaseces, las guerras y los bloqueos tienen efectos visibles en los precios; el comercio es una herramienta estratégica.
- **Problemas habituales:** precios que oscilan sin control; el jugador no entiende por qué cambia un precio.
- **Cómo lo adaptamos:** ajuste semanal amortiguado, rutas con capacidad y riesgo, y el panel “¿por qué?” que muestra los tres mayores contribuyentes a cada cambio. Mercados externos simplificados en los bordes del mapa.
- **Features:** F-ECO-02, F-ECO-03, F-ECO-12.

#### P-04 · Comercio por redes de nodos

- **Qué es:** el comercio fluye por una red dirigida de nodos hacia ciertos centros; las potencias compiten por controlar el flujo y llevarlo a sus puertos.
- **Por qué funciona:** da sentido geográfico a la expansión comercial y crea conflictos por rutas.
- **Problemas habituales:** la red suele ser fija y abstracta; el valor comercial aparece de la nada.
- **Cómo lo adaptamos:** la red sale de la geografía y de la infraestructura (puertos, caminos, ríos, estrechos), cambia cuando cambian esas condiciones y transporta **bienes reales** con conservación exacta. El control de una ruta se traduce en peajes, privilegios y seguridad.
- **Features:** F-ECO-03, F-TRD-01 a F-TRD-06.

### Política e instituciones

#### P-05 · Grupos de interés que respaldan o bloquean leyes

- **Qué es:** facciones de la sociedad (nobleza, clero, mercaderes, militares, obreros) tienen poder y preferencias sobre las leyes. Cambiar una ley exige apoyo suficiente.
- **Por qué funciona:** la política se convierte en negociación: no basta con querer una reforma, hay que construir la coalición.
- **Problemas habituales:** el poder de los grupos parece arbitrario; las reformas se convierten en una espera pasiva.
- **Cómo lo adaptamos:** el poder de cada grupo se deriva de su riqueza, número, organización y control de instituciones; el jugador puede actuar sobre esas fuentes (crear cargos, conceder tierras, reprimir, comprar apoyos), y el proceso de reforma tiene etapas con riesgo de reacción.
- **Features:** F-GOV-02, F-GOV-03, F-GOV-06.

#### P-06 · Estamentos con privilegios negociables

- **Qué es:** los órdenes de la sociedad tradicional tienen privilegios (exenciones, cargos, autonomía) que el Estado puede conceder o retirar.
- **Por qué funciona:** captura la tensión central del Estado premoderno: el rey necesita a la nobleza y al clero, pero cada concesión limita su poder.
- **Problemas habituales:** privilegios como simples botones de bonificación; desaparecen bruscamente en una fecha.
- **Cómo lo adaptamos:** los privilegios son leyes y contratos con contrapartidas concretas (soldados, dinero, legitimidad); los estamentos se transforman gradualmente en grupos de interés modernos cuando cambian la economía y las instituciones.
- **Features:** F-GOV-02, F-GOV-11, F-GOV-12.

#### P-07 · Control territorial que decae con la distancia

- **Qué es:** el control efectivo de una provincia depende de su distancia a la capital o a un centro administrativo, y afecta a impuestos y reclutamiento.
- **Por qué funciona:** frena la expansión ilimitada y premia la infraestructura y la administración.
- **Problemas habituales:** la distancia es en línea recta e ignora mares, montañas y caminos.
- **Cómo lo adaptamos:** la “distancia” es el **tiempo de viaje real** por la red de rutas de la época, de modo que un camino nuevo, un puerto o el ferrocarril amplían el alcance del Estado. El control se muestra como porcentaje y es una de las primeras cosas que el jugador aprende a leer.
- **Features:** F-GOV-04, F-GOV-05.

#### P-08 · Innovaciones institucionales que se difunden

- **Qué es:** grandes cambios (renacimiento, imprenta, banca, ilustración) nacen en un lugar y se extienden a provincias vecinas; adoptarlos permite progresar.
- **Por qué funciona:** la historia se siente geográfica: las ideas viajan por rutas y ciudades.
- **Problemas habituales:** el origen y la fecha suelen estar predeterminados.
- **Cómo lo adaptamos:** las innovaciones nacen donde se cumplen sus condiciones (ciudades, alfabetización, comercio, instituciones de saber) y se difunden por comercio, migración y contacto. Pueden nacer en lugares distintos en cada partida.
- **Features:** F-SCI-02, F-SCI-04, F-CUL-05.

#### P-09 · Situaciones históricas de larga duración

- **Qué es:** procesos que duran años o décadas (una guerra civil, una crisis sucesoria, una reforma religiosa) con etapas, indicadores y salidas distintas.
- **Por qué funciona:** da forma narrativa a los grandes procesos sin reducirlos a un evento.
- **Problemas habituales:** se disparan por fecha y país aunque las causas no existan.
- **Cómo lo adaptamos:** situaciones con ventana, roles, precondiciones, caducidad y variantes (sección 07), evaluadas por 101 History.
- **Features:** F-NAR-01 a F-NAR-04.

#### P-10 · Eventos con opciones y cadenas narrativas

- **Qué es:** ventanas con texto, ilustración y dos o más opciones que producen efectos y pueden encadenar otros eventos.
- **Por qué funciona:** aporta sabor histórico, decisiones memorables y contexto.
- **Problemas habituales:** eventos repetitivos, opciones con una respuesta obvia, efectos ocultos.
- **Cómo lo adaptamos:** cada evento muestra las condiciones que lo dispararon y los efectos completos de cada opción en el registro causal; hay límites de repetición y opciones con costes reales en ambos lados.
- **Features:** F-NAR-05 a F-NAR-08.

#### P-11 · Árboles de objetivos nacionales

- **Qué es:** cada país tiene un árbol de objetivos que se completan con el tiempo y otorgan efectos, y que guían el comportamiento histórico de la IA.
- **Por qué funciona:** da dirección al jugador y personalidad a cada país.
- **Problemas habituales:** árboles fijos por país que fuerzan la historia y caducan cuando el mundo cambia.
- **Cómo lo adaptamos:** **ambiciones dinámicas** generadas por la identidad, la geografía, los rivales y la situación del momento. Un país puede tener “dominar los estrechos” en 1350 y “sobrevivir a la coalición” en 1420. Las ambiciones no otorgan bonificaciones mágicas: indican objetivos y miden el progreso.
- **Features:** F-NAR-09, F-NAR-10.

### Personajes y dinastías

#### P-12 · Personajes con rasgos, dinastías y sucesión

- **Qué es:** gobernantes y herederos con edad, salud, capacidades y personalidad; la sucesión puede provocar crisis.
- **Por qué funciona:** humaniza el Estado y crea giros inesperados (un rey niño, un heredero incapaz).
- **Problemas habituales:** el peso de un solo personaje es enorme incluso en épocas institucionalizadas.
- **Cómo lo adaptamos:** el peso de los personajes escala con la institucionalización del Estado (sección 16). En 1300 un rey lo es casi todo; en 1950 un primer ministro es reemplazable.
- **Features:** F-CHR-01, F-CHR-02.

#### P-13 · Intriga y facciones de corte

- **Qué es:** los personajes forman facciones, conspiran, se alían o se traicionan para cambiar la sucesión, obtener cargos o derrocar al gobernante.
- **Por qué funciona:** genera drama político interno sin necesidad de guerra.
- **Problemas habituales:** exige simular a muchas personas; puede desplazar al resto del juego.
- **Cómo lo adaptamos:** solo los personajes con poder decisivo; las facciones se vinculan a grupos de interés y regiones, no solo a relaciones personales.
- **Features:** F-CHR-05, F-CHR-06.

#### P-14 · Vasallaje con contratos

- **Qué es:** los vasallos tienen obligaciones (tributo, tropas) y derechos (autonomía, protección) que pueden renegociarse.
- **Por qué funciona:** representa bien el Estado compuesto premoderno y crea tensiones internas.
- **Problemas habituales:** vasallos que son simplemente países pequeños obedientes.
- **Cómo lo adaptamos:** contratos con cláusulas explícitas, control efectivo separado de la soberanía nominal y vasallos con IA propia que calcula si le conviene seguir.
- **Features:** F-DIP-03, F-DIP-10.

### Diplomacia y guerra

#### P-15 · Expansión agresiva que provoca coaliciones

- **Qué es:** conquistar genera alarma en los vecinos, que pueden formar coaliciones defensivas.
- **Por qué funciona:** frena la bola de nieve y hace que la expansión requiera diplomacia.
- **Problemas habituales:** la alarma se calcula con fórmulas opacas; las coaliciones aparecen o desaparecen de forma artificial.
- **Cómo lo adaptamos:** la amenaza percibida depende del poder relativo, la proximidad, el historial de agresión y la información disponible; cada país explica por qué se une o no a una coalición.
- **Features:** F-DIP-05, F-DIP-01.

#### P-16 · Puntuación de guerra y paz por cláusulas

- **Qué es:** el progreso de la guerra se mide con una puntuación que limita lo que se puede exigir en la paz.
- **Por qué funciona:** da una salida clara a las guerras y evita conquistas totales instantáneas.
- **Problemas habituales:** la puntuación se convierte en un juego en sí mismo; ocupar provincias sin valor sube la cuenta.
- **Cómo lo adaptamos:** la puntuación pesa los objetivos de guerra declarados, el control de lugares clave, el estado de los ejércitos y el agotamiento del rival. La paz se compone de cláusulas, y las condiciones demasiado duras generan agravio duradero.
- **Features:** F-WAR-07, F-WAR-12.

#### P-17 · Agotamiento bélico

- **Qué es:** cuanto más dura una guerra, más descontento y menos capacidad de seguir.
- **Por qué funciona:** obliga a buscar la paz.
- **Problemas habituales:** es un número abstracto desconectado de la economía.
- **Cómo lo adaptamos:** el agotamiento **emerge** de bajas, impuestos extraordinarios, precios, saqueos y propaganda. No es un contador independiente.
- **Features:** F-WAR-13.

#### P-18 · Frentes y planes operacionales

- **Qué es:** el jugador dibuja frentes y flechas de ofensiva; la IA mueve las unidades para ejecutarlos.
- **Por qué funciona:** permite dirigir guerras enormes sin mover cada unidad.
- **Problemas habituales:** comportamientos absurdos de la ejecución automática; poco control cuando falla.
- **Cómo lo adaptamos:** disponible cuando la época lo justifica (ejércitos de masas y comunicaciones rápidas); antes, el jugador maneja ejércitos con órdenes de campaña. La ejecución informa de por qué no avanza.
- **Features:** F-WAR-09, F-WAR-14.

#### P-19 · Plantillas de formación

- **Qué es:** el jugador diseña la composición de sus divisiones o ejércitos (proporción de infantería, caballería, artillería, apoyo).
- **Por qué funciona:** convierte la doctrina en una decisión del jugador.
- **Problemas habituales:** composiciones óptimas que todos copian.
- **Cómo lo adaptamos:** las plantillas existen desde que hay ejércitos permanentes; los costes reales (equipo, caballos, suministro, mando) y el terreno impiden una composición universalmente óptima.
- **Features:** F-WAR-15.

#### P-20 · Producción militar en líneas con eficiencia

- **Qué es:** la industria produce equipo en líneas que ganan eficiencia con el tiempo; cambiar de modelo la reduce.
- **Por qué funciona:** captura la tensión entre modernizar y producir en masa.
- **Problemas habituales:** la producción militar está separada del resto de la economía.
- **Cómo lo adaptamos:** las líneas son edificios con modo de producción militar que consumen bienes del mercado; un esfuerzo bélico mueve trabajadores y materias primas desde la economía civil.
- **Features:** F-WAR-16, F-ECO-01.

#### P-21 · Suministro por centros y capacidad de ruta

- **Qué es:** los ejércitos reciben suministros desde centros logísticos por rutas con capacidad limitada.
- **Por qué funciona:** la logística decide las guerras y el mapa importa.
- **Problemas habituales:** suministro abstracto que aparece en el frente.
- **Cómo lo adaptamos:** el suministro son bienes reales transportados desde depósitos; antes de la época moderna domina el forrajeo local con sus consecuencias sobre la población.
- **Features:** F-WAR-04.

### Ciencia, cultura y fin de partida

#### P-22 · Equipos de investigación y ministros especializados

- **Qué es:** la investigación la hacen equipos o personas con especialidades y nivel; el gobierno tiene ministros con efectos.
- **Por qué funciona:** da cara humana a la ciencia y a la administración.
- **Problemas habituales:** son listas estáticas por país.
- **Cómo lo adaptamos:** los equipos son **instituciones** (universidades, academias, talleres, laboratorios, empresas) con personas cualificadas, financiación y especialidad; nacen, crecen y emigran.
- **Features:** F-SCI-04, F-SCI-05.

#### P-23 · Integración cultural con derechos por grupo

- **Qué es:** cada cultura tiene un estatus en el Estado (aceptada, tolerada, discriminada) que afecta a su lealtad y a su asimilación.
- **Por qué funciona:** los imperios multiculturales se sienten como tales.
- **Problemas habituales:** la integración es un botón con un temporizador.
- **Cómo lo adaptamos:** el estatus se fija por leyes, afecta a derechos, impuestos y acceso a cargos, y la asimilación depende de causas materiales (sección 06).
- **Features:** F-CUL-01 a F-CUL-04.

#### P-24 · Crisis sistémicas, federaciones y herramientas abiertas

- **Qué es:** en las fases avanzadas de la partida aparecen grandes crisis que amenazan a todos y empujan a cooperar; las federaciones permiten compartir soberanía. El género, además, cuida mucho el mapa como interfaz, los modos de mapa, el libro de estadísticas y el modding abierto.
- **Por qué funciona:** mantiene la tensión al final de la partida y alarga la vida del juego gracias a la comunidad.
- **Problemas habituales:** crisis artificiales que no surgen de la partida.
- **Cómo lo adaptamos:** las crisis tardías son históricas o derivadas de la simulación (guerras mundiales, cambio climático, crisis financieras, pandemias); las federaciones y organizaciones internacionales surgen de la negociación. Mapa, estadísticas y mods siguen las secciones 18, 20 y 26.
- **Features:** F-ENV-05, F-DIP-08, F-PLT-02, F-UX-09.

### Lo que no se adopta

| Práctica del género | Por qué se descarta | Alternativa |
| --- | --- | --- |
| Recursos abstractos de poder que se acumulan (“puntos” administrativos, diplomáticos o militares) | Desconectan las capacidades de la economía y de las personas. | Capacidades derivadas de dinero, burocracia, personas cualificadas e instituciones. |
| Misiones o árboles fijos por país | Fuerzan la historia y caducan con la divergencia. | Ambiciones dinámicas (P-11). |
| Sucesos garantizados por fecha | Rompen la causalidad. | Situaciones condicionales (P-09). |
| Juegos separados por época con conversión de partidas | Interrumpen la continuidad. | Una sola partida continua. |
| Bonificaciones ocultas para la IA | El jugador no puede entender ni prever. | IA con las mismas reglas; dificultad declarada y visible. |
| Modificadores sin origen visible | Ilegibilidad. | Registro causal. |

### Lecciones que se convierten en reglas

| Problema frecuente | Regla de diseño de 101 |
| --- | --- |
| Modificadores apilados que nadie entiende. | Todo modificador relevante pasa por el registro causal y es consultable. |
| Bola de nieve: el más grande siempre gana. | Coste creciente de administración, coaliciones y tensiones internas proporcionales al tamaño. |
| Final de partida aburrido. | Crisis sistémicas, transformación institucional y objetivos que cambian con la época. |
| Microgestión repetitiva. | Asesores delegables con reglas configurables. |
| Eventos sin contexto. | Todo evento muestra las condiciones que lo dispararon. |
| Mapa ilegible con muchos países pequeños. | Modos de mapa agregados, etiquetas adaptativas y filtros por jerarquía. |

## 03. Catálogo de features

Cada feature tiene un ID estable para el backlog y el registro de decisiones. El tier indica cuándo es necesaria, no cuándo se empieza.

### Núcleo, tiempo y partida

| ID | Feature | Tier |
| --- | --- | --- |
| F-CORE-01 | Calendario continuo con día absoluto y fecha juliana/gregoriana de presentación. | MVP |
| F-CORE-02 | Pausa, cinco velocidades, modo máximo y “avanzar hasta fecha”. | MVP |
| F-CORE-03 | Pausas automáticas configurables por tipo de suceso. | Slice |
| F-CORE-04 | Guardado y carga deterministas, con autoguardado rotativo. | MVP |
| F-CORE-05 | Modo observador: ver la partida sin controlar ningún país. | Slice |
| F-CORE-06 | Cambio de país durante la partida (opcional, desactiva logros). | 1.0 |
| F-CORE-07 | Repeticiones a partir de semilla y diario de comandos. | 1.0 |
| F-CORE-08 | Cuatro modos de campaña (estricto, dinámico, alternativo, sandbox). | Slice |
| F-CORE-09 | Reglas de partida personalizables (dificultad, agresividad de la IA, epidemias). | 1.0 |
| F-CORE-10 | Crónica de la partida exportable. | 1.0 |

### Mapa y geografía

| ID | Feature | Tier |
| --- | --- | --- |
| F-MAP-01 | Mapa de provincias con selección, zoom y paneo fluidos. | MVP |
| F-MAP-02 | Modos de mapa: político, terreno, población, cultura, religión, economía, comercio, militar, diplomacia, tecnología, control. | Slice |
| F-MAP-03 | Etiquetas de países curvadas y adaptativas al tamaño. | Slice |
| F-MAP-04 | Estilo cartográfico que evoluciona con la época (sección 19). | 1.0 |
| F-MAP-05 | Niebla de conocimiento geográfico: el mapa conocido se amplía con la exploración. | 1.0 |
| F-MAP-06 | Mapas de calor y comparación entre dos fechas. | 1.0 |
| F-MAP-07 | Rutas comerciales y de suministro visibles con su capacidad. | Slice |
| F-MAP-08 | Cambios geográficos simulados (canales, desecación, nivel del mar). | Post |

### Población, cultura y religión

| ID | Feature | Tier |
| --- | --- | --- |
| F-POP-01 | Cohortes por provincia con ocupación, cultura, religión, estrato y necesidades. | MVP |
| F-POP-02 | Natalidad, mortalidad y migración ligadas a alimentos, salud, guerra y salarios. | MVP |
| F-POP-03 | Movilidad social entre ocupaciones según empleo y educación. | Slice |
| F-POP-04 | Asimilación y conversión graduales, con resistencia y retroceso. | Slice |
| F-POP-05 | Identidades superpuestas (local, regional, religiosa, dinástica, nacional). | 1.0 |
| F-POP-06 | Surgimiento de nacionalismos por alfabetización, imprenta y prensa. | 1.0 |
| F-POP-07 | Cismas y reformas religiosas emergentes, no programadas. | 1.0 |
| F-POP-08 | Urbanización: ciudades que crecen o se vacían por causas económicas. | Slice |

### Economía

| ID | Feature | Tier |
| --- | --- | --- |
| F-ECO-01 | Cadena recursos → producción → transporte → consumo con conservación exacta. | MVP |
| F-ECO-02 | Mercados regionales con precios por oferta y demanda. | MVP |
| F-ECO-03 | Rutas comerciales con capacidad, costes, peajes y bloqueos. | Slice |
| F-ECO-04 | Edificios y modos de producción que cambian con la tecnología. | Slice |
| F-ECO-05 | Presupuesto del Estado: impuestos, gasto, deuda, intereses, impago. | MVP |
| F-ECO-06 | Moneda: acuñación, devaluación e inflación. | Slice |
| F-ECO-07 | Banca, crédito privado y préstamos entre Estados. | Slice |
| F-ECO-08 | Compañías comerciales, monopolios y concesiones. | 1.0 |
| F-ECO-09 | Industrialización: energía, fábricas, ferrocarriles. | 1.0 |
| F-ECO-10 | Bancos centrales, política monetaria y ciclos económicos. | 1.0 |
| F-ECO-11 | Cadenas de suministro globales y sanciones modernas. | Post |
| F-ECO-12 | Explicación de cada precio con sus mayores contribuyentes. | Slice |

### Gobierno y política

| ID | Feature | Tier |
| --- | --- | --- |
| F-GOV-01 | Formas de gobierno construidas con primitivas (actor, institución, competencia, lealtad). | MVP |
| F-GOV-02 | Estamentos y grupos de interés con poder, lealtad y demandas. | Slice |
| F-GOV-03 | Leyes en categorías (propiedad, impuestos, religión, ciudadanía, trabajo, comercio). | Slice |
| F-GOV-04 | Capacidad del Estado: alcance administrativo, burocracia, corrupción. | Slice |
| F-GOV-05 | Control territorial efectivo frente a soberanía nominal. | MVP |
| F-GOV-06 | Rebeliones, revueltas campesinas y guerras civiles. | Slice |
| F-GOV-07 | Parlamentos, elecciones y partidos cuando existan las instituciones. | 1.0 |
| F-GOV-08 | Revoluciones y cambios de régimen con bandos y programas. | 1.0 |
| F-GOV-09 | Constituciones y división de poderes. | 1.0 |
| F-GOV-10 | Estado de bienestar, sindicatos y movimientos sociales modernos. | Post |

### Diplomacia e inteligencia

| ID | Feature | Tier |
| --- | --- | --- |
| F-DIP-01 | Relaciones multidimensionales (confianza, interés, agravio, dependencia). | MVP |
| F-DIP-02 | Tratados componibles: cada tratado es un conjunto de cláusulas. | Slice |
| F-DIP-03 | Vasallaje, tributo, protectorado y unión personal. | Slice |
| F-DIP-04 | Matrimonios dinásticos y reclamaciones hereditarias. | Slice |
| F-DIP-05 | Coaliciones defensivas frente a potencias amenazantes. | Slice |
| F-DIP-06 | Información imperfecta con retraso según las comunicaciones de la época. | Slice |
| F-DIP-07 | Espionaje, sabotaje, propaganda y robo tecnológico. | 1.0 |
| F-DIP-08 | Organizaciones internacionales, bloques comerciales y alianzas multilaterales. | 1.0 |
| F-DIP-09 | Disuasión nuclear y crisis de escalada. | Post |

### Guerra

| ID | Feature | Tier |
| --- | --- | --- |
| F-WAR-01 | Ejércitos con personal, equipo, moral, organización y suministro. | MVP |
| F-WAR-02 | Movimiento por red de provincias con costes de terreno y estación. | MVP |
| F-WAR-03 | Asedios con fortificaciones, guarnición, hambre y asalto. | MVP |
| F-WAR-04 | Logística: capacidad de ruta, depósitos, forrajeo y saqueo. | Slice |
| F-WAR-05 | Guerra naval: galeras, flotas de vela, bloqueo, convoyes. | Slice |
| F-WAR-06 | Reclutamiento por época: levas feudales, mercenarios, ejércitos permanentes, conscripción. | Slice |
| F-WAR-07 | Objetivos de guerra, puntuación bélica y negociación de paz por cláusulas. | MVP |
| F-WAR-08 | Ocupación, resistencia y reconstrucción. | Slice |
| F-WAR-09 | Frentes y planes operacionales delegables. | 1.0 |
| F-WAR-10 | Aviación, guerra blindada y operaciones combinadas. | 1.0 |
| F-WAR-11 | Ciberoperaciones, misiles y guerra electrónica. | Post |

### Ciencia, clima y mundo

| ID | Feature | Tier |
| --- | --- | --- |
| F-SCI-01 | Grafo tecnológico con descubrimiento, prototipo, adopción y producción. | Slice |
| F-SCI-02 | Difusión por comercio, migración, educación y espionaje. | Slice |
| F-SCI-03 | Límite de adelanto calibrado por época. | Slice |
| F-SCI-04 | Instituciones científicas: universidades, academias, laboratorios. | 1.0 |
| F-ENV-01 | Clima histórico reconstruido con variación por semilla. | Slice |
| F-ENV-02 | Epidemias por red de contactos (incluida la peste negra). | Slice |
| F-ENV-03 | Hambrunas, sequías e inundaciones con cadenas de efectos. | Slice |
| F-ENV-04 | Exploración y descubrimiento de rutas y territorios. | 1.0 |
| F-ENV-05 | Clima simulado por emisiones a partir del siglo XX. | Post |

### Personajes

| ID | Feature | Tier |
| --- | --- | --- |
| F-CHR-01 | Gobernantes, herederos, consortes y regentes con rasgos y capacidades. | Slice |
| F-CHR-02 | Dinastías con árbol genealógico y reclamaciones. | Slice |
| F-CHR-03 | Consejeros y generales con competencias y lealtad. | Slice |
| F-CHR-04 | Figuras históricas que aparecen solo si sus condiciones existen. | 1.0 |

### Interfaz y experiencia

| ID | Feature | Tier |
| --- | --- | --- |
| F-UX-01 | Tooltips anidados con causa, alcance, duración y respuestas. | Slice |
| F-UX-02 | Panel “¿por qué?” en toda variable importante. | Slice |
| F-UX-03 | Línea de tiempo comparada (historia real frente a partida). | 1.0 |
| F-UX-04 | Enciclopedia integrada con fuentes y nivel de confianza. | 1.0 |
| F-UX-05 | Asesores delegables con reglas configurables. | Slice |
| F-UX-06 | Tutorial progresivo y escenarios de aprendizaje. | 1.0 |
| F-UX-07 | Accesibilidad: escalado, daltonismo, atajos, lectura de pantalla parcial. | 1.0 |
| F-UX-08 | Localización: español e inglés desde el inicio. | Slice |

### Plataforma y comunidad

| ID | Feature | Tier |
| --- | --- | --- |
| F-PLT-01 | Simulación headless y 101 Lab. | MVP |
| F-PLT-02 | Mods de datos (países, eventos, mapas) con validador. | 1.0 |
| F-PLT-03 | Integración con Steam Workshop. | 1.0 |
| F-PLT-04 | Logros y estadísticas. | 1.0 |
| F-PLT-05 | Multijugador cooperativo y competitivo en lockstep. | Post |
| F-PLT-06 | Editor de escenarios para la comunidad (101 Forge público). | Post |

### Ampliaciones: núcleo, mapa, población y economía

| ID | Feature | Tier |
| --- | --- | --- |
| F-CORE-11 | Velocidad adaptativa: la partida frena automáticamente durante batallas o crisis seguidas por el jugador. | 1.0 |
| F-CORE-12 | Marcadores en la línea de tiempo para volver a momentos clave de la partida (desde autoguardados). | 1.0 |
| F-CORE-13 | Modo “hasta mi muerte”: partida con un único guardado para quien busca tensión. | 1.0 |
| F-CORE-14 | Desafíos: escenarios con objetivos y reglas especiales. | Post |
| F-CORE-15 | Partida compartida asíncrona: exportar una partida para que otro jugador la continúe. | Post |
| F-MAP-09 | Vista de capitales, ciudades y fortalezas con iconos escalables. | Slice |
| F-MAP-10 | Superposición de dos modos (p. ej. religión con bordes políticos). | 1.0 |
| F-MAP-11 | Mapa de “historia real” superpuesto para comparar fronteras en la misma fecha. | 1.0 |
| F-MAP-12 | Exportar el mapa en alta resolución con leyenda. | 1.0 |
| F-POP-09 | Pirámides de población simplificadas por provincia y país. | 1.0 |
| F-POP-10 | Diásporas con redes comerciales y culturales propias. | 1.0 |
| F-POP-11 | Refugiados y desplazados por guerra, hambre o persecución. | Slice |
| F-POP-12 | Educación como inversión con efecto diferido en la alfabetización. | 1.0 |
| F-ECO-13 | Gremios con monopolios, aprendices y conflictos con mercaderes. | Slice |
| F-ECO-14 | Ferias periódicas que concentran comercio en fechas y lugares concretos. | Slice |
| F-ECO-15 | Arrendamiento de impuestos a particulares, con corrupción y eficacia variables. | Slice |
| F-ECO-16 | Mercados financieros: bonos, acciones y crisis especulativas. | 1.0 |
| F-ECO-17 | Empresas privadas que invierten según rentabilidad esperada. | 1.0 |
| F-ECO-18 | Contabilidad nacional visible: producto, inversión, consumo, balanza comercial. | 1.0 |

### Comercio, rutas y colonias

| ID | Feature | Tier |
| --- | --- | --- |
| F-TRD-01 | Red de rutas generada por geografía e infraestructura, no fija. | Slice |
| F-TRD-02 | Peajes, aduanas y privilegios comerciales negociables. | Slice |
| F-TRD-03 | Piratería y corso como amenaza y como política de Estado. | Slice |
| F-TRD-04 | Barrios y factorías de comerciantes extranjeros (p. ej. colonias italianas en puertos levantinos). | Slice |
| F-TRD-05 | Convoyes y escoltas para proteger el comercio. | 1.0 |
| F-TRD-06 | Monopolios comerciales y compañías con flota propia. | 1.0 |
| F-TRD-07 | Colonias de asentamiento y de explotación con poblamiento real. | 1.0 |
| F-TRD-08 | Puertos de escala y bases navales lejanas. | 1.0 |
| F-TRD-09 | Canales interoceánicos como proyectos de gran escala. | 1.0 |
| F-TRD-10 | Bloqueos y sanciones con efectos medibles en precios. | Slice |

### Gobierno y política

| ID | Feature | Tier |
| --- | --- | --- |
| F-GOV-11 | Privilegios estamentales como contratos con contrapartidas. | Slice |
| F-GOV-12 | Transformación gradual de estamentos en grupos de interés modernos. | 1.0 |
| F-GOV-13 | Cortes, dietas y asambleas representativas premodernas. | Slice |
| F-GOV-14 | Reformas administrativas: provincias, gobernadores, intendentes. | Slice |
| F-GOV-15 | Corrupción y venta de cargos con efectos sobre la eficacia. | Slice |
| F-GOV-16 | Policía, censura y control de la información. | 1.0 |
| F-GOV-17 | Golpes militares y juntas. | 1.0 |
| F-GOV-18 | Referéndums, autonomías y federalización. | Post |

### Cultura

| ID | Feature | Tier |
| --- | --- | --- |
| F-CUL-01 | Estatus de cada cultura en el Estado (dominante, aceptada, tolerada, discriminada). | Slice |
| F-CUL-02 | Rasgos culturales que cambian lentamente con las condiciones. | Slice |
| F-CUL-03 | Hibridación: nacimiento de culturas nuevas por contacto prolongado. | 1.0 |
| F-CUL-04 | Lenguas de prestigio y de administración distintas de la popular. | Slice |
| F-CUL-05 | Movimientos culturales (humanismo, ilustración, romanticismo) que surgen y se difunden. | 1.0 |
| F-CUL-06 | Patrimonio: monumentos, obras y escuelas que dan prestigio y atraen talento. | 1.0 |
| F-CUL-07 | Nombres de lugares que cambian según la cultura dominante. | Slice |
| F-CUL-08 | Banderas y escudos generados por reglas heráldicas y vexilológicas. | Slice |

### Religión

| ID | Feature | Tier |
| --- | --- | --- |
| F-REL-01 | Política religiosa del Estado (oficial, tolerancia, autonomía comunitaria, persecución). | Slice |
| F-REL-02 | Autoridades religiosas como actores diplomáticos con intereses propios. | Slice |
| F-REL-03 | Doctrinas con rasgos que afectan a economía, política y sociedad. | Slice |
| F-REL-04 | Herejías, cismas y reformas emergentes. | 1.0 |
| F-REL-05 | Órdenes religiosas y militares con propiedades y fuerzas. | Slice |
| F-REL-06 | Peregrinaciones como flujo de personas, dinero y contagio. | 1.0 |
| F-REL-07 | Misiones y conversión gradual por contacto. | 1.0 |
| F-REL-08 | Secularización como proceso social, no como ley única. | 1.0 |

### Narrativa e historia

| ID | Feature | Tier |
| --- | --- | --- |
| F-NAR-01 | Situaciones con ventana, roles, precondiciones, caducidad y variantes. | Slice |
| F-NAR-02 | Etapas visibles de cada situación con indicadores de progreso. | Slice |
| F-NAR-03 | Índice de divergencia por región. | Slice |
| F-NAR-04 | Restauraciones de identidades desaparecidas. | Slice |
| F-NAR-05 | Eventos con opciones cuyos efectos completos son visibles. | Slice |
| F-NAR-06 | Eventos de personaje (enfermedades, matrimonios, conjuras). | Slice |
| F-NAR-07 | Límites de repetición y variedad de eventos. | Slice |
| F-NAR-08 | Ilustraciones de eventos por época y región. | 1.0 |
| F-NAR-09 | Ambiciones nacionales dinámicas. | Slice |
| F-NAR-10 | Hitos de época sin bonificaciones desequilibrantes. | 1.0 |
| F-NAR-11 | Notas históricas: cada situación enlaza a su entrada de enciclopedia. | 1.0 |
| F-NAR-12 | Crónica comparada al terminar la partida. | 1.0 |

### Diplomacia

| ID | Feature | Tier |
| --- | --- | --- |
| F-DIP-10 | Vasallos con IA propia que evalúa si le conviene seguir. | Slice |
| F-DIP-11 | Rehenes y garantías personales en tratados premodernos. | Slice |
| F-DIP-12 | Conferencias de paz multilaterales. | 1.0 |
| F-DIP-13 | Neutralidad declarada y derecho de paso. | Slice |
| F-DIP-14 | Arbitraje de terceros (autoridades religiosas, tribunales internacionales). | 1.0 |
| F-DIP-15 | Ayuda exterior y préstamos condicionados. | 1.0 |
| F-DIP-16 | Embargos y sanciones multilaterales. | 1.0 |

### Guerra

| ID | Feature | Tier |
| --- | --- | --- |
| F-WAR-12 | Objetivos de guerra declarados que determinan la puntuación. | Slice |
| F-WAR-13 | Agotamiento bélico emergente de bajas, impuestos, precios y saqueos. | Slice |
| F-WAR-14 | Órdenes de campaña (asediar, devastar, perseguir, defender) para épocas premodernas. | Slice |
| F-WAR-15 | Plantillas de formación con costes y terreno. | 1.0 |
| F-WAR-16 | Producción militar en líneas con eficiencia. | 1.0 |
| F-WAR-17 | Mercenarios como entidades con contrato, lealtad y riesgo de rebelión. | Slice |
| F-WAR-18 | Fortificaciones construibles y su modernización. | Slice |
| F-WAR-19 | Guerra de guerrillas y resistencia en territorio ocupado. | 1.0 |
| F-WAR-20 | Inteligencia militar y niebla de guerra. | Slice |
| F-WAR-21 | Prisioneros, rescates e intercambios. | Slice |
| F-WAR-22 | Leyes de la guerra que evolucionan con las instituciones internacionales. | Post |

### Ciencia, clima y personajes

| ID | Feature | Tier |
| --- | --- | --- |
| F-SCI-05 | Instituciones científicas con personas cualificadas que pueden emigrar. | 1.0 |
| F-SCI-06 | Patentes, secretos industriales y transferencia tecnológica. | 1.0 |
| F-SCI-07 | Expediciones científicas y sociedades eruditas. | 1.0 |
| F-SCI-08 | Proyectos de gran escala (catedrales, canales, programas espaciales). | 1.0 |
| F-ENV-06 | Erupciones volcánicas con efectos climáticos regionales y globales. | 1.0 |
| F-ENV-07 | Deforestación y agotamiento del suelo. | 1.0 |
| F-ENV-08 | Plagas agrícolas y enfermedades del ganado. | 1.0 |
| F-ENV-09 | Contaminación urbana e industrial. | Post |
| F-ENV-10 | Medidas sanitarias por época (cuarentena, lazaretos, vacunación). | Slice |
| F-CHR-05 | Facciones de corte vinculadas a grupos de interés. | Slice |
| F-CHR-06 | Conjuras y golpes palaciegos. | 1.0 |
| F-CHR-07 | Educación de herederos. | 1.0 |
| F-CHR-08 | Regencias con consejo y riesgos propios. | Slice |
| F-CHR-09 | Retratos modulares por cultura, época y edad. | 1.0 |
| F-CHR-10 | Biografía automática de cada gobernante en la crónica. | 1.0 |

### Asesores, estadísticas y modos de juego

| ID | Feature | Tier |
| --- | --- | --- |
| F-ADV-01 | Asesor económico con reglas (deuda máxima, prioridades de inversión). | Slice |
| F-ADV-02 | Asesor comercial (rutas, privilegios, flotas mercantes). | 1.0 |
| F-ADV-03 | Asesor diplomático para relaciones menores. | 1.0 |
| F-ADV-04 | Generales con órdenes de campaña delegadas. | Slice |
| F-ADV-05 | Registro de todas las acciones de los asesores, reversibles cuando sea posible. | Slice |
| F-ADV-06 | Recomendaciones explicadas, nunca obligatorias. | 1.0 |
| F-STA-01 | Libro de estadísticas con series temporales por país y región. | Slice |
| F-STA-02 | Comparación entre países en cualquier indicador. | 1.0 |
| F-STA-03 | Exportación de estadísticas en CSV. | 1.0 |
| F-STA-04 | Gráficas de la partida frente a estimaciones históricas. | 1.0 |
| F-STA-05 | Rankings de potencias por economía, ejército, población y prestigio. | Slice |
| F-STA-06 | Panel de salud del Estado (finanzas, legitimidad, control, alimentos). | Slice |
| F-MOD-01 | Modo historiador: observar sin intervenir con herramientas de análisis. | 1.0 |
| F-MOD-02 | Modo aprendizaje con escenarios cortos guiados. | 1.0 |
| F-MOD-03 | Modo “qué pasaría si”: cambiar una condición inicial y comparar. | Post |
| F-MOD-04 | Partidas con reglas de dificultad visibles y sin trampas ocultas. | 1.0 |
| F-MOD-05 | Inicio en entidad no soberana (rebelde, vasallo, compañía). | Post |
| F-MOD-06 | Escenarios regionales cortos (100–150 años). | 1.0 |

### Calidad de vida, audio y multijugador

| ID | Feature | Tier |
| --- | --- | --- |
| F-QOL-01 | Búsqueda universal de provincias, países, personajes y entradas. | Slice |
| F-QOL-02 | Historial de navegación en paneles (atrás y adelante). | Slice |
| F-QOL-03 | Notificaciones agrupadas y filtrables. | Slice |
| F-QOL-04 | Paneles anclables y comparables lado a lado. | 1.0 |
| F-QOL-05 | Deshacer órdenes dadas en pausa. | Slice |
| F-QOL-06 | Plantillas de leyes y presupuestos guardables. | 1.0 |
| F-QOL-07 | Recordatorios programados por el jugador. | 1.0 |
| F-QOL-08 | Modo de pantalla de datos para segundos monitores. | Post |
| F-QOL-09 | Atajos de teclado para todos los paneles. | Slice |
| F-QOL-10 | Tooltips fijables para leer con calma. | Slice |
| F-UX-09 | Libro de estadísticas integrado con el registro causal. | 1.0 |
| F-UX-10 | Glosario contextual en tooltips. | 1.0 |
| F-AUD-01 | Música adaptativa por región, época y tensión. | 1.0 |
| F-AUD-02 | Ambientación sonora del mapa por zoom. | 1.0 |
| F-AUD-03 | Señales sonoras distintas por tipo de alerta. | Slice |
| F-AUD-04 | Narración opcional de la crónica. | Post |
| F-MP-01 | Partidas cooperativas (varios jugadores en un país). | Post |
| F-MP-02 | Partidas competitivas en lockstep determinista. | Post |
| F-MP-03 | Reconexión y carga en caliente desde el anfitrión. | Post |
| F-MP-04 | Detección de desincronización por hash con informe automático. | Post |
| F-MP-05 | Velocidad votada y pausas limitadas. | Post |
| F-MP-06 | Partidas por turnos de tiempo largo (jugar por correo). | Post |
| F-PLT-07 | Guardado en la nube. | 1.0 |
| F-PLT-08 | Informes de error con consentimiento y repetición adjunta. | 1.0 |
| F-PLT-09 | Compatibilidad con Steam Deck y resoluciones pequeñas. | 1.0 |
| F-PLT-10 | Soporte de mods para traducciones comunitarias. | 1.0 |

### Ampliaciones por época

| ID | Feature | Tier |
| --- | --- | --- |
| F-MED-01 | Cabalgadas y devastación de comarcas como táctica de guerra. | Slice |
| F-MED-02 | Juramentos de vasallaje con ceremonias y testigos que afectan a la legitimidad. | Slice |
| F-MED-03 | Fueros urbanos negociables a cambio de dinero o tropas. | Slice |
| F-MED-04 | Órdenes militares con encomiendas y castillos propios. | Slice |
| F-MED-05 | Peregrinaciones y jubileos como flujos económicos y de prestigio. | 1.0 |
| F-MED-06 | Rescate de nobles capturados. | Slice |
| F-MED-07 | Tributos de protección a potencias nómadas. | Slice |
| F-MED-08 | Torneos y prestigio caballeresco. | Post |
| F-EMO-01 | Compañías comerciales con accionistas, flota y ejército. | 1.0 |
| F-EMO-02 | Colonización con poblamiento, mestizaje y resistencia. | 1.0 |
| F-EMO-03 | Confesionalización y gestión de minorías religiosas. | 1.0 |
| F-EMO-04 | Bancarrotas de la Corona con renegociación de deuda. | 1.0 |
| F-EMO-05 | Intendentes y reformas centralizadoras con resistencia regional. | 1.0 |
| F-EMO-06 | Corso con patente y piratería independiente. | 1.0 |
| F-EMO-07 | Correo postal regular que amplía el alcance del Estado. | 1.0 |
| F-EMO-08 | Academias científicas y sociedades eruditas. | 1.0 |
| F-IND-01 | Revoluciones políticas con bandos, programas y guerras civiles. | 1.0 |
| F-IND-02 | Partidos políticos con bases sociales y coaliciones. | 1.0 |
| F-IND-03 | Sindicatos, huelgas y legislación laboral. | 1.0 |
| F-IND-04 | Ferrocarriles que transforman la logística y el comercio. | 1.0 |
| F-IND-05 | Emigración masiva intercontinental. | 1.0 |
| F-IND-06 | Ciclos económicos y crisis bursátiles. | 1.0 |
| F-IND-07 | Abolición de la esclavitud y de la servidumbre como procesos políticos. | 1.0 |
| F-IND-08 | Prensa de masas y opinión pública. | 1.0 |
| F-IND-09 | Imperialismo con protectorados, esferas de influencia y resistencia. | 1.0 |
| F-IND-10 | Exposiciones universales y prestigio industrial. | Post |
| F-CON-01 | Economía de guerra: racionamiento, controles de precios, reconversión. | 1.0 |
| F-CON-02 | Ideologías de masas con programas y movimientos juveniles. | 1.0 |
| F-CON-03 | Economía planificada con planes quinquenales y cuotas. | 1.0 |
| F-CON-04 | Propaganda y censura en tiempos de guerra. | 1.0 |
| F-CON-05 | Escalada nuclear con umbrales visibles. | 1.0 |
| F-CON-06 | Carrera espacial como proyecto de prestigio. | Post |
| F-CON-07 | Organismos internacionales con votaciones y misiones. | 1.0 |
| F-CON-08 | Guerra por delegación y apoyo a insurgencias. | 1.0 |
| F-DIG-01 | Cadenas de suministro con nodos críticos. | Post |
| F-DIG-02 | Ciberoperaciones ofensivas y defensivas. | Post |
| F-DIG-03 | Desinformación y opinión pública en redes. | Post |
| F-DIG-04 | Transición energética con costes y ganadores. | Post |
| F-DIG-05 | Automatización y su efecto sobre el empleo. | Post |
| F-DIG-06 | Integración regional con cesiones de soberanía. | Post |
| F-DIG-07 | Migraciones climáticas. | Post |
| F-DIG-08 | Deuda soberana y rescates internacionales. | Post |
| F-FUT-01 | Tecnologías posteriores a 2060 con costes y riesgos. | Post |
| F-FUT-02 | Proyectos espaciales de larga duración. | Post |
| F-FUT-03 | Geoingeniería con riesgos internacionales. | Post |
| F-FUT-04 | Nuevas formas de gobierno derivadas de la partida. | Post |

### Herramientas, laboratorio y desarrollo

| ID | Feature | Tier |
| --- | --- | --- |
| F-FRG-01 | Editor de entidades con validación en tiempo real. | MVP |
| F-FRG-02 | Editor de situaciones con vista previa de condiciones. | Slice |
| F-FRG-03 | Editor de mapa (localizaciones, provincias, terreno). | Slice |
| F-FRG-04 | Editor del grafo tecnológico con detección de ciclos. | Slice |
| F-FRG-05 | Simulación de prueba de unos años desde el editor. | Slice |
| F-FRG-06 | Comparación de dos versiones de un archivo de datos. | 1.0 |
| F-FRG-07 | Importación de tablas desde hojas de cálculo. | Slice |
| F-FRG-08 | Exportación de paquetes de mods. | 1.0 |
| F-LAB-01 | Ejecución de cientos de campañas en paralelo. | MVP |
| F-LAB-02 | Informes HTML con distribuciones y alertas. | MVP |
| F-LAB-03 | Comparación de dos versiones del juego con las mismas semillas. | Slice |
| F-LAB-04 | Bisección automática de desincronizaciones. | Slice |
| F-LAB-05 | Mapa de calor de divergencia histórica media. | Slice |
| F-LAB-06 | Exportación a Parquet para análisis externo. | Slice |
| F-LAB-07 | Panel de salud de la IA (bloqueos, bancarrotas, guerras absurdas). | Slice |
| F-LAB-08 | Perfiles de rendimiento por sistema y por año simulado. | Slice |
| F-DEV-01 | Consola de depuración con consultas al estado. | MVP |
| F-DEV-02 | Visualización del registro causal de cualquier variable. | MVP |
| F-DEV-03 | Modo de inspección de decisiones de la IA. | Slice |
| F-DEV-04 | Recarga en caliente de datos durante el desarrollo. | Slice |
| F-DEV-05 | Captura automática de semilla y comandos en cada error. | Slice |

### Accesibilidad y localización ampliadas

| ID | Feature | Tier |
| --- | --- | --- |
| F-ACC-01 | Tamaño de fuente independiente del escalado de la interfaz. | 1.0 |
| F-ACC-02 | Modo de alto contraste en mapa e interfaz. | 1.0 |
| F-ACC-03 | Patrones y símbolos en todos los modos de mapa. | 1.0 |
| F-ACC-04 | Reducción de animaciones y destellos. | 1.0 |
| F-ACC-05 | Navegación completa por teclado. | 1.0 |
| F-ACC-06 | Lectura en voz de tooltips y alertas mediante el lector del sistema, donde sea posible. | Post |
| F-ACC-07 | Velocidad de juego mínima muy lenta para quien necesita más tiempo. | Slice |
| F-L10N-01 | Español e inglés completos. | Slice |
| F-L10N-02 | Francés, alemán, portugués de Brasil, ruso, chino simplificado, japonés. | Post |
| F-L10N-03 | Topónimos por cultura e idioma del jugador. | Slice |
| F-L10N-04 | Calendarios culturales opcionales en la fecha mostrada. | 1.0 |

---

# Parte II · Mundo y contenido histórico

## 04. Mundo, mapa y tiempo

### Estructura geográfica

| Capa | Descripción | Mutabilidad |
| --- | --- | --- |
| Localización | Unidad física indivisible: elevación, bioma, costa, ríos, recursos, habitabilidad. | Solo por procesos simulados explícitos. |
| Provincia | Agrupación administrativa de localizaciones; unidad de control y de cohortes. | Reorganizable por el Estado. |
| Región económica | Mercado con precios propios, centro urbano y acceso a rutas. | Cambia con la infraestructura. |
| Entidad política | Soberanía, vasallaje, protectorado, federación, control efectivo. | Totalmente dinámica. |
| Macrorregión | Agrupación para estadísticas, IA y filtros (Balcanes, Levante, Magreb…). | Fija; solo informativa. |

> **Regla:** la geografía física es inmutable salvo por procesos simulados explícitos (canales, desecación, deforestación, subida del nivel del mar). Las divisiones políticas y administrativas son siempre datos derivados y reorganizables.

### Resolución del mapa (propuesto)

| Escala | Localizaciones | Provincias | Mercados | Uso |
| --- | --- | --- | --- | --- |
| S | ~1.500 | 300–400 | 20–30 | Vertical slice. |
| M | ~8.000 | ~2.000 | ~120 | Continente (Europa + Mediterráneo + Oriente Próximo). |
| L | ~25.000 | 5.000+ | ~400 | Mundo completo. |

La densidad no es uniforme: las regiones con más población, ciudades y documentación (Europa, Mediterráneo, India, China) tienen provincias más pequeñas. Los desiertos, la tundra y el océano tienen celdas grandes. Así el mapa refleja dónde se concentraba la actividad sin inflar el coste en zonas vacías.

### Terreno y movimiento

| Terreno | Movimiento | Defensa | Suministro | Notas |
| --- | --- | --- | --- | --- |
| Llanura | Rápido | Bajo | Alto | Caballería eficaz. |
| Colinas | Medio | Medio | Medio | — |
| Montaña | Lento | Muy alto | Bajo | Pasos y puertos de montaña como cuellos de botella. |
| Bosque | Lento | Alto | Medio | Emboscadas; madera. |
| Pantano | Muy lento | Alto | Bajo | Enfermedades. |
| Desierto | Lento | Medio | Muy bajo | Agua como recurso logístico. |
| Estepa | Rápido | Bajo | Medio | Pastoreo; ventaja nómada. |
| Ciudad / fortaleza | — | Por fortificación | Por almacenes | Asedios. |
| Río | Cruce costoso | Bonificación al defensor | Transporte fluvial | Puentes y vados. |
| Estrecho | Requiere flota | — | — | Bósforo, Dardanelos, Gibraltar, Otranto. |

La **estación** modifica todo: lluvias de otoño, invierno en montaña, deshielo y crecidas, monzones. En 1300 casi ninguna campaña se sostiene en invierno; en 1900 sí, a un coste.

### Periodización como referencia, no como bloqueo

| Periodo de diseño | Sistemas distintivos |
| --- | --- |
| 1300–1500 | Feudalismo, dinastías, agricultura, vasallaje, asedios, gremios, epidemias. |
| 1500–1750 | Expansión oceánica, mercados intercontinentales, manufacturas, artillería, Estados fiscales. |
| 1750–1914 | Industrialización, urbanización, ferrocarriles, nacionalismos, banca, ciencia organizada. |
| 1914–1991 | Guerra industrial, aviación, mecanización, producción bélica, bloques y armas nucleares. |
| 1991–2060 | Digitalización, globalización, cadenas complejas, automatización, ciberespacio y clima. |
| 2060+ | Extensión plausible según el mundo simulado. |

Ningún sistema se activa por fecha. Un sistema aparece cuando existen las condiciones que lo hacen relevante: el sistema ferroviario existe cuando alguien desarrolla ferrocarriles.

### Reloj de simulación

Se separan tres conceptos: **paso temporal del motor**, **frecuencia de cada sistema** y **velocidad de visualización**.

| Escala | Uso principal |
| --- | --- |
| Hora / subdía | Operaciones militares modernas, misiones, incidentes tácticos seleccionados. |
| Día | Movimientos, suministros urgentes, sucesos políticos, decisiones de IA. |
| Semana | Mercados regionales, rutas, diplomacia operativa. |
| Mes | Producción, consumo, salarios, recaudación, ciencia, migración. |
| Trimestre / año | Demografía estructural, instituciones, objetivos estratégicos, estadísticas. |

**Escalonamiento:** los cálculos mensuales no se ejecutan todos el día 1. Cada provincia, mercado o país tiene un día de cálculo dentro del mes derivado de su ID, para repartir la carga y evitar picos.

### Calendario interno

- El motor cuenta el tiempo como un **número de día absoluto** (entero) desde una época fija, con calendario gregoriano proléptico. Toda la lógica usa ese número.
- La interfaz puede mostrar la fecha en calendario **juliano o gregoriano** según la región y la época, porque la adopción del gregoriano empezó en 1582 y se extendió durante siglos. También podrá mostrar calendarios hégira, bizantino (*anno mundi*) u otros como opción cultural.
- Los datos históricos se normalizan a día absoluto en el pipeline, guardando el calendario original de la fuente.

### Especificación detallada del mapa (v0.7, propuesto)

Base de `docs/specs/map-pipeline.md` y de la parte geográfica de `e101-map`.

#### Campos de una localización

| Campo | Tipo | Ejemplo |
| --- | --- | --- |
| `id` | `LocationId` (estable entre versiones) | `loc_bithynia_017` |
| Geometría | Polígono en el pipeline; en el motor, solo centroide, área y vecinos | Centroide (40,43 N; 29,72 E), 410 km² |
| Elevación media y máxima | Metros | 180 / 920 |
| Terreno dominante | Enumeración de la tabla de terreno | Colinas |
| Bioma y suelo | Enumeración | Bosque mediterráneo; suelo fértil |
| Costa | Ninguna / costa / puerto natural | Costa |
| Río | Ninguno / río navegable / río no navegable | Río no navegable |
| Recursos | Lista con potencial | Grano (alto), madera (medio), seda (bajo) |
| Habitabilidad | 0–1 | 0,85 |
| Sismicidad | 0–3 | 2 |
| Paludismo | 0–3 | 1 |

#### Campos de una provincia

| Campo | Contenido |
| --- | --- |
| Localizaciones | Lista (1–12 en la escala S) |
| Centro | Ciudad o aldea principal; determina la posición de etiquetas e iconos |
| Fortificación | Nivel 0–6 (sección 13) |
| Mercado | Región económica a la que pertenece |
| Infraestructura | Caminos (0–3), puentes, puerto (0–3), acueductos |
| Edificios | Lista de edificios con niveles y modos |
| Cohortes | Lista (sección 09) |
| Controlador y propietario | Entidad que controla de hecho y entidad soberana (pueden diferir) |
| Seguridad | 0–1, derivada de ejércitos hostiles, bandolerismo, devastación |
| Historial | Nombres por cultura, propietarios, batallas, sucesos (alimenta la crónica) |

#### Tipos de adyacencia

| Tipo | Cruce | Coste base | Notas |
| --- | --- | --- | --- |
| Tierra | Libre | Según terreno de destino | — |
| Río | Vado o puente | +1 día sin puente; ataque × 0,7 | Crecidas en deshielo: +2 días |
| Paso de montaña | Estrecho | Según terreno; cerrado en invierno en alta montaña | Ancho de frente 1.500 |
| Estrecho | Requiere barcos o puente | 1 día con barcos propios o alquilados | Bósforo, Dardanelos, Otranto, Mesina |
| Mar (costa a costa) | Requiere flota o transporte | Distancia / velocidad del barco | Estacional |
| Calzada principal | Mejora de la adyacencia terrestre | × 0,8 del tiempo | *Via Egnatia*, caminos reales |

#### Grafo de tiempos de viaje

El “tiempo de viaje” que usan el control (sección 11), las noticias (sección 12), la migración (sección 09) y la logística (sección 13) es el **mismo grafo**, con pesos distintos por tipo de viajero:

| Viajero | Velocidad relativa | Uso |
| --- | --- | --- |
| Mensajero a caballo | 1,0 (≈ 60–80 km/día en camino) | Control, noticias |
| Mercader con carga | 0,35 | Comercio terrestre |
| Ejército | 0,30 (ajustado por tamaño y composición) | Movimiento militar |
| Migrantes | 0,25 | Migración |
| Barco | Según tipo y estación | Todos los anteriores por mar |

**Algoritmo:** para cada Estado, un Dijkstra multiorigen desde la capital y los centros administrativos (gobernadores) calcula los días a cada provincia. Se recalcula **solo** cuando cambian las aristas relevantes (un camino nuevo, una provincia que pasa a ser insegura, un estrecho bloqueado, el cambio de estación); el resultado se cachea por Estado y estación. En la escala S cuesta menos de 1 ms por Estado; en la escala L se limita a los Estados afectados por el cambio.

**Ejemplo:** de Constantinopla a Tesalónica hay unos 6 días por mar en verano y unos 12 por la *Via Egnatia*; en invierno, el mar pasa a 10 días con riesgo alto y el camino a 16. Por eso el control bizantino sobre Macedonia empeora cada invierno y mejora con una flota propia: la geografía, no un modificador, explica el efecto.

#### Estaciones por macrorregión

| Macrorregión | Lluvias de otoño | Invierno | Deshielo | Estación de campaña óptima |
| --- | --- | --- | --- | --- |
| Egeo y costas griegas | Octubre–noviembre | Diciembre–febrero (suave) | — | Abril–octubre |
| Balcanes interiores | Octubre–noviembre | Diciembre–marzo | Marzo–abril | Mayo–septiembre |
| Meseta anatolia | Noviembre | Diciembre–marzo (frío) | Marzo–abril | Mayo–octubre |
| Llanura panónica | Octubre | Diciembre–febrero | Marzo | Mayo–octubre |
| Estepa póntica | Octubre | Noviembre–marzo (muy frío) | Abril | Mayo–septiembre (los nómadas prefieren el invierno para cruzar ríos helados) |
| Levante y Egipto (borde) | — | Diciembre–febrero (lluvioso) | — | Octubre–mayo (el verano es duro en el desierto) |

#### Proceso del pipeline geográfico, paso a paso

| Paso | Herramienta | Entrada | Salida | Validación |
| --- | --- | --- | --- | --- |
| 1. Costas y relieve | QGIS + scripts | Natural Earth, modelo de elevación | Polígonos de tierra, mar y lagos | Sin huecos ni solapes |
| 2. Ríos | Scripts | Hidrografía base | Líneas con caudal y navegabilidad | Ríos conectados al mar o a lagos |
| 3. Localizaciones | Generación semiautomática + edición | Relieve, densidad de población histórica (HYDE como referencia) | Polígonos de localización | Tamaño dentro del rango de la escala |
| 4. Provincias | Edición manual guiada | Localizaciones + fuentes históricas | Agrupaciones | Contigüidad (o enlace marítimo declarado) |
| 5. Adyacencias | Script | Polígonos + estrechos y pasos declarados | Grafo | Sin provincias aisladas sin justificar |
| 6. Textura de IDs | Script de rasterizado | Polígonos | Imagen de 16 bits por píxel | Cada ID tiene píxeles; ningún píxel sin ID en tierra |
| 7. Compilación | `e101-content` | Todo lo anterior | Binario versionado | Hash reproducible en dos máquinas |

## 05. El mundo en 1300

Esta sección es el **inventario de partida** del mundo. Sirve para dimensionar el contenido, elegir la vertical y priorizar regiones. Los gobernantes indicados son los que reinaban en 1300 según la historiografía general; todos deben confirmarse en la Biblia histórica (nivel de confianza A/B, sección 24).

### Panorama

En 1300 el mundo está marcado por el **imperio mongol fragmentado** en cuatro grandes kanatos, un **Mediterráneo** disputado entre repúblicas comerciales italianas, cruzados en retirada, Bizancio debilitado y el sultanato mameluco; una **Europa occidental** de monarquías en consolidación; una **India** dominada en el norte por el sultanato de Delhi; un **sudeste asiático** en plena reorganización tras las invasiones mongolas; y unas **Américas** sin contacto con el resto del mundo, con Mesoamérica y los Andes en vísperas del surgimiento de los imperios mexica e inca. Faltan unas cinco décadas para la peste negra.

### Europa occidental

| Entidad | Gobierno en 1300 | Gobernante | Notas de diseño |
| --- | --- | --- | --- |
| Reino de Francia | Monarquía feudal en centralización | Felipe IV el Hermoso | Conflicto con el papado; Estado fiscal temprano. |
| Reino de Inglaterra | Monarquía con Parlamento | Eduardo I | Guerras con Escocia; Gales conquistado. |
| Escocia | Reino en guerra de independencia | Guardianes del reino | Balliol depuesto en 1296; caso de restauración. |
| Corona de Castilla | Monarquía | Fernando IV (regencia de María de Molina) | Minoría de edad, nobleza turbulenta. |
| Corona de Aragón | Monarquía compuesta | Jaime II | Expansión mediterránea; origen de la Compañía Catalana. |
| Reino de Portugal | Monarquía | Dionisio I | Estabilidad; futura vocación atlántica. |
| Reino de Navarra | Unión personal con Francia | Juana I y Felipe IV | Unión personal como mecánica. |
| Emirato de Granada | Sultanato nazarí | Muhammad II | Último Estado musulmán de la península. |
| Reino de Irlanda / señoríos | Señorío inglés y reinos gaélicos | — | Control efectivo frente a soberanía nominal. |

### Europa central y el Imperio

| Entidad | Gobierno | Gobernante | Notas de diseño |
| --- | --- | --- | --- |
| Sacro Imperio Romano Germánico | Monarquía electiva sobre cientos de entidades | Alberto I de Habsburgo, rey de romanos | Representar como **organización** de entidades, no como un país. |
| Reino de Bohemia | Monarquía | Venceslao II | Minas de plata de Kutná Hora; rey de Polonia desde 1300. |
| Reino de Polonia | Reunificación en curso | Venceslao II | Fragmentación feudal en retroceso. |
| Reino de Hungría | Monarquía | Andrés III | Último Árpád; su muerte en 1301 abre una crisis sucesoria. |
| Austria, Baviera, Sajonia, Brandeburgo… | Principados del Imperio | Diversas casas | Agregar en grupos en la escala M. |
| Confederación suiza | Alianza de cantones (1291) | — | Caso de federación emergente. |
| Liga Hanseática | Red de ciudades comerciales | — | Organización comercial, no Estado. |
| Orden Teutónica | Estado monástico militar | Gran maestre | Cruzadas bálticas contra Lituania. |

### Italia

| Entidad | Gobierno | Gobernante | Notas de diseño |
| --- | --- | --- | --- |
| República de Venecia | República oligárquica | Dux Pietro Gradenigo | Imperio marítimo: Creta, Negroponte, Modón, Corón. |
| República de Génova | República con facciones | Familias Doria, Spinola, Grimaldi, Fieschi | Pera, Caffa; rival de Venecia. |
| República de Florencia | Comuna gremial | Priores (Dante es prior en 1300) | Banca, paño; güelfos negros y blancos. |
| Señoría de Milán | Señoría | Mateo I Visconti | Pierde el poder en 1302 y lo recupera después. |
| Estados Pontificios | Teocracia | Bonifacio VIII | Jubileo de 1300; choque con Francia. |
| Reino de Nápoles | Monarquía angevina | Carlos II de Anjou | Guerra por Sicilia. |
| Reino de Sicilia (Trinacria) | Monarquía aragonesa | Federico III | Paz de Caltabellotta en 1302. |

### Norte y este de Europa

| Entidad | Gobierno | Gobernante | Notas de diseño |
| --- | --- | --- | --- |
| Reino de Noruega | Monarquía | Haakon V | Futura unión con Suecia y Dinamarca. |
| Reino de Suecia | Monarquía | Birger Magnusson | Conflictos dinásticos. |
| Reino de Dinamarca | Monarquía | Erico VI Menved | Control del Sund. |
| Gran Ducado de Lituania | Monarquía pagana en expansión | Vytenis | Último gran Estado pagano de Europa. |
| República de Nóvgorod | República mercantil | Asamblea (*veche*) | Comercio de pieles; vínculo hanseático. |
| Principados de la Rus | Vasallos de la Horda de Oro | Gran príncipe de Vladímir: Andréi Aleksándrovich; Moscú: Daniel | Moscú aún es menor; ascenso no garantizado. |
| Horda de Oro | Kanato mongol | Toqta | Domina la estepa póntica y cobra tributo a la Rus. |

### Balcanes, Anatolia y Mediterráneo oriental

Detalle completo en la sección 29 (vertical slice).

| Entidad | Gobernante | Notas |
| --- | --- | --- |
| Imperio bizantino | Andrónico II Paleólogo | Crisis fiscal y militar; pierde Anatolia occidental. |
| Beylik otomano | Osmán I | Pequeño principado fronterizo en Bitinia. |
| Otros beyliks turcos | Germiyan, Karamán, Karasi, Menteşe, Candar, Saruhan… | Fragmentación tras el declive del sultanato selyúcida de Rum. |
| Reino de Serbia | Esteban Milutin | Expansión hacia Macedonia. |
| Imperio búlgaro | Teodoro Svetoslav | Restauración tras la presión mongola. |
| Imperio de Trebisonda | Alejo II | Comercio de la ruta de Tabriz. |
| Reino de Chipre | Enrique II de Lusignan | Refugio de las órdenes militares tras 1291. |
| Armenia cilicia | Dinastía hetúmida | Aliada de los mongoles frente a los mamelucos. |

### Mundo islámico y África

| Entidad | Gobierno | Gobernante | Notas de diseño |
| --- | --- | --- | --- |
| Sultanato mameluco | Sultanato militar | al-Nasir Muhammad (segundo reinado) | Egipto y Siria; Estado esclavo-militar; muy rico. |
| Iljanato | Kanato mongol | Ghazan | Conversión al islam en 1295; reformas fiscales. |
| Sultanato benimerín | Sultanato | Abu Yaqub Yusuf | Asedio de Tremecén (1299–1307). |
| Reino zayyaní (Tremecén) | Sultanato | — | Bajo asedio benimerín. |
| Sultanato hafsí | Sultanato | — | Ifriqiya; comercio con Italia. |
| Imperio de Malí | Imperio | Mansa (a confirmar) | Oro transahariano; Mansa Musa reinará desde c. 1312. |
| Etiopía salomónica | Imperio cristiano | Wedem Arad | Rivalidad con sultanatos musulmanes de Ifat. |
| Sultanato de Kilwa | Ciudad-Estado comercial | — | Comercio swahili del oro. |
| Gran Zimbabue | Reino | — | Oro y ganado; comercio índico. |
| Reino de Kanem | Imperio saheliano | — | Rutas al Mediterráneo. |
| Reinos yoruba e Ifé; Benín | Reinos urbanos | — | Escultura, comercio regional. |
| Makuria | Reino cristiano nubio | — | En declive bajo presión mameluca. |

### Asia central, meridional y oriental

| Entidad | Gobierno | Gobernante | Notas de diseño |
| --- | --- | --- | --- |
| Dinastía Yuan | Kanato mongol / imperio chino | Temür Kan (Chengzong) | La mayor economía del mundo; papel moneda. |
| Kanato de Chagatai | Kanato | Duwa | Asia central; guerras con Yuan e Iljanato. |
| Sultanato de Delhi | Sultanato | Alauddin Khalji | Resiste a los mongoles; reformas de mercado. |
| Reinos del Decán y del sur | Kakatiya, Yadava, Hoysala, Pandya | Prataparudra, Ramachandra, Ballala III, Maravarman Kulasekara I | Serán atacados por Delhi en las décadas siguientes. |
| Japón | Shogunato Kamakura (regencia Hōjō) | Emperador Go-Fushimi; regente Hōjō | Endeudado tras repeler las invasiones mongolas. |
| Goryeo | Monarquía vasalla de Yuan | Chungnyeol | Vasallaje y matrimonios con la casa Yuan. |
| Đại Việt | Monarquía | Trần Anh Tông | Venció a los mongoles en 1288. |
| Champa | Reinos | — | Rival de Đại Việt. |
| Imperio jemer | Monarquía | Indravarman III | Angkor en lento declive. |
| Sukhothai | Reino tai | Loe Thai | Tras Ram Khamhaeng. |
| Lan Na | Reino tai | Mangrai | Fundó Chiang Mai en 1296. |
| Majapahit | Reino javanés | Kertarajasa (Raden Wijaya) | Fundado en 1293; futura talasocracia. |
| Samudera Pasai | Sultanato | — | Islamización del archipiélago. |
| Tíbet | Bajo tutela Yuan (escuela Sakya) | — | Poder religioso-político. |

### Américas

En 1300 no hay contacto con Eurasia. El diseño debe dar a estas sociedades **sistemas propios** (tributo, redes de intercambio, calendarios, guerra ritual, agricultura de chinampas o andenes), no versiones empobrecidas de los europeos.

| Entidad o región | Situación en 1300 | Notas de diseño |
| --- | --- | --- |
| Cuenca de México | Ciudades-Estado: Azcapotzalco (tepanecas), Culhuacán, Texcoco, Xaltocan | Los mexicas aún no han fundado Tenochtitlan (tradicionalmente 1325). |
| Cholula | Gran centro religioso y comercial | Peregrinación y comercio. |
| Purépecha | Señoríos en el lago de Pátzcuaro | Unificación en las décadas siguientes. |
| Mixtecas y zapotecas | Señoríos en Oaxaca | Códices; alianzas matrimoniales. |
| Mayas del Posclásico | Liga de Mayapán | Comercio marítimo de cacao y sal. |
| Chimú | Reino en la costa norte del Perú | Capital Chan Chan; irrigación. |
| Cusco | Señorío local | Los incas aún no se han expandido. |
| Reinos aymaras | Altiplano | Lupaca, Colla. |
| Misisipianos | Cacicazgos (Cahokia en declive) | Montículos; maíz. |
| Pueblos ancestrales | Migraciones por la sequía | Abandono de Mesa Verde. |

### Oceanía

| Entidad o región | Situación | Notas |
| --- | --- | --- |
| Tonga | Esfera de influencia marítima del Tuʻi Tonga | Red de tributo insular. |
| Aotearoa | Asentamiento polinesio reciente | Población pequeña. |
| Australia | Pueblos aborígenes | Modelar como sociedades sin Estado con territorio y cultura. |

### Ampliación del inventario de 1300

Las tablas anteriores recogen las entidades principales. Estas añaden las que completan cada región en la escala L. Donde el gobernante no se indica, se completará en la Biblia histórica.

#### Europa occidental: ducados, condados y reinos menores

| Entidad | Situación en 1300 | Nota de diseño |
| --- | --- | --- |
| Reino de Mallorca | Jaime II de Mallorca, vasallo de Aragón | Reino insular con territorios en el Rosellón y Montpellier. |
| Ducado de Aquitania (Gascuña) | En manos de Eduardo I, vasallo del rey de Francia | Feudo de un rey extranjero: origen de grandes guerras. |
| Ducado de Bretaña | Juan II | Gran vasallo semiautónomo. |
| Ducado de Borgoña | Roberto II | Futuro núcleo de un Estado entre Francia y el Imperio. |
| Condado de Flandes | Ocupado por Francia (1300); conde Guido de Dampierre prisionero | Ciudades textiles que se rebelarán (Courtrai, 1302). |
| Condado de Provenza | De los Anjou de Nápoles | Territorio separado de su soberano por el mar. |
| Condado de Saboya | Amadeo V | Controla pasos alpinos. |
| Delfinado de Vienne | Humberto I | Pasará a Francia en el siglo XIV. |
| Condados de Foix y Bearn | Casa de Foix | Señoríos pirenaicos. |
| Condados de Henao y Holanda | Juan II de Avesnes, unidos desde 1299 | Unión personal en los Países Bajos. |
| Ducado de Brabante | Juan II | Ciudades comerciales (Bruselas, Lovaina, Amberes). |
| Principado-obispado de Lieja | Príncipe-obispo | Entidad eclesiástica soberana. |
| Señorío de las Islas | Señores gaélico-nórdicos | Poder marítimo en las Hébridas. |
| Reinos gaélicos de Irlanda | Reyes y señores locales | Control inglés limitado fuera del Pale. |

#### Sacro Imperio: principados representativos

| Entidad | Tipo | Nota |
| --- | --- | --- |
| Austria y Estiria | Ducados de los Habsburgo | Base del poder del rey de romanos. |
| Baviera | Ducado de los Wittelsbach | Dividido entre ramas. |
| Palatinado del Rin | Electorado Wittelsbach | Uno de los siete electores. |
| Brandeburgo | Margraviato ascanio | Electorado. |
| Sajonia-Wittenberg | Ducado ascanio | Electorado. |
| Maguncia, Colonia, Tréveris | Arzobispados electores | Principados eclesiásticos. |
| Tirol y Carintia | Condados y ducados alpinos | Pasos hacia Italia. |
| Wurtemberg | Condado | Eberhard I. |
| Meissen y Turingia | Margraviato y landgraviato de los Wettin | Minas de plata. |
| Brunswick-Luneburgo | Ducado güelfo | Norte de Alemania. |
| Mecklemburgo y Pomerania | Ducados bálticos | Comercio hanseático. |
| Ducados de Silesia | Ducados piastas | Fragmentados; entre Polonia y Bohemia. |
| Ciudades imperiales | Lübeck, Núremberg, Colonia, Fráncfort, Augsburgo… | Autonomía urbana; muchas en la Hansa. |

En la escala L el Imperio puede tener más de 200 entidades. Se agruparán en las escalas S y M y se mostrarán con un modo de mapa jerárquico.

#### Italia: señorías y comunas

| Entidad | Situación | Nota |
| --- | --- | --- |
| Marquesado de Montferrato | Juan I | Disputas con Saboya y Milán. |
| Marquesado de Saluzzo | Casa de Saluzzo | Pequeño Estado alpino. |
| Verona | Señoría de los Della Scala | Futura potencia regional. |
| Ferrara y Módena | Señoría de los Este (Azzo VIII) | Estado dinástico duradero. |
| Mantua | Señoría de los Bonacolsi | Pasará a los Gonzaga en 1328. |
| Padua | Comuna | Universidad; rival de Verona. |
| Pisa | República en declive tras Meloria (1284) | Pierde el dominio naval ante Génova. |
| Lucca y Siena | Repúblicas | Banca, seda y paño. |
| Bolonia | Comuna en la órbita papal | Universidad más antigua de Europa. |
| Rímini | Señoría de los Malatesta | Romaña fragmentada. |
| Judicado de Arborea | Reino sardo | Resistirá a Aragón durante un siglo. |
| Córcega | Bajo dominio genovés | Revueltas recurrentes. |

#### Europa oriental y Rus

| Entidad | Situación | Nota |
| --- | --- | --- |
| Reino de Galitzia-Volinia | Yuri I | Entre la Horda, Polonia, Hungría y Lituania. |
| Principado de Tver | Miguel Yaroslávich | Rival principal de Moscú por el título de gran príncipe. |
| Principados de Riazán y Smolensk | Príncipes de la casa de Rurik | Frontera con la estepa y con Lituania. |
| República de Pskov | Autonomía respecto a Nóvgorod | Comercio y defensa frente a la Orden Livonia. |
| Confederación livonia | Orden Livonia y obispados | Tierras bálticas cruzadas. |
| Ducados de Mazovia y Cuyavia | Piastas | Polonia fragmentada. |
| Pomerelia | Disputada | La Orden Teutónica la tomará en 1308. |
| Croacia | Unida a Hungría; banes Šubić (Pablo I) | Poder nobiliario casi independiente. |
| Banato de Bosnia | Bajo la influencia de los Šubić | Iglesia bosnia propia. |

#### Mundo islámico, Cáucaso y África: ampliación

| Entidad | Situación | Nota |
| --- | --- | --- |
| Reino de Georgia | Dividido bajo dominio iljánida | Reunificación posible en el siglo XIV. |
| Kartíes de Herat | Vasallos del Iljanato | Dinastía persa local. |
| Ormuz | Reino comercial del golfo Pérsico | Llave del comercio con la India. |
| Rasúlidas de Yemen | Sultanato (al-Muayyad Dawud) | Comercio del mar Rojo. |
| Omán | Imamato ibadí y señoríos costeros | Navegación del Índico. |
| Jerifato de La Meca | Bajo protección mameluca | Autoridad religiosa y peregrinación. |
| Emiratos kurdos | Señoríos de montaña | Autonomía entre grandes imperios. |
| Sultanato de Ifat | Sultanato musulmán | Rival de Etiopía. |
| Mogadiscio | Ciudad-Estado | Comercio índico. |
| Gao | Bajo dominio de Malí | Núcleo del futuro Imperio songhai. |
| Ciudades hausa (Kano, Katsina, Zaria) | Ciudades-Estado | Comercio transahariano oriental. |
| Takrur | Reino del río Senegal | Islamización temprana. |
| Reino de Benín | Monarquía del oba | Arte en bronce, comercio regional. |
| Alwa | Reino cristiano nubio | Sur de Makuria. |
| Pueblos del Kongo | Señoríos sin unificar | El reino del Kongo surgirá a finales del siglo XIV. |

#### Asia: ampliación

| Entidad | Situación | Nota |
| --- | --- | --- |
| Ranthambore | Reino rajput (Hammir Dev) | Caerá ante Delhi en 1301. |
| Mewar | Reino rajput | Resistencia duradera. |
| Gujarat | Conquistado por Delhi en 1299 | Puertos clave del Índico. |
| Bengala | Gobernadores semiautónomos de Delhi | Riqueza agrícola; independencia en el siglo XIV. |
| Ganga orientales (Orissa) | Reino hindú | Templos y comercio marítimo. |
| Reino ahom | Valle del Brahmaputra | Fundado en 1228; durará siglos. |
| Valle de Katmandú | Reyes Malla | Ciudades newar. |
| Jaffna | Reino tamil del norte de Sri Lanka | Comercio de perlas. |
| Reino cingalés | Capitales móviles (Yapahuwa, Kurunegala) | Budismo theravada. |
| Maldivas | Sultanato | Conchas de cauri como moneda. |
| Myinsaing | Tres hermanos tras el colapso de Pagan | Sucesión birmana fragmentada. |
| Martaban (Ramanya) | Reino mon de Wareru | Costa birmana. |
| Arakán | Reino costero | Entre Bengala y Birmania. |
| Champa | Jaya Sinhavarman III | Guerras con Đại Việt. |
| Dharmasraya (Malayu) | Reino de Sumatra | Sucesor de Srivijaya. |
| Brunéi y Butuan | Señoríos comerciales | Comercio con China. |
| Okinawa | Jefaturas que darán lugar a tres reinos | Comercio entre China y Japón. |
| Ainu | Sociedades de Hokkaido | Fuera del control japonés. |
| Uigures de Qocho | Bajo dominio Yuan | Budismo y comercio de la Ruta de la Seda. |
| Kanato ogodeí | Kaidu (muere en 1301) | Guerra contra Yuan; absorbido por Chagatai. |

#### Américas: ampliación

| Entidad | Región | Nota |
| --- | --- | --- |
| Tlaxcallan | Altiplano central | Confederación de señoríos; rival de los futuros mexicas. |
| Huexotzinco | Altiplano poblano | Potencia regional en los siglos XIV y XV. |
| Xaltocan | Norte de la cuenca | Señorío otomí. |
| Chalco y Xochimilco | Sur de la cuenca | Chinampas y agricultura intensiva. |
| Totonacapan | Costa del Golfo | Centro en Cempoala. |
| Señoríos huastecos | Golfo norte | Algodón y comercio. |
| Tututepec | Costa de Oaxaca | Señorío mixteco expansivo. |
| Zaachila | Valles centrales de Oaxaca | Señorío zapoteco. |
| K'iche', kaqchikel, tz'utujil, mam | Altos de Guatemala | Reinos mayas rivales. |
| Pipiles y lencas | Centroamérica | Cacao y comercio. |
| Cacicazgos taínos | Antillas mayores | Sociedades jerarquizadas. |
| Muiscas | Altiplano colombiano | Zipa y zaque; oro y sal. |
| Chincha | Costa sur del Perú | Comercio marítimo. |
| Ychsma | Costa central del Perú | Santuario de Pachacamac. |
| Chancas | Sierra central | Rivales de Cusco. |
| Cañaris y quitus | Andes del norte | Señoríos que resistirán la expansión inca. |
| Diaguitas y mapuches | Andes del sur | Sociedades agrícolas y guerreras. |
| Tupinambá y guaraníes | Costa y cuencas del Brasil y Paraguay | Aldeas y migraciones. |
| Calusa | Florida | Sociedad compleja basada en la pesca. |
| Moundville y Etowah | Sureste norteamericano | Cacicazgos misisipianos. |
| Hohokam | Desierto de Sonora | Canales de riego. |
| Naciones iroquesas | Noreste | Antes de su confederación. |
| Thule (inuit) | Ártico | Expansión hacia el este; contacto con los nórdicos de Groenlandia. |

### Entidades históricas por época (referencia)

Estas listas no son estados iniciales ni guiones. Son la **referencia** con la que 101 Lab compara el modo histórico estricto, y el catálogo de identidades, nombres y banderas que el motor puede usar si una entidad similar surge en la partida.

#### Hacia 1450

| Región | Entidades |
| --- | --- |
| Europa occidental | Francia, Inglaterra, Escocia, Castilla, Aragón, Portugal, Navarra, Granada, Estado borgoñón, Bretaña. |
| Europa central | Sacro Imperio (Habsburgo), Bohemia, Hungría, Polonia, Lituania, Confederación suiza, Orden Teutónica, Hansa. |
| Italia | Venecia, Milán (Sforza desde 1450), Florencia (Médici), Nápoles (Aragón), Estados Pontificios, Saboya, Génova. |
| Norte y este | Unión de Kalmar, Moscovia, Nóvgorod, Tver, Gran Horda, Kanato de Crimea (desde 1441), Kanato de Kazán (desde 1438). |
| Balcanes y Anatolia | Bizancio, despotado de Morea, despotado serbio, Bosnia, Valaquia, Moldavia, Albania (Skanderbeg), Imperio otomano, Karamán, Trebisonda. |
| Mundo islámico | Mamelucos, Kara Koyunlu, Ak Koyunlu, Timúridas, Uzbekos, Nogai, Marruecos (benimerines y wattásidas), Hafsíes. |
| Asia meridional | Sultanato de Delhi (lodi desde 1451), Bahmaníes, Vijayanagara, Gujarat, Bengala, Malwa, Jaunpur. |
| Asia oriental | Ming, Joseon, Japón (shogunato Ashikaga), Ryukyu, Đại Việt (Lê), Champa. |
| Sudeste asiático | Ayutthaya, Lan Xang, Lan Na, Ava, Hanthawaddy, Malaca, Majapahit, Pasai, Brunéi. |
| África | Songhai, Malí, Kanem-Bornu, ciudades hausa, Benín, Oyo, Kongo, Etiopía, Adal, Kilwa, Mutapa. |
| Américas | Triple Alianza mexica, Tlaxcallan, Purépecha, Tututepec, reinos mayas, Tawantinsuyu, Chimú. |

#### Hacia 1600

| Región | Entidades |
| --- | --- |
| Europa | Monarquía Hispánica (con Portugal desde 1580), Francia, Inglaterra, Escocia, Provincias Unidas, Sacro Imperio, Austria, Polonia-Lituania, Suecia, Dinamarca-Noruega, Rusia, Venecia, Toscana, Saboya, Estados Pontificios. |
| Mundo islámico | Imperio otomano, Persia safávida, Kanato de Bujará, Kanato de Crimea, Marruecos saadí. |
| Asia | Imperio mogol, sultanatos del Decán, Ming, Joseon, Japón (unificación Toyotomi y Tokugawa), Ayutthaya, Toungoo, Aceh, Mataram, Johor. |
| África | Kanem-Bornu, Kongo, Etiopía, Mutapa, Oyo; caída de Songhai (1591). |
| Américas | Virreinatos de Nueva España y del Perú, Brasil portugués, pueblos independientes del norte y del sur. |

#### Hacia 1750

| Región | Entidades |
| --- | --- |
| Europa | Gran Bretaña, Francia, España, Portugal, Provincias Unidas, Monarquía de los Habsburgo, Prusia, Sajonia, Baviera, Polonia-Lituania, Rusia, Suecia, Dinamarca-Noruega, Venecia, Cerdeña-Piamonte, Nápoles. |
| Mundo islámico | Imperio otomano, Persia (afsharíes y zand), Imperio durrani (desde 1747), Marruecos alauí. |
| Asia meridional | Mogoles en declive, Confederación maratha, Hyderabad, Bengala, Mysore. |
| Asia oriental y sudeste | Qing, Joseon, Japón Tokugawa, Ayutthaya, Konbaung (desde 1752), Vietnam dividido (Trịnh y Nguyễn). |
| África | Ashanti, Dahomey, Oyo, Etiopía, Estados del Sahel. |
| Américas | Trece Colonias, Nueva Francia, virreinatos españoles, Brasil. |

#### Hacia 1850

| Región | Entidades |
| --- | --- |
| Europa | Reino Unido, Francia, España, Portugal, Bélgica, Países Bajos, Prusia, Austria, Confederación Germánica, Cerdeña-Piamonte, Dos Sicilias, Estados Pontificios, Suiza, Dinamarca, Suecia-Noruega, Rusia, Grecia, Serbia autónoma. |
| Mundo islámico | Imperio otomano, Egipto de Mehmet Alí, Persia qayar, Afganistán, Marruecos. |
| Asia | India bajo la Compañía británica, Qing, Japón, Siam, Vietnam (Nguyễn), Birmania. |
| África | Etiopía, Califato de Sokoto, reino zulú, Madagascar, Liberia, Estados del Sahel. |
| Américas | Estados Unidos, México, Imperio del Brasil, Confederación Argentina, Chile, Perú, Bolivia, Nueva Granada, Venezuela, Ecuador, Paraguay, Uruguay, Centroamérica, Haití, República Dominicana. |
| Oceanía | Reino de Hawái, Tonga, colonias británicas en Australia y Nueva Zelanda. |

#### Hacia 1914

| Región | Entidades |
| --- | --- |
| Europa | Reino Unido, Francia, Alemania, Austria-Hungría, Rusia, Italia, España, Portugal, Bélgica, Países Bajos, Suiza, Suecia, Noruega, Dinamarca, Serbia, Montenegro, Bulgaria, Rumanía, Grecia, Albania. |
| Asia y mundo islámico | Imperio otomano, Persia, Afganistán, China republicana, Japón, Siam, imperios coloniales. |
| África | Etiopía, Liberia; el resto bajo dominio colonial. |
| Américas | Estados Unidos, México en revolución, Brasil, Argentina, Chile, Perú, Colombia, Venezuela, Cuba y el resto de repúblicas. |

#### Hacia 1950

| Región | Entidades y bloques |
| --- | --- |
| Bloques | Estados Unidos y aliados; URSS y Estados satélites; movimiento de descolonización. |
| Europa | Alemania Occidental y Oriental, Yugoslavia, Estados de Europa occidental y del Este. |
| Asia | República Popular China, Taiwán, India, Pakistán, Indonesia, Corea del Norte y del Sur, Japón, Filipinas, Israel, Estados árabes. |
| África y Américas | Primeras independencias africanas en la década siguiente; repúblicas americanas consolidadas. |

#### Hacia 2026

193 Estados miembros de las Naciones Unidas más territorios de estatus disputado. Se cargan como **referencia de identidades** (nombres, banderas, instituciones), no como mundo inicial.

### Dimensión del contenido

| Ámbito | Entidades soberanas aproximadas en 1300 | Prioridad |
| --- | --- | --- |
| Mediterráneo oriental y Balcanes | 20–25 | Vertical slice. |
| Resto de Europa | 60–80 (más cientos dentro del Imperio) | Primera expansión. |
| Mundo islámico y África | 40–60 | Primera expansión (norte) y segunda (subsahariana). |
| Asia | 40–60 | Segunda expansión. |
| Américas y Oceanía | 30–50 | Tercera expansión, con sistemas propios. |

**Entidades no estatales:** pueblos nómadas, sociedades tribales y territorios sin Estado se representan como **entidades sociales** con población, cultura y control sobre su territorio, aunque no tengan soberanía formal. No hay “tierra vacía” donde vive gente.

## 06. Culturas, idiomas y religiones

### Modelo

La identidad de una cohorte tiene varias dimensiones independientes:

| Dimensión | Estructura | Ejemplo |
| --- | --- | --- |
| Cultura | Cultura → grupo cultural → familia | Castellano → ibérico → latino-romance |
| Idioma | Idioma → rama → familia | Castellano → iberorromance → indoeuropeo |
| Religión | Confesión → rama → familia | Ortodoxa griega → cristianismo oriental → cristianismo |
| Identidad política | Lealtades a dinastía, ciudad, reino, nación | “Romano” (bizantino), “veneciano”, “osmanlí” |
| Estrato | Ocupación y nivel de vida | Campesino, mercader, noble |

Cultura e idioma se separan porque no siempre coinciden: la élite bizantina habla griego y se considera “romana”; en el Egipto mameluco la élite militar es de origen túrquico o circasiano, y la mayoría habla árabe.

### Rasgos culturales

Cada cultura tiene **rasgos** que modifican comportamientos, no números fijos para siempre: tradición marítima, pastoralismo, tradición escrita, estructura familiar, prácticas de herencia, tradición militar (caballería, infantería, arquería a caballo), artesanías. Los rasgos cambian lentamente según las condiciones: una cultura que pasa tres siglos en ciudades portuarias adquiere tradición marítima.

### Procesos culturales

| Proceso | Factores | Resultado |
| --- | --- | --- |
| Asimilación | Prestigio, integración económica, educación, matrimonios mixtos, política estatal. | Una cohorte cambia de cultura gradualmente. |
| Resistencia | Densidad cultural, instituciones propias, religión distinta, represión. | Frena la asimilación; puede generar movimientos. |
| Hibridación | Contacto prolongado y fronteras culturales. | Surge una cultura nueva (p. ej. comunidades mixtas del Levante franco). |
| Diáspora | Migración, comercio, persecución. | Cohortes fuera de su región de origen con redes propias. |
| Estandarización lingüística | Imprenta, escuelas, burocracia, prensa. | Idiomas regionales absorbidos o revitalizados. |
| Nacionalismo | Alfabetización, prensa, guerra de masas, opresión percibida. | Identidad nacional como lealtad dominante (siglos XVIII–XX en adelante). |

### Grupos culturales iniciales (escala L)

| Región | Grupos culturales principales en 1300 |
| --- | --- |
| Iberia | Castellano, leonés-asturiano, gallego-portugués, catalán, aragonés, vasco, andalusí (árabe hispano), mozárabe (residual), judío sefardí. |
| Francia y Países Bajos | Francés (norte), occitano, bretón, normando, flamenco, valón, picardo. |
| Islas británicas | Inglés, escocés de las tierras bajas, gaélico escocés, irlandés, galés, córnico, anglonormando (élite). |
| Italia | Toscano, véneto, lombardo, ligur, romano, napolitano, siciliano, sardo, friulano. |
| Mundo germánico | Alto alemán (bávaro, alemánico, franconio), bajo alemán, neerlandés, frisón, alemán del Báltico. |
| Escandinavia | Danés, sueco, noruego, islandés, sami. |
| Europa centro-oriental | Polaco, checo, eslovaco, húngaro (magiar), esloveno, croata, judío asquenazí. |
| Rus y estepa | Ruso antiguo (Nóvgorod, Vladímir-Súzdal, Kiev), lituano, letón, prusiano antiguo, fino-úgricos, kipchak, tártaro. |
| Balcanes | Griego (romeo), serbio, búlgaro, albanés, valaco (arrumano), bosnio, raguseo (dálmata/croata). |
| Anatolia y Cáucaso | Turco oguz, griego anatolio, armenio, georgiano, kurdo, laz. |
| Mundo árabe | Árabe egipcio, levantino, iraquí, hiyazí, magrebí; beduino; copto; siríaco. |
| Magreb y Sahara | Bereberes (zenata, sanhaya, masmuda), tuareg, árabe hilaliano. |
| Irán y Asia central | Persa, tayiko, kurdo, baluchi, uzbeko-túrquico, mongol. |
| África occidental | Mandinga, soninké, wolof, songhay, hausa, kanuri, yoruba, edo, igbo, akan. |
| África oriental y austral | Amhara, tigray, oromo, somalí, swahili, nubio, shona, kongo. |
| Subcontinente indio | Indostaní, punyabí, bengalí, guyaratí, marathi, telugu, kannada, tamil, malayalam, cingalés, rajputs (como identidad). |
| China y Asia oriental | Han (con subgrupos regionales), mongol, yurchen, tibetano, uigur, coreano, japonés, ryukyuense. |
| Sudeste asiático | Vietnamita (kinh), cham, jemer, tai (siamés, lao, shan), birmano, mon, javanés, malayo, sundanés, filipinos. |
| Mesoamérica | Nahua (tepaneca, acolhua, mexica, chalca, tlaxcalteca), otomí, purépecha, mixteco, zapoteco, totonaca, huasteco, maya yucateco, maya k'iche', kaqchikel. |
| Andes y Sudamérica | Quechua, aymara, mochica-chimú, mapuche, guaraní, arawak, tupí. |
| Norteamérica | Misisipianos, pueblos ancestrales, iroqueses, algonquinos, sioux, inuit. |
| Oceanía | Polinesio (tongano, samoano, maorí, hawaiano), melanesio, aborígenes australianos. |

### Religiones iniciales

| Familia | Ramas y confesiones en 1300 |
| --- | --- |
| Cristianismo | Católica latina; ortodoxa (patriarcados de Constantinopla, Alejandría, Antioquía, Jerusalén; Iglesias búlgara y serbia); armenia apostólica; copta y etíope (miafisitas); siríaca occidental; Iglesia del Oriente (presente en Asia central y China); movimientos disidentes (cátaros en extinción, valdenses, bogomilos). |
| Islam | Sunismo (escuelas hanafí, malikí, shafií, hanbalí); chiismo (duodecimano, ismailí nizarí y mustalí, zaydí); ibadismo; órdenes sufíes como redes sociales. |
| Judaísmo | Rabínico (sefardí, asquenazí, romaniote, mizrají); caraíta. |
| Religiones de la India | Hinduismo (shivaísmo, vishnuismo, shaktismo, bhakti emergente); jainismo; budismo residual. |
| Budismo | Theravada (Sri Lanka, sudeste asiático continental); Mahayana (China, Corea, Japón, Vietnam); Vajrayana (Tíbet, Mongolia). |
| Asia oriental | Confucianismo (como sistema ético-estatal), taoísmo, religión popular china, sintoísmo. |
| Irán | Zoroastrismo (minoritario). |
| Tradicionales | Tengrismo y chamanismo de la estepa; paganismo báltico (Lituania); religiones tradicionales africanas; religiones mesoamericanas; religión andina; religiones de Norteamérica y Oceanía. |

### Grupos culturales adicionales (escala L)

| Región | Grupos |
| --- | --- |
| Cáucaso | Georgianos (kartlianos, imeretios, mingrelios), osetios, circasianos, abjasios, chechenos, ávaros, lezguinos. |
| Siberia y norte | Yakutos, evenkos, samoyedos, janti, mansi, chukchis. |
| Estepa y Asia central | Kipchak, kankali, karluk, kirguís, mongoles occidentales, tayikos de montaña. |
| Cuerno de África | Afar, agaw, sidama, harari, beja. |
| Sahel y África occidental | Fulani, tukulor, bambara, dogon, mossi, serer, susu, kru. |
| África central y austral | Luba, lunda, tío, kikuyu, sukuma, nguni, sotho, tswana, herero, joisán. |
| Océano Índico | Malgache, comorense, swahili de la costa. |
| Himalaya | Newar, khas, lepcha, bhutia. |
| Archipiélago malayo | Buguis, makasar, minangkabau, balineses, moluqueños, dayak. |
| Filipinas | Tagalo, visaya, ilocano, maguindanao, tausug. |
| Norteamérica | Pueblos de la costa del Pacífico (haida, tlingit), llanuras, algonquinos del noreste, muscogui, cheroqui. |
| Sudamérica | Arawak amazónicos, caribes, pueblos del Chaco, tehuelches, yámanas. |

### Familias lingüísticas

| Familia | Ramas relevantes en 1300 |
| --- | --- |
| Indoeuropea | Romance, germánica, eslava, báltica, celta, griega, albanesa, armenia, iraní, indoaria. |
| Túrquica | Oguz, kipchak, karluk, chuvasia. |
| Mongólica | Mongol, oirate. |
| Urálica | Fino-úgrica (húngaro, finés, estonio), samoyeda. |
| Afroasiática | Semítica (árabe, hebreo, arameo, amhárico), bereber, cushítica, chádica (hausa), copta. |
| Kartveliana | Georgiano, mingrelio, laz. |
| Nigerocongolesa | Mande, atlántica, kwa, yoruboide, edoide, bantú. |
| Nilo-sahariana | Kanuri, songhay, nubio, nilóticas. |
| Sinotibetana | Chino (variedades), tibetano, birmano. |
| Austroasiática | Jemer, mon, vietnamita. |
| Tai-kadai | Siamés, lao, shan, tai ahom. |
| Austronesia | Malayo, javanés, cham, malgache, filipinas, polinesias. |
| Dravídica | Tamil, telugu, kannada, malayalam. |
| Japónica y coreana | Japonés, ryukyuense; coreano. |
| Aisladas | Vasco, ainu, burushaski. |
| Americanas | Uto-azteca (náhuatl), otomangue (mixteco, zapoteco, otomí), maya, purépecha (aislada), quechua, aimara, tupí-guaraní, arawak, caribe, iroquesa, algonquina, esquimo-aleutiana. |
| Australianas | Pama-ñungana y otras. |

El idioma determina la **inteligibilidad mutua** (que facilita la asimilación y el comercio), la **lengua de administración** (que exige letrados) y la **toponimia** de cada cultura.

### Catálogo de rasgos culturales

| Rasgo | Efecto sistémico |
| --- | --- |
| Tradición marítima | Mejores tripulaciones, astilleros y comercio naval. |
| Tradición ecuestre | Caballería más barata y eficaz; movilidad en la estepa. |
| Pastoralismo nómada | Población móvil, difícil de gravar y de conquistar; ejércitos rápidos. |
| Agricultura intensiva de regadío | Alta densidad de población; dependencia de obras hidráulicas. |
| Tradición urbana | Gremios, mercados y élites urbanas con poder político. |
| Tradición escrita y burocrática | Mayor capacidad del Estado; registros fiscales. |
| Tradición oral | Menor coste de élites letradas; transmisión más lenta del saber técnico. |
| Herencia partible | Fragmentación de tierras y de reinos. |
| Primogenitura | Concentración del patrimonio; conflicto entre hermanos menores. |
| Linajes extensos (clanes) | Lealtades fuertes de clan; difícil integración en el Estado. |
| Tradición mercantil | Mejores redes de crédito y comercio a distancia. |
| Tradición de mercenariado | Oferta de soldados profesionales para otros Estados. |
| Tradición fronteriza | Bonos de guerra irregular; economía de botín. |
| Arquitectura defensiva | Fortificaciones más baratas o eficaces. |
| Artesanía especializada | Calidad en bienes concretos (seda, vidrio, metal, cerámica). |
| Tradición jurídica codificada | Justicia más previsible; atrae comercio. |
| Hospitalidad y patronazgo | Relaciones clientelares; corrupción y lealtad personal. |
| Sincretismo religioso | Menor resistencia a la conversión; hibridación cultural. |
| Identidad diaspórica | Redes transregionales; vulnerabilidad a la persecución. |
| Tradición de asambleas | Base para instituciones representativas. |

Los rasgos no son esencias permanentes: aparecen y desaparecen con las condiciones materiales y se describen siempre como **tradiciones sociales**, nunca como capacidades innatas de un pueblo.

### Rasgos doctrinales de las religiones

| Rasgo | Opciones | Efecto |
| --- | --- | --- |
| Autoridad | Centralizada, sinodal, local, ninguna | Capacidad de imponer ortodoxia; riesgo de cisma. |
| Clero | Celibato, clero casado, sin clero profesional | Propiedad de la Iglesia; transmisión de cargos. |
| Relación con el Estado | Teocracia, iglesia de Estado, separación | Legitimidad del gobernante. |
| Préstamo con interés | Prohibido, restringido, permitido | Desarrollo bancario; papel de minorías. |
| Proselitismo | Activo, pasivo, cerrado | Velocidad de conversión. |
| Tolerancia doctrinal | Alta, media, baja | Estabilidad con minorías. |
| Monacato | Fuerte, débil, ausente | Tierras eclesiásticas, saber, caridad. |
| Peregrinación | Obligatoria, valorada, ausente | Flujos de personas, dinero y contagio. |
| Lengua sagrada | Única, vernácula permitida | Alfabetización y difusión de textos. |
| Guerra santa | Doctrina activa, condicional, ausente | Motivos de guerra disponibles. |
| Ley religiosa | Integral, parcial, ausente | Instituciones de justicia y comercio. |
| Escatología | Mesiánica, cíclica, ninguna | Movimientos milenaristas en crisis. |

### Fichas culturales de la vertical

| Cultura | Idioma | Religión mayoritaria | Núcleo en 1300 | Rasgos | Nota de diseño |
| --- | --- | --- | --- | --- | --- |
| Griego (romeo) | Griego medieval | Ortodoxa | Constantinopla, Tracia, Tesalónica, Morea, Epiro, costas de Anatolia | Tradición urbana, escrita y burocrática, marítima | Se considera heredera de Roma; identidad “romana”, no étnica. |
| Turco oguz | Turco anatolio | Suní hanafí; órdenes sufíes | Anatolia central y occidental | Tradición fronteriza, ecuestre | Mezcla de guerreros de frontera, derviches y población convertida. |
| Turcomano nómada | Turco oguz | Suní con prácticas populares | Mesetas y pastos de Anatolia | Pastoralismo nómada, ecuestre | Difícil de gravar; fuente de soldados y de inestabilidad. |
| Serbio | Serbio antiguo | Ortodoxa (Iglesia serbia) | Raška, Zeta, Macedonia norte | Tradición fronteriza, monacato fuerte | Dinastía Nemanjić y monasterios como pilares. |
| Búlgaro | Búlgaro medio | Ortodoxa (patriarcado de Tarnovo) | Bulgaria danubiana | Tradición escrita eslava | Memoria imperial; presión mongola. |
| Albanés | Albanés | Católica y ortodoxa | Montañas del Epiro y Albania | Linajes extensos, mercenariado | Clanes con gran autonomía; soldados para otros Estados. |
| Valaco (arrumano) | Romance balcánico | Ortodoxa | Tesalia, Pindo, Danubio | Pastoralismo trashumante | Disperso; base de los futuros principados rumanos. |
| Húngaro | Magiar | Católica | Llanura panónica | Tradición ecuestre, asambleas nobiliarias | Nobleza con fuerte poder político. |
| Veneciano | Véneto | Católica | Venecia, Creta, Negroponte | Tradición mercantil, marítima, jurídica | Élite colonial reducida sobre poblaciones griegas. |
| Genovés (ligur) | Ligur | Católica | Génova, Pera, Caffa, Chíos (desde 1304) | Tradición mercantil, marítima | Facciones familiares; empresas privadas coloniales. |
| Franco de Morea | Francés y griego | Católica | Acaya, Atenas | Tradición caballeresca, arquitectura defensiva | Élite feudal latina sobre población griega. |
| Catalán | Catalán | Católica | Corona de Aragón; Compañía en Oriente | Mercenariado, marítima | La Compañía Catalana como entidad sin territorio. |
| Armenio | Armenio | Iglesia armenia | Cilicia, Anatolia oriental | Tradición mercantil, diaspórica | Redes comerciales desde Tabriz a Crimea. |
| Judío romaniote | Judeogriego | Judaísmo | Ciudades bizantinas | Identidad diaspórica, tradición escrita | Comunidades urbanas con autonomía comunitaria. |
| Tártaro (kipchak) | Kipchak | Islam en expansión; tengrismo residual | Estepa póntica, Crimea | Pastoralismo nómada, ecuestre | Base de la Horda de Oro; comercio de Caffa. |
| Laz y griego póntico | Laz; griego | Ortodoxa | Trebisonda y costa del mar Negro | Marítima, montañesa | Base del Imperio de Trebisonda. |

### Mecánica religiosa

- **Doctrina como conjunto de rasgos** (jerarquía clerical, autoridad central, actitud ante el préstamo con interés, proselitismo, relación con el Estado). Cambiar rasgos crea movimientos de reforma o cismas.
- **Cismas y reformas emergentes:** una “reforma” aparece cuando coinciden corrupción percibida del clero, nuevas formas de difusión (imprenta), alfabetización y príncipes con interés en romper con la autoridad religiosa. No existe un evento “Reforma protestante en 1517”: existe la posibilidad de que algo así ocurra.
- **Tolerancia y minorías:** cada Estado tiene una política religiosa (oficial, tolerada, discriminada, perseguida) con efectos sobre la estabilidad, la migración (diásporas) y la economía.
- **Autoridades religiosas como actores:** el papado, los patriarcados, el califato abasí de El Cairo (bajo los mamelucos) y otros pueden ser actores diplomáticos con intereses propios.

### Especificación detallada de cultura y religión (v0.7, propuesto)

Base de `docs/specs/culture-religion.md`.

#### Asimilación cultural: parámetros

```text
asimilación_mensual = cohorte × 0,0012 × prestigio × integración × contacto ÷ resistencia
```

*Comprobación:* una cohorte del 5 % sin instituciones propias (prestigio 1,3; integración 0,6; contacto 0,9; resistencia 1,1) pierde un 0,9 % anual, la mitad en unos 75 años; una cohorte mayoritaria del 70 % con religión e instituciones propias (integración 0,3; contacto 0,3; resistencia 5,9) pierde un 0,03 % anual, menos del 6 % en dos siglos.

| Factor | Cálculo | Rango |
| --- | --- | --- |
| Prestigio de la cultura dominante | 1,0 base; +0,3 si es la de la corte; +0,2 si es lengua de administración; +0,2 si tiene tradición escrita y la otra no | 0,5–2,0 |
| Integración económica | Cuota de los ingresos de la cohorte que provienen de intercambios con la cultura dominante | 0,1–1,0 |
| Contacto | Cuota de la cultura dominante en la provincia (mínimo 0,05) | 0,05–1,0 |
| Resistencia | 1 + densidad cultural (cuota propia en la provincia × 2) + religión distinta (+1,5) + instituciones propias (+1 por escuela, tribunal o clero propio) + represión percibida (+1) | 1–8 |

Con estos valores, una cohorte pequeña de una cultura sin instituciones, rodeada por la dominante, se asimila en unas tres o cuatro generaciones; una cohorte mayoritaria con religión e iglesia propias apenas se asimila en siglos. Las élites conquistadoras minoritarias pueden asimilarse **hacia** la mayoría si la cultura mayoritaria tiene más prestigio local (el caso de muchas élites de frontera).

**Hibridación (F-CUL-03):** si dos culturas conviven en una provincia con cuotas entre el 30 % y el 70 % durante más de 80 años, con matrimonios mixtos permitidos y sin persecución, se evalúa la aparición de una cultura híbrida; si se crea, hereda rasgos de ambas y se registra como nueva identidad con nombre generado y editable.

#### Conversión religiosa: parámetros

```text
conversión_mensual = cohorte × 0,0003 × ventaja_legal × presión_social × proselitismo × presencia_institucional
                     ÷ resistencia_religiosa
```

| Factor | Valores |
| --- | --- |
| Ventaja legal | 1,0 si no hay diferencia; 1,5 si la religión del Estado exime de un impuesto (por ejemplo, capitación de no musulmanes); 2,0 si da acceso a cargos y tierras |
| Presión social | 0,5 + cuota de la religión de destino en la provincia |
| Proselitismo (rasgo doctrinal) | Activo 1,5; pasivo 1,0; cerrado 0,2 |
| Presencia institucional | 1 + 0,2 × instituciones de la religión de destino (mezquitas, monasterios, órdenes sufíes, misiones) en la provincia |
| Resistencia religiosa | 1 + 2 × (instituciones propias activas) + 1 si la jerarquía propia está cerca (patriarcado, sede episcopal) + 1 si hay persecución (efecto de martirio) |

**Ingresos frente a conversión.** Cuando la religión dominante cobra un impuesto a los no creyentes, la conversión reduce los ingresos del Estado: el jugador ve en el “¿por qué?” de sus ingresos que la islamización de Anatolia (o la cristianización de una frontera) tiene un coste fiscal, y puede elegir políticas que la aceleren o la frenen.

#### Políticas religiosas del Estado

| Política | Legitimidad de los fieles de la religión oficial | Legitimidad de las minorías | Conversión hacia la oficial | Emigración de minorías | Ingresos | Riesgo |
| --- | --- | --- | --- | --- | --- | --- |
| Religión oficial con tolerancia y autonomía comunitaria (tipo *millet*) | +0 | +5 | × 1,0 | × 0,5 | Impuesto a minorías posible | Bajo |
| Religión oficial con tolerancia simple | +0 | 0 | × 1,0 | × 1,0 | — | Bajo |
| Discriminación legal (cargos, tierras) | +3 | −15 | × 1,8 | × 1,5 | + (confiscaciones puntuales) | Medio: agravio |
| Persecución | +5 (con fieles fanáticos +10) | −35 | × 2,5 (con huida y resistencia) | × 4,0 | Pérdida de cohortes productivas | Alto: rebeliones, apoyo exterior, diásporas |
| Expulsión | +5 | — | — | Cohortes enteras en 1–3 años | Pérdida inmediata de población y capital | Muy alto |

Las expulsiones y persecuciones siguen la política de contenido sensible de la sección 09: tienen costes humanos visibles, dejan memoria (agravio de la diáspora durante siglos) y nunca se presentan como una mejora sin contrapartida.

#### Autoridades religiosas como actores

| Autoridad (1300) | Recursos | Herramientas | Intereses |
| --- | --- | --- | --- |
| Papado | Rentas eclesiásticas, red episcopal, legitimidad | Excomunión, interdicto, convocatoria de cruzada, dispensas matrimoniales, arbitraje | Autoridad sobre la Iglesia latina, Estados Pontificios, unión con Oriente bajo primacía romana |
| Patriarcado de Constantinopla | Monasterios, legitimidad ortodoxa | Condena, legitimación del emperador, unión o rechazo de la unión | Independencia frente a Roma; propiedad monástica |
| Patriarcados y Iglesias autocéfalas (Tarnovo, Peć más tarde) | Clero nacional | Legitimación de monarcas propios | Autocefalia, prestigio |
| Califato abasí de El Cairo | Legitimidad simbólica | Investidura de sultanes | Protección mameluca |
| Órdenes sufíes | Redes de *tekkes*, discípulos | Apoyo a gobernantes de frontera, conversión | Patronazgo, tierras (*waqf*) |
| Órdenes militares (Hospitalarios, Teutónicos) | Encomiendas, castillos, flota | Guerra santa, préstamos | Supervivencia de la orden, misión |

Cada autoridad tiene IA propia con una utilidad simplificada (sección 17) y puede ser un actor de la diplomacia: una excomunión baja la legitimidad del excomulgado con su clero (−15) y sus fieles (−5), y da casus belli a terceros con interés.

#### Emergencia de reformas y cismas

```text
presión_de_reforma (por confesión y región, 0–100) =
      25 × corrupción_percibida_del_clero (riqueza del clero / riqueza media, simonía, pluralidad de cargos)
    + 20 × alfabetización de las cohortes urbanas
    + 20 × difusión de textos (imprenta, traducciones vernáculas)
    + 20 × interés de príncipes (confiscación posible de tierras eclesiásticas / ingresos del Estado)
    + 15 × crisis (epidemias, guerras, cisma de la autoridad central)
```

| Umbral | Efecto |
| --- | --- |
| > 40 | Aparecen predicadores y movimientos (personajes generados) con un programa doctrinal: cambiar uno o varios rasgos de la confesión. |
| > 60 | Un príncipe o una ciudad puede adoptar el movimiento como política del Estado; se crea una **confesión nueva** con los rasgos cambiados. |
| > 80 | Guerras de religión probables: las situaciones genéricas de guerra religiosa se activan con los actores que correspondan. |

La autoridad central puede reducir la presión con reformas internas (menos corrupción, concilios), con represión (efectiva a corto plazo, con mártires) o con concesiones a los príncipes. Así, una “Reforma” puede nacer en Bohemia en 1410, en el norte de Alemania en 1520, en otro lugar o no nacer, según las condiciones.

#### Pruebas específicas

| Prueba | Criterio |
| --- | --- |
| `assimilation_generations` | Una cohorte del 5 % sin instituciones propias pierde más de la mitad de su tamaño por asimilación en 60–120 años. |
| `majority_resists` | Una cohorte del 70 % con religión distinta e instituciones propias se asimila menos de un 10 % en 200 años. |
| `conversion_tax_link` | Cuando la conversión reduce la base del impuesto a minorías, el “¿por qué?” de los ingresos lo muestra como contribución. |
| `reform_not_scripted` | En 100 campañas sandbox, la primera confesión nueva de la Iglesia latina aparece en al menos tres regiones distintas. |

## 07. Historia guiada y divergencia causal

### 101 History: motor de plausibilidad histórica (propuesto)

Una capa independiente consulta la historia documentada, reconoce condiciones del mundo y asigna prioridades históricas **solo a acciones posibles**. Mantiene la trayectoria de referencia sin sobrescribir el estado real de la partida.

#### Tres clases de reglas

| Clase | Comportamiento | Ejemplo |
| --- | --- | --- |
| Duras | Requisitos físicos, tecnológicos y operativos no negociables. | No hay misiles modernos sin electrónica, propelentes e industria. |
| Blandas | Sesgos nacionales basados en geografía, instituciones e intereses. | Una potencia marítima busca rutas si dispone de puertos y flota. |
| Condicionales | Eventos con periodo, actores, requisitos y rutas alternativas. | Guerra sucesoria, unificación, revolución o independencia. |

#### Anatomía de una situación histórica

| Campo | Contenido |
| --- | --- |
| Ventana | Periodo en el que es plausible; fuera de ella pierde peso o caduca. |
| Actores | Roles, no países fijos: “potencia expansiva con flota”, “dinastía con pretendiente”. |
| Precondiciones | Condiciones medibles del mundo, con peso. |
| Caducidad | Qué divergencia invalida la situación o la transforma en otra. |
| Variantes | Resultados alternativos según el estado del mundo. |
| Fuentes | Referencia historiográfica y nivel de confianza. |

#### Ejemplo: la caída de Constantinopla

| Campo | Valor |
| --- | --- |
| Ventana | 1390–1520, con máximo de plausibilidad 1440–1470. |
| Actores | Sitiador: potencia con artillería de asedio y control de ambas orillas del estrecho. Defensor: poseedor de Constantinopla. |
| Precondiciones | El sitiador controla Tracia y Bitinia; dispone de bombardas grandes; el defensor no tiene aliados navales con flota en la zona; murallas sin modernizar. |
| Caducidad | Si Constantinopla está en manos de una potencia fuerte, la situación se transforma en “asedio de la ciudad imperial” genérico. |
| Variantes | Caída por asalto; rendición negociada; asedio fallido con tregua; intervención veneciana o genovesa. |
| Resultado no forzado | El asedio se decide por el sistema militar; la situación solo eleva la prioridad de la IA sitiadora. |

### Catálogo inicial de situaciones (muestra)

| Situación | Ventana orientativa | Condiciones principales | Región |
| --- | --- | --- | --- |
| Compañía Catalana en Oriente | 1302–1315 | Mercenarios ociosos tras una paz; un Estado rico en crisis militar. | Bizancio |
| Crisis sucesoria húngara | 1301–1310 | Extinción de la dinastía; pretendientes extranjeros. | Hungría |
| Guerra de los Cien Años | 1330–1460 | Rey inglés con reclamación al trono francés y feudos en Francia. | Francia/Inglaterra |
| Peste negra | 1340–1360 | Rutas comerciales que conectan la estepa con el Mediterráneo; brote en Asia central. | Global |
| Guerras civiles bizantinas | 1320–1360 | Regencias, nobleza terrateniente fuerte, crisis fiscal. | Bizancio |
| Imperio serbio | 1330–1360 | Rey serbio fuerte, Bizancio en guerra civil. | Balcanes |
| Fundación de Valaquia y Moldavia | 1310–1370 | Voivodatos rumanos fuera del control húngaro o tártaro. | Balcanes |
| Gran Cisma de Occidente | 1370–1420 | Papado bajo presión de una monarquía; disputas electorales. | Europa |
| Unión de Kalmar | 1380–1400 | Reina o rey con derechos en varios reinos nórdicos. | Escandinavia |
| Unión polaco-lituana | 1380–1390 | Lituania pagana presionada; Polonia sin heredero varón. | Europa del este |
| Irrupción de Timur | 1370–1405 | Caudillo carismático en Transoxiana; kanatos debilitados. | Asia central |
| Interregno otomano | Tras una derrota catastrófica del sultán | Muerte o captura del gobernante con varios hijos. | Anatolia |
| Hussitas | 1410–1440 | Crítica a la Iglesia, identidad local, universidad activa. | Bohemia |
| Unión de las Iglesias | 1430–1450 | Bizancio necesita ayuda occidental. | Mediterráneo |
| Caída de Constantinopla | 1440–1470 | Ver ejemplo detallado. | Bizancio |
| Unión dinástica ibérica | 1460–1480 | Matrimonio entre herederos de grandes coronas. | Iberia |
| Conquista de Granada | 1480–1500 | Emirato dividido; reinos cristianos unidos. | Iberia |
| Viajes atlánticos | 1480–1520 | Navegación oceánica, financiación y motivación comercial. | Atlántico |
| Fundación de Tenochtitlan | 1320–1330 | Grupo migrante nahua sin tierras en la cuenca de México. | Mesoamérica |
| Triple Alianza mexica | 1420–1440 | Caída del dominio tepaneca; alianza de ciudades. | Mesoamérica |
| Expansión inca | 1430–1470 | Cusco vence a un rival regional (chancas) con liderazgo fuerte. | Andes |
| Reforma religiosa | 1500–1560 | Imprenta, crítica del clero, príncipes interesados. | Europa |
| Mohács | 1520–1530 | Potencia otomana fuerte frente a Hungría aislada. | Balcanes |
| Revolución militar | 1550–1650 | Pólvora madura, Estados fiscales, fortificación abaluartada. | Global |
| Revoluciones atlánticas | 1770–1830 | Ilustración, crisis fiscal, colonias con élites propias. | Atlántico |
| Industrialización | 1760–1850 | Carbón accesible, capital, mercados, máquina de vapor. | Global |
| Unificaciones nacionales | 1840–1880 | Nacionalismo, Estado núcleo fuerte, rival exterior débil. | Europa |
| Gran guerra entre potencias | 1890–1950 | Bloques, carrera armamentista, crisis detonante. | Global |
| Revolución socialista | 1900–1950 | Industrialización rápida, guerra perdida, movimiento obrero organizado. | Global |
| Descolonización | 1940–1980 | Metrópolis debilitadas, movimientos locales, presión internacional. | Global |
| Era nuclear y bloques | 1945+ | Armas nucleares en varias potencias rivales. | Global |
| Revolución digital | 1970+ | Semiconductores, redes, capital riesgo. | Global |
| Transición energética | 2000+ | Calentamiento observado, alternativas maduras, presión social. | Global |

### Cuatro modos de campaña

| Modo | Comportamiento de la IA |
| --- | --- |
| Histórico estricto | Muy persistente en prioridades y ventanas; los hechos aún exigen causas suficientes. |
| Histórico dinámico (predeterminado) | Equilibrio entre tendencias documentadas y respuestas a las decisiones del jugador. |
| Alternativo plausible | Menor dependencia de rutas nacionales; mayor peso de capacidades y contexto. |
| Sandbox causal | Sin sesgos históricos específicos; mantiene física, geografía, necesidades y tecnología. |

### Reconvergencia y divergencia

Los Estados conservan identidades y reclamaciones latentes tras desaparecer. La IA puede intentar restaurarlos si confluyen población, apoyo político, condiciones diplomáticas y poder material. Reconverger **no significa revertir fronteras automáticamente**.

**Regla de divergencia:** cuanto más se aleje una región de las causas originales, menos peso tendrán sus eventos específicos. Cada región mantiene un **índice de divergencia** respecto a la trayectoria de referencia (control político, población, instituciones, tecnología), visible en 101 Lab y, opcionalmente, para el jugador.

### Especificación detallada de 101 History (v0.7, propuesto)

Base de `docs/specs/history.md`.

#### Ciclo de evaluación

| Paso | Frecuencia | Qué hace |
| --- | --- | --- |
| 1. Filtrado por ventana | Mensual (escalonado por situación) | Descarta las situaciones fuera de su ventana o caducadas. |
| 2. Asignación de roles | Mensual | Para cada rol, puntúa a las entidades candidatas y elige la mejor (empates por ID). |
| 3. Plausibilidad | Mensual | Calcula la plausibilidad de la situación con sus actores. |
| 4. Activación | Al superar el umbral | La situación pasa a **activa**: aparece en el panel de los actores (si son visibles para ellos) y empieza a emitir sesgos. |
| 5. Etapas | Según la situación | Avanza por sus etapas cuando se cumplen sus condiciones de progreso. |
| 6. Resolución o caducidad | Al cumplirse una variante o una condición de caducidad | Registra el resultado en la crónica y en el índice de divergencia. |

#### Plausibilidad

```text
plausibilidad = factor_ventana(año) × (Σ pesos de las precondiciones cumplidas / Σ pesos totales)
                × ajuste_de_modo × (1 − peso_divergencia_regional)

factor_ventana: 0 antes del inicio; sube linealmente hasta 1 al empezar el pico;
                1 durante el pico; baja linealmente hasta 0 al final de la ventana
ajuste_de_modo: estricto 1,2; dinámico 1,0; alternativo 0,6; sandbox 0
peso_divergencia_regional = min(1, divergencia_de_la_región / 60)
```

| Umbral | Valor | Efecto |
| --- | --- | --- |
| Activación | 0,60 | La situación se vuelve visible y empieza a sesgar a la IA. |
| Mantenimiento | 0,40 | Por debajo durante 12 meses, la situación se suspende (puede reactivarse). |
| Caducidad | Condición explícita o fin de ventana | Se cierra o se transforma en otra situación. |

**Sesgo a la IA.** Una situación activa añade a las acciones coherentes con su rol un término de sesgo histórico de `plausibilidad × intensidad × peso_del_modo`, con un máximo de **+20 pu** por acción (sección 17). Es suficiente para inclinar decisiones parejas y nunca para imponer una acción con utilidad claramente negativa ni para habilitar una acción imposible.

#### Índice de divergencia por región

```text
divergencia (0–100) = 35 × D_política     (cuota de provincias cuyo controlador no comparte identidad
                                            con el de la referencia en esa fecha)
                    + 25 × D_población    (|log(población_simulada / referencia)|, saturado en 1)
                    + 20 × D_instituciones (cuota de categorías de ley distintas de la referencia)
                    + 20 × D_tecnología   (años medios de adelanto o retraso en técnicas clave / 50, saturado)
```

Se calcula cada año por macrorregión con la trayectoria de referencia de las “Entidades históricas por época”. Una divergencia de 60 o más anula el sesgo de las situaciones específicas de esa región; las situaciones **genéricas** (crisis sucesoria, guerra civil, reforma religiosa) siguen funcionando porque dependen de condiciones, no de la historia concreta.

#### Ejemplo de evaluación: la Compañía Catalana en Oriente

| Precondición | Peso | Estado en marzo de 1302 (partida histórica) | Cumplida |
| --- | --- | --- | --- |
| Existe una compañía mercenaria grande ociosa (≥ 3.000 combatientes) sin contrato | 30 | La paz de Caltabellotta deja sin empleo a los almogávares | Sí |
| Un Estado rico en crisis militar con amenaza > 60 | 30 | Bizancio, amenaza turca 72 | Sí |
| Ese Estado puede pagar al menos 4 meses de adelanto | 20 | Tesoro bizantino suficiente con préstamos | Sí |
| Rutas marítimas entre ambos | 10 | Sí, por Sicilia | Sí |
| Afinidad o enemigo común | 10 | Enemigo común turco; afinidad religiosa baja (latinos y ortodoxos) | Parcial (5) |

Plausibilidad = 1,0 (pico 1302–1305) × 95/100 × 1,0 × (1 − 0,05) ≈ **0,90**: se activa. El sesgo eleva la utilidad de “contratar a la compañía” para Bizancio y de “aceptar el contrato” para la compañía, pero la decisión la toman las IA o el jugador con sus utilidades. Si el jugador bizantino tiene el tesoro saneado y un ejército propio, la contratación puede no compensarle, y la situación caduca a los tres años o se transforma en “la compañía busca patrón” con otro Estado.

#### Formato de etapas

Las situaciones largas tienen etapas con condiciones de progreso y efectos de sesgo propios:

| Etapa (ejemplo: guerras civiles bizantinas) | Condición de avance | Sesgos activos |
| --- | --- | --- |
| 1. Tensión dinástica | Regencia o coemperador con facción propia | +sesgo a formar facciones |
| 2. Ruptura | Facción con fuerza > 0,6 del gobernante | +sesgo a pedir apoyo exterior (Serbia, beyliks) |
| 3. Guerra abierta | Proclamación de un pretendiente | Sesgo a intervenir para vecinos con interés |
| 4. Resolución | Paz entre bandos o eliminación de uno | Crónica y efectos de largo plazo |

#### Pruebas específicas

| Prueba | Criterio |
| --- | --- |
| `bias_capped` | Ninguna acción recibe más de +20 pu por sesgo histórico. |
| `no_forced_events` | En modo sandbox, la plausibilidad de toda situación específica es 0. |
| `divergence_monotone_with_conquest` | Conquistar una región entera eleva su divergencia política al menos 30 puntos. |
| `situation_expiry` | Ninguna situación queda activa después del fin de su ventana. |

## 08. Estados dinámicos y entidades formables

### Identidad no equivale a Estado soberano

Se separan **identidad histórica**, **instituciones**, **régimen**, **dinastía**, **administración**, **fronteras** y **control militar**. Las identidades pueden sobrevivir a la desaparición del gobierno soberano y reaparecer por vías distintas.

| Proceso | Mecanismo |
| --- | --- |
| Unificación | Coaliciones, identidad, reclamaciones, diplomacia, reforma o conquista. |
| Fragmentación | Pérdida de control, crisis fiscal, rebeliones, presión de élites o autonomías. |
| Restauración | Movimiento legitimista o nacional, apoyos externos y continuidad identitaria. |
| Cambio de régimen | Reformas, sucesiones, revoluciones, golpes, elecciones y tratados. |
| Federación o confederación | Negociación de competencias, financiación, defensa y soberanía. |
| Descolonización | Movimientos locales, incentivos internacionales y capacidades administrativas. |
| Surgimiento | Una entidad social o un voivodato se convierte en Estado (Valaquia, Suiza). |

### Entidades formables como identidades emergentes

En lugar de un botón “formar país X”, una entidad nueva aparece cuando una **identidad compartida** y un **centro político** coinciden en un territorio suficiente. El nombre y la bandera surgen de la cultura, la religión y la dinastía dominantes.

| Identidad posible | Condiciones típicas | Variantes plausibles |
| --- | --- | --- |
| España | Unión de las coronas ibéricas cristianas, control de la meseta y del litoral. | Hispania bajo Aragón; Iberia unida con Portugal; reinos separados. |
| Italia | Nacionalismo, Estado núcleo fuerte, expulsión de potencias externas. | Federación de repúblicas; Italia papal; Italia del norte. |
| Alemania | Identidad nacional, unión aduanera, Estado núcleo militar. | Gran Alemania con Austria; confederación; varias Alemanias. |
| Polonia-Lituania | Unión dinástica y luego institucional. | Lituania ortodoxa; Polonia sola. |
| Rusia | Principado de la Rus que se libera del tributo de la estepa y unifica a los demás. | Unificación desde Tver o Nóvgorod; Rus lituana. |
| Imperio otomano | Beylik que cruza a Europa y conquista la ciudad imperial. | Imperio con capital en Bursa o Edirne; Anatolia fragmentada. |
| Imperio romano restaurado | Poseedor de Constantinopla con Anatolia y los Balcanes, o potencia latina con legitimidad imperial. | Restauración bizantina; Imperio latino; reclamación otomana como *Kayser-i Rûm*. |
| México | Independencia de un territorio con identidad propia tras un periodo colonial, o consolidación de un imperio mesoamericano. | Imperio de la Triple Alianza que sobrevive; república federal; monarquía. |
| Tawantinsuyu | Cusco unifica los Andes centrales. | Confederación andina; Chimú dominante. |
| Unión europea u organizaciones regionales | Integración económica y política tras guerras devastadoras. | Bloques distintos según la partida. |

### Continuidad de la identidad

Cada entidad conserva una línea histórica: nombres anteriores, gobiernos, fronteras, capitales, batallas, tratados y crisis. Esa línea alimenta la crónica y las reclamaciones latentes.

**Continuidad del jugador (abierto):** si el Estado del jugador colapsa, puede controlar una entidad sucesora (heredera institucional, movimiento de restauración o fragmento mayor). Falta decidir si el colapso total termina la partida.

**Propuesta para resolver A-11:** el colapso total **no** termina la partida por defecto. Se ofrecen, por orden, (1) el fragmento mayor que conserve la dinastía o la capital, (2) un movimiento de restauración activo con la misma identidad, (3) cualquier entidad de la misma cultura, o (4) el modo observador. Una opción de partida (“caída definitiva”) permite que el colapso sea el final para quien prefiera la tensión.

### Especificación detallada de identidades y Estados (v0.7, propuesto)

#### Ciclo de vida de una entidad

```text
Entidad social (sin soberanía) ──surgimiento──▶ Estado soberano ──vasallaje──▶ Estado vasallo
        ▲                                         │   ▲                        │
        │                                   colapso   │ restauración           independencia
        │                                         ▼   │                        ▼
        └────────────── absorción ◀── Identidad latente (sin territorio, con memoria y reclamaciones)
```

Una entidad sin provincias no se borra: pasa a **identidad latente**, con su historia, su dinastía (si sobrevive), sus reclamaciones y una **fuerza de memoria** que decae a la mitad en 50 años si nadie la sostiene (cohortes de su cultura, instituciones religiosas propias, pretendientes en el exilio). Mientras la fuerza de memoria sea > 20, puede aparecer un movimiento de restauración.

#### Emergencia de una identidad formable

Cada identidad formable se define en datos con **regiones núcleo**, **culturas y religiones asociadas** y **condiciones**. Cada año se evalúa:

```text
cobertura    = provincias núcleo controladas por entidades que comparten la cultura o el grupo cultural
               asociados / provincias núcleo totales
centro       = existe una entidad que controla la capital histórica o la provincia más poblada del núcleo
legitimidad  = la entidad central tiene legitimidad ≥ 50 con los grupos de la identidad
se ofrece la proclamación si cobertura ≥ 0,60 y centro y legitimidad
```

| Ejemplo | Núcleo | Cultura o vínculo | Condición adicional |
| --- | --- | --- | --- |
| Restauración del Imperio romano de Oriente | Tracia, Bitinia, Macedonia, Grecia continental, costa egea de Anatolia | Griego (romeo) u otra con legitimidad imperial reconocida | Controlar Constantinopla |
| Imperio serbio | Raška, Zeta, Macedonia, Tesalia | Serbio | Rey serbio con prestigio ≥ 60 y patriarcado propio |
| Unión de los beyliks anatolios | Anatolia occidental y central (≥ 6 regiones) | Turco oguz | Absorber o vasallizar al menos a 4 beyliks |
| Valaquia | Llanura entre los Cárpatos y el Danubio | Valaco | Voivoda con ejército propio y sin vasallaje efectivo |

La proclamación es una **decisión** (del jugador o de la IA), no un efecto automático: cambia nombre, bandera, títulos y reclamaciones, da legitimidad con los grupos de la identidad (+10) y puede alarmar a vecinos (amenaza +10 a quien tenga reclamaciones en el núcleo).

#### Nombres y banderas

- **Nombre:** se elige de una tabla por identidad, régimen y cultura de la dinastía (“Imperio de los romanos”, “Despotado de…”, “Sultanato de…”). Si la entidad es nueva y no tiene tabla, el nombre se compone con reglas (`tipo_de_régimen + de + topónimo_de_la_capital`) y queda editable por el jugador.
- **Bandera y escudo:** si hay datos históricos, se usan; si no, se generan con reglas heráldicas (tinturas, particiones y muebles por cultura y religión) o vexilológicas (desde el siglo XVIII). La generación es determinista por semilla.

#### Fragmentación

Una entidad se fragmenta cuando una guerra civil termina en partición, cuando un gobernador con lealtad < 20 y control propio > 60 % en su región se declara independiente, o cuando una herencia partible divide el reino (cultura con herencia partible). El fragmento hereda leyes, cultura y parte de la deuda proporcional a su población.

---

# Parte III · Sistemas de juego

## 09. Población y sociedad

### Modelo híbrido agregado

Se simulan grupos de población (*cohortes*) por provincia, estrato socioeconómico, ocupación, cultura, religión, educación y nivel de vida. Millones de habitantes no se actualizan como agentes individuales. En ciudades o batallas visualizadas se crean agentes locales temporales solo cuando aportan información jugable.

| Dimensión | Variables principales | Relaciones |
| --- | --- | --- |
| Demografía | Estructura de edad simplificada (niños, adultos, ancianos), natalidad, mortalidad, migración. | Alimentos, salud, guerra, clima y salarios. |
| Clase y trabajo | Ocupación, ingresos, propiedad, empleo. | Edificios, industrias, leyes y educación. |
| Identidad | Cultura, idioma, religión, identidad política. | Integración, conflictos, instituciones, migración. |
| Necesidades | Comida, vivienda, ropa, combustible, seguridad, servicios, bienes de lujo. | Mercados, pobreza, bienestar y legitimidad. |
| Movilización | Hombres en edad de servir, reservas, reclutados. | Guerra, producción y oposición política. |
| Alfabetización | Proporción alfabetizada por cohorte. | Ciencia, burocracia, nacionalismo, prensa. |

**Control de la explosión combinatoria:** las cohortes que caen por debajo de un umbral de tamaño se fusionan con la más parecida de su provincia, y la fusión se registra. Objetivo: en la escala S, entre 30 y 70 cohortes por provincia.

### Ocupaciones (conjunto inicial para 1300–1600)

| Ocupación | Produce o aporta | Clase típica |
| --- | --- | --- |
| Campesinos dependientes | Cereales, ganado, trabajo para el señor. | Baja |
| Campesinos libres | Cereales, ganado, impuestos. | Baja-media |
| Pastores y nómadas | Ganado, caballos, lana; movilidad militar. | Variable |
| Pescadores y marineros | Pescado, tripulaciones. | Baja |
| Artesanos | Manufacturas por gremio. | Media |
| Mercaderes | Comercio, crédito, rutas. | Media-alta |
| Banqueros | Crédito, cambio, préstamos al Estado. | Alta |
| Clero | Servicios religiosos, educación, administración. | Variable |
| Nobleza terrateniente | Mando militar, administración local, renta. | Alta |
| Soldados profesionales | Fuerza militar, mercenariado. | Variable |
| Funcionarios y letrados | Burocracia, justicia, recaudación. | Media |
| Esclavizados y siervos sin derechos | Trabajo forzado (sección de contenido sensible). | — |

Desde 1600 se añaden obreros de manufactura, profesionales, empresarios; desde 1800, obreros industriales, ingenieros, empleados; desde 1950, técnicos y trabajadores de servicios. Las ocupaciones nuevas aparecen cuando los edificios y las instituciones que las requieren existen.

### Necesidades y nivel de vida

Cada estrato consume una **cesta** de bienes por persona y mes. Si la cesta no se cubre, baja el nivel de vida y suben la mortalidad, la emigración y el descontento. El nivel de vida es visible en el mapa y en el panel de provincia, con la lista de bienes que faltan.

### Modelo demográfico (propuesto)

Todas las tasas son **mensuales**, se calculan por cohorte y se almacenan en punto fijo. Los valores iniciales son orientativos y deben calibrarse con 101 Lab (Anexo F).

```text
nacimientos  = adultos × tasa_natalidad_base × f_vida(nivel_de_vida) × f_paz(seguridad)
muertes      = población × tasa_mortalidad_base × g_alimentos(cobertura) × g_salud(saneamiento, medicina)
             + muertes_epidemia + muertes_guerra + muertes_hambruna
migración_ij = población_i × α × max(0, atractivo_j − atractivo_i) / coste_viaje_ij
               (limitada al 1 % mensual por cohorte; los refugiados no tienen límite)
atractivo    = salario_real + seguridad + tolerancia_hacia_la_cohorte + tierra_disponible
```

| Parámetro | Valor inicial orientativo (1300) | Notas |
| --- | --- | --- |
| Natalidad bruta | 35–45 por mil al año | Típica de sociedades agrarias preindustriales. |
| Mortalidad bruta en años normales | 30–40 por mil al año | El crecimiento a largo plazo queda cerca de cero, con oscilaciones. |
| Mortalidad infantil | Implícita en la tasa bruta | Se separa cuando la medicina lo justifique (siglo XIX). |
| Elasticidad de la mortalidad a la falta de alimentos | Alta | Una cobertura del 70 % durante seis meses produce una hambruna visible. |
| Fracción de adultos | ~55 % | Estructura de edad simplificada en tres franjas. |

**Transición demográfica:** cuando mejoran la alimentación, el saneamiento y la medicina, la mortalidad cae antes que la natalidad, y la población crece rápido hasta que la urbanización, la educación y el coste de criar hijos reducen la natalidad. El motor no programa esta transición: debe **emerger** de los factores anteriores.

### Movilidad social y asimilación

```text
cambio_ocupación = cohorte × β × vacantes_destino × (salario_destino / salario_origen − 1)
                   (si es positivo, con límite mensual del 0,5 %; requiere educación o capital si la ocupación lo exige)

asimilación      = cohorte × tasa_base × prestigio_cultura_dominante × integración_económica
                   × contacto (cuota de población dominante en la provincia)
                   ÷ resistencia (densidad cultural, religión distinta, instituciones propias, represión)
```

La conversión religiosa sigue la misma forma, con sus propios factores (misiones, ventajas legales, presión social, tolerancia). Ambas pueden ir **en los dos sentidos**: una élite conquistadora minoritaria puede asimilarse a la población conquistada.

### Evolución de los grupos sociales

Los grupos sociales cambian según las condiciones. No hay clases rígidas por siglo: cuentan la propiedad, el ingreso, la actividad y la influencia. Salud pública, saneamiento, epidemias, derechos, desigualdad y alfabetización emergen de sistemas materiales e institucionales, no de eventos aislados.

### Contenido histórico sensible

La esclavitud, la trata, la colonización, la violencia masiva, las persecuciones y los genocidios forman parte de la historia que el juego simula. Principios:

- **Sistemas, no recompensas:** se modelan con sus costes humanos, sociales, económicos y de legitimidad. Nunca son una bonificación sin consecuencias.
- **Personas, no mercancías:** la trata se modela como migración forzada dentro del sistema de población, no como un bien comerciable con icono en el mercado.
- **Agencia de los afectados:** resistencia, rebelión, huida, memoria y reclamaciones.
- **Sin caricaturas:** culturas y religiones se describen con respeto; nombres endónimos con opción de exónimos.
- **Revisión:** el contenido sensible pasa por revisión editorial específica antes de integrarse.
- **Opciones de presentación:** el jugador puede ajustar el detalle de las descripciones sin alterar la simulación.

### Especificación detallada de población (v0.7, propuesto)

Esta especificación es la base de `docs/specs/population.md`. Todos los valores son **iniciales**: se calibran con 101 Lab contra el Anexo F y se consolidan en la tabla de parámetros globales (Anexo AI). Las cantidades de personas se guardan como `Qty` (tres decimales implícitos): una cohorte puede tener 1.234,567 personas internamente, aunque la interfaz redondee.

#### Estructura de una cohorte

| Campo | Tipo | Rango o valores | Uso |
| --- | --- | --- | --- |
| `id` | `CohortId` (slotmap generacional) | — | Identidad estable mientras exista. |
| `province` | `ProvinceId` | — | Ubicación; toda cohorte vive en una provincia. |
| `occupation` | `OccupationId` | Catálogo por época | Empleo, cesta y estrato por defecto. |
| `culture` | `CultureId` | — | Asimilación, lealtad, nombres. |
| `religion` | `ReligionId` | — | Conversión, política religiosa. |
| `legal_status` | enum | `Free`, `Dependent`, `Enslaved`, `Privileged` | Derechos, movilidad, impuestos (ver contenido sensible). |
| `origin` | enum | `Native`, `Migrant`, `Refugee`, `Colonist` | Integración y retorno. |
| `size` | `Qty` | ≥ 0 | Número de personas. |
| `age_share` | 3 × `Ratio` | Suman 10.000 pb | Niños (0–14), adultos (15–49), mayores (50+). |
| `literacy` | `Ratio` | 0–10.000 pb | Burocracia, ciencia, prensa, nacionalismo. |
| `wealth` | `Money` | ≥ 0 | Ahorro acumulado de la cohorte. |
| `income_month` | `Money` | ≥ 0 | Ingreso del último cierre mensual. |
| `living_standard` | `Ratio` | 0–30.000 pb | Nivel de vida (NV) de 0,00 a 3,00 (ver abajo). |
| `grievance` | `Ratio` | 0–10.000 pb | Agravio acumulado contra el régimen. |
| `support` | `[Ratio; N_grupos]` | 0–10.000 pb | Apoyo a cada grupo de interés o facción relevante. |
| `mobilized` | `Qty` | ≤ adultos | Personas reclutadas que no trabajan. |
| `pending_flows` | índice a tabla aparte | — | Flujos de transición por debajo del umbral (ver fusión). |

**Memoria estimada:** unos 112 bytes por cohorte sin el vector de apoyos, más 2 bytes por grupo de interés. En la escala S (≈350 provincias × 30–70 cohortes) son unas 17.500 cohortes y menos de 3 MB; en la escala L (≈5.000 provincias × 40 de media) unas 200.000 cohortes y unos 30 MB. El coste no está en la memoria, sino en el cálculo mensual, que se reparte por escalonamiento.

#### Clave de identidad, creación y fusión

La **clave** de una cohorte es `(provincia, ocupación, cultura, religión, condición jurídica)`. No puede haber dos cohortes con la misma clave en la misma provincia; el origen y el resto de campos son atributos que se promedian al fusionar.

**Creación por flujos.** Los procesos que mueven personas entre claves (movilidad social, asimilación, conversión, migración) no crean una cohorte nueva por cada persona. Los flujos se acumulan en una tabla de transición por provincia, indexada por la clave de destino:

```text
si existe la cohorte destino:        se suma el flujo directamente
si no existe y acumulado < U_crear:  el flujo espera en pending_flows (las personas siguen
                                     contándose en la cohorte de origen hasta materializarse)
si acumulado ≥ U_crear:              se crea la cohorte destino con el acumulado
```

| Parámetro | Valor inicial | Nota |
| --- | --- | --- |
| `U_crear` | 50 personas | Por debajo, el cambio es invisible y no merece una fila en el panel. |
| `U_fusion` | max(100 personas; 0,3 % de la población de la provincia) | Cohortes más pequeñas se fusionan en el cierre mensual. |
| `MAX_COHORTES_PROVINCIA` | 70 (escala S), 50 (escala M), 40 (escala L) | Tope duro. |

**Distancia entre cohortes** (para elegir con quién se fusiona una cohorte pequeña):

| Diferencia | Coste |
| --- | --- |
| Misma ocupación, distinta cultura del mismo grupo cultural | 1 |
| Distinta cultura de distinto grupo | 3 |
| Distinta religión de la misma familia | 2 |
| Distinta familia religiosa | 4 |
| Distinta ocupación del mismo estrato | 2 |
| Distinto estrato | 5 |
| Distinta condición jurídica | **prohibido** (nunca se fusionan) |

La cohorte se fusiona con la de menor coste; los empates se resuelven por menor `CohortId`. Los atributos continuos (edad, alfabetización, agravio, apoyos) se promedian ponderados por tamaño; la riqueza se suma. Cada fusión registra una contribución `Origin::Merge` en el registro causal de la cohorte receptora, para que “¿por qué hay 120 armenios más en Sis?” tenga respuesta.

**Prioridad de clave al fusionar:** se conserva la clave de la cohorte **mayor**. Así, un pequeño grupo de artesanos judíos que cae por debajo del umbral se integra en la cohorte de comerciantes judíos de la ciudad (coste 2) antes que en la de artesanos griegos (coste 4 + 3), lo que respeta la identidad religiosa y cultural, que es la información más relevante para la política.

#### Estructura de edad

Tres franjas bastan para reclutamiento, fuerza de trabajo, dependencia y mortalidad diferencial. Cada mes:

```text
paso_a_adultos  = niños   × (1/180)        # 15 años × 12 meses
paso_a_mayores  = adultos × (1/420)        # 35 años × 12 meses
nacimientos     → niños
muertes_franja  = tamaño_franja × tasa_franja × modificadores
```

| Franja | Mortalidad base anual (1300, años normales) | Cuota típica en una población agraria estable |
| --- | --- | --- |
| Niños (0–14) | 55 ‰ | ~35 % |
| Adultos (15–49) | 16 ‰ | ~55 % |
| Mayores (50+) | 85 ‰ | ~10 % |
| **Media ponderada** | **≈ 36,5 ‰** | — |

Con una natalidad bruta de 40 ‰ (≈ 72,7 ‰ por adulto), el crecimiento en años buenos ronda el +3,5 ‰ anual; las crisis (hambrunas, guerras, epidemias) lo devuelven a una tendencia secular cercana a cero, como en las sociedades agrarias preindustriales. Las tasas anuales se convierten a mensuales con una tabla precalculada en punto fijo (`r_mes = 1 − (1 − r_año)^(1/12)`), nunca con potencias de flotantes.

#### Funciones de modificación (tablas por tramos)

Todas las funciones *f* y *g* del modelo demográfico son **tablas por tramos lineales** en datos (`games/epoch/data/rules/population.ron`), editables por diseño y por mods. Valores iniciales:

| Nivel de vida (NV) | 0,50 | 0,80 | 1,00 | 1,50 | 2,00 | 3,00 |
| --- | --- | --- | --- | --- | --- | --- |
| `f_vida` (natalidad) | 0,80 | 0,95 | 1,00 | 1,04 | 1,02 | 0,95 |

| Cobertura alimentaria | 1,00 | 0,90 | 0,80 | 0,70 | 0,60 | 0,50 | ≤ 0,40 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `g_alimentos` (mortalidad) | 1,00 | 1,15 | 1,50 | 2,20 | 3,50 | 5,50 | 8,00 |

| Seguridad de la provincia | 1,00 | 0,70 | 0,40 | 0,10 |
| --- | --- | --- | --- | --- |
| `f_paz` (natalidad) | 1,00 | 0,95 | 0,85 | 0,70 |

| Factor de salud | Multiplicador de mortalidad |
| --- | --- |
| Ciudad > 20.000 habitantes sin saneamiento (antes del siglo XIX) | × 1,15 |
| Ciudad con acueducto y cloacas funcionales | × 1,05 |
| Saneamiento moderno | × 0,85 |
| Medicina científica básica (siglo XIX) | × 0,80 sobre niños |
| Vacunación extendida | × 0,60 sobre niños |
| Antibióticos | × 0,70 general |

**Comprobación de la regla de hambruna de la v0.6:** con cobertura del 70 % durante seis meses, la mortalidad mensual pasa de ≈ 3,0 ‰ a ≈ 6,7 ‰; el exceso acumulado es de unos 22 ‰, es decir, un 2,2 % de la población muerta de más en medio año, a lo que se suman emigración y caída de nacimientos. Es una hambruna visible sin llegar a catástrofe; la catástrofe llega con coberturas por debajo del 50 %.

**Natalidad en la transición demográfica.** A partir de la urbanización y la escolarización, la natalidad se multiplica por `h_crianza(urbanización, alfabetización_media)`, una tabla que vale 1,00 con alfabetización < 30 % y baja hasta 0,45 con alfabetización > 90 % y urbanización > 70 %. Con la caída previa de la mortalidad por saneamiento y medicina, la transición **emerge** sin programarla.

#### Nivel de vida y cestas

El nivel de vida (NV) se define con una regla legible: cada estrato tiene tres cestas por persona y mes (subsistencia, comodidad y lujo). La cohorte compra en orden y su NV es la suma de las coberturas:

```text
NV = cobertura_subsistencia + cobertura_comodidad + cobertura_lujo      (cada una de 0 a 1)
```

Un NV de 0,80 significa “cubre el 80 % de su subsistencia”; 1,40 significa “cubre la subsistencia y el 40 % de la comodidad”. La interfaz muestra el NV junto con la lista de bienes que faltan, ordenada por cuánto pesan en la cesta.

**Cestas del periodo 1300–1600 (por persona y mes, valores iniciales).** “GE” es kilogramo de *grano equivalente* (aporte calórico de 1 kg de trigo).

| Estrato | Subsistencia | Comodidad (adicional) | Lujo (adicional) |
| --- | --- | --- | --- |
| Bajo (campesinos, jornaleros, pescadores) | 16 GE alimento básico; 0,5 kg sal; 0,8 l aceite o grasa; 0,15 unidades de tejido; 25 kg leña (× 1,6 en invierno) | 4 GE (carne, pescado, legumbres); 3 l vino o cerveza; 0,1 unidades de tejido | Raro; 0,05 unidades de paño fino |
| Medio (artesanos, mercaderes menores, clero rural, soldados) | Igual que el bajo + 0,2 unidades de tejido | 8 GE variados; 6 l vino; 0,3 unidades de paño; servicios urbanos 0,3 uc | 0,1 unidades de seda o paño fino; 10 g especias; 0,5 uc en servicios |
| Alto (grandes mercaderes, banqueros, alto clero, funcionarios superiores) | Igual que el medio | 15 GE variados; 10 l vino; 0,6 unidades de paño; 1,5 uc en servicios | 0,4 unidades de seda; 60 g especias; 0,2 kg azúcar; 4 uc en servicios y objetos |
| Élite (nobleza mayor, familia gobernante) | Igual que el alto | Igual que el alto × 1,5 | 1,5 unidades de seda; 200 g especias; 1 kg azúcar; 20 uc en servicios, joyas y patronazgo |

La **uc** (unidad de cuenta) se define en la especificación económica de la sección 10. Los servicios (vivienda urbana, servicios religiosos, educación) se pagan en dinero a las cohortes que los prestan; no son bienes almacenables.

**Sustitución dentro de una categoría.** El alimento básico puede cubrirse con grano, arroz, pescado, carne o legumbres, cada uno con su equivalencia (1 kg de pescado = 0,45 GE; 1 kg de carne = 0,70 GE; 1 kg de arroz = 1,05 GE; 1 kg de legumbres = 0,95 GE). La cuota de cada bien es proporcional a `preferencia_cultural × (1 / precio_por_GE)²`, calculada en punto fijo. El cuadrado hace que la sustitución responda con claridad a los precios sin caer en soluciones de “todo o nada”.

#### Ingresos y gasto de una cohorte

```text
ingreso_mes = salarios (edificios donde trabaja)
            + rentas (edificios o tierras que posee)
            + beneficio mercantil (si es una cohorte de mercaderes)
            + transferencias (limosnas, subsidios, botín, paga militar)
            − impuestos directos y cargas señoriales
gasto       = compra de cestas en orden hasta agotar ingreso + fracción de riqueza disponible
ahorro      = ingreso − gasto  (si es positivo, aumenta wealth; si es negativo, lo consume)
```

| Estrato | Fracción de la riqueza que puede gastar al mes para sostener la subsistencia | Propensión a ahorrar el excedente |
| --- | --- | --- |
| Bajo | 20 % | 10 % |
| Medio | 10 % | 25 % |
| Alto | 5 % | 40 % (inversión, préstamos, compra de tierra) |
| Élite | 5 % | 30 % (el resto se gasta en lujo y patronazgo) |

El ahorro de los estratos alto y élite alimenta el **capital invertible** de la provincia, que la inversión privada (sección 10) y los préstamos al Estado consumen. Así, una nobleza que gasta todo en lujo deja menos capital para molinos y barcos: una consecuencia legible de las leyes y de la cultura de corte.

#### Migración detallada

La migración se calcula en el cierre mensual de la provincia de origen.

```text
destinos candidatos = provincias a ≤ 30 días de viaje
                    ∪ la ciudad principal de su mercado
                    ∪ provincias con diáspora de su misma cultura o religión (hasta 3)

atractivo_j = 0,40 × salario_real_j / salario_real_ref
            + 0,25 × seguridad_j
            + 0,20 × tolerancia_j(cultura, religión)
            + 0,15 × tierra_libre_j            (solo para ocupaciones agrarias)

flujo_ij    = tamaño_i × α × max(0, atractivo_j − atractivo_i − umbral) / (1 + días_ij / 10)
```

| Parámetro | Valor inicial | Nota |
| --- | --- | --- |
| α | 0,02 | Fracción máxima teórica por mes antes del límite. |
| umbral | 0,10 | Las diferencias pequeñas no mueven a nadie (arraigo). |
| Límite por cohorte y mes | 1 % (población libre); 0 % para personas sin libertad de movimiento salvo huida | — |
| Huida (personas dependientes o esclavizadas) | Probabilidad mensual 0,2–2 % según agravio, control efectivo y cercanía de refugio | Se registra como huida, no como migración. |

**Refugiados.** Cuando la seguridad de una provincia cae por debajo de 0,30 (devastación, asedio, persecución), el límite del 1 % desaparece y hasta un 10 % mensual de cada cohorte afectada se desplaza a la provincia segura más cercana con tolerancia ≥ 0,5. Los refugiados llevan `origin = Refugee`, tienen un 30 % menos de productividad durante 12 meses y un 2 % mensual de probabilidad de **retorno** si su provincia recupera seguridad > 0,6. La llegada masiva de refugiados presiona los precios de alimentos del destino y puede bajar la tolerancia local: el sistema lo muestra en el “¿por qué?” de ambos lados.

**Diásporas.** Una cohorte fuera del núcleo de su cultura conserva un vínculo con él. El comercio entre provincias con diásporas de una misma cultura mercantil tiene una prima de riesgo un 20 % menor (redes de confianza) y las persecuciones en una provincia aumentan la emigración hacia las otras de la red.

#### Movilidad social detallada

```text
vacantes_destino = plazas libres en edificios para esa ocupación (o demanda de servicios)
flujo            = cohorte × β × min(1, vacantes / cohorte) × max(0, salario_dest / salario_orig − 1 − fricción)
```

| Paso de ocupación | β mensual | Fricción | Requisito |
| --- | --- | --- | --- |
| Campesino libre → jornalero urbano | 0,010 | 0,15 | Ciudad en el mismo mercado. |
| Jornalero → artesano | 0,004 | 0,30 | Gremio abierto o sin gremio; capital mínimo de 2 uc por persona. |
| Artesano → mercader | 0,002 | 0,40 | Capital de 20 uc por persona; alfabetización ≥ 20 %. |
| Cualquier libre → clero | 0,001 | 0,20 | Plazas en instituciones religiosas; puede exigir celibato (rasgo doctrinal). |
| Cualquiera → soldado profesional | Según contratación | 0 | El reclutamiento es una decisión del Estado o de un contratista. |
| Mercader → banquero | 0,0005 | 0,50 | Capital de 200 uc por persona; ley de préstamo con interés compatible. |
| Campesino dependiente → libre | **Solo por ley** o por huida | — | Se modela como cambio de condición jurídica, no como movilidad. |

El límite mensual de la v0.6 (0,5 %) se mantiene como tope por cohorte. La movilidad descendente (artesano arruinado → jornalero) ocurre cuando la riqueza por persona cae a cero y el ingreso no cubre la subsistencia durante tres meses seguidos.

#### Alfabetización

```text
alfabetización_adultos(t+1) = alf + (alf_objetivo − alf) × 1/240     # convergencia en ~20 años
alf_objetivo = base_ocupación × acceso_educativo(provincia) × multiplicador_técnico
```

| Ocupación (1300) | Base de alfabetización |
| --- | --- |
| Clero regular y secular | 60–90 % |
| Funcionarios y letrados | 90 % |
| Mercaderes y banqueros | 45–65 % |
| Artesanos urbanos | 10–20 % |
| Nobleza | 20–60 % según cultura |
| Campesinado | 1–3 % |

El acceso educativo depende de las instituciones de la provincia (escuelas parroquiales, madrasas, universidades). La imprenta y el papel barato aplican un multiplicador técnico de 1,3 y 1,15; la escolarización pública obligatoria (siglo XIX) eleva la base campesina hasta el 60–95 %. Los nacimientos heredan la alfabetización de los adultos multiplicada por el acceso educativo, así que el cambio es generacional y lento.

#### Movilización

```text
reserva_movilizable = adultos × 0,5 (varones) × aptitud (0,6–0,8) × fracción_legal(ley de ejército)
```

| Ley de ejército | Fracción legal de la reserva movilizable | Coste para la economía |
| --- | --- | --- |
| Levas feudales | 5–10 % (solo nobles y sus séquitos, más milicias locales) | Bajo: pocos trabajadores. |
| Milicia urbana | 10–15 % de artesanos y mercaderes, solo en defensa | Medio en ciudades. |
| Mercenarios | 0 % local; se contratan cohortes de soldados profesionales de otras regiones | Dinero, no trabajadores. |
| Ejército permanente | 1–3 % | Salarios continuos. |
| Conscripción masiva | 10–25 % | Muy alto: las plazas de los edificios quedan vacías. |

Los movilizados siguen perteneciendo a su cohorte (para no fragmentarla), pero **no trabajan** y su consumo pasa a pagarlo el ejército. Las bajas militares se restan de la franja de adultos de su cohorte de origen. Una guerra larga con conscripción vacía las plazas agrarias y baja la producción de grano: es la versión material del agotamiento bélico.

#### Urbanización y capacidad de las ciudades

Una provincia es **urbana** si más del 30 % de su población trabaja en ocupaciones no agrarias o si su núcleo supera 10.000 habitantes. La población urbana tiene un **techo blando**:

```text
techo_urbano = (alimento_importable_por_rutas + alimento_local_excedente) / consumo_per_cápita
             × factor_agua (acueductos, pozos, río)
```

Por encima del techo, la mortalidad urbana sube un 10 % por cada 10 % de exceso y la inmigración se frena. Constantinopla en 1300 depende del grano del mar Negro y de Tracia: si se pierde una de las dos fuentes, su techo baja y la ciudad empieza a vaciarse. La partida reproduce sin guion la decadencia demográfica de una capital sin hinterland.

#### Condición jurídica y contenido sensible en el modelo

- La condición jurídica es un campo de la cohorte, no una ocupación. Una cohorte `Enslaved` tiene ingreso 0; quien la explota cubre como mucho su cesta de subsistencia, con el NV resultante visible.
- Su agravio crece cada mes en función del trato (ley), del NV y de la represión; su **huida** y su **rebelión** usan los mismos sistemas que cualquier otra cohorte, sin reducción artificial.
- La **manumisión**, la abolición y la redención de cautivos son leyes y acciones del Estado o de particulares que cambian la condición jurídica; generan contribuciones visibles al registro causal y, cuando corresponde, demandas de grupos de interés.
- La captura de personas en guerra (cautivos, rescates) se modela como transferencia entre poblaciones con registro completo; los rescates usan el sistema de prisioneros de la sección 13.

#### Ejemplo resuelto: Bitinia en un mes de 1302

*Provincia de Nicea (Bitinia), mayo de 1302. Población: 38.000 personas. La frontera con el beylik otomano lleva meses con incursiones.*

| Paso | Cálculo | Resultado |
| --- | --- | --- |
| 1. Cobertura alimentaria | La cosecha local cubre el 85 % porque los saqueos han destruido el 20 % de los campos; el mercado de Constantinopla no compensa (el camino es inseguro). | Cobertura media de subsistencia 0,85; NV de los campesinos 0,85. |
| 2. Mortalidad | Base mensual ≈ 3,0 ‰ × `g_alimentos(0,85)` ≈ 1,32 × ciudad de Nicea (amurallada, sin saneamiento) 1,15 sobre su población urbana. | ≈ 150 muertes en el mes (≈ 115 en años normales). |
| 3. Natalidad | 20.900 adultos × 6,06 ‰ × `f_vida(0,85)` ≈ 0,96 × `f_paz(0,45)` ≈ 0,87. | ≈ 106 nacimientos (≈ 127 en años normales). |
| 4. Seguridad | 0,45 por las incursiones: por encima del umbral de refugiados (0,30). | Migración ordinaria, no refugiados. |
| 5. Migración | Atractivo de Nicea 0,41; de Constantinopla 0,62; de Nicomedia 0,47. Solo Constantinopla supera el umbral (diferencia 0,21 > 0,10). Flujo = 38.000 × 0,02 × 0,11 / (1 + 6/10). | ≈ 52 personas hacia Constantinopla (cohortes libres). |
| 6. Agravio | Impuesto de guerra + NV < 1 + derrota reciente en la región. | Agravio de los campesinos +1,8 puntos; apoyo a la aristocracia local −0,5. |
| 7. Resultado neto | 106 − 150 − 52. | **−96 personas en el mes**; si continúa un año, Nicea pierde un 3 % de su población y su recaudación cae más que proporcionalmente por el control efectivo. |

El panel de la provincia muestra: “Población −96 este mes. Mayores causas: falta de alimento (+35 muertes sobre lo normal), emigración a Constantinopla (−52), menos nacimientos por inseguridad (−21)”. Cada línea enlaza a su causa: los saqueos de la frontera, el camino inseguro y el impuesto de guerra.

#### Invariantes y pruebas específicas

| Invariante o prueba | Formulación |
| --- | --- |
| Conservación con fusión | La suma de tamaños antes y después de una fusión es idéntica (exacta en `Qty`). |
| Edad coherente | Las tres cuotas de edad suman exactamente 10.000 pb tras cada mes (el redondeo se asigna a la franja mayor). |
| Tope de cohortes | Ninguna provincia supera `MAX_COHORTES_PROVINCIA` tras el cierre mensual. |
| Condición jurídica | Nunca se fusionan cohortes de distinta condición jurídica (prueba de propiedad con 10.000 fusiones aleatorias). |
| Estabilidad secular | `pop_stability_200y`: sin crisis inyectadas, la población del slice varía entre −10 % y +40 % en 200 años. |
| Respuesta a hambruna | `famine_response`: cobertura 0,6 durante 6 meses produce un exceso de mortalidad entre el 3 % y el 6 %. |
| Refugiados acotados | Ninguna provincia recibe en un mes más refugiados que el 50 % de su población previa. |
| Determinismo del orden | El resultado de la migración es idéntico con 1 y con 16 hilos. |

## 10. Economía, producción y finanzas

### Cadena económica

**Recursos naturales → extracción → transformación → transporte → consumo o inversión.** Las industrias requieren trabajadores, capital, materias primas, energía y acceso a mercados.

### Bienes del slice (1300–1600)

| Bien | Origen | Uso principal |
| --- | --- | --- |
| Grano | Agricultura | Alimento básico, forraje, impuestos en especie. |
| Ganado | Pastoreo | Alimento, cuero, tracción. |
| Pescado | Pesca | Alimento; salazón para flotas. |
| Sal | Salinas y minas | Conservación; monopolio estatal frecuente. |
| Vino | Viñedos | Consumo, comercio, renta eclesiástica. |
| Aceite de oliva | Olivares | Alimento, iluminación, jabón. |
| Azúcar | Plantaciones (Chipre, Creta) | Lujo; motor de trabajo forzado posterior. |
| Madera | Bosques | Construcción, barcos, combustible. |
| Hierro | Minas y forjas | Herramientas, armas, armaduras. |
| Cobre y estaño | Minas | Bronce, artillería, moneda. |
| Plata y oro | Minas, comercio | Moneda; base de la masa monetaria. |
| Lana | Pastoreo | Textiles. |
| Paño | Talleres textiles | Bien manufacturado clave del comercio. |
| Seda | Sericultura e importación | Lujo; Bizancio y Persia. |
| Especias | Importación del Índico | Lujo; motor del comercio levantino. |
| Alumbre | Minas (Focea en Anatolia) | Mordiente imprescindible para teñir paño. |
| Pieles y cera | Comercio del mar Negro y del norte | Lujo y uso religioso. |
| Caballos | Cría | Caballería, transporte. |
| Pertrechos navales | Brea, cáñamo, velas | Construcción y mantenimiento de flotas. |
| Armas y armaduras | Talleres | Equipamiento militar. |

Cada bien tiene un **tipo de almacenamiento** (perecedero, almacenable, estratégico) que define si existen inventarios físicos o solo flujos.

### Edificios iniciales

| Categoría | Edificios |
| --- | --- |
| Agricultura | Campos, viñedos, olivares, huertas de regadío, pastos, molinos. |
| Extracción | Minas de hierro, plata, sal, alumbre; aserraderos; pesquerías. |
| Manufactura | Talleres textiles, forjas, curtidurías, astilleros, prensas de aceite, ingenios de azúcar. |
| Comercio | Mercados, ferias, lonjas, *fondachi* y factorías, aduanas, puertos. |
| Administración | Palacio, cancillería, tesoro, tribunal, casa de la moneda. |
| Religión y saber | Iglesias, mezquitas, monasterios, madrasas, universidades. |
| Militar | Castillos, murallas urbanas, arsenales, cuarteles, atalayas. |
| Infraestructura | Caminos, puentes, acueductos, canales, faros. |

Cada edificio tiene **modos de producción** (por ejemplo, “molino de agua” frente a “molino manual”) que cambian la relación entre insumos, trabajo y producto cuando se adopta una tecnología.

### Mercados y precios

- Cada región económica tiene un mercado. El precio de cada bien se ajusta cada semana según la relación entre demanda y oferta, con amortiguación para evitar oscilaciones.
- El comercio entre mercados se mueve por **rutas** con capacidad, coste por distancia, peajes y riesgo (piratería, guerra). Los mercaderes mueven bienes cuando la diferencia de precio supera el coste.
- El jugador ve, para cada precio, los **tres mayores contribuyentes** a su cambio (sequía, bloqueo, ejército acampado).

### Finanzas públicas

| Ingresos | Gastos |
| --- | --- |
| Impuesto sobre la tierra | Ejército y flota |
| Diezmo o impuestos en especie | Corte y administración |
| Aduanas y peajes | Fortificaciones e infraestructura |
| Monopolios (sal, alumbre) | Intereses de la deuda |
| Tributos de vasallos | Subsidios y tributos pagados |
| Acuñación (señoreaje) | Instituciones religiosas y educativas |
| Préstamos | Reconstrucción y ayuda en hambrunas |

La deuda tiene acreedores concretos (banqueros florentinos, genoveses, la propia nobleza); un impago arruina a esos acreedores y daña la capacidad futura de pedir prestado.

### Modelo económico (propuesto)

#### Producción

Cada edificio tiene un número de **plazas** por ocupación y un **modo de producción** con coeficientes fijos de insumos y productos (función de producción de proporciones fijas):

```text
nivel_actividad = min( trabajadores_empleados / plazas,
                       insumo_k_disponible / insumo_k_requerido   para cada insumo k )
producción      = nivel_actividad × producto_base × productividad
productividad   = f(tecnología, infraestructura, rasgos culturales, control efectivo, daño de guerra)
```

La proporción fija hace los cuellos de botella **visibles**: si falta hierro, la forja produce menos y el panel dice exactamente qué insumo limita.

#### Precios

```text
desequilibrio = (demanda − oferta) / max(oferta, mínimo)
precio(t+1)   = precio(t) × (1 + acotar(k × desequilibrio, −x, +x))
```

| Parámetro | Valor inicial | Función |
| --- | --- | --- |
| *k* (amortiguación) | 0,10 por semana | Evita oscilaciones. |
| *x* (límite de cambio) | ±10 % por semana | Impide saltos absurdos. |
| Precio mínimo y máximo | 0,2 y 10 veces el precio base | Mantiene la economía en un rango jugable. |

#### Comercio entre mercados

```text
margen        = precio_destino − precio_origen − coste_transporte − peajes − prima_de_riesgo
si margen > 0:  flujo = min( capacidad_ruta_libre, capital_mercantil / precio_origen,
                             0,2 × diferencia_de_existencias_necesaria_para_igualar_precios )
```

El ajuste parcial (20 % por semana) evita que todo el comercio salte de golpe a la ruta más rentable. Los mercaderes que hacen el comercio son cohortes reales, y su beneficio es ingreso de esas cohortes.

#### Ingresos, salarios y consumo

- El **valor añadido** de un edificio (ventas menos insumos) se reparte entre salarios, renta del propietario e impuestos según las leyes y la propiedad.
- Cada estrato tiene una **cesta** por persona y mes con tres niveles: subsistencia, comodidad y lujo. Se compra en orden de prioridad hasta agotar el ingreso.
- Los bienes de una misma categoría son **sustituibles** (grano y pescado como alimento; lana y lino como tejido), con proporciones que dependen de los precios.

#### Moneda

Cada Estado acuña monedas con un contenido de metal. Una **devaluación** genera ingresos inmediatos al tesoro, pero, a medida que los mercados la detectan, suben los precios en esa moneda y cae la confianza de los acreedores. La masa monetaria solo cambia por acuñación, fundición, pérdida o impago, siempre registrados.

#### Ejemplo resuelto: sequía en Tracia (1305)

| Paso | Qué ocurre | Dónde se ve |
| --- | --- | --- |
| 1 | La anomalía climática reduce la cosecha de grano de Tracia un 40 %. | Modo de mapa de clima; panel de provincia. |
| 2 | La oferta de grano del mercado de Constantinopla cae; el desequilibrio sube el precio un 10 % semanal hasta estabilizarse un 60 % por encima del base. | Panel de mercado: “¿por qué?” → sequía (−40 % oferta local). |
| 3 | El margen hace rentable importar grano de Crimea; los mercaderes genoveses lo traen por el mar Negro. | Rutas: aumento del volumen Caffa → Constantinopla. |
| 4 | Génova cobra más y gana peso político en Pera; Bizancio pierde ingresos aduaneros. | Diplomacia: dependencia comercial de Génova. |
| 5 | Las cohortes pobres urbanas no cubren su cesta; sube la mortalidad y el descontento. | Población y política: legitimidad baja entre los pobres urbanos. |
| 6 | El jugador puede abrir los graneros, prohibir exportaciones o negociar con Génova. | Cada opción muestra sus costes en el registro causal. |

### Invariantes contables

| Invariante | Formulación |
| --- | --- |
| Conservación de bienes | Existencias finales = iniciales + producción − consumo − destrucción ± comercio. |
| Conservación del dinero | Toda variación de la masa monetaria procede de una acuñación, una destrucción o un impago registrados. |
| Balance de deuda | Lo que un actor debe es exactamente lo que otro tiene a cobrar. |
| Población | Final = inicial + nacimientos − muertes ± migración. |
| No negatividad | Existencias, población y reservas nunca son negativas; los déficits se expresan como escasez. |

> **PRUEBA DE CAUSALIDAD**  
> Una campaña militar prolongada debe consumir hombres, suministros y tesorería; elevar la demanda de industrias bélicas, alterar el comercio y afectar a la legitimidad y a los hogares. Si una guerra no repercute en la economía, los sistemas están demasiado aislados.

### Especificación detallada de economía (v0.7, propuesto)

Base de `docs/specs/economy.md` y `docs/specs/state-finance.md`. Los precios y rendimientos son **valores de diseño** (confianza D salvo indicación) elegidos para que los órdenes de magnitud sean coherentes entre sí y con el Mediterráneo del siglo XIV. La Biblia histórica puede corregirlos; la calibración final la hace 101 Lab.

#### Unidad de cuenta

Toda la contabilidad interna usa una **unidad de cuenta (uc)** fija: el valor de 3,5 g de oro fino, equivalente aproximado al ducado veneciano de 1284. La uc **no es una moneda del juego**: es la vara de medir del motor, y no se devalúa nunca. Cada Estado acuña sus propias monedas, cuyo valor en uc depende de su contenido de metal y de la confianza del mercado.

| Moneda (1300) | Emisor | Metal | Valor de partida en uc | Confianza |
| --- | --- | --- | --- | --- |
| Ducado | Venecia | Oro, ~3,5 g | 1,00 | A (por definición) |
| Hiperpirón | Bizancio | Oro rebajado (≈ 50 % de ley o menos, en descenso) | 0,50 | C — verificar ley exacta en 1300 |
| Génova (genovino) | Génova | Oro, ~3,5 g | 1,00 | B |
| Grosso | Venecia | Plata, ~2,2 g | 0,045 | B |
| Aspro (akçe temprano y monedas selyúcidas) | Beyliks | Plata | 0,03 | C |
| Dinar de plata y monedas locales | Serbia, Bulgaria | Plata | 0,03–0,05 | C |
| Florín | Florencia | Oro, ~3,5 g | 1,00 | A |

**Relación oro/plata:** precio de mercado, no constante; valor inicial 1:11, con rango de 1:9 a 1:14 en los siglos XIV–XVI según flujos de metal (confianza B para el rango).

#### Precios base del slice (1300–1600)

| Bien | Unidad | Precio base (uc) | Almacenamiento | Pérdida mensual en almacén | Peso para transporte |
| --- | --- | --- | --- | --- | --- |
| Grano | tonelada | 9 | Almacenable | 1 % | 1 t |
| Arroz | tonelada | 11 | Almacenable | 1 % | 1 t |
| Legumbres | tonelada | 8 | Almacenable | 1 % | 1 t |
| Carne y ganado en pie | tonelada de carne | 30 | Perecedero (ganado vivo: almacenable) | 15 % (carne) | 1 t |
| Pescado (fresco / salado) | tonelada | 15 / 25 | Perecedero / almacenable | 20 % / 2 % | 1 t |
| Sal | tonelada | 20 | Almacenable | 0 % | 1 t |
| Aceite de oliva | hectolitro | 3 | Almacenable | 0,5 % | 0,09 t |
| Vino | hectolitro | 2 | Almacenable | 1 % | 0,1 t |
| Azúcar | quintal (50 kg) | 25 | Almacenable | 0,5 % | 0,05 t |
| Especias (mezcla) | quintal | 100 | Almacenable | 0,2 % | 0,05 t |
| Seda en bruto | quintal | 250 | Almacenable | 0,2 % | 0,05 t |
| Lana | quintal | 4 | Almacenable | 0,5 % | 0,05 t |
| Paño común / fino | pieza (~30 m) | 6 / 25 | Almacenable | 0,2 % | 0,03 t |
| Tejido basto (unidad de cesta) | unidad (~1 m²) | 0,2 | Almacenable | 0,2 % | 0,001 t |
| Alumbre | quintal | 3 | Almacenable | 0 % | 0,05 t |
| Hierro en barras | quintal | 2,5 | Almacenable | 0,1 % | 0,05 t |
| Cobre | quintal | 6 | Almacenable | 0 % | 0,05 t |
| Plata | kg | 10 | Estratégico | 0 % | — (mueve el Estado o el mercader) |
| Madera de construcción | tonelada | 1,5 | Almacenable | 0,5 % | 1 t |
| Leña | tonelada | 1,2 | Almacenable | 0,5 % | 1 t |
| Pertrechos navales | lote (equipo para una galera durante un año) | 120 | Almacenable | 0,5 % | 2 t |
| Caballo de silla / de guerra | cabeza | 12 / 45 | Estratégico | 0,5 % (mortalidad) | 0,5 t |
| Equipo de infantería | lote por soldado | 3 | Almacenable | 0,2 % | 0,02 t |
| Equipo de caballería pesada | lote por jinete | 40 | Almacenable | 0,2 % | 0,05 t |
| Pólvora (desde su adopción) | quintal | 8 | Estratégico | 0,5 % | 0,05 t |

**Comprobación de órdenes de magnitud:** la cesta de subsistencia del estrato bajo (sección 09) cuesta ≈ 0,23 uc por persona y mes (≈ 0,14 de alimento básico, 0,01 de sal, 0,024 de aceite, 0,03 de tejido, 0,03 de leña); unos 2,8 uc al año por persona y 12–14 uc por hogar campesino. El salario de un jornalero urbano del modelo ronda 1,2–1,8 uc al mes, coherente con la idea de que un hogar de trabajadores cubre la subsistencia y poco más.

#### Calendario agrícola

La producción agraria **no es mensual uniforme**: ocurre en los meses de cosecha y se almacena. El consumo sí es mensual. Por eso existen la escasez de primavera, la especulación con el grano y el valor estratégico de los graneros.

| Macrorregión | Cereal | Vid | Olivo | Otros |
| --- | --- | --- | --- | --- |
| Mediterráneo costero (Grecia, Tracia, Egeo, Chipre) | Junio–julio | Septiembre–octubre | Noviembre–enero | Hortalizas: marzo–octubre, 1/8 cada mes |
| Meseta anatolia | Julio–agosto | Septiembre | — | Ganado: partos en primavera; venta en otoño |
| Llanura panónica y Danubio | Julio–agosto | Septiembre–octubre | — | Mijo y avena: agosto |
| Costa del mar Negro y Crimea | Julio | Septiembre | — | Pesca: abril–noviembre |
| Delta del Nilo (externo) | Abril–mayo | — | — | Crecida: agosto–septiembre |

El clima del año (sección 15) multiplica la cosecha en el mes en que se recoge. Un año malo se nota **de golpe** en julio y se sufre durante los diez meses siguientes, a medida que se vacían los graneros.

#### Edificios de referencia del slice

Cada edificio se construye en **niveles**; un nivel es la unidad que se crea, se amplía o se destruye. Los valores son por nivel y por año (la producción agraria se concentra en los meses de cosecha).

| Edificio | Plazas por nivel | Modo inicial | Insumos anuales | Productos anuales | Coste de construcción | Mantenimiento anual |
| --- | --- | --- | --- | --- | --- | --- |
| Campos de cereal (100 ha, año y vez) | 25 campesinos | Arado ligero | 13 t grano (semilla) | 39 t grano | 150 uc + 2 años | 3 uc |
| Campos de cereal | 25 campesinos | Rotación trienal (tierras húmedas) | 15 t grano | 56 t grano | Requiere arado pesado; 80 uc de mejora | 4 uc |
| Olivar (50 ha) | 12 campesinos | Tradicional | 1 t herramientas eq. (0,4 uc) | 45 hl aceite | 200 uc + 8 años hasta plena producción | 2 uc |
| Viñedo (30 ha) | 15 campesinos | Tradicional | 2 uc en toneles | 150 hl vino | 180 uc + 4 años | 3 uc |
| Pastos (500 ha) | 6 pastores | Trashumante | — | 4 t carne, 30 quintales de lana, 60 cueros | 20 uc | 1 uc |
| Pesquería costera | 15 pescadores | Barcas | 0,5 lotes de pertrechos (60 uc) cada 5 años | 25 t pescado | 60 uc | 4 uc |
| Salina | 10 trabajadores | Evaporación solar | — | 120 t sal (julio–septiembre) | 120 uc | 3 uc |
| Molino de agua | 3 artesanos | Molino de agua | Grano | Harina (95 % del grano) con productividad 2,5 | 90 uc | 4 uc |
| Taller textil | 20 artesanos | Telar de pedal | 60 quintales de lana, 6 quintales de alumbre, tintes | 50 piezas de paño común | 100 uc | 5 uc |
| Forja | 6 artesanos | Forja manual | 30 quintales de hierro, 20 t leña o carbón vegetal | Herramientas (40 uc) o 60 lotes de equipo de infantería | 70 uc | 3 uc |
| Astillero (galeras) | 60 artesanos | Construcción en serie limitada | 300 t madera, 3 lotes de pertrechos | 1 galera ligera cada 8 meses | 600 uc | 30 uc |
| Mina de plata | 80 mineros | Pozos y galerías | 200 t madera, 40 quintales de hierro | 120 kg plata | 1.200 uc | 40 uc |
| Mina de alumbre (Focea) | 50 mineros | Calcinación | 400 t leña | 1.500 quintales de alumbre | 800 uc | 30 uc |
| Ingenio de azúcar | 40 trabajadores | Prensa hidráulica | 300 t caña, 150 t leña | 60 quintales de azúcar | 900 uc | 35 uc |

**Comprobación de la explotación agraria:** un nivel de campos de cereal en año y vez produce 39 t brutas, 26 t netas de semilla, que alimentan a unas 135 personas durante un año (192 kg/persona). Los 25 campesinos y sus familias (≈ 70 personas) consumen la mitad; el resto paga renta, diezmo e impuestos y abastece a las ciudades. Con la rotación trienal, la producción neta pasa de 26 t a 41 t (+58 %) y el excedente comercializable se duplica con creces, porque el consumo de las familias campesinas apenas cambia: la técnica tiene un efecto económico real y medible.

#### Algoritmo de precios con existencias

La v0.6 define el ajuste semanal; esta versión añade las existencias, que son las que dan inercia y sentido a la especulación:

```text
oferta_semana   = producción_local + importaciones + liberación_de_existencias
demanda_semana  = consumo + exportaciones + compras_para_existencias
existencias_obj = consumo_semanal_medio × semanas_de_reserva(bien)      # grano: 26 semanas tras la cosecha
presión         = (demanda − oferta) / max(oferta, mínimo)
                + 0,25 × (existencias_obj − existencias) / existencias_obj
precio(t+1)     = precio(t) × (1 + acotar(0,10 × presión, −10 %, +10 %))
```

Los mercaderes y los graneros públicos **compran para existencias** cuando el precio está por debajo del medio de 52 semanas y **liberan** cuando está por encima, con un límite del 10 % de las existencias por semana. El precio sube antes de que la escasez sea total, porque los mercados anticipan, y baja con lentitud tras la cosecha, porque los almacenes se reponen.

**Ejemplo numérico (grano en Tesalónica tras una mala cosecha):**

| Semana | Oferta (t) | Demanda (t) | Existencias / objetivo | Presión | Cambio aplicado | Precio (uc/t) |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.000 | 1.000 | 100 % | 0,00 | 0 % | 9,00 |
| 1 (cosecha −35 %) | 650 | 1.000 | 70 % | 0,54 + 0,075 | +6,2 % | 9,56 |
| 2 | 700 | 980 | 62 % | 0,40 + 0,095 | +5,0 % | 10,04 |
| 4 | 820 | 960 | 55 % | 0,17 + 0,11 | +2,8 % | 10,60 |
| 8 | 930 | 950 | 50 % | 0,02 + 0,125 | +1,5 % | 11,30 |
| 20 | 980 | 940 | 58 % | −0,04 + 0,105 | +0,6 % | 12,10 |

El precio sube rápido al principio y sigue subiendo lentamente mientras las existencias estén por debajo del objetivo, aunque el flujo semanal ya esté equilibrado. Es el comportamiento que el jugador reconoce como “escasez”, y el “¿por qué?” lo explica con dos líneas: “oferta local −35 % (sequía)” y “graneros por debajo de lo normal”.

#### Transporte: costes por medio

| Medio | Coste relativo por t·km | Coste base (uc por t·km) | Velocidad típica (km/día) | Notas |
| --- | --- | --- | --- | --- |
| Mar abierto (nave redonda) | 1 | 0,0008 | 80–120 | Estacional: −50 % de capacidad y +100 % de riesgo de noviembre a febrero. |
| Galera mercante | 2 | 0,0016 | 60–100 | Bienes de alto valor; más segura frente a piratas. |
| Río navegable | 4 | 0,0032 | 30–50 (aguas abajo), 15–25 (aguas arriba) | Danubio, Nilo; caudal estacional. |
| Camino con carros | 15 | 0,012 | 20–30 | Requiere camino; barro en otoño y deshielo. |
| Animales de carga | 25 | 0,020 | 25–35 | Montaña, estepa, desierto. |
| Caravana del desierto | 20 | 0,016 | 30–40 | Agua como recurso; peajes de oasis. |

**Consecuencia:** llevar grano 2.000 km por mar cuesta ≈ 1,6 uc/t (18 % de su precio base); llevarlo 300 km por tierra cuesta ≈ 3,6 uc/t (40 %). Por eso las ciudades costeras pueden importar grano lejano y las del interior pasan hambre con cosechas locales malas: la geografía decide sin reglas especiales.

**Prima de riesgo** = `valor_carga × (riesgo_piratería + riesgo_guerra + riesgo_meteorológico)`. Valores de partida en el Egeo: piratería 1–4 % por viaje según la presencia de flotas y beyliks corsarios; guerra 5–25 % si atraviesa zonas en guerra; meteorológico 1 % (verano) a 6 % (invierno). El seguro marítimo (tecnología) reduce la **varianza** del riesgo para el mercader, no el riesgo físico.

#### Capital mercantil

Cada mercado tiene un **capital mercantil** igual a la riqueza de sus cohortes de mercaderes y banqueros más el crédito disponible. El comercio de la sección 10 queda limitado por ese capital: una ciudad sin mercaderes ricos no puede aprovechar diferencias de precio aunque existan. Las colonias mercantiles extranjeras (barrios venecianos o genoveses) aportan **su propio capital**, con su origen registrado: así se ve, por ejemplo, que el 70 % del comercio de Constantinopla lo financia capital italiano.

#### Inversión privada

Cada cierre trimestral, las cohortes con capital evalúan construir o ampliar edificios:

```text
beneficio_anual_esperado = (precio_medio_52s(productos) × productos − precio_medio_52s(insumos) × insumos)
                           − salarios − mantenimiento
rentabilidad             = beneficio_anual_esperado / coste_de_construcción
se invierte si           rentabilidad > tipo_de_interés_local + prima_de_riesgo_provincial + 3 %
```

- La prima de riesgo provincial sube con la guerra, la baja seguridad y la inestabilidad política (0 % en paz a 15 % en frontera activa).
- Se invierte primero en el proyecto de mayor rentabilidad; como máximo un 30 % del capital de la cohorte por trimestre.
- La construcción consume bienes reales (madera, piedra, herramientas) del mercado durante su duración y emplea a jornaleros.
- Las leyes de propiedad deciden **quién** puede invertir (en una economía de *pronoia*, los grandes terratenientes; en una república mercantil, cualquier mercader).

El Estado también puede construir (gasto público) y el jugador puede subvencionar o prohibir tipos de edificio. El asesor económico (F-ADV-01) aplica las mismas reglas con los límites que el jugador fije.

#### Fiscalidad detallada

| Impuesto | Base | Fórmula de recaudación mensual | Notas |
| --- | --- | --- | --- |
| Impuesto sobre la tierra | Valor de la producción agraria | `tipo × producción × control × eficacia − coste_de_recaudación` | Se recauda sobre todo tras la cosecha (60 % en los dos meses siguientes). |
| Capitación | Personas libres | `tipo_por_persona × población_sujeta × control` | Regresivo; alto agravio entre los pobres. |
| Diezmo (para el clero) | Producción agraria | 10 % nominal; efectivo 5–8 % | No es del Estado: financia instituciones religiosas. |
| Aduanas (*kommerkion* y análogos) | Valor del comercio que entra o sale | `tipo × valor × (1 − exención_del_comerciante)` | Venecianos y genoveses con exenciones totales o parciales por privilegio. |
| Peajes de paso | Tráfico en estrechos, puentes, puertas | `tarifa × tráfico` | Fuente clave para quien controle el Bósforo o los Dardanelos. |
| Monopolios | Sal, alumbre, seda | `margen × ventas` | Pueden arrendarse a particulares. |
| Señoreaje | Acuñación | `(valor_facial − valor_metal − coste) × monedas acuñadas` | La devaluación lo aumenta temporalmente. |
| Tributos de vasallos | Contrato | Cantidad fija o proporcional | Su cobro depende de la lealtad del vasallo. |
| Contribuciones extraordinarias | Votadas por asamblea o impuestas | Proporcional a la riqueza de los estamentos | Exigen negociación o generan agravio. |

**Eficacia de recaudación** = `capacidad_administrativa_relativa × (1 − corrupción) × alfabetización_de_funcionarios`, entre 0,30 (Estado feudal fragmentado) y 0,90 (burocracia moderna). **Coste de recaudación** = 5–15 % de lo recaudado según el sistema.

**Arrendamiento de impuestos (F-ECO-15).** El Estado subasta la recaudación de una provincia por un precio fijo anual, cobrado por adelantado o en dos plazos:

```text
precio_de_subasta ≈ recaudación_esperada × (0,70 a 0,85)
recaudación_del_arrendatario = recaudación_esperada × presión_extra (1,10 a 1,40)
agravio_extra = f(presión_extra) en las cohortes afectadas
```

El Estado gana liquidez inmediata y certidumbre; pierde un 15–30 % del rendimiento y paga con agravio. El arrendatario es una cohorte (o un personaje) real que se enriquece y gana poder político. Es la mecánica que explica por qué Estados débiles venden su fiscalidad y por qué eso los debilita más.

#### Deuda pública

| Instrumento | Época | Plazo | Tipo de interés orientativo | Acreedores típicos |
| --- | --- | --- | --- | --- |
| Préstamo de banqueros | 1300+ | 6 meses – 3 años | 8–20 % anual (más con riesgo alto) | Compañías bancarias italianas, mercaderes |
| Préstamo forzoso urbano consolidado | 1300+ (repúblicas) | Perpetuo | 4–5 % | Ciudadanos de la república |
| Empeño de joyas, rentas o territorios | 1300+ | Hasta la devolución | Implícito alto | Banqueros, Estados vecinos, órdenes |
| Rentas sobre ingresos (juros, *rentes*) | 1450+ | Perpetuo o vitalicio | 5–8 % | Particulares, instituciones |
| Deuda de banco público | 1600+ | Variable | 3–6 % | Accionistas, mercado |
| Bonos negociables | 1700+ | 10–40 años | 3–6 % | Mercado financiero |

```text
tipo_ofrecido = tipo_base(época, mercado) + prima_de_riesgo
prima_de_riesgo = 2 % × (deuda / ingresos_anuales)
                + 6 % × impagos_recordados       (cada impago pesa 1,0 y decae a la mitad en 15 años)
                + 3 % × (1 − estabilidad_política)
                − 2 % × garantías (rentas o territorios empeñados)
```

**Impago.** Si el servicio de la deuda supera el dinero disponible tras los gastos mínimos (ejército en campaña, corte básica), el Estado elige o se ve forzado a:

| Opción | Efecto inmediato | Efecto duradero |
| --- | --- | --- |
| Suspensión de pagos | Libera el servicio de la deuda | Acreedores arruinados (pérdida de riqueza de cohortes concretas); +1 impago recordado. |
| Quita negociada (20–60 %) | Reduce el principal | +0,5 impago recordado; los acreedores aceptan si la alternativa es peor. |
| Conversión a perpetua a menor interés | Reduce el servicio | Pérdida de confianza moderada. |
| Confiscación (de acreedores extranjeros o de minorías) | Liquidez inmediata | Agravio diplomático, huida de capital, persecución registrada. |
| Devaluación para pagar en moneda depreciada | Alivia en el corto plazo | Inflación, pérdida de confianza en la moneda. |

Las bancarrotas no son castigos abstractos: arruinan a acreedores reales, que pueden ser la base de un grupo de interés o de una potencia extranjera (la quiebra de una gran compañía bancaria puede desencadenar una crisis en su ciudad de origen).

#### Moneda y devaluación

```text
valor_metal(moneda)       = ley × peso × precio_del_metal
valor_percibido(t+1)      = valor_percibido + (valor_metal − valor_percibido) × velocidad_de_detección
velocidad_de_detección    = 1/6 mensual (≈ semivida de 4 meses) en mercados con cambistas y ensayadores;
                            1/18 en mercados rurales o aislados
señoreaje_de_devaluación  = (valor_percibido − valor_metal) × monedas_nuevas_acuñadas
```

Mientras el mercado no detecta la devaluación, el Estado paga con moneda sobrevalorada (ganancia inmediata). Cuando la detecta, los precios en esa moneda suben en la misma proporción y los acreedores exigen pagos en moneda fuerte o en uc. **Ley de Gresham:** si dos monedas circulan con el mismo valor facial y distinto contenido de metal, la buena se atesora o se exporta (las existencias de moneda buena caen un 5 % mensual hacia el exterior).

**Nivel de precios por mercado.** Además de los precios relativos, cada mercado tiene un **nivel de precios** expresado en uc que responde lentamente a la masa monetaria:

```text
nivel_objetivo = (masa_monetaria × velocidad) / producción_real
nivel(t+1)     = nivel + (nivel_objetivo − nivel) × 1/36      # ajuste mensual lento
```

La entrada masiva de plata americana (siglo XVI) eleva el nivel de precios de forma gradual y desigual por mercados, según su conexión con Sevilla, Génova y Amberes: la revolución de los precios emerge del comercio de metal.

#### Gremios y ferias

- **Gremios (F-ECO-13):** un gremio controla las plazas de una ocupación en un mercado. Si la ley lo permite, limita la entrada (fricción de movilidad +0,30), fija un precio mínimo (precio no puede bajar del 90 % de la media de 52 semanas) y exige calidad (productividad +5 %). Obtiene poder político proporcional a la riqueza de sus cohortes y entra en conflicto con los mercaderes que quieren importar.
- **Ferias (F-ECO-14):** un mercado con feria multiplica por 3 su capacidad de comercio y reduce un 50 % los peajes durante las semanas de la feria; atrae capital mercantil de mercados a ≤ 20 días. Las ferias crecen si su seguridad y sus privilegios se mantienen, y mueren si la ruta se desplaza.

#### Ejemplo resuelto: presupuesto bizantino de partida (1300)

Cifras **propuestas** para el estado inicial (confianza C). La historiografía atribuye al imperio de Andrónico II unos ingresos del orden de un millón de hiperpirones anuales hacia 1320 (confianza B); con el hiperpirón a ≈ 0,5 uc, el presupuesto de partida ronda 500.000 uc.

| Ingresos | uc/año | Gastos | uc/año |
| --- | --- | --- | --- |
| Impuesto sobre la tierra (Tracia, Macedonia, islas) | 230.000 | Mercenarios y guarniciones | 190.000 |
| Impuestos urbanos de Constantinopla y Tesalónica | 80.000 | Corte, ceremonial y palacio | 85.000 |
| Aduanas (*kommerkion*, mermado por exenciones italianas) | 55.000 | Administración y recaudación | 60.000 |
| Monopolios y peajes | 45.000 | Subsidios y pagos a aliados | 45.000 |
| Señoreaje | 25.000 | Fortificaciones y obras | 30.000 |
| Otros (multas, confiscaciones, tributos) | 30.000 | Instituciones religiosas y caridad | 35.000 |
| — | — | Intereses de la deuda | 25.000 |
| **Total** | **465.000** | **Total** | **470.000** |

El imperio empieza con un **déficit pequeño pero estructural**, sin flota y con exenciones aduaneras que regalan una parte del comercio a sus rivales. El primer problema del jugador bizantino ya está en el presupuesto, no en un evento: cualquier guerra lo desborda, y las salidas (devaluar, arrendar impuestos, gravar a la Iglesia, renegociar privilegios con Venecia y Génova, contratar menos mercenarios) tienen costes que el registro causal enumera.

#### Invariantes y pruebas específicas

| Prueba | Criterio |
| --- | --- |
| `economy_closed_100y` | Conservación exacta de bienes y dinero en un escenario cerrado sin comercio externo. |
| `harvest_shock` | Una cosecha −40 % en un mercado aislado sube el precio entre +40 % y +90 % en 20 semanas y vuelve al ±15 % del base en dos cosechas normales. |
| `transport_gradient` | Con una sola fuente de grano, el precio aumenta con la distancia según la tabla de costes (±5 %). |
| `debasement_detection` | Una devaluación del 20 % se refleja en precios en 12 ± 4 meses en un mercado con cambistas. |
| `tax_farm_tradeoff` | El arrendamiento aumenta la liquidez inmediata y reduce la recaudación anual entre un 15 % y un 30 %. |
| `default_creditors` | Un impago reduce exactamente la riqueza de los acreedores registrados por el importe impagado. |
| `investment_response` | Si el precio de un bien sube un 50 % durante dos años, la capacidad de producción privada aumenta en el mercado sin intervención del Estado. |

## 11. Gobierno, instituciones y política

La autoridad depende de instituciones, legitimidad, élites, grupos sociales, burocracia, leyes, capacidad fiscal y control territorial. El motor representa todos los regímenes con **las mismas primitivas parametrizables**: actor, institución, competencia, lealtad y recurso.

### Tipos de gobierno como combinaciones

| Régimen | Quién decide | Cómo se legitima | Ejemplos en 1300 |
| --- | --- | --- | --- |
| Monarquía feudal | Rey con grandes vasallos | Dinastía, religión, juramentos | Francia, Castilla, Hungría |
| Monarquía burocrática | Soberano con funcionarios | Tradición imperial, religión | Bizancio, Yuan |
| Sultanato militar | Élite militar | Poder, religión, protección | Mamelucos |
| República oligárquica | Consejos de familias mercantiles | Constitución urbana | Venecia, Génova |
| Comuna gremial | Gremios y asambleas | Participación ciudadana | Florencia |
| Teocracia | Autoridad religiosa | Mandato divino | Estados Pontificios |
| Orden militar | Maestre y capítulo | Misión religiosa | Orden Teutónica, Hospitalarios |
| Kanato / confederación tribal | Kan y nobleza tribal | Linaje, victoria | Horda de Oro, Chagatai |
| Beylik fronterizo | Bey y guerreros | Botín, guerra fronteriza | Otomanos, Karasi |

Más adelante, las mismas primitivas permiten monarquías absolutas, constitucionales, repúblicas parlamentarias, regímenes de partido único, federaciones y juntas militares.

### Estamentos y grupos de interés

| Grupo | Quiere | Puede hacer |
| --- | --- | --- |
| Nobleza | Tierras, exención fiscal, cargos | Rebelarse, negar levas, apoyar pretendientes |
| Clero | Rentas, autoridad moral, exenciones | Excomulgar, legitimar o deslegitimar |
| Burguesía mercantil | Rutas seguras, bajos aranceles, crédito | Prestar o negar crédito, financiar facciones |
| Gremios | Monopolios, regulación | Huelgas, revueltas urbanas |
| Campesinado | Tierra, impuestos bajos, paz | Revueltas, huida, bandolerismo |
| Ejército profesional | Pago puntual, prestigio | Motines, golpes de Estado |

Cada grupo tiene **poder** (según riqueza, número y organización), **lealtad** y **demandas**. Las leyes y decisiones cambian su lealtad; su poder decide qué ocurre cuando están descontentos.

### Leyes iniciales (categorías y ejemplos)

| Categoría | Opciones de ejemplo |
| --- | --- |
| Sucesión | Primogenitura, elección, tanistry, rotación, designación |
| Tierra | Feudo hereditario, *pronoia*/*iqta* (concesión revocable), propiedad libre, propiedad eclesiástica |
| Impuestos | En especie, en moneda, arrendamiento fiscal, catastro |
| Religión | Religión oficial exclusiva, tolerancia de minorías, autonomía comunitaria (*millet*), persecución |
| Ejército | Levas feudales, mercenarios, milicia urbana, ejército permanente |
| Comercio | Libre comercio, privilegios a extranjeros, monopolios estatales, prohibiciones |
| Justicia | Señorial, real, religiosa, mixta |

### Capacidad del Estado y control

- **Alcance administrativo:** cada Estado puede gestionar eficazmente un número de provincias que depende de burocracia, comunicaciones e infraestructura. Más allá, crecen la corrupción, la evasión fiscal y el separatismo.
- **Control efectivo** por provincia (0–100 %): fracción del territorio donde las órdenes se cumplen. Determina la recaudación real y el reclutamiento.
- **Legitimidad:** aceptación del régimen por cada grupo; puede ser alta para unos y baja para otros.

### Cálculos clave del gobierno (propuesto)

```text
control_objetivo  = capacidad_administrativa × 1 / (1 + días_de_viaje_al_centro / D0)
                    × (1 − penalización_por_cultura_o_religión_ajena)
control(t+1)      = control(t) + 0,05 × (control_objetivo − control(t))    [mensual]
D0                = días de viaje a los que el control cae a la mitad; depende de las comunicaciones
                    (orientativo: 15 días en 1300, 30 con correo organizado, 90+ con telégrafo)

legitimidad_g     = suma de contribuciones para el grupo g (dinastía, religión compartida, victorias,
                    demandas atendidas, leyes afines, prosperidad), registradas en el registro causal

presión_rebelde_g = descontento_g × poder_g × (1 − control_medio)
```

Cuando la presión de un grupo supera umbrales sucesivos, pasa por **agitación → movimiento → rebelión**. En cada etapa aparecen demandas concretas que el gobierno puede atender, negociar o reprimir. Reprimir reduce la presión a corto plazo y aumenta el agravio a largo plazo.

**Capacidad administrativa** = funcionarios cualificados × eficacia institucional − corrupción. Crece con la burocracia, la alfabetización y la tecnología de registros (papel, contabilidad, imprenta, estadística).

### Rebeliones y guerras civiles

Las rebeliones tienen **bando, programa y apoyos**: una revuelta campesina pide menos impuestos; una facción noble apoya a un pretendiente; una ciudad quiere autonomía. Pueden negociarse, reprimirse o triunfar, y cada salida cambia leyes, élites y fronteras.

### Especificación detallada de gobierno y política (v0.7, propuesto)

Base de `docs/specs/politics.md`. Escalas: legitimidad, lealtad, apoyo y presión se expresan de 0 a 100 en la interfaz y como `Ratio` en el motor.

#### Las cinco primitivas, formalizadas

| Primitiva | Definición | Campos principales | Ejemplo (Venecia, 1300) |
| --- | --- | --- | --- |
| **Actor** | Persona o colectivo con preferencias y capacidad de actuar. | Tipo (personaje, grupo de interés, institución corporativa), preferencias por categoría de ley, recursos. | El dux; las familias del patriciado; los *popolani* ricos. |
| **Institución** | Órgano con reglas de composición y decisión. | Miembros (qué actores la forman), regla de decisión (unanimidad, mayoría, mayoría cualificada, decisión personal), quórum, mandato. | Gran Consejo (cerrado desde la *Serrata* de 1297), Senado, Consejo de los Cuarenta. |
| **Competencia** | Derecho a decidir sobre una materia. | Materia, titular (institución), veto (otra institución que puede bloquear), plazo. | Impuestos: Gran Consejo; política exterior: Senado; justicia criminal: Cuarenta. |
| **Lealtad** | Disposición de un actor a obedecer y sostener a otro. | De quién a quién, valor 0–100, componentes registrados. | Patriciado → república: alta; dux → patriciado: vigilado. |
| **Recurso** | Lo que un actor puede movilizar. | Dinero, tropas, votos, clientela, legitimidad religiosa, información. | Capital mercantil, galeras, votos en el Consejo. |

**Competencias del catálogo** (cada régimen las asigna a sus instituciones): `taxation`, `extraordinary_taxation`, `war_and_peace`, `treaties`, `legislation`, `justice`, `appointments`, `succession`, `coinage`, `religion`, `military_command`, `land_grants`. Una decisión del jugador que toca una competencia que no controla directamente se convierte en una **propuesta** a la institución titular.

**Tipos de gobierno de 1300 como plantillas de datos:**

| Plantilla | Instituciones | Quién tiene `extraordinary_taxation` | Quién tiene `succession` |
| --- | --- | --- | --- |
| Monarquía feudal | Rey, consejo real, curia de grandes vasallos, asamblea estamental (si existe) | Asamblea estamental o consentimiento de los grandes vasallos | Ley de sucesión + reconocimiento de los grandes |
| Monarquía burocrática | Emperador, consejo, administración central, Iglesia | Emperador (con riesgo de agravio) | Designación del emperador + aclamación |
| República oligárquica | Consejos de patricios, magistraturas electivas | Consejo mayor | Elección por el consejo |
| Sultanato militar | Sultán, emires, cuerpo de mamelucos, ulemas | Sultán, condicionado a la lealtad de los emires | Elección de facto por los emires |
| Beylik fronterizo | Bey, guerreros de frontera, derviches, notables | Bey | Familia del bey (sin regla fija) |
| Kanato | Kan, *kurultai*, nobleza tribal | Kan | *Kurultai* entre descendientes del linaje |
| Orden militar | Maestre, capítulo general | Capítulo | Elección por el capítulo |
| Teocracia | Autoridad religiosa, curia | Autoridad religiosa | Elección por el colegio religioso |

#### Grupos de interés en 1300

| Grupo | Composición (cohortes y personajes) | Preferencias típicas |
| --- | --- | --- |
| Aristocracia terrateniente | Nobleza con tierras, *pronoiarios*, timariotas (más tarde) | Tierra hereditaria, exención fiscal, cargos militares, sin centralización. |
| Clero y monasterios | Clero secular y regular; instituciones con tierras | Exención fiscal, autoridad doctrinal, propiedad inalienable. |
| Mercaderes y banqueros | Cohortes mercantiles locales | Rutas seguras, bajos aranceles, crédito al Estado con garantías. |
| Colonias mercantiles extranjeras | Venecianos, genoveses, pisanos, catalanes en puertos ajenos | Privilegios aduaneros, barrios autónomos, protección. |
| Gremios y artesanos | Cohortes urbanas organizadas | Monopolios, regulación de precios, protección frente a importaciones. |
| Pueblo urbano | Jornaleros, pobres urbanos | Pan barato, empleo, limosnas, seguridad. |
| Campesinado | Libres y dependientes | Impuestos bajos, paz, tierra, fin de cargas señoriales. |
| Ejército y mercenarios | Soldados profesionales, compañías, guardia | Paga puntual, botín, prestigio, tierras. |
| Guerreros de frontera (*gazi*, *akritai*) | Cohortes militares fronterizas | Guerra de botín, autonomía, tierras conquistadas. |
| Ulemas y órdenes sufíes | Juristas, cadíes, derviches | Ley religiosa, fundaciones piadosas (*waqf*), influencia sobre el gobernante. |

#### Poder de un grupo

```text
poder_bruto_g = 0,35 × riqueza_relativa_g + 0,20 × número_relativo_g
              + 0,25 × organización_g     + 0,20 × control_institucional_g
poder_g       = poder_bruto_g / Σ poder_bruto        (los poderes de un Estado suman 1)
```

| Componente | Cómo se mide | Cómo puede cambiarlo el jugador |
| --- | --- | --- |
| Riqueza relativa | Riqueza de sus cohortes / riqueza total del Estado | Impuestos, confiscaciones, concesiones de tierras y monopolios. |
| Número relativo | Población de sus cohortes / población total | Muy lento (demografía, migración). |
| Organización (0–1) | Instituciones propias (gremio, orden, asamblea), cohesión cultural, líderes con capacidad | Prohibir o reconocer gremios y asambleas; cooptar líderes. |
| Control institucional (0–1) | Cuota de cargos y escaños que ocupa | Nombramientos, venta de cargos, reformas administrativas. |

Un grupo numeroso pero sin organización (el campesinado) tiene poco poder cotidiano, aunque su **presión rebelde** puede ser enorme: el modelo distingue poder político ordinario y capacidad de revuelta.

#### Proceso de reforma de una ley

Una ley no cambia con un clic. El proceso tiene etapas visibles:

| Etapa | Duración | Qué ocurre | Riesgo |
| --- | --- | --- | --- |
| 1. Propuesta | Inmediata | El jugador elige la nueva opción; el panel muestra el apoyo y la oposición previstos por grupo. | Ninguno. |
| 2. Negociación | 1–6 meses (según régimen y competencia) | El jugador puede ofrecer **concesiones** a grupos concretos para cambiar su postura. | Los opositores con poder > 0,20 pueden convocar una asamblea, negar fondos o conspirar. |
| 3. Decisión | Un día | Se aplica la regla de decisión de la institución titular. | Si fracasa, coste de legitimidad para quien la impulsó (−3 a −10 con los grupos que la apoyaban). |
| 4. Implantación | 12–60 meses | Los efectos crecen linealmente desde 0 hasta el 100 %; la resistencia puede frenarla. | Si la presión de los perjudicados supera 70, la implantación se detiene y aparece una rebelión con programa “derogar la ley”. |

**Regla de decisión para gobiernos personales** (monarquías, sultanatos, beyliks): la ley se aprueba si

```text
autoridad_del_soberano + Σ_g poder_g × apoyo_g  >  1,2 × Σ_g poder_g × oposición_g
autoridad_del_soberano = 0,15 a 0,45 según legitimidad propia, capacidad del gobernante y control del ejército
```

**Regla para asambleas y consejos:** cada grupo representado vota según su postura ponderada por sus escaños; la ley exige la mayoría de la institución (simple, de dos tercios o unanimidad según los datos del régimen).

**Concesiones disponibles** (cada una con coste real y registrado):

| Concesión | Coste | Efecto típico sobre la postura del grupo |
| --- | --- | --- |
| Cargo para un miembro del grupo | Control institucional del grupo +0,02; pérdida de eficacia si el elegido es incompetente | +5 a +15 |
| Exención fiscal temporal | Ingresos perdidos durante N años | +10 a +25 |
| Concesión de tierras | Tierra de la Corona o confiscada; riqueza del grupo + | +15 a +30 |
| Pago en dinero | Tesoro | +1 por cada 0,5 % de los ingresos anuales del Estado, hasta +20 |
| Promesa de una ley futura | Si no se cumple en el plazo, agravio doble | +10 a +20 |
| Matrimonio con la familia gobernante | Opción dinástica consumida | +20 a +35 (solo aristocracia) |
| Represión de los líderes | Agravio duradero; riesgo de mártires | La oposición baja a corto plazo y la presión rebelde sube a medio |

#### Legitimidad

La legitimidad se calcula **por grupo**. La legitimidad nacional es la media ponderada por poder, y la estabilidad del Estado (variable visible) se deriva de ella.

| Contribución | Valor | Duración o decaimiento | Grupos más sensibles |
| --- | --- | --- | --- |
| Dinastía establecida (≥ 3 generaciones) | +20 | Permanente mientras dure | Aristocracia, clero |
| Unción o investidura religiosa | +10 a +15 | Permanente durante el reinado | Clero, campesinado |
| Religión compartida con el gobernante | +10 | Permanente | Todos |
| Religión distinta tolerada / perseguida | −5 / −25 | Mientras dure la política | El grupo afectado |
| Victoria importante | +8 | Decae a la mitad en 3 años | Ejército, aristocracia |
| Derrota importante | −10 | Decae a la mitad en 4 años | Ejército, aristocracia |
| Usurpación | −30 | Decae a la mitad en 15 años | Todos |
| Demanda atendida | +5 a +15 | Decae a la mitad en 5 años | El grupo demandante |
| Demanda ignorada tras un ultimátum | −10 a −20 | Decae a la mitad en 8 años | El grupo demandante |
| Prosperidad (NV medio del grupo) | (NV − 1) × 15 | Recalculado cada mes | Pueblo urbano, campesinado |
| Impuesto extraordinario sin consentimiento | −8 a −15 | Mientras dure + 2 años | Los grupos que lo pagan |
| Hambruna no atendida | −15 | Decae a la mitad en 5 años | Pueblo urbano, campesinado |
| Gobernante menor de edad o regencia | −10 | Mientras dure | Aristocracia |

```text
legitimidad_g = clamp(50 + Σ contribuciones_g, 0, 100)
legitimidad   = Σ_g poder_g × legitimidad_g
estabilidad   = legitimidad − 0,5 × presión_rebelde_máxima + 10 × control_medio − 10
```

El punto de partida de 50 representa la aceptación pasiva de cualquier poder establecido. Por debajo de 30 en un grupo con poder > 0,15 aparecen demandas formales; por debajo de 15, conspiraciones o movimientos (según el grupo).

#### Control efectivo: ejemplo resuelto

Bizancio en 1300, capacidad administrativa relativa 0,85 (burocracia heredada, pero con funcionarios insuficientes), D0 = 15 días (sin correo organizado).

| Provincia | Días de viaje al centro (ruta más rápida) | Penalización cultural o religiosa | Control objetivo | Lectura |
| --- | --- | --- | --- | --- |
| Constantinopla | 0 | 0 | 0,85 × 1 / (1 + 0) = **85 %** | Núcleo. |
| Adrianópolis | 5 (camino) | 0 | 0,85 / 1,33 = **64 %** | Tracia, buen control. |
| Tesalónica | 6 (mar) / 12 (tierra) | 0 | 0,85 / 1,40 = **61 %** | El mar acerca la segunda ciudad. |
| Mistrá (Morea) | 10 (mar + tierra) | 0 | 0,85 / 1,67 = **51 %** | El déspota local gobierna casi solo. |
| Nicea (Bitinia) | 4, pero camino inseguro: ×2 | 0 | 0,85 / 1,53 = **56 %** | Inseguridad = distancia. |
| Filadelfia (Lidia) | 18 (ya incluye el recargo por inseguridad) | −15 % (población mixta y presión turca) | 0,85 / 2,20 × 0,85 = **33 %** | Enclave casi autónomo. |

**Inseguridad como distancia:** los días de viaje se multiplican por 2 si la ruta atraviesa provincias con seguridad < 0,5 y por 4 si cruza territorio enemigo. Recuperar la seguridad de un camino aumenta el control de toda la región que depende de él, una relación que el jugador puede ver en el modo de mapa de control.

**Alcance administrativo.** Cada provincia consume capacidad: `coste_provincia = 1 + 0,02 × población_en_miles + 0,5 × (si es urbana)`. Si la suma de costes supera la capacidad, el control objetivo de **todas** las provincias se multiplica por `capacidad / suma_de_costes` y la corrupción sube un 2 % por cada 10 % de exceso. Expandirse sin funcionarios degrada lo que ya se tenía.

#### Capacidad administrativa y corrupción

```text
capacidad_administrativa = funcionarios_cualificados × eficacia_institucional × (1 − corrupción)
funcionarios_cualificados = cohortes de letrados y funcionarios × alfabetización
eficacia_institucional    = 0,4 (base) + tecnología de registros (papel +0,05, partida doble +0,05,
                            imprenta +0,10, estadística +0,10…) + leyes (catastro +0,10, carrera
                            burocrática +0,10)

corrupción(t+1) = corrupción + 0,02 × (corrupción_objetivo − corrupción)        [mensual]
corrupción_objetivo = 0,10 + 0,25 × venta_de_cargos + 0,15 × salarios_insuficientes
                    + 0,10 × exceso_de_alcance − 0,15 × inspección (cargo de control activo)
```

La corrupción reduce la recaudación, la eficacia de las órdenes y la calidad de los ejércitos de levas, y **aumenta la riqueza** de las cohortes de funcionarios: tiene ganadores visibles, lo que explica por qué cuesta reducirla.

#### Cargos principales

Los cargos son competencias delegadas en personajes. Su ocupante aporta su capacidad (0–20) y sus rasgos.

| Cargo genérico | Ejemplo bizantino | Ejemplo veneciano | Ejemplo otomano temprano | Efecto de la capacidad del titular |
| --- | --- | --- | --- | --- |
| Canciller / primer ministro | *Mesazōn* | Gran canciller | Visir (desde la década de 1320) | Eficacia institucional ± 0,005 por punto sobre 10 |
| Tesorero | *Logothetēs tou genikou* | Procuradores y camarlengos | Defterdar (más tarde) | Eficacia de recaudación ± 1 % por punto |
| Comandante del ejército | Gran doméstico | Capitán general | Hermanos e hijos del bey | Mando de ejércitos sin general asignado |
| Comandante de la flota | Megaduque | Capitán general del mar | — | Mando naval |
| Autoridad religiosa (si es nombrada) | Patriarca (elegido con presión imperial) | Patriarca de Grado | Jeque sufí cercano al bey | Legitimidad religiosa y relación con el clero |
| Gobernador regional | Déspota, *kephalē* | Duque de Candía, *bailo* | *Uç beyi* (señor de la marca) | Control efectivo +1 % por punto sobre 10 en su región; riesgo de autonomía si su lealtad es baja |

#### Presión rebelde, demandas y salidas

```text
presión_rebelde_g = descontento_g × (0,5 × poder_g + 0,5 × capacidad_de_revuelta_g) × (1 − control_medio_g)
descontento_g     = (100 − legitimidad_g) × (1 + agravio_medio_g)
capacidad_de_revuelta_g = número_relativo × (armas disponibles, tradición militar, líderes) 
```

| Umbral de presión (0–100) | Estado | Qué ocurre |
| --- | --- | --- |
| < 20 | Calma | Nada visible. |
| 20–45 | Agitación | Aparece una **demanda** concreta en el panel político (rebaja de un impuesto, destitución de un ministro, privilegio). Recaudación del grupo −10 %. |
| 45–70 | Movimiento | Líder identificado (personaje generado o existente); asambleas, impagos, deserciones; posible apoyo extranjero. Recaudación −30 %, reclutamiento −50 % entre sus cohortes. |
| > 70 | Rebelión | Ejército rebelde = 1–6 % de las cohortes del grupo (más con tradición militar o apoyo noble); controla las provincias donde su fuerza supera la guarnición. |

| Respuesta | Efecto inmediato | Efecto a largo plazo |
| --- | --- | --- |
| Atender la demanda | Presión −40 a −60 | Puede generar nuevas demandas si el grupo gana poder; coste de la concesión. |
| Negociar parcialmente | Presión −20 a −30 | Agravio estable. |
| Reprimir | Presión −30 si la fuerza basta | Agravio +15 que decae a la mitad en 10 años; riesgo de mártires (presión de otros grupos +5). |
| Ignorar | Nada | Escala al umbral siguiente en 3–12 meses. |

**Guerra civil.** Una rebelión se convierte en guerra civil cuando controla al menos el 25 % de las provincias del Estado, o cuando un grupo con poder > 0,25 (normalmente la aristocracia o el ejército) la apoya con un pretendiente. En la guerra civil, el Estado se divide en dos bandos con su propio tesoro, ejército y legitimidad; la paz puede reunificarlo, partirlo o cambiar la dinastía.

#### Privilegios estamentales como contratos

Cada privilegio es una cláusula con contrapartida, registrada como ley del Estado y visible para el grupo que la disfruta:

| Privilegio | Contrapartida esperada | Revocarlo |
| --- | --- | --- |
| Exención fiscal de la nobleza | Servicio militar personal con séquito | Ingresos + / lealtad noble −20 a −35 |
| Inmunidad de las tierras monásticas | Oraciones, caridad, legitimidad religiosa | Ingresos + / legitimidad del clero −25 |
| Jurisdicción señorial | Orden local sin coste para el Estado | Control + / poder noble − / coste judicial |
| Fueros urbanos | Pago anual y milicia | Ingresos variables / revuelta urbana posible |
| Barrio autónomo extranjero | Comercio y aranceles negociados | Ingresos aduaneros + / guerra comercial con la metrópoli del barrio |
| Monopolio gremial | Calidad y orden urbano | Precios − / gremios −30 |

#### Ejemplo resuelto: gravar las tierras monásticas en Bizancio

| Paso | Detalle |
| --- | --- |
| Propuesta | El jugador quiere retirar la inmunidad fiscal a los monasterios de Tracia y Macedonia (+28.000 uc anuales esperados). |
| Posturas | Clero (poder 0,22): oposición 90. Aristocracia (0,30): oposición 30 (teme ser la siguiente). Mercaderes (0,10): apoyo 40. Ejército (0,16): apoyo 70 (quiere su paga). Pueblo urbano (0,12): neutral. Campesinado (0,10): apoyo 20. |
| Cálculo | Apoyo ponderado: 0,10 × 0,40 + 0,16 × 0,70 + 0,10 × 0,20 = 0,172. Oposición: 0,22 × 0,90 + 0,30 × 0,30 = 0,288. Autoridad del emperador: 0,25. Prueba: 0,25 + 0,172 = 0,422 > 1,2 × 0,288 = 0,346 → **se aprobaría**. |
| Riesgo | La legitimidad del clero bajaría unos 25 puntos (de 62 a 37); el patriarca puede condenar la medida y la presión rebelde del clero subiría hasta la agitación. |
| Alternativa mostrada | Concesión a la aristocracia (exención de sus nuevas tierras en Macedonia) para que su oposición baje a 10, o reforma parcial (solo monasterios con más de N parroquias). |

El jugador ve el resultado previsto **antes** de decidir, con la explicación de cada número. La incertidumbre (la reacción exacta del patriarca, las posturas futuras) se muestra como rango, no como secreto.

#### Pruebas específicas

| Prueba | Criterio |
| --- | --- |
| `power_sums_to_one` | En todo Estado y mes, Σ poder_g = 1 exactamente (redondeo asignado al grupo mayor). |
| `reform_cannot_skip` | Ninguna ley alcanza efectos completos antes de su periodo de implantación. |
| `overextension_bites` | Duplicar las provincias sin aumentar funcionarios reduce el control medio del núcleo al menos un 20 %. |
| `rebellion_has_program` | Toda rebelión tiene un grupo, un líder y al menos una demanda resoluble. |
| `civil_war_resolves` | En 100 campañas, toda guerra civil termina en reunificación, partición o cambio de régimen en ≤ 25 años. |

## 12. Diplomacia, alianzas e inteligencia

### Relaciones multidimensionales

| Dimensión | Qué mide | Cómo cambia |
| --- | --- | --- |
| Confianza | Fiabilidad percibida | Tratados cumplidos o rotos |
| Interés | Beneficio mutuo actual | Comercio, enemigos comunes |
| Agravio | Ofensas acumuladas | Guerras, insultos, reclamaciones; decae con el tiempo |
| Amenaza | Peligro percibido | Poder relativo, proximidad, agresividad |
| Afinidad | Cercanía cultural, religiosa, dinástica | Lenta |
| Dependencia | Necesidad económica o militar | Comercio, préstamos, protección |

### Acciones diplomáticas

| Acción | Efecto |
| --- | --- |
| Enviar embajada | Mejora la información y la confianza; permite negociar. |
| Proponer tratado | Conjunto de cláusulas (alianza, comercio, paso militar, tributo, matrimonio). |
| Matrimonio dinástico | Crea vínculos y posibles reclamaciones. |
| Garantizar independencia | Compromiso de defensa con coste reputacional si se incumple. |
| Exigir tributo | Vasallaje parcial a cambio de no atacar. |
| Ofrecer vasallaje | Protección a cambio de autonomía. |
| Subsidiar | Dinero a cambio de influencia o apoyo militar. |
| Mediar | Interviene en una guerra ajena para lograr la paz. |
| Excomunión o condena religiosa | Para actores religiosos; daña la legitimidad del objetivo. |
| Declarar la guerra | Requiere un motivo; sin él, la legitimidad y la confianza ajena caen. |

### Motivos de guerra (casus belli)

Reclamación dinástica, reclamación territorial histórica, defensa de correligionarios, cruzada o yihad (con condiciones), represalia por agravio, independencia, apoyo a un pretendiente, ruptura de tratado, control de una ruta comercial, guerra preventiva. Cada motivo define objetivos de guerra aceptables y su coste de legitimidad.

### Negociación de paz

La paz se compone de cláusulas: cesiones territoriales, reparaciones, liberación de vasallos, cambios de dinastía, derechos comerciales, desmilitarización, intercambio de rehenes. La puntuación bélica limita lo que se puede exigir; las cláusulas demasiado duras generan agravio duradero y deseo de revancha.

### Información imperfecta

Cada actor decide con lo que sabe, no con el estado real. Lo que conoce de otros depende de la distancia, las comunicaciones de la época, el comercio y la inteligencia. En 1300 las noticias tardan semanas; en 2000, minutos.

### Inteligencia y operaciones encubiertas

Reconocimiento, infiltración, contraespionaje, propaganda, sabotaje, soborno de cortesanos, apoyo a rebeldes y robo tecnológico. Cada operación tiene coste, probabilidad de éxito, riesgo de descubrimiento y consecuencias diplomáticas si se descubre.

### IA diplomática

Una alianza se mantiene mientras aporta beneficios o mientras romperla tiene costes. La IA reconoce amenazas, valora compromisos, negocia y reacciona a cambios de poder, y registra la explicación de cada decisión estratégica.

### Especificación detallada de diplomacia (v0.7, propuesto)

Base de `docs/specs/diplomacy.md`. Las relaciones son **direccionales**: lo que Venecia piensa de Génova no es lo que Génova piensa de Venecia.

#### Dimensiones de la relación: rangos y dinámica

| Dimensión | Rango | Valor neutro | Dinámica mensual | Principales causas de cambio |
| --- | --- | --- | --- | --- |
| Confianza | 0–100 | 50 | Converge hacia 50 a un 1 % mensual | Tratado cumplido +2/año; tratado roto −20 a −40; espía descubierto −10; ayuda en guerra +15. |
| Interés | −100 a +100 | 0 | Recalculado cada mes | Comercio mutuo, enemigo común, dependencia, rivalidad por las mismas rutas o tierras. |
| Agravio | 0–100 | 0 | Decae a la mitad en 10 años (20 si hay reclamación activa) | Guerra +10 a +40; pérdida de provincias +15 por provincia núcleo; insulto diplomático +5; persecución de correligionarios +10. |
| Amenaza | 0–100 | 0 | Recalculada cada mes (ver fórmula) | Poder relativo, proximidad, agresividad, información. |
| Afinidad | −50 a +50 | 0 | Muy lenta (décadas) | Misma religión +15, misma familia religiosa +5, mismo grupo cultural +10, dinastía emparentada +5 a +20. |
| Dependencia | 0–100 | 0 | Recalculada cada mes | Cuota del comercio exterior que pasa por el otro; deuda con él; protección militar recibida. |

El **interés** se calcula, no se acumula:

```text
interés_ij = 30 × comercio_ij / comercio_total_i
           + 25 × enemigos_comunes (normalizado por su amenaza)
           − 30 × rivalidad_territorial (reclamaciones cruzadas, fronteras disputadas)
           − 20 × rivalidad_comercial (mismas rutas, mismos mercados)
           + 15 × dependencia_ij
```

#### Disposición a aceptar una propuesta

```text
aceptación = utilidad_de_las_cláusulas_para_el_receptor            (estimada por su IA, sección 17)
           + 0,30 × (confianza − 50)
           + 0,20 × interés
           − 0,40 × agravio
           + 0,10 × afinidad
           + ajuste_por_personalidad (diplomático +10, paranoico −10, vengativo −0,2 × agravio)
se acepta si aceptación > umbral(tipo de tratado)
```

| Tipo de tratado | Umbral |
| --- | --- |
| Acuerdo comercial | 0 |
| Derecho de paso | 10 |
| Tregua o paz | según puntuación bélica (ver abajo) |
| Alianza defensiva | 25 |
| Alianza ofensiva | 40 |
| Vasallaje voluntario | 50 (o amenaza > 70 de un tercero) |
| Matrimonio dinástico | 15 |

La pantalla de negociación muestra la aceptación prevista **por cláusula**, con su contribución, para que el jugador construya un tratado aceptable en lugar de probar a ciegas.

#### Catálogo de cláusulas

| Cláusula | Parámetros | Obligación | Coste de romperla |
| --- | --- | --- | --- |
| Paz / tregua | Duración (años) | No atacar | Confianza −40 con el afectado, −15 con todos los que lo saben; legitimidad −10 |
| Alianza defensiva | Duración; ámbito (todas las guerras o contra un rival) | Entrar en guerra si el otro es atacado | Confianza −30; agravio +15 |
| Alianza ofensiva | Objetivo; reparto previsto | Atacar conjuntamente | Confianza −25 |
| Derecho de paso | Duración; ejércitos o flotas | Permitir tránsito | Confianza −10 |
| Neutralidad | Duración | No unirse a enemigos | Confianza −20 |
| Comercio preferente | Arancel reducido (%); duración | Aplicar el arancel | Confianza −10; interés −15 |
| Exención aduanera | % de exención; mercados | No cobrar aduana | Confianza −20; posible casus belli “ruptura de tratado” |
| Barrio o factoría | Provincia; autonomía | Ceder un barrio con jurisdicción propia | Agravio +20; casus belli |
| Tributo | Cantidad anual o % de ingresos | Pagarlo | Casus belli automático para el receptor |
| Subsidio | Cantidad, duración, condición | Pagar si se cumple la condición | Confianza −15 |
| Préstamo | Principal, interés, garantías | Devolver | Impago (sección 10) |
| Vasallaje | Contrato (ver abajo) | Según contrato | Rebelión o casus belli |
| Matrimonio | Personajes; acuerdo sobre herencia | Celebrarlo | Confianza −15; agravio +10 |
| Rehenes | Personaje; duración | Custodiarlo con seguridad | Si se le ejecuta: agravio +50 |
| Cesión territorial | Provincias | Entregar el control | — (se ejecuta al firmar) |
| Reparaciones | Cantidad y plazos | Pagar | Casus belli |
| Desmilitarización | Provincia o estrecho; duración | No fortificar ni guarnecer | Casus belli |
| Liberación de prisioneros | Lista o “todos” | Liberar | Agravio +20 |
| Reconocimiento de título | Título (rey, emperador, sultán) | Reconocer | Agravio +10 |
| Garantía de independencia | Garante, protegido | Defender al protegido | Confianza −30 con el protegido y −10 con todos |

Un tratado es **un conjunto de cláusulas** con fecha de inicio y de fin. Las cláusulas pueden ser asimétricas, y el motor comprueba que no sean contradictorias (no se puede firmar una alianza con dos Estados en guerra entre sí sin una cláusula de excepción).

#### Vasallaje como contrato

| Cláusula del contrato | Valores posibles |
| --- | --- |
| Tributo | 0–30 % de los ingresos del vasallo, o cantidad fija |
| Contingente militar | 0–50 % de su ejército a petición, con límite de meses por año |
| Política exterior | Libre / consulta obligatoria / controlada por el señor |
| Sucesión | Libre / confirmación del señor / designación del señor |
| Justicia y religión | Autonomía total / apelación al señor |
| Protección | El señor defiende al vasallo (obligación con coste reputacional) |

**¿Seguir o independizarse?** La IA del vasallo evalúa cada año:

```text
utilidad_seguir        = protección × amenaza_externa + beneficios_comerciales + afinidad
                         − coste_del_tributo − coste_de_los_contingentes − agravio_hacia_el_señor
utilidad_independencia = autonomía_ganada − amenaza_externa_sin_protección
                         − probabilidad_de_guerra_con_el_señor × coste_esperado_de_esa_guerra
se rebela si utilidad_independencia − utilidad_seguir > 15 y la ocasión es buena
             (señor en guerra, en regencia o con ejército inferior al del vasallo + aliados)
```

Los vasallos no esperan a una cifra arbitraria: aprovechan **ocasiones**. Un señor en guerra civil pierde vasallos; uno victorioso los retiene aunque cobre más.

#### Amenaza y coaliciones

```text
amenaza_ij = 100 × poder_relativo_j_sobre_i (0–1, saturado a 3×)
           × proximidad_ij       (1 si son vecinos; 0,6 a ≤ 15 días; 0,3 a ≤ 45 días; 0,1 más lejos)
           × agresividad_j       (0,3 + expansión_reciente_j, que suma 0,1 por provincia tomada
                                  por la fuerza y decae a la mitad en 10 años)
           × fiabilidad_de_la_información_ij (0,5–1,0)
poder_relativo = (ejército_estimado + 0,5 × flota_estimada + 0,3 × ingresos_estimados) del otro
                 / los propios, todo según la información disponible
```

Una **coalición defensiva** se forma cuando al menos dos Estados tienen amenaza > 60 hacia el mismo país, interés mutuo ≥ 0 y no están en guerra entre sí. Cada candidato decide entrar con su propia utilidad (sección 17), y el panel diplomático explica la decisión: “Serbia se une porque la amenaza otomana es 74 y comparte enemigo con Hungría; Bulgaria no se une porque su agravio con Serbia es 58”. La coalición se disuelve cuando la amenaza media de sus miembros baja de 40 durante dos años o cuando logra su objetivo.

#### Motivos de guerra (casus belli)

| Motivo | Requisito | Objetivos permitidos | Coste de legitimidad al declarar | Agravio que genera |
| --- | --- | --- | --- | --- |
| Reclamación dinástica | Personaje con reclamación válida | Trono, unión personal, provincias reclamadas | 0 | Medio |
| Reclamación territorial histórica | Reclamación con fuerza ≥ 30 | Provincias reclamadas | 0 a −5 | Medio |
| Defensa de correligionarios | Persecución activa de su religión | Cambiar la política religiosa, liberar provincias | 0 (+5 con el clero) | Medio |
| Guerra santa | Doctrina activa y convocatoria de una autoridad religiosa (o rasgo de frontera) | Conquista amplia, tributo | +5 con el clero; −10 con minorías | Alto |
| Represalia | Agravio ≥ 40 por una ofensa concreta | Reparaciones, humillación, una provincia | 0 | Bajo |
| Ruptura de tratado | El otro rompió una cláusula | La cláusula, reparaciones | 0 | Bajo |
| Apoyo a un pretendiente | Pretendiente en la corte propia | Cambio de gobernante | −3 | Medio |
| Independencia | Ser vasallo o provincia rebelde | Independencia | 0 | Medio |
| Control de una ruta | Interés comercial ≥ 30 y rivalidad en la ruta | Barrios, exenciones, provincias costeras | −5 | Medio |
| Guerra preventiva | Amenaza ≥ 70 | Desmilitarización, una provincia | −8 | Alto |
| Guerra de frontera (incursión) | Tradición fronteriza; vecino de otra religión | Botín, tributo, provincias limítrofes | 0 en la frontera; −5 en el centro | Bajo pero acumulativo |
| Sin motivo | — | Cualquiera | −20 y confianza −20 con todos | Muy alto |

#### Puntuación bélica

```text
puntuación_bando = 40 × cumplimiento_de_objetivos       (control de lo declarado, ponderado)
                 + 25 × ocupación_ponderada               (valor económico y simbólico de lo ocupado)
                 + 20 × balance_de_batallas               (bajas infligidas / recibidas, ponderadas por
                                                           tamaño, con decaimiento: las batallas antiguas
                                                           pesan menos)
                 + 15 × agotamiento_del_rival             (sección 13)
puntuación neta = puntuación_propia − puntuación_rival      (−100 a +100)
```

**Coste de las cláusulas de paz en puntuación:**

| Cláusula exigida | Coste |
| --- | --- |
| Cada provincia ocupada y declarada objetivo | 8–25 según su valor |
| Provincia no declarada | ×2 (y agravio doble) |
| Reparaciones | 1 punto por cada 2 % de los ingresos anuales del perdedor |
| Tributo anual | 3 puntos por cada 1 % de ingresos, por cada 10 años |
| Exención aduanera o barrio | 10–20 |
| Cambio de gobernante | 40 |
| Vasallaje | 30–60 según tamaño |
| Liberación de prisioneros | 0–5 |

**Aceptación de la IA:** acepta una paz si `puntuación_neta_rival ≥ coste_total`, o si su propio agotamiento supera 70 (acepta pagar más), o si su información indica que seguir empeora su posición. Las paces muy duras (coste > 80) generan agravio adicional de +20 y una reclamación de revancha que dura 50 años.

#### Información imperfecta

```text
retraso_de_noticias_ij (días) = días_de_viaje_de_un_mensajero(i, j) × factor_de_red
factor_de_red = 1,0 (sin red) | 0,7 (embajada permanente) | 0,5 (correo organizado) | 0,05 (telégrafo) | ≈0 (radio y redes)
error_de_estimación = ±(40 % − 10 % × nivel_de_inteligencia − 15 % si hay embajada − 10 % si hay comercio intenso)
                      con mínimo ±5 %
```

| Información | Cómo se presenta | Ejemplo |
| --- | --- | --- |
| Tamaño de ejércitos | Rango | “Entre 4.000 y 7.000 hombres (estimación de hace 18 días)”. |
| Tesoro y deuda | Categoría | “Endeudado; dificultades para pagar a sus tropas”. |
| Alianzas secretas | Conocidas o no | Solo con inteligencia o si se activan. |
| Muerte de un gobernante | Con retraso | Una muerte en Tabriz llega a Constantinopla en 3–5 semanas. |
| Movimientos de flotas | Retraso + zona | “Flota avistada al sur de Eubea hace 6 días”. |

La IA decide con estas mismas estimaciones (sección 17); por eso puede equivocarse, y la interfaz puede mostrar después la diferencia entre lo que creía y lo que era cierto.

#### Operaciones encubiertas

| Operación | Coste | Duración | Éxito base | Descubrimiento si falla / si tiene éxito | Efecto |
| --- | --- | --- | --- | --- | --- |
| Red de informadores | 0,5 % de ingresos/año | Continua | — | 5 % anual | Nivel de inteligencia +1 (máx. 3) |
| Soborno de un cortesano | 2–20 uc × rango | 1–3 meses | 50 % | 40 % / 10 % | Información interna; voto o postura favorable |
| Apoyo a rebeldes | Dinero o armas | Continua | Según fuerza rebelde | 30 % anual | Presión rebelde +10 a +25 en el objetivo |
| Propaganda (desde la imprenta) | Dinero | 3–12 meses | 60 % | 20 % / 20 % | Legitimidad de un grupo −5 a −15 en el objetivo |
| Sabotaje de un astillero o almacén | 30–200 uc | 1–2 meses | 35 % | 60 % / 25 % | Destruye un 20–50 % de la producción o existencias |
| Robo de técnica | 50–500 uc | 6–24 meses | 25 % (+ afinidad técnica) | 50 % / 20 % | Progreso de descubrimiento +30 a +70 % de la técnica |
| Asesinato | Muy alto | 1–6 meses | 15 % | 80 % / 50 % | Muerte del objetivo; agravio +60 si se descubre; legitimidad −20 para el autor descubierto |

Toda probabilidad se tira con el RNG por contador y se registra; el informe de una operación fallida muestra qué factores la hicieron fracasar.

#### Ejemplo resuelto: el tratado veneciano-bizantino tras la guerra de 1296–1302

*Situación de trabajo (confianza B para el marco general; las cifras son de diseño).* Venecia y Bizancio llevan años en guerra; Venecia ha saqueado islas del Egeo y exige indemnizaciones por los daños sufridos por sus mercaderes. Bizancio está agotado y sin flota.

| Cláusula propuesta por Venecia | Coste en puntuación | Aceptación bizantina (contribución) |
| --- | --- | --- |
| Tregua de 10 años | 0 | +25 (necesita la paz) |
| Indemnización a los mercaderes venecianos (≈ 4 % de los ingresos anuales bizantinos) | 2 | −8 |
| Confirmación de la exención aduanera veneciana | 15 | −20 |
| Venecia conserva islas ocupadas del Egeo | 25 | −30 |
| **Puntuación neta veneciana: +38** | **Total: 42** | **Suma: −33 + relación (confianza 30, agravio 45)** |

La IA bizantina rechaza el paquete completo (coste 42 > 38). La interfaz de Venecia sugiere retirar una isla (−12): el tratado resultante (coste 30) se acepta porque la puntuación lo permite y el agotamiento bizantino (68) lo hace preferible a seguir. El agravio bizantino sube a 55 y queda una reclamación sobre la isla retenida: semilla de la siguiente crisis.

#### Pruebas específicas

| Prueba | Criterio |
| --- | --- |
| `treaty_consistency` | Ningún Estado queda obligado a la vez a defender y a atacar al mismo actor. |
| `coalition_forms` | Un Estado que conquista 10 provincias en 10 años provoca una coalición en ≥ 60 % de las campañas si hay al menos dos vecinos con amenaza > 60. |
| `vassal_opportunism` | La tasa de rebelión de vasallos se multiplica al menos por 3 durante las guerras civiles del señor. |
| `information_lag` | La IA reacciona a la muerte de un gobernante lejano con un retraso igual al de las noticias (±1 día). |
| `peace_terminates` | En 100 campañas, ninguna guerra dura más de 40 años sin una tregua intermedia. |

## 13. Guerra, logística y mando militar

### Un marco militar único con doctrinas por época

Cada fuerza tiene personal, experiencia, equipamiento, moral, organización, mando y suministros. La forma de combatir cambia según doctrina, comunicaciones, movilidad y tecnología, pero todo usa el mismo modelo de fuerza.

### Unidades por época (tierra)

| Época | Tipos de unidad | Reclutamiento |
| --- | --- | --- |
| 1300–1450 | Caballería pesada, caballería ligera, arqueros a caballo, arqueros y ballesteros, infantería de lanzas, milicias, máquinas de asedio | Levas feudales, mercenarios (compañías), milicias urbanas, guerreros tribales |
| 1450–1600 | Piqueros, arcabuceros, gendarmes, caballería ligera, artillería de asedio y de campaña | Mercenarios, primeros ejércitos permanentes, *timar* y jenízaros |
| 1600–1800 | Infantería de línea con mosquete y bayoneta, dragones, artillería de campaña | Ejércitos permanentes, reclutamiento forzoso |
| 1800–1914 | Infantería con fusil, artillería de retrocarga, caballería, ingenieros | Conscripción masiva, reservas |
| 1914–1945 | Infantería, ametralladoras, artillería pesada, blindados, aviación | Movilización total |
| 1945+ | Mecanizada, blindada, aerotransportada, misiles, fuerzas especiales | Profesional o conscripción |

### Resolución de batallas (propuesto)

1. **Contacto:** se comparan reconocimiento y mando para decidir quién elige el terreno.
2. **Fases:** cada día de batalla tiene fases de proyectiles, choque y persecución; la doctrina determina el peso de cada una.
3. **Desgaste:** pérdidas por fuego y choque, modificadas por terreno, equipo, experiencia y fortificaciones.
4. **Moral y organización:** cuando caen por debajo de un umbral, la unidad se retira o se desbanda.
5. **Persecución:** la caballería y la movilidad convierten una retirada en desastre.
6. **Informe:** la pantalla de batalla muestra la contribución de cada factor.

### Asedios

| Factor | Efecto |
| --- | --- |
| Fortificación | Nivel de murallas y su adaptación a la artillería. |
| Guarnición | Tamaño, moral, comida almacenada. |
| Suministro del sitiador | Si se agota, el asedio fracasa o el ejército se dispersa. |
| Epidemia en el campamento | Riesgo creciente con el tiempo y el clima. |
| Artillería | Abre brechas según calibre y tecnología. |
| Bloqueo naval | Necesario en ciudades costeras. |
| Asalto | Rápido y costoso; puede fracasar. |
| Rendición negociada | Según moral, hambre y condiciones ofrecidas. |

### Fórmulas de combate y asedio (propuestas)

```text
fuerza_efectiva  = efectivos × equipamiento(0–1) × organización(0–1) × suministro(0–1)
ancho_de_frente  = límite de tropas que combaten a la vez según terreno y época;
                   el resto queda en reserva y entra cuando hay bajas o retiradas
daño_por_fase    = fuerza_efectiva_comprometida × letalidad(arma, fase, época)
                   × mod(terreno, fortificación, doctrina, mando, experiencia)
                   × aleatoriedad acotada (0,85–1,15, del RNG por contador)
pérdida_moral    = daño_recibido / efectivos × sensibilidad_moral(doctrina, experiencia, causa)
retirada         = si moral < 30 %; desbandada si moral < 10 % y sin línea de retirada
```

Las bajas de una batalla se dividen en **muertos, heridos (recuperables), prisioneros y desertores**. Los heridos vuelven si hay suministro y tiempo; los prisioneros entran en la negociación de paz.

```text
progreso_asedio  = (potencia_de_artillería + zapadores + asalto_preparado)
                   ÷ (nivel_de_fortificación × moral_de_la_guarnición)
comida_guarnición(t+1) = comida(t) − consumo_diario × efectivos   (si hay bloqueo total)
probabilidad_de_rendición_mensual = f(hambre, moral, brecha abierta, condiciones ofrecidas)
```

#### Ejemplo: por qué falla un asedio

| Factor | Valor | Efecto |
| --- | --- | --- |
| Fortificación | Murallas de nivel alto, no adaptadas a la artillería | Reduce el progreso a un tercio. |
| Artillería del sitiador | Ninguna | Progreso casi nulo salvo por hambre. |
| Bloqueo naval | No: la ciudad recibe grano por mar | La comida de la guarnición no baja. |
| Suministro del sitiador | 60 % por agotamiento de la comarca | Desgaste del 3 % mensual por hambre y enfermedad. |
| **Conclusión que muestra la interfaz** | “El asedio no avanza: sin artillería ni bloqueo naval, la ciudad puede resistir indefinidamente.” | El jugador sabe qué cambiar. |

### Logística

- Cada provincia tiene **capacidad de suministro** según producción local, estación y daño. Un ejército mayor que la capacidad sufre desgaste.
- Las **rutas de suministro** llevan bienes desde depósitos; su capacidad depende de caminos, ríos, mar y (después) ferrocarril.
- **Forrajeo y saqueo** permiten sobrevivir a costa de la población local, con consecuencias demográficas y políticas.

### Guerra naval

Galeras (dependientes de costa y de remeros), naves redondas, carracas, galeones, navíos de línea, acorazados, portaaviones, submarinos. Las flotas controlan zonas marítimas, protegen o atacan el comercio, transportan ejércitos y bloquean puertos.

### Dos escalas de decisión

- **Estratégica:** objetivos de guerra, presupuestos, producción, diplomacia y movilización.
- **Operacional:** campañas, ejércitos, áreas de suministro, asedios, planes y frentes.

La microgestión táctica no es una prioridad. La IA militar ejecuta operaciones delegadas y explica por qué falla un avance.

### Especificación detallada militar (v0.7, propuesto)

Base de `docs/specs/military.md`. Las cifras de unidades son **relativas** (una infantería de lanzas media vale 10 en choque) y se calibran con 101 Lab y con batallas de referencia documentadas.

#### Organización de una fuerza

```text
Ejército
├── comandante (personaje) y estado mayor (personajes secundarios, opcional)
├── compañías (unidad mínima, 100–1.000 hombres en 1300)
│     ├── tipo de unidad, hombres, equipo (0–1), experiencia (0–100)
│     ├── moral (0–100), organización (0–100), origen (leva, mercenaria, permanente…)
│     └── contrato (si es mercenaria) y cohorte de origen (si es leva)
├── tren: carros, animales de carga, existencias de alimento y forraje
└── orden activa (marchar, asediar, devastar, perseguir, defender, invernar)
```

#### Unidades de 1300–1450 (valores iniciales)

| Tipo | Reclutamiento (uc/hombre) | Paga (uc/hombre/mes) | Consumo (GE/día) | Velocidad relativa | Choque | Proyectil | Defensa | Persecución | Moral base |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Caballería pesada (caballeros, *kataphraktoi* tardíos) | 45 + caballo de guerra | 3,0 | 1,0 + 8 kg forraje | 1,0 | 30 | 0 | 14 | 8 | 70 |
| Caballería ligera | 15 + caballo | 1,2 | 0,9 + 6 kg forraje | 1,4 | 12 | 2 | 6 | 14 | 55 |
| Arqueros a caballo | 15 + 2 caballos | 1,2 | 0,9 + 10 kg forraje | 1,5 | 8 | 14 | 6 | 16 | 60 |
| Infantería pesada (hombres de armas a pie) | 20 | 1,5 | 0,9 | 0,8 | 16 | 0 | 16 | 2 | 65 |
| Infantería de lanzas | 4 | 0,6 | 0,8 | 0,9 | 10 | 0 | 12 | 2 | 50 |
| Almogávares (infantería ligera de choque) | 5 | 1,0 | 0,7 | 1,1 | 14 | 3 | 8 | 6 | 70 |
| Arqueros y ballesteros | 6 | 0,8 | 0,8 | 0,9 | 3 | 12 | 6 | 3 | 45 |
| Milicia urbana | 2 | 0,3 (solo en servicio) | 0,8 | 0,8 | 6 | 3 | 9 | 1 | 40 |
| Guerreros tribales y de frontera | 1 | botín | 0,8 | 1,2 | 8 | 6 | 5 | 10 | 55 |
| Ingenieros y zapadores | 8 | 1,0 | 0,8 | 0,7 | 2 | 0 | 4 | 0 | 40 |
| Máquinas de asedio (trabuquete, por máquina con dotación) | 60 | 6 | 15 hombres × 0,8 | 0,5 | — | Asedio 6 | — | — | — |
| Bombarda (desde su adopción, por pieza) | 120 + pólvora | 10 | 20 hombres × 0,8 | 0,4 | — | Asedio 15 | — | — | — |

**Contrapartidas** que impiden una composición óptima universal: la caballería pesada es decisiva en llanura pero cara, consume forraje y sufre en montaña y pantano; los arqueros a caballo son letales en estepa y llanura, pero apenas sirven en asedios; la infantería de lanzas es barata pero quebradiza sin apoyo; los almogávares son excelentes en terreno quebrado y cobran mucho.

#### Modificadores de terreno por tipo

| Terreno | Caballería pesada | Caballería ligera / arqueros a caballo | Infantería | Proyectiles |
| --- | --- | --- | --- | --- |
| Llanura | × 1,25 | × 1,15 | × 1,0 | × 1,0 |
| Estepa | × 1,10 | × 1,30 | × 0,9 | × 1,1 |
| Colinas | × 0,85 | × 0,95 | × 1,05 | × 1,05 (defensor) |
| Montaña | × 0,50 | × 0,70 | × 1,15 (ligera × 1,3) | × 1,15 (defensor) |
| Bosque | × 0,60 | × 0,75 | × 1,10 | × 0,80 |
| Pantano | × 0,40 | × 0,60 | × 0,85 | × 0,85 |
| Cruce de río (atacante) | × 0,60 | × 0,70 | × 0,70 | × 1,0 |

#### Movimiento

```text
días_para_cruzar_una_provincia = días_base(terreno) × estación × (1 + 0,10 × miles_de_hombres_sobre_5)
                                 × (0,8 si hay camino principal) × (1,5 si la provincia es hostil y no hay guías)
```

| Terreno | Días base (ejército a pie, 1300) | Otoño lluvioso | Invierno | Deshielo |
| --- | --- | --- | --- | --- |
| Llanura | 4 | × 1,3 | × 1,5 | × 1,4 |
| Colinas | 5 | × 1,3 | × 1,6 | × 1,4 |
| Montaña | 8 | × 1,4 | × 3,0 (pasos cerrados por nieve: infranqueable en alta montaña) | × 1,8 |
| Bosque | 7 | × 1,4 | × 1,6 | × 1,5 |
| Pantano | 9 | × 1,8 | × 1,3 (helado) | × 2,0 |
| Desierto | 6 | × 1,0 | × 1,0 | × 1,0 (verano × 1,4 por el calor) |
| Estepa | 3 | × 1,2 | × 2,0 | × 1,5 |

Un ejército solo de caballería se mueve un 35 % más rápido. Las estaciones son por macrorregión y año (sección 15).

#### Suministro y desgaste

```text
capacidad_de_suministro(provincia, mes) = (excedente_agrario_almacenado + forraje_disponible)
                                          / consumo_diario_por_hombre × factor_estación
consumo_del_ejército = Σ hombres × consumo(tipo) + animales × forraje
si consumo ≤ capacidad:  sin desgaste por hambre; la provincia pierde lo consumido (vía mercado o requisa)
si consumo > capacidad:  desgaste_mensual = 2 % + 6 % × (consumo/capacidad − 1), máx. 15 %
                         + enfermedad en el campamento: 1 % por mes inmóvil, ×2 en verano junto a pantanos
```

| Forma de abastecerse | Coste para el ejército | Coste para la provincia |
| --- | --- | --- |
| Compra en el mercado | Dinero al precio local (sube por la demanda) | Precio del grano + |
| Requisa ordenada | Ninguno inmediato | Agravio +5/mes; NV −0,05 |
| Forrajeo libre | Ninguno | Agravio +10/mes; existencias −50 %; seguridad −0,2 |
| Devastación (orden explícita) | Ninguno; niega recursos al enemigo | Edificios agrarios −20 a −40 %; seguridad −0,5; refugiados |
| Depósitos y convoyes | Transporte desde un depósito propio | Ninguno |

Las existencias que el ejército lleva en su tren duran `alimento_en_tren / consumo_diario` días. En 1300 un ejército de 10.000 hombres con caballería consume unas 9–10 t de grano y 30–40 t de forraje al día: una provincia agraria media lo sostiene semanas, no meses. Esa cifra explica por qué las campañas premodernas son cortas, estacionales y depredadoras.

#### Batalla: algoritmo completo

1. **Contacto y elección del terreno.** Cada bando calcula `reconocimiento = caballería_ligera_relativa + capacidad_del_comandante + conocimiento_local`. El que gana por más de 20 % elige si combate o se retira y aplica el terreno de la provincia o, en colinas y montaña, un **terreno favorable** (+10 % a su defensa).
2. **Despliegue.** El **ancho de frente** limita cuántos combaten a la vez:

| Terreno | Ancho de frente por bando (hombres, 1300) |
| --- | --- |
| Llanura y estepa | 8.000 |
| Colinas | 5.000 |
| Bosque | 3.000 |
| Montaña y pasos | 1.500 |
| Puente o vado | 800 |

3. **Fases de cada día** (hasta 3 días por batalla en 1300; hasta semanas en épocas industriales):
   - **Proyectiles:** daño = Σ (hombres comprometidos × proyectil × equipo × modificador de terreno) × 0,0008 × aleatoriedad (0,85–1,15).
   - **Choque:** daño = Σ (hombres × choque × equipo × organización × terreno × mando) × 0,0012 × aleatoriedad, reducido por la defensa del objetivo (`× 10 / (10 + defensa)`).
   - **Moral:** cada bando pierde `100 × daño_recibido / hombres × sensibilidad` (sensibilidad 1,0 base; 0,7 veteranos; 1,3 levas; 1,5 sin paga).
4. **Ruptura.** Si la moral de un bando cae por debajo de 30, se retira; por debajo de 10, se desbanda. Las compañías en reserva entran cuando se abren huecos.
5. **Persecución.** El vencedor inflige un daño extra = `persecución_total × 0,003 × (1 − terreno_cerrado)` durante la retirada; contra un ejército desbandado, × 3.
6. **Bajas finales:**

| Situación | Muertos | Heridos (recuperables) | Prisioneros | Desertores |
| --- | --- | --- | --- | --- |
| Vencedor | 30 % | 60 % | 2 % | 8 % |
| Vencido en retirada ordenada | 35 % | 40 % | 10 % | 15 % |
| Vencido en desbandada | 35 % | 15 % | 30 % | 20 % |

Los heridos vuelven a filas en 1–3 meses si hay suministro; los prisioneros nobles generan rescates (sección 12); los desertores vuelven a su cohorte de origen y bajan su lealtad.

#### Ejemplo ilustrativo: una batalla en la frontera de Bitinia (1302)

*Inspirado en el encuentro de Bafeo; los efectivos reales son inciertos (confianza C) y aquí se usan cifras de diseño.*

| Bando | Fuerza | Moral inicial | Mando |
| --- | --- | --- | --- |
| Bizantino | 2.000: 600 caballería pesada (mercenarios alanos y tropas imperiales), 1.400 infantería de lanzas mal pagada | 55 (paga atrasada: sensibilidad 1,5 en la infantería) | Capacidad 9 |
| Otomano | 4.500: 3.000 caballería ligera y arqueros a caballo, 1.500 guerreros de frontera | 65 | Capacidad 13 |

| Fase | Resultado |
| --- | --- |
| Reconocimiento | Ventaja otomana (+46 %): elige combatir en llanura abierta junto al mar. |
| Proyectiles, día 1 | Los arqueros a caballo infligen ≈ 60 bajas a la infantería bizantina, que no puede responder; su moral cae a 41. |
| Choque | La caballería pesada bizantina carga y causa ≈ 90 bajas; los otomanos ceden y vuelven a disparar (movilidad 1,5 frente a 0,9). |
| Moral | La infantería bizantina cae por debajo de 30 al final del día y se retira; la caballería alana la cubre. |
| Persecución | 3.000 jinetes ligeros persiguen en llanura: ≈ 250 bajas más. |
| Informe | “Derrota bizantina. Factores: inferioridad numérica (×2,2), infantería sin paga (sensibilidad 1,5), arqueros a caballo en llanura (+15 %), mando inferior (−4).” |

La consecuencia importa más que la batalla: el campo de Bitinia queda abierto a incursiones, la seguridad baja y empieza el proceso del ejemplo de población de la sección 09.

#### Asedios por niveles de fortificación

| Nivel | Descripción (1300–1500) | Defensa | Meses mínimos de asedio sin artillería | Guarnición típica | Coste de construcción del nivel |
| --- | --- | --- | --- | --- | --- |
| 0 | Sin defensas | 0 | — (se ocupa al llegar) | — | — |
| 1 | Empalizada, torre o recinto pequeño | 2 | 1 | 50–200 | 40 uc |
| 2 | Castillo de piedra | 4 | 3 | 100–400 | 250 uc |
| 3 | Ciudad amurallada | 6 | 6 | 500–2.000 | 800 uc |
| 4 | Gran ciudad con doble muralla | 9 | 12 | 2.000–6.000 | 3.000 uc |
| 5 | Murallas teodosianas (único) | 14 | 24+ | 5.000–10.000 | No construible |
| 6 | Fortificación abaluartada (desde su tecnología) | 12 (pero × 3 frente a artillería) | 9 | 1.000–4.000 | 6.000 uc |

```text
progreso_mensual = (asedio_de_máquinas + asedio_de_artillería × (1/3 si el nivel no está adaptado,
                    o × 1/6 si es abaluartado) + 0,5 × zapadores) / (defensa × moral_guarnición/50)
brecha            = cuando el progreso acumulado ≥ 10: se abre una brecha (defensa −50 % hasta repararla)
asalto            = probabilidad_de_éxito = 0,15 + 0,35 × (si hay brecha) + 0,2 × superioridad_numérica(≥ 4:1)
                    − 0,10 × nivel_de_fortificación; coste: 10–30 % del atacante, 30–60 % de la guarnición
hambre            = si bloqueo total (tierra y mar): días_de_comida = existencias / (guarnición + civiles)
rendición mensual = 0,02 + 0,5 × (1 − días_de_comida/90 si < 90) + 0,2 × brecha + condiciones_ofrecidas
                    − 0,2 × esperanza_de_socorro (ejército aliado a ≤ 30 días)
```

**Ejemplo: el bloqueo de una gran ciudad bitinia.** Un beylik sin máquinas ni artillería no puede abrir brecha en una ciudad de nivel 3. Construye fortines alrededor (nivel 1), corta los caminos y deja que el hambre trabaje. La ciudad tiene existencias para 14 meses con su población; si no recibe socorro ni grano por mar, la probabilidad de rendición sube cada mes a partir del décimo. El jugador otomano ve una barra de “meses de comida estimados” (con el error de su inteligencia) y el jugador bizantino ve la misma barra exacta: los dos saben qué está en juego. El historial de asedios largos de Bitinia en las décadas de 1310 y 1320 emerge de esta mecánica, sin guion.

#### Guerra naval (1300–1500)

| Barco | Tripulación | Remeros | Soldados embarcados | Carga | Velocidad | Temporada | Coste | Mantenimiento/mes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Galera ligera | 30 | 100–150 | 20–40 | 10 t | Rápida (remo + vela) | Marzo–octubre | 600 uc | 45 uc |
| Galera de mercado (*galea grossa*) | 40 | 150–200 | 30–60 | 100–150 t | Media | Marzo–octubre | 1.000 uc | 60 uc |
| Nave redonda / coca | 15–30 | 0 | 0–50 | 200–400 t | Lenta, dependiente del viento | Todo el año con riesgo invernal | 800 uc | 25 uc |
| Carraca (desde su tecnología) | 40–80 | 0 | 50–150 | 400–800 t | Media | Todo el año | 2.000 uc | 50 uc |
| Barca de corso | 10–20 | 20–40 | 10–20 | 2 t | Muy rápida | Marzo–noviembre | 80 uc | 6 uc |

- **Zonas marítimas:** el mar se divide en zonas (Egeo norte, Egeo sur, Mármara, mar Negro occidental…). Una flota **controla** una zona si su fuerza efectiva supera tres veces la de cualquier rival presente; controlar una zona permite bloquear sus puertos y protege o interrumpe las rutas que la cruzan.
- **Autonomía de las galeras:** necesitan agua y víveres cada 7–10 días; lejos de puertos propios o aliados pierden un 5 % de fuerza efectiva por semana. Por eso el control de islas y bases (Creta, Negroponte, Quíos, Rodas) es decisivo.
- **Combate naval:** usa el mismo esquema que el terrestre: fase de proyectiles (ballestas, más tarde artillería), fase de abordaje (soldados embarcados × choque) y fase de captura o hundimiento. Los barcos capturados cambian de bando con un 50 % de su tripulación.
- **Bloqueo:** eficacia = `fuerza_de_bloqueo / (fuerza_de_bloqueo + 0,5 × tráfico_del_puerto)`, reducida un 40 % en invierno. Un bloqueo eficaz al 80 % reduce en un 80 % las importaciones del puerto, y por tanto alimenta la mecánica de hambre de los asedios.
- **Tempestades:** probabilidad mensual de pérdidas del 1–3 % por flota en verano y del 5–12 % en invierno, salvo en puerto.

#### Agotamiento bélico como variable derivada

```text
agotamiento (0–100) = 30 × bajas_acumuladas / reserva_movilizable
                    + 20 × (impuestos_extraordinarios / ingresos_ordinarios)
                    + 20 × max(0, precio_del_alimento / precio_base − 1)       (en los mercados propios)
                    + 15 × provincias_propias_ocupadas_o_devastadas / provincias
                    + 10 × meses_de_guerra / 60
                    +  5 × deuda_nueva_de_guerra / ingresos_anuales
                    − propaganda y legitimidad de la causa (hasta −15)
```

Cada término es una contribución en el registro causal: “Agotamiento 64: bajas (22), precio del grano (18), impuestos extraordinarios (12), duración (9), ocupación (6), propaganda (−3)”. El agotamiento reduce la moral de las levas (−0,3 por punto), aumenta la presión rebelde de los grupos que pagan la guerra y hace que la IA acepte paces peores.

#### Mercenarios y contratos

| Cláusula | Valores típicos (1300) |
| --- | --- |
| Paga mensual | 1,0–3,0 uc por hombre según tipo (× 1,2–1,5 sobre la paga de tropas propias) |
| Adelanto | 1–4 meses de paga al firmar |
| Duración | 3–12 meses, renovable |
| Botín | 0–100 % para la compañía; el resto para el patrón |
| Rescates de prisioneros | Normalmente para quien captura |
| Tierras o concesiones | Opcional; aumenta mucho la lealtad y el riesgo de que se asienten |

```text
lealtad_mercenaria(t+1) = lealtad + 5 × (paga al día) − 12 × meses_de_atraso
                          + 3 × victorias_recientes − 10 × si el patrón ha intentado reducir la paga
                          + afinidad con el patrón (religión, cultura) − agravio por violencia contra la compañía
si meses_de_atraso ≥ 3:        riesgo mensual de motín = 10 % + 10 % × (atraso − 3)
si lealtad < 20 y atraso ≥ 4:  la compañía pasa a ser una entidad independiente con objetivos propios
```

**La Compañía Catalana** es el caso de diseño: entra en el slice como una entidad sin territorio (≈ 6.500 personas entre combatientes y acompañantes, confianza B), con su contrato, su lealtad y su personalidad de IA “mercenaria”. Si el patrón paga y la usa bien, es una herramienta decisiva; si se retrasa o intenta eliminar a sus jefes, la compañía saquea, cambia de patrón o conquista un Estado propio. El motor no fuerza ninguno de los tres desenlaces.

#### Levas feudales

```text
contingente_de_un_vasallo = obligación_contractual × (0,5 + lealtad/200) × disponibilidad_estacional
días_de_servicio          = 40 a 90 días por año fuera de sus tierras (según contrato); después,
                            cada mes adicional exige paga o reduce la lealtad −10
```

Una leva que se queda sin paga ni botín más allá de su plazo **se disuelve** gradualmente (10 % por semana). El rey que quiere campañas largas necesita dinero (mercenarios, ejército permanente) o vasallos muy leales: la tensión entre ambos modelos impulsa las reformas fiscales y militares de las épocas siguientes.

#### Ocupación y resistencia

- **Control del ocupante:** empieza en 10 % y sube un 5 % mensual hasta un máximo de `0,5 × control_objetivo` mientras dure la guerra.
- **Resistencia:** la presión rebelde de las cohortes ocupadas se calcula con legitimidad 20 hacia el ocupante, más afinidad cultural y religiosa.
- **Reconstrucción:** los edificios dañados recuperan un 5 % de capacidad al mes si hay trabajadores y capital, y la seguridad un 0,05 mensual si no hay ejércitos hostiles.

#### Pruebas específicas

| Prueba | Criterio |
| --- | --- |
| `battle_symmetry` | Dos ejércitos idénticos en terreno neutro: cada bando gana el 50 % ± 5 % de 1.000 batallas con semillas distintas. |
| `terrain_matters` | Caballería pesada contra infantería de lanzas: gana > 70 % en llanura y < 35 % en montaña con efectivos iguales. |
| `siege_without_artillery` | Una ciudad de nivel 3 con suministro por mar no cae en 5 años ante un sitiador sin artillería ni flota. |
| `supply_ceiling` | Un ejército 3 veces mayor que la capacidad de suministro pierde entre el 12 % y el 15 % mensual. |
| `mercenary_arrears` | Con 6 meses de atraso, una compañía se amotina en ≥ 70 % de las campañas. |
| `war_exhaustion_composed` | El agotamiento coincide con la suma de sus contribuciones registradas (exacto). |

## 14. Ciencia y tecnología

La investigación es un grafo de capacidades científicas, conocimientos prácticos e infraestructura. Se distinguen **descubrimiento**, **prototipo**, **adopción** y **producción masiva**. La difusión ocurre por comercio, educación, migración, espionaje y contactos culturales.

### Ramas del grafo

| Rama | Contenido |
| --- | --- |
| Agricultura y alimentación | Rotación de cultivos, regadío, nuevas especies, fertilizantes, mecanización. |
| Energía y materiales | Molinos, carbón, vapor, metalurgia, electricidad, petróleo, nuclear, renovables. |
| Manufactura | Talleres, manufacturas, fábricas, cadena de montaje, automatización. |
| Transporte y navegación | Barcos, cartografía, caminos, canales, ferrocarril, automóvil, aviación. |
| Comunicación e información | Papel, imprenta, correo, telégrafo, radio, computación, redes. |
| Militar | Armas, fortificación, organización, doctrina. |
| Ciencias y medicina | Matemáticas, astronomía, química, biología, medicina, salud pública. |
| Instituciones y saber | Universidades, contabilidad, banca, burocracia, estadística. |

### Tecnologías del slice (1300–1600)

| Tecnología | Prerrequisitos | Efecto principal |
| --- | --- | --- |
| Rotación trienal | Arado pesado, ganado | Más cereal por hectárea en tierras húmedas. |
| Molino de agua mejorado | Carpintería, ríos | Más harina y fuerza para batanes y forjas. |
| Molino de viento | Carpintería | Fuerza motriz sin ríos. |
| Papel | Contacto con productores | Abarata la administración y los registros. |
| Contabilidad por partida doble | Aritmética comercial, papel | Mejores empresas y finanzas públicas. |
| Letra de cambio | Contabilidad, red de mercaderes | Comercio a distancia sin mover metal. |
| Seguro marítimo | Letra de cambio | Reduce el riesgo comercial. |
| Brújula y portulanos | Navegación costera | Navegación en invierno y mar abierto. |
| Coca y carraca | Astilleros, timón de codaste | Mayor carga y alcance. |
| Gafas | Vidrio de calidad | Alarga la vida laboral de letrados y artesanos. |
| Reloj mecánico | Metalurgia fina | Organización del trabajo urbano. |
| Pólvora | Conocimiento químico, salitre | Base de las armas de fuego. |
| Bombardas | Pólvora, fundición | Artillería de asedio temprana. |
| Artillería de bronce | Bombardas, metalurgia del cobre | Asedios rápidos. |
| Arcabuz | Pólvora, metalurgia | Infantería de fuego. |
| Fortificación abaluartada | Artillería, geometría | Defensa contra artillería. |
| Imprenta de tipos móviles | Papel, metalurgia, prensas | Difusión del saber, alfabetización, crisis religiosas. |
| Astrolabio náutico | Astronomía, navegación | Navegación oceánica. |
| Carabela | Carraca, vela latina | Exploración atlántica. |
| Galeaza | Galera, artillería naval | Potencia de fuego en el Mediterráneo. |
| Alto horno | Metalurgia, energía hidráulica | Hierro barato. |
| Universidad | Clero letrado, ciudades | Capacidad científica e institucional. |

### Investigación, adopción y difusión (propuesto)

```text
progreso_descubrimiento = inversión × capacidad_institucional (personas cualificadas, instituciones)
                          × (1 + conocimiento_accesible_de_vecinos_y_socios)
                          ÷ coste_base × multiplicador_de_adelanto

multiplicador_de_adelanto = 1 si la fecha está dentro de la ventana histórica;
                            crece por cada década de adelanto hasta el límite N, donde es infinito

difusión_hacia_j = contacto_ij (comercio, migración, guerra, espionaje)
                   × capacidad_de_absorción_j (alfabetización, instituciones, industria afín)

adopción         = curva logística: la fracción de edificios que usa una técnica crece
                   según su rentabilidad frente a la técnica anterior y el capital disponible
```

Así, descubrir la imprenta no cambia nada por sí solo: hacen falta papel barato, metalurgia, capital, lectores y una rentabilidad que justifique montar prensas. Una sociedad puede conocer una técnica y no adoptarla durante décadas porque no le compensa.

### Límite de adelanto

Una tecnología no puede descubrirse más de *N* años antes del inicio de su ventana histórica, aunque se cumplan todos los prerrequisitos. *N* crece con la época y es un parámetro de diseño visible.

> **EJEMPLO DE REGLA**  
> Ninguna nación puede saltar del siglo XV a una tecnología contemporánea mediante investigación acumulada. Una nación excepcionalmente avanzada puede adelantarse modestamente si completa toda la cadena de requisitos.

### Progresión posterior a 2060

Energía, materiales, biomedicina, transporte, computación y organización social pueden ampliarse con tecnologías diseñadas y reglas procedurales conservadoras. El calendario continúa sin límite; **el contenido significativo futuro tiene un alcance limitado que deberá ampliarse**.

### Especificación detallada de tecnología (v0.7, propuesto)

Base de `docs/specs/technology.md`. La tecnología no se compra con puntos abstractos: la producen **personas cualificadas** que trabajan en **instituciones** con **financiación**, y solo cambia el mundo cuando se **adopta** porque es rentable.

#### Ficha de un nodo del grafo

| Campo | Contenido | Ejemplo (imprenta de tipos móviles) |
| --- | --- | --- |
| Rama | Una de las ocho ramas | Comunicación e información |
| Prerrequisitos técnicos | Otros nodos | Papel, metalurgia fina, prensa de tornillo |
| Prerrequisitos materiales | Bienes que deben existir en el mercado | Papel, plomo, estaño, antimonio (o aleación sustituta) |
| Prerrequisitos institucionales | Instituciones o leyes | Talleres urbanos con capital; ninguna prohibición religiosa de imprimir |
| Ventana histórica | Inicio y fin de referencia | 1440–1480 |
| Adelanto máximo (N) | Años antes del inicio de la ventana | 25 (época 1300–1500) |
| Coste de descubrimiento | Años-sabio | 450 |
| Coste del prototipo | Bienes + años-sabio | 200 uc y 40 años-sabio |
| Efectos | Modos de producción, unidades, leyes, parámetros | Modo `printing_press`; alfabetización ×1,3 a largo plazo; presión de reforma religiosa |

#### Capacidad de investigación

```text
años_sabio_al_mes(institución) = personas_cualificadas × dedicación (0–1) × eficacia × financiación_relativa / 12
eficacia = 0,5 (base) + 0,1 × tradición escrita + 0,2 × especialidad coincidente + 0,1 × red de correspondencia
```

| Institución (1300) | Personas cualificadas típicas | Dedicación a investigación | Especialidades | Coste anual |
| --- | --- | --- | --- | --- |
| Taller artesano avanzado | 3–10 artesanos maestros | 0,10 | Manufactura, materiales | Incluido en la producción |
| Monasterio con biblioteca | 10–40 clérigos letrados | 0,05 | Agricultura, medicina, saber | 50–300 uc |
| Madrasa | 5–30 ulemas y estudiantes | 0,05 | Derecho, astronomía, medicina | 50–200 uc |
| Universidad | 30–200 maestros | 0,15 | Saber, medicina, derecho | 500–3.000 uc |
| Arsenal estatal | 50–300 artesanos | 0,05 | Naval, militar | Parte del gasto militar |
| Corte con patronazgo | 3–15 eruditos | 0,30 | Variable | 100–1.000 uc |
| Casa de comercio con contabilidad | 5–20 mercaderes letrados | 0,05 | Instituciones, navegación | Privado |

Un año-sabio cuesta en 1300 unos 8–15 uc (salario más materiales). Bizancio, con su patriarcado, sus monasterios y una corte erudita, dispone de unos 30–50 años-sabio anuales efectivos; Venecia, con su arsenal y sus casas de comercio, una cifra similar pero orientada a navegación e instituciones. Los beyliks apenas tienen capacidad propia: dependen de la **difusión**.

#### Etapas y su efecto en el juego

| Etapa | Qué exige | Qué cambia |
| --- | --- | --- |
| Descubrimiento | Años-sabio acumulados ≥ coste (por Estado o por institución) | Se conoce; aparece en el grafo como “conocida”; se difunde. |
| Prototipo | Un primer edificio, unidad o institución construido con su coste | Muestra la rentabilidad real; habilita la adopción. |
| Adopción | Curva logística (ver abajo) | Los edificios cambian de modo, las unidades se reequipan, las leyes se vuelven posibles. |
| Producción masiva | Adopción > 50 % en el Estado | Coste del modo −20 %; difusión hacia otros Estados × 1,5. |

#### Difusión del conocimiento

```text
progreso_j(t+1) = progreso_j + tasa × contacto_ij × absorción_j × (1 − progreso_j)   [mensual, por técnica]
contacto_ij  = 0,5 × comercio_ij/comercio_total_j + 0,3 × migración_de_cualificados_ij
             + 0,2 × guerra_ij (captura de material, prisioneros) + 0,4 × libros_impresos_ij (tras la imprenta)
absorción_j  = alfabetización_de_cualificados × instituciones_afines × industria_relacionada (0–1)
tasa         = 0,02 (antes de la imprenta), 0,05 (con imprenta), 0,15 (con telégrafo), 0,40 (con redes)
```

La difusión alimenta el **progreso de descubrimiento** del receptor: aprender de otros es más barato que inventar, pero exige capacidad de absorción. Una sociedad sin artesanos metalúrgicos no aprende a fundir artillería por mucho que compre cañones; solo puede **comprarlos** o **contratar** a quien sepa (y la migración de personas cualificadas es una de las palancas más potentes del jugador).

#### Adopción

```text
cuota(t+1) = cuota + r × cuota × (1 − cuota) × ventaja        [trimestral, por Estado y modo]
ventaja    = max(0, rentabilidad_nuevo_modo / rentabilidad_modo_actual − 1)
r          = 0,15 (base), × 1,5 si hay capital abundante, × 0,5 si los gremios se oponen
cuota mínima tras el prototipo = 1 %
```

Si la ventaja es cero (la técnica no compensa con los precios de la provincia), la cuota **no crece**, por mucho que la técnica se conozca. Si un modo nuevo pierde rentabilidad (por ejemplo, porque falta un insumo), la cuota puede retroceder un 2 % trimestral.

#### Límite de adelanto por época

| Época de la ventana | Adelanto máximo N | Multiplicador de coste por adelanto |
| --- | --- | --- |
| 1300–1500 | 25 años | `1 + 0,5 × (años_de_adelanto / 10)²` |
| 1500–1750 | 30 años | Igual |
| 1750–1914 | 20 años | Igual |
| 1914–1991 | 12 años | `1 + 1,0 × (años_de_adelanto / 10)²` |
| 1991–2060 | 10 años | Igual |
| Después de 2060 | Diseñado por nodo | Diseñado por nodo |

Con N = 25, descubrir una técnica 20 años antes de su ventana cuesta el triple (1 + 0,5 × 4 = 3); a 25 años o más, es imposible. La interfaz muestra el multiplicador y el año en que deja de aplicarse.

#### Ejemplo: la imprenta en Venecia y en Constantinopla (partida hipotética)

| Año | Venecia | Constantinopla |
| --- | --- | --- |
| 1445 | Descubre la técnica por difusión desde talleres alemanes (contacto comercial alto, absorción 0,7). | La conoce por noticias, pero su absorción es 0,35 (pocos talleres metalúrgicos con capital). |
| 1450 | Prototipo: un taller cuesta 200 uc; rentabilidad estimada 34 % frente al 8 % de los copistas. | Sin prototipo: la élite letrada prefiere la copia manuscrita y el capital escasea (prima de riesgo de guerra 15 %). |
| 1470 | Adopción 18 %; el precio de los libros baja un 60 %. | Si la ciudad ha caído, la técnica la adopta el nuevo poseedor según su propia rentabilidad y sus leyes. |
| 1500 | Producción masiva; la alfabetización urbana crece 0,2 puntos al año. | — |

#### Pruebas específicas

| Prueba | Criterio |
| --- | --- |
| `no_tech_beyond_lead` | En 1.000 campañas, ninguna técnica se descubre más de N años antes de su ventana. |
| `knowledge_without_adoption` | Una técnica sin ventaja de rentabilidad mantiene su cuota de adopción por debajo del 5 % durante 50 años. |
| `diffusion_needs_absorption` | Con absorción 0, el progreso por difusión es exactamente 0. |
| `graph_acyclic` | El validador rechaza cualquier ciclo de prerrequisitos. |

## 15. Clima, epidemias y exploración

| Subsistema | Diseño |
| --- | --- |
| Clima | Anomalías de temperatura y precipitación por macrorregión y año, a partir de reconstrucciones históricas, con ruido controlado por la semilla. |
| Desastres | Sequías, inundaciones, terremotos, erupciones volcánicas con efectos regionales. |
| Epidemias | Transmisión por red de rutas y densidad, con mortalidad, inmunidad y medidas. |
| Conocimiento geográfico | Mapa conocido por cada Estado; exploración y cartografía. |
| Recursos y entorno | Bosques, agotamiento de minas, contaminación, habitabilidad. |
| Crisis sistémicas | Hambrunas, interrupciones comerciales, quiebras, epidemias y grandes conflictos. |

### Modelo de epidemias (propuesto)

- Cada provincia tiene fracciones de población **susceptible, infectada, recuperada y fallecida** por enfermedad (modelo compartimental simplificado).
- El contagio entre provincias viaja por las **mismas rutas** del comercio y del ejército, ponderado por volumen de tráfico. Así, más comercio implica más riqueza y también más riesgo.
- Cada enfermedad tiene parámetros: transmisibilidad, letalidad, duración de la inmunidad, estacionalidad, vectores.
- Las medidas disponibles dependen de la época: cuarentenas (desde el siglo XIV en puertos italianos), cordones sanitarios, saneamiento, vacunas, antibióticos.

**Peste negra:** no se dispara en 1347. Se modela un foco endémico en la estepa con probabilidad de salto a las rutas comerciales; si las rutas del mar Negro y del Mediterráneo están activas a mediados del siglo XIV, la probabilidad de pandemia es alta. Si una guerra o un bloqueo cierra esas rutas, puede retrasarse o seguir otro camino. Sus efectos a largo plazo (escasez de mano de obra, salarios más altos, crisis del señorío) emergen de los sistemas económicos y políticos.

### Fórmulas de epidemias (propuestas)

```text
nuevos_infectados_i = β × estacionalidad × S_i × I_i / N_i  +  importación_i
importación_i       = Σ_j tráfico_ji × (I_j / N_j) × probabilidad_de_transmisión_por_viajero
recuperados_i       = γ × I_i
fallecidos_i        = μ × I_i
S, I, R, F          = susceptibles, infectados, recuperados, fallecidos (por provincia y enfermedad)
```

El **tráfico** entre provincias es el mismo que mueven el comercio, los ejércitos, los peregrinos y los migrantes. Las cuarentenas reducen el tráfico (y, con él, el comercio); los lazaretos reducen la transmisión; las vacunas trasladan población de susceptibles a recuperados.

| Enfermedad (ejemplos) | Rasgos de diseño |
| --- | --- |
| Peste bubónica | Alta letalidad, vectores (ratas y pulgas), brotes recurrentes durante siglos. |
| Viruela | Inmunidad duradera; catastrófica en poblaciones sin exposición previa. |
| Cólera | Ligada al agua y al saneamiento urbano (siglo XIX). |
| Tifus | Asociado a ejércitos, cárceles y hambrunas. |
| Gripe pandémica | Muy contagiosa, letalidad variable, global en la era del transporte rápido. |

### Exploración

El conocimiento geográfico es por Estado. Explorar requiere barcos capaces, financiación, motivación (comercio, religión, prestigio) y tecnología de navegación. Descubrir una ruta no la hace rentable: hacen falta puertos, mercados y protección.

### Especificación detallada de clima, epidemias y exploración (v0.7, propuesto)

Base de `docs/specs/climate-epidemics.md`.

#### Anomalías climáticas

Cada macrorregión tiene, cada año, dos índices: **temperatura** (desviación respecto a la media 1300–1850) y **humedad** (índice de sequía de −3 a +3). Su origen depende del modo de campaña:

```text
anomalía(macrorregión, año) = w × reconstrucción_histórica(año) + (1 − w) × ruido_correlacionado(semilla)
```

| Modo de campaña | w | Efecto |
| --- | --- | --- |
| Histórico estricto | 0,85 | Los años malos históricos casi siempre son malos. |
| Histórico dinámico | 0,60 | Se reconoce la tendencia (Pequeña Edad de Hielo), no cada año concreto. |
| Alternativo plausible | 0,30 | Tendencias de largo plazo, años distintos. |
| Sandbox causal | 0 | Clima generado con las estadísticas de la época. |

El **ruido** está correlacionado en el espacio (macrorregiones vecinas se parecen, coeficiente 0,6) y en el tiempo (autocorrelación anual 0,3), para que las sequías duren y abarquen regiones, como en la realidad. Las reconstrucciones candidatas son los atlas de sequía por árboles (del tipo *Old World Drought Atlas*) y series paleoclimáticas regionales, con licencia por verificar (Anexo D).

**Efecto en las cosechas** (multiplicador del mes de cosecha):

| Índice de humedad | −3 | −2 | −1 | 0 | +1 | +2 | +3 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cereal de secano mediterráneo | 0,45 | 0,65 | 0,85 | 1,00 | 1,05 | 0,95 | 0,80 |
| Cereal de regadío | 0,80 | 0,90 | 0,97 | 1,00 | 1,00 | 0,95 | 0,85 (inundación) |
| Pastos | 0,50 | 0,70 | 0,88 | 1,00 | 1,08 | 1,05 | 0,95 |

| Temperatura | −1,5 °C o menos | −0,8 °C | 0 | +0,8 °C |
| --- | --- | --- | --- | --- |
| Cereal en el norte y en la montaña | 0,70 | 0,88 | 1,00 | 1,04 |
| Vid y olivo | 0,75 (heladas) | 0,90 | 1,00 | 1,00 |
| Duración del invierno militar | +30 días | +15 días | 0 | −10 días |

**Erupciones volcánicas (F-ENV-06).** Las grandes erupciones se modelan como sucesos con un año de enfriamiento global (−0,5 a −1,5 °C) y uno o dos años de cosechas malas en el hemisferio afectado. En el modo estricto, las conocidas (por ejemplo, la de 1600 en los Andes) ocurren en su año con probabilidad alta; en los demás modos, su frecuencia sigue la estadística de la época.

**Terremotos.** Probabilidad anual por provincia según la sismicidad de datos (alta en Anatolia, el Egeo y el Levante). Un terremoto daña edificios (10–60 %) y fortificaciones (un nivel puede caer), mata a un 0,5–5 % de la población urbana y puede abrir oportunidades: un muro caído es una brecha.

#### Hambruna como cadena de efectos

| Eslabón | Mecanismo (ya especificado) | Sección |
| --- | --- | --- |
| Mala cosecha | Multiplicador climático del mes de cosecha | 15 |
| Subida del precio | Algoritmo de precios con existencias | 10 |
| Cobertura de cestas | Compra en orden hasta agotar el ingreso | 09 |
| Mortalidad y emigración | `g_alimentos`, migración y refugiados | 09 |
| Descontento | Legitimidad por prosperidad y por hambruna no atendida | 11 |
| Respuestas del Estado | Abrir graneros, prohibir exportaciones, importar, rebajar impuestos | 10–11 |
| Epidemias oportunistas | El tifus y la disentería ganan transmisibilidad con NV < 0,8 | 15 |

#### Parámetros de enfermedades (sistema semanal)

El sistema de epidemias corre **semanalmente** por provincia. β es la tasa de contagio semanal en una provincia urbana densa; se multiplica por la densidad relativa (0,6–1,2) y por la estacionalidad.

| Enfermedad | β semanal (urbano) | Salida semanal γ | Letalidad de los casos | Inmunidad | Estacionalidad | Rasgos |
| --- | --- | --- | --- | --- | --- | --- |
| Peste bubónica | 1,60 | 0,90 | 50–60 % | Pierde un 10 %/año (vuelve a susceptibles) | Máxima en verano y otoño | Reservorio en la estepa; rebrotes cada 10–20 años. |
| Peste neumónica (variante) | 2,40 | 1,50 | 90 % | Igual | Invierno | Solo como complicación de brotes intensos. |
| Viruela | 2,00 | 0,50 | 15–30 % (40–60 % en poblaciones sin exposición) | Permanente | Leve | Endémica en ciudades; catastrófica en primer contacto. |
| Tifus | 1,20 | 0,50 | 10–40 % | Parcial | Invierno | × 2 en ejércitos, cárceles y hambrunas. |
| Disentería | 1,10 | 0,70 | 5–15 % | Ninguna | Verano | × 2 en campamentos y asedios. |
| Malaria | — (vector) | — | 1–5 % anual en zonas palúdicas | Parcial | Verano | Endémica en pantanos y deltas; frena la colonización de llanuras húmedas. |
| Cólera (siglo XIX) | 1,80 | 1,00 | 30–50 % | Corta | Verano | Agua y saneamiento. |
| Gripe pandémica | 2,50 | 1,20 | 1–3 % | Por cepa | Invierno | Global con transporte rápido. |

**Comprobación con la peste negra.** Con β = 1,60 y γ = 0,90, el número reproductivo urbano es R₀ ≈ 1,8 y la fracción final de infectados ≈ 73 %; con letalidad del 50 %, muere ≈ 36 % de la población urbana. En el campo, con densidad 0,8, R₀ ≈ 1,4, infectados ≈ 51 % y mortalidad ≈ 25 %. Con un 15–25 % de población urbana, la media regional (≈ 26–28 % en el primer brote) deja la población en torno al 72–74 % de la anterior; los rebrotes de las décadas siguientes, la hambruna y la desorganización la bajan hacia el 60–70 %, dentro del rango del Anexo F (50–80 %).

#### Reservorio y salto de la peste

```text
probabilidad_semanal_de_salto(provincia_reservorio → ruta) = 0,0008 × tráfico_relativo × factor_clima
factor_clima = 1,5 en años cálidos y húmedos en la estepa (favorables a roedores), 0,7 en años fríos
```

| Modo de campaña | Ajuste |
| --- | --- |
| Estricto | El reservorio de la estepa póntico-caspia tiene una ventana de actividad alta entre 1338 y 1346 (× 5). |
| Dinámico | Ventana de actividad alta entre 1320 y 1370 (× 2), sin año preferente. |
| Alternativo / sandbox | Sin ventana; solo la probabilidad base. |

Si el salto ocurre, la enfermedad se propaga por el **tráfico real**: caravanas hasta Tana y Caffa, barcos genoveses hacia Constantinopla, Sicilia y Génova, peregrinos y ejércitos. Una guerra que cierre el mar Negro retrasa o desvía la pandemia; un comercio más intenso la acelera.

#### Medidas sanitarias

| Medida | Disponible desde | Efecto | Coste |
| --- | --- | --- | --- |
| Huida de las élites | Siempre | Su mortalidad −40 %; administración −30 % durante el brote | Legitimidad −5 con el pueblo urbano |
| Cuarentena de barcos (40 días) | Siglo XIV (ciudades italianas, primero en el Adriático) | Importación de infectados −70 % | Comercio del puerto −30 % mientras dure |
| Cordón sanitario terrestre | Siglos XV–XVI | Tráfico terrestre −60 % | Comercio −40 %; tropas ocupadas |
| Lazareto | Siglo XV | β local −20 % | 300 uc + mantenimiento |
| Magistratura de salud permanente | Siglos XV–XVI | Reacción a un brote 4 semanas antes | Funcionarios |
| Variolización / vacunación | Siglo XVIII | Mueve susceptibles a inmunes (2–10 % anual) | Médicos y campañas |
| Saneamiento urbano | Siglo XIX | β del cólera y la disentería −60 % | Gran inversión en obras |
| Antibióticos | Siglo XX | Letalidad de la peste y del tifus −90 % | Industria farmacéutica |

#### Exploración

```text
alcance_de_un_barco (días sin repostar) = agua_y_víveres / consumo_de_la_tripulación
probabilidad_de_éxito_de_una_expedición = 0,30 × navegación (portulanos, brújula, astrolabio…)
                                        + 0,30 × barco_adecuado (alcance ≥ distancia × 1,5)
                                        + 0,20 × capacidad_del_capitán + 0,20 × conocimiento_previo
coste = barcos + tripulación × meses + equipamiento; pérdida esperada = (1 − éxito) × barcos
```

Una expedición con éxito añade localizaciones al **mapa conocido** del Estado que la financia, y quizá rutas nuevas. Una ruta descubierta solo se usa si su margen comercial (sección 10) es positivo: hacen falta puertos de escala, mercados en destino y protección. El conocimiento geográfico se difunde como la tecnología (comercio, cartógrafos que emigran, mapas impresos, espionaje).

#### Pruebas específicas

| Prueba | Criterio |
| --- | --- |
| `plague_final_size` | En provincia urbana aislada sin medidas, la mortalidad de un brote de peste está entre el 30 % y el 42 %. |
| `quarantine_tradeoff` | La cuarentena reduce la mortalidad del puerto al menos un 30 % y su comercio entre un 20 % y un 40 % durante el brote. |
| `climate_correlation` | La correlación espacial y temporal del ruido climático coincide con los parámetros (±0,05) en 1.000 años generados. |
| `famine_chain` | Una sequía −3 en un mercado aislado produce hambruna visible (exceso de mortalidad > 2 %) y caída de legitimidad del pueblo urbano. |

## 16. Personajes y dinastías

### Nivel de detalle

No se simula a cada persona. Se simulan los **personajes con poder decisivo**: gobernantes, herederos, consortes, regentes, consejeros principales, generales y almirantes, líderes religiosos de primer nivel y, en épocas modernas, líderes de partidos y movimientos.

| Atributo | Uso |
| --- | --- |
| Edad y salud | Sucesiones, regencias, muertes en batalla. |
| Capacidades (administración, diplomacia, mando, intriga, saber) | Modifican el rendimiento del cargo que ocupan. |
| Rasgos de personalidad | Sesgan las decisiones de la IA (prudente, ambicioso, piadoso, cruel). |
| Lealtades | A la dinastía, a un grupo de interés, a una facción. |
| Relaciones | Familia, amistades, rivalidades. |
| Reclamaciones | Sobre títulos y territorios, heredables. |

### Dinastías

Las dinastías tienen árbol genealógico, prestigio, reclamaciones y ramas. Los matrimonios crean derechos de sucesión que pueden desencadenar uniones personales o guerras sucesorias.

### Figuras históricas

Los personajes históricos (por ejemplo, un gran conquistador o un reformador religioso) **no aparecen por fecha**. Pueden nacer en la dinastía correspondiente si la dinastía existe, con rasgos sesgados hacia los históricos pero no idénticos. Si la dinastía se extinguió, la figura no aparece.

### Transición a la época moderna

A medida que crecen las instituciones, el peso de los personajes disminuye: en 1300 la muerte de un rey puede hundir un reino; en 1900 un primer ministro es reemplazable. El sistema escala la influencia de los personajes según la institucionalización del Estado.

### Especificación detallada de personajes y dinastías (v0.7, propuesto)

Base de `docs/specs/characters.md`.

#### Escalas

| Atributo | Escala | Media de la población de personajes | Nota |
| --- | --- | --- | --- |
| Administración, diplomacia, mando, intriga, saber | 0–20 | 8 | 15+ es excepcional; 3− es incapaz. |
| Salud | 0–100 | 70 | Por debajo de 30, riesgo alto de muerte y de incapacidad. |
| Prestigio personal | 0–100 | 20 | Victorias, títulos, patronazgo. |
| Ambición, piedad, crueldad (ejes de personalidad) | −10 a +10 | 0 | Los rasgos del Anexo AB se derivan de valores extremos de estos ejes y de sucesos. |
| Lealtad hacia el gobernante | 0–100 | 50 | Componentes registrados, como la legitimidad. |

**Generación al nacer:** cada capacidad = `media_de_los_progenitores × 0,3 + 8 × 0,7 + ruido(−4, +4)`. **Educación** (F-CHR-07) entre los 6 y los 16 años: un tutor con capacidad *c* en una materia añade `(c − 8) × 0,3` a esa materia del heredero, con un máximo de +4. **Edad:** las capacidades alcanzan su máximo entre los 30 y los 50 años; desde los 60 pierden 0,2 puntos al año (el saber no decae).

#### Mortalidad de los personajes

| Edad | Mortalidad anual base (élite, 1300) |
| --- | --- |
| 0–4 | 120 ‰ |
| 5–14 | 15 ‰ |
| 15–29 | 12 ‰ |
| 30–44 | 18 ‰ |
| 45–59 | 35 ‰ |
| 60–69 | 70 ‰ |
| 70+ | 150 ‰ |

Modificadores: salud (`× (1 + (70 − salud)/50)`), rasgos (robusto × 0,8; enfermizo × 1,8), epidemia en su provincia (según la letalidad de la enfermedad y la huida de las élites), batalla (comandante: 1–4 % por batalla; 10 % en una desbandada), parto para las consortes (1–2 % por parto en 1300). La medicina moderna reduce la base en épocas posteriores con la misma lógica que la población.

#### Leyes de sucesión: algoritmos

| Ley | Algoritmo | Riesgos típicos |
| --- | --- | --- |
| Primogenitura agnaticia | Hijo varón mayor; si no hay, su línea; si no, el hermano siguiente y su línea… | Extinción de la línea masculina → crisis con pretendientes cognaticios. |
| Primogenitura cognaticia de preferencia masculina | Como la anterior, pero las hijas heredan antes que los colaterales | Uniones personales con dinastías extranjeras por matrimonio. |
| Designación | El gobernante designa entre sus parientes (o adopta); si muere sin designar, decide el grupo más poderoso | Conflictos si la designación es tardía. |
| Elección | Un colegio (electores, *kurultai*, consejo) elige entre candidatos elegibles; cada elector vota por su utilidad | Compra de votos, intervención extranjera. |
| Sucesión abierta de hijos | Todos los hijos varones son elegibles; heredan el que controla la capital y el tesoro o el que vence | Guerras fratricidas, interregnos. |
| Sucesión lateral (por antigüedad en la dinastía) | El miembro más anciano de la generación mayor | Desposesión de hijos; división del patrimonio. |
| Tanistry | El linaje elige al más apto entre los parientes adultos | Facciones dentro del clan. |

#### Pretendientes

```text
fuerza_del_pretendiente = fuerza_de_la_reclamación (0–100, según la ley y la cercanía genealógica)
                        × apoyo (Σ poder de los grupos que lo prefieren, internos y externos)
                        × recursos (tropas propias, dinero, aliado extranjero)
se proclama si fuerza > 0,6 × fuerza_del_sucesor_legal y su ambición ≥ 0
```

**Ejemplo: Hungría, 1301.** Muere Andrés III, último varón de la casa de Árpád (confianza A). Los candidatos de trabajo son tres, todos con reclamación por línea femenina: Carlos Roberto de Anjou (apoyado por el papado y parte de la nobleza del sur), Venceslao de Bohemia (apoyado por otra parte de la nobleza y con los recursos de su padre) y Otón de Baviera. El motor no elige: calcula fuerzas, abre la situación “crisis sucesoria” (sección 07) y deja que la guerra, la diplomacia y las concesiones a los magnates (cuyo poder sube un 0,10 durante el interregno) decidan. El resultado histórico es una salida posible, no la obligatoria.

#### Regencias

- Se abren si el heredero es menor de 16 años (14 en algunas culturas, por datos) o si el gobernante queda incapacitado (salud < 15).
- El **regente** es la madre, el pariente varón adulto más cercano o un consejo, según la cultura y la ley.
- Durante la regencia: autoridad del soberano × 0,6; poder de la aristocracia +0,05; legitimidad −10 (sección 11).
- **Riesgo de usurpación** mensual = `0,3 % × (ambición del regente + 5) × (1 − legitimidad/100) × (1 + apoyo_aristocrático)`; con un regente ambicioso y una corte dividida, ronda el 1–2 % mensual.

#### Índice de institucionalización y peso de los personajes

```text
institucionalización I (0–1) = 0,30 × capacidad_administrativa_relativa
                             + 0,25 × antigüedad_media_de_las_instituciones (saturada a 150 años)
                             + 0,25 × estabilidad_de_la_regla_de_sucesión (sucesiones sin conflicto / totales)
                             + 0,20 × instituciones representativas y burocracia profesional
peso_personal w = 1 − 0,8 × I
```

| Ejemplo | I aproximado | w |
| --- | --- | --- |
| Beylik fronterizo en 1300 | 0,10 | 0,92 |
| Reino feudal en 1300 | 0,25 | 0,80 |
| Bizancio o Venecia en 1300 | 0,45–0,55 | 0,56–0,64 |
| Monarquía administrativa del siglo XVIII | 0,65 | 0,48 |
| Estado constitucional en 1900 | 0,85 | 0,32 |

Todos los efectos de las capacidades y rasgos del gobernante se multiplican por *w*. Un sultán brillante en 1300 transforma su Estado; un primer ministro brillante en 1900 lo mejora en el margen. Las sucesiones violentas y las regencias **bajan** I con el tiempo: el sistema recuerda.

#### Facciones de corte y conjuras

| Elemento | Especificación |
| --- | --- |
| Formación | Una facción nace cuando al menos dos personajes con poder comparten un objetivo (pretendiente, política, destitución) y su lealtad al gobernante es < 40. |
| Fuerza | Σ (prestigio + capacidad de intriga + poder del grupo de interés que representa cada miembro). |
| Demandas | Una por facción, visible si la inteligencia interna ≥ 1 (si no, se intuye por señales). |
| Conjura | Progreso mensual = fuerza × intriga del líder / (vigilancia del gobernante + guardia); al llegar a 100 se ejecuta (golpe, asesinato, proclamación). |
| Descubrimiento | Probabilidad mensual = 5 % + 2 % × miembros + intriga del jefe de seguridad × 0,5 %. |
| Respuestas | Comprar, desterrar, encarcelar, ejecutar (con agravio de su grupo), aceptar la demanda. |

#### Matrimonios

```text
valor_del_matrimonio = valor_de_alianza (interés y confianza resultantes)
                     + valor_de_reclamación (probabilidad de herencia × valor del territorio)
                     + prestigio de la dinastía del cónyuge − dote o compensación
                     − riesgo (enemigos de la otra dinastía, diferencia religiosa)
```

La IA busca matrimonios con valor > 0 y respeta las restricciones religiosas y culturales de los datos (matrimonios mixtos posibles en unas culturas e impensables en otras, con su coste de legitimidad).

#### Figuras históricas

En cada nacimiento de una dinastía con **plantilla histórica** pendiente (por ejemplo, el hijo histórico de un gobernante), si los progenitores existen y la fecha de nacimiento cae en ±5 años de la histórica, el niño recibe la plantilla con probabilidad *p* (estricto 0,9; dinámico 0,6; alternativo 0,25; sandbox 0). La plantilla sesga capacidades y rasgos (±3 sobre los valores históricos) y fija el nombre; no garantiza la vida ni la carrera. Una figura histórica también puede “aparecer” como plantilla en otro miembro de la familia si el original murió en la infancia (solo en el modo estricto).

#### Pruebas específicas

| Prueba | Criterio |
| --- | --- |
| `succession_always_resolves` | Toda muerte de gobernante produce un sucesor o una crisis con candidatos en el mismo tick. |
| `regency_risk_bounds` | La tasa de usurpación en regencias está entre el 5 % y el 25 % en 1.000 regencias simuladas. |
| `character_weight_scales` | El efecto medio de un gobernante con administración 18 sobre la recaudación es al menos el doble en I = 0,2 que en I = 0,8. |
| `life_expectancy` | La edad media de muerte de gobernantes adultos en 1300–1500 está entre 45 y 60 años. |

## 17. IA de países

### Arquitectura híbrida

Ningún modelo de lenguaje decide las acciones de los países durante la partida. La simulación usa reglas, funciones de utilidad, objetivos jerárquicos, planificación limitada, presupuestos y memoria.

| Nivel | Frecuencia | Responsabilidad | Técnica propuesta |
| --- | --- | --- | --- |
| Gran estrategia | Anual / al cambiar el contexto | Metas nacionales, prioridades, rivales, alianzas. | Objetivos jerárquicos con pesos históricos. |
| Política y diplomacia | Mensual / por eventos | Reformas, tratados, crisis, presupuestos. | Funciones de utilidad con memoria. |
| Economía | Semanal / mensual | Inversión, producción, comercio, financiación. | Heurísticas con presupuesto y retroalimentación. |
| Militar | Diaria / horaria si aplica | Planes, movilización, rutas, frentes. | Planificación jerárquica de tareas (HTN) sobre la red logística. |
| Historia | Periódica / por condiciones | Sesgos históricos, eventos, restauraciones. | Consultas a 101 History. |

### Personalidad nacional

La IA de cada país combina la personalidad del gobernante, los intereses de los grupos de poder, la identidad cultural y la situación geográfica. Una república mercantil prioriza rutas y crédito; un beylik fronterizo, la guerra de botín; un imperio en declive, la supervivencia y las alianzas.

### Presupuesto de cómputo

Cada país “piensa” en días escalonados y con un tiempo máximo por decisión. Un país en guerra recibe más presupuesto que uno en paz. Los países pequeños y lejanos del jugador pueden usar decisiones más simples sin que el jugador lo perciba.

### Cómo puntúa una decisión (propuesto)

```text
utilidad(acción) = Σ_i peso_i(personalidad, ambiciones, sesgo_histórico) × beneficio_esperado_i
                   − coste_esperado − aversión_al_riesgo × riesgo
```

El beneficio y el coste se estiman con la **información que tiene el país**, no con el estado real. La IA elige la acción de mayor utilidad entre las posibles; si ninguna supera un umbral, no hace nada (no actuar también es una decisión).

#### Ejemplo: Venecia evalúa una guerra contra Génova (1350)

| Factor | Valor estimado | Peso (república mercantil) | Contribución |
| --- | --- | --- | --- |
| Ganancia comercial esperada (rutas del mar Negro) | Alta | Alto | +++ |
| Coste financiero de la guerra | Alto | Alto | −− |
| Probabilidad de victoria naval | Media | Medio | + |
| Riesgo para colonias (Creta, Negroponte) | Medio | Alto | −− |
| Aliados disponibles | Aragón dispuesto | Medio | + |
| Sesgo histórico (rivalidad veneciano-genovesa) | Presente | Bajo-medio | + |
| **Resultado** | Utilidad ligeramente positiva | — | Declara la guerra solo si encuentra un aliado; si no, busca un acuerdo comercial. |

El registro de esta evaluación es lo que la interfaz muestra cuando el jugador pregunta “¿por qué me declaró la guerra?”.

### Observabilidad

- Registrar las alternativas consideradas, las restricciones y los factores de utilidad.
- Detectar decisiones sin presupuesto, guerras imposibles o tratados contradictorios.
- Comparar el comportamiento agregado en cientos de campañas.
- Crear pruebas de comportamiento por país y época sin exigir un resultado exacto.

### Especificación detallada de la IA de países (v0.7, propuesto)

Base de `docs/specs/ai.md`. La IA usa **las mismas reglas, comandos e información imperfecta** que el jugador. No tiene acceso al estado real de otros países, solo a sus estimaciones.

#### Canal de decisión

```text
1. Percepción      construir el "mundo estimado" del país a partir de la información disponible (sección 12)
2. Diagnóstico     calcular indicadores: amenaza máxima, salud fiscal, legitimidad, agotamiento,
                   seguridad alimentaria, oportunidades (vecinos en crisis)
3. Objetivos       actualizar la jerarquía de objetivos (anual o al cambiar el diagnóstico)
4. Candidatos      generar como máximo K acciones por capa a partir de los objetivos activos
5. Puntuación      utilidad de cada candidata (fórmula de la sección 17 + términos de abajo)
6. Selección       la mejor, si supera el umbral y la inercia del plan actual
7. Planificación   descomponer las acciones militares en tareas (HTN) sobre la red logística
8. Ejecución       emitir comandos; los comandos se validan igual que los del jugador
9. Registro        guardar candidatas, puntuaciones y factores para el panel "¿por qué?" y para Lab
```

#### Jerarquía de objetivos

| Nivel | Ejemplos | Horizonte | Origen |
| --- | --- | --- | --- |
| Ambición nacional | “Dominar el comercio del mar Negro”, “Restaurar el Imperio”, “Sobrevivir a la coalición” | 20–50 años | Identidad, geografía, situaciones activas (101 History), personalidad |
| Objetivo estratégico | “Tomar Bursa”, “Expulsar a Génova de Pera”, “Sanear el tesoro” | 3–15 años | Descomposición de la ambición según el diagnóstico |
| Objetivo operativo | “Bloquear Bursa por tierra”, “Conseguir una alianza naval”, “Reducir el gasto un 15 %” | Meses–3 años | Descomposición del estratégico |
| Tarea | “Mover el ejército 2 a Prusa”, “Proponer tratado a Aragón”, “Subir la aduana del grano” | Días–meses | HTN y heurísticas |

Cada objetivo tiene **condiciones de éxito, de abandono y de revisión**. Se abandona un objetivo si su coste estimado supera tres veces el previsto o si su utilidad cae por debajo de cero durante un año.

#### Términos de utilidad (unidades comunes)

Todos los beneficios y costes se convierten a **puntos de utilidad (pu)**: 1 pu equivale al valor de 1 % de los ingresos anuales del país, para que las decisiones sean comparables entre Estados de tamaño distinto.

| Término | Cómo se mide | Peso típico por personalidad |
| --- | --- | --- |
| Ganancia económica | Variación esperada de ingresos netos durante 10 años, descontada | Comercio primero 1,5; expansión fronteriza 0,8 |
| Seguridad | Reducción de la amenaza máxima × 2 pu por punto | Supervivencia 2,0; hegemonía 1,0 |
| Territorio | Valor de las provincias (ingresos + población + valor simbólico) | Expansión 1,5; comercio 0,6 |
| Legitimidad | Variación esperada × poder de los grupos | Todos 1,0; reformista 0,7 en reformas |
| Prestigio | Títulos, ciudades simbólicas, victorias | Prestigio imperial 1,5 |
| Ambición | Progreso del objetivo de nivel 1 | 0,5–1,5 según la intensidad de la ambición |
| Sesgo histórico | Prioridad de 101 History para la acción | 0 (sandbox) a 1,0 (estricto); nunca habilita acciones imposibles |
| Coste esperado | Dinero, bajas (convertidas por su efecto en agotamiento y producción), agravio ajeno | Todos 1,0 |
| Riesgo | Desviación de los resultados estimados × aversión al riesgo | Prudente 1,5; audaz 0,5 |

**Descuento temporal:** `valor_futuro / (1 + d)^años`, con d = 0,10 (base), 0,05 para personalidades de largo plazo (repúblicas mercantiles, dinastías estables) y 0,20 para gobernantes viejos, enfermos o en crisis.

#### Estimación de una guerra

```text
p_victoria  = simulación_rápida(fuerzas_estimadas, aliados_probables, logística, terreno, estación)
              (resolución agregada de tipo Lanchester con los parámetros de la sección 13, 20 repeticiones
               con el RNG por contador sobre las estimaciones, no sobre el estado real)
valor_guerra = p_victoria × valor_de_los_objetivos − (1 − p_victoria) × coste_de_la_derrota
             − coste_esperado (paga, bajas, comercio perdido, agotamiento) − agravio_de_terceros
se declara si valor_guerra > umbral_de_guerra (personalidad) y existe un casus belli
```

El umbral de guerra va de +5 pu (oportunista, audaz) a +25 pu (prudente, comercio primero). Sin casus belli, el coste incluye la penalización de “sin motivo” (sección 12), lo que hace raras pero posibles las guerras injustificadas.

#### Gestión del presupuesto (heurística ordenada)

1. Mantener una **reserva** de 3 meses de gastos ordinarios (6 en guerra).
2. Pagar el servicio de la deuda (salvo que la utilidad del impago supere 20 pu).
3. Pagar al ejército en campaña y a los mercenarios contratados.
4. Gastos de legitimidad mínimos (corte, culto) según la cultura.
5. Inversión según los objetivos activos (fortificaciones en fronteras amenazadas, barcos si la ambición es marítima, obras con rentabilidad).
6. Si falta dinero: subir impuestos con menor coste de legitimidad, pedir prestado si el tipo es < 15 %, arrendar impuestos, devaluar (solo con personalidad dispuesta y deuda alta).

#### Inercia y coherencia

- Un plan nuevo solo sustituye al actual si su utilidad supera la del actual en un **15 %** (histéresis), para evitar cambios de rumbo cada mes.
- Los tratados se valoran con el coste de romperlos (sección 12): la IA no abandona una alianza útil por una ganancia marginal.
- La IA no repite una propuesta rechazada al mismo país antes de 6 meses, salvo que cambie la situación de forma relevante (puntuación bélica ±15, nueva amenaza).

#### Presupuesto de cómputo

| Capa | Frecuencia | Candidatas máximas (K) | Presupuesto por país y decisión (escala S, PC de referencia) |
| --- | --- | --- | --- |
| Gran estrategia | Anual o por cambio de diagnóstico | 8 | 2 ms |
| Política y diplomacia | Mensual escalonada | 12 | 0,5 ms |
| Economía | Mensual escalonada | 10 | 0,3 ms |
| Militar operativa | Diaria (en guerra) / semanal (en paz) | 6 por ejército | 0,2 ms por ejército |

**Presupuesto global objetivo:** la IA consume ≤ 25 % del tick medio (≤ 2,5 ms de 10 ms) en la escala S. Los países en guerra con el jugador o fronterizos con él reciben prioridad; los lejanos y en paz pueden usar K reducido sin que el jugador perciba diferencia.

#### Dificultad visible

| Nivel | Qué cambia | Qué no cambia nunca |
| --- | --- | --- |
| Fácil | La IA usa K reducido y un umbral de guerra +10 pu más alto contra el jugador. | Las reglas, la información imperfecta, la economía. |
| Normal | Ninguna ventaja. | — |
| Difícil | La IA usa K completo, mejor descuento a largo plazo y coordinación de coaliciones contra el jugador (+10 % de disposición). | No recibe recursos gratuitos ni información oculta. |
| Muy difícil (opcional) | Además, +10 % de eficacia de recaudación para la IA, **mostrado** en el panel de reglas de la partida. | — |

#### Ejemplo resuelto: el beylik otomano decide entre bloquear Bursa o saquear la costa (1320)

| Opción | Ganancia | Seguridad | Territorio | Ambición “Tomar Bursa” | Coste | Riesgo (× 0,8) | Utilidad |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Bloqueo de Bursa (fortines, 4–8 años) | +18 pu (descontado) | +4 | +30 (ciudad y comarca) | +25 | −32 (fortines, ejército inmóvil) | −8 | **+37** |
| Saqueo de la costa de Mármara | +22 pu (botín inmediato) | −3 (agravio bizantino) | 0 | +2 | −9 | −4 | **+8** |
| Paz y comercio con Bizancio | +6 | +6 | 0 | 0 | 0 | −1 | **+11** |

La IA elige el bloqueo, lo descompone en tareas (construir dos fortines, mantener 1.500 jinetes en la comarca, cortar el camino de Nicomedia) y lo revisa cada año. El panel “¿por qué?” del jugador bizantino muestra la estimación otomana tal como la conoce su inteligencia, con el margen de error correspondiente.

#### Salud de la IA y métricas de Lab

| Métrica | Umbral de alerta |
| --- | --- |
| Meses sin acción válida (por país) | > 12 |
| Guerras declaradas con `p_victoria` estimada < 0,2 | > 5 % de las guerras |
| Bancarrotas evitables (reserva disponible no usada) | > 0 |
| Propuestas repetidas rechazadas | > 3 por año y par de países |
| Cambios de objetivo estratégico por década | > 4 |
| Tiempo de IA por tick | > 25 % del tick medio |

---

# Parte IV · Experiencia

## 18. Interfaz, mapa y accesibilidad

### Pantallas principales

| Pantalla | Contenido |
| --- | --- |
| Mapa | Vista central con modos, filtros, etiquetas, ejércitos, flotas y rutas. |
| Panel de país | Resumen, gobierno, economía, ejército, diplomacia, cultura, tecnología, historia. |
| Panel de provincia | Población por cohortes, edificios, producción, control, cultura, religión, historial. |
| Mercado | Precios, oferta, demanda, rutas, contribuyentes de cada cambio. |
| Presupuesto | Ingresos, gastos, deuda, acreedores, proyecciones. |
| Política | Grupos de interés, leyes, legitimidad, facciones, rebeliones. |
| Diplomacia | Relaciones multidimensionales, tratados, negociaciones, inteligencia. |
| Guerra | Objetivos, puntuación, frentes, asedios, logística, propuesta de paz. |
| Tecnología | Grafo navegable, difusión mundial, límites de adelanto. |
| Personajes | Corte, dinastía, consejo, generales. |
| Línea de tiempo | Historia de la partida frente a historia real; comparación de mapas por fecha. |
| Enciclopedia | Entradas sobre entidades, culturas, religiones, tecnologías y sucesos, con fuentes. |
| 101 Lab (desarrollo) | Gráficas agregadas de muchas campañas. |

### Modos de mapa

Político, terreno, población (densidad y crecimiento), cultura, religión, idioma, nivel de vida, economía (producción por bien), precios, comercio (rutas y volumen), suministro, militar (ejércitos, fortificaciones), diplomacia (relaciones desde el país seleccionado), control efectivo, legitimidad, tecnología (difusión de una tecnología concreta), clima, epidemias, divergencia histórica.

### Legibilidad

Nunca se muestra solo “−5 estabilidad”. Cada cambio indica **causa, alcance, duración y posibles respuestas**, y permite navegar a la causa de la causa.

| Pregunta del jugador | Respuesta que debe poder dar la interfaz |
| --- | --- |
| ¿Por qué sube el precio del grano? | Oferta y demanda, con los tres mayores contribuyentes. |
| ¿Por qué perdí esta batalla? | Comparativa de factores: número, suministro, terreno, mando, doctrina, moral. |
| ¿Por qué no puedo investigar esto? | Los prerrequisitos que faltan, cada uno enlazado a su ruta. |
| ¿Por qué me declaró la guerra? | Las alternativas que evaluó la IA y los factores decisivos. |

### La primera hora de juego

La gran estrategia pierde a muchos jugadores en la primera hora. El objetivo es que, al terminarla, el jugador haya tomado decisiones con consecuencias y entienda **cómo preguntar “¿por qué?”**.

| Minuto | Qué ve y hace el jugador | Qué aprende |
| --- | --- | --- |
| 0–3 | Elige país en un mapa con fichas breves: dificultad, estilo de juego, reto principal. Recomendación inicial: Bizancio para aprender, Venecia para comerciar, otomanos para expandirse. | Que cada país juega distinto. |
| 3–8 | Pausa inicial. Un asesor presenta tres cosas: el tesoro, la amenaza principal y un objetivo sugerido. | Las tres preguntas básicas: dinero, peligro, objetivo. |
| 8–15 | Primera decisión guiada: un problema de financiación con tres opciones y sus efectos completos. | A leer efectos en el registro causal. |
| 15–25 | Avanza el tiempo. Aparece un cambio de precio o de estabilidad; el tutorial invita a abrir “¿por qué?”. | La herramienta central del juego. |
| 25–40 | Primera negociación diplomática y primer movimiento de un ejército. | Diplomacia y guerra básica. |
| 40–60 | Primer suceso no guiado. El jugador decide solo; el tutorial solo ofrece ayuda si la pide. | Autonomía; el juego deja de llevarle de la mano. |

**Principios del tutorial:**

- Enseñar en contexto, nunca con pantallas largas de texto.
- Cada lección termina con una decisión real, no con un botón de “siguiente”.
- Se puede desactivar en cualquier momento y retomar desde el menú.
- Las ventanas de ayuda enlazan a la enciclopedia para quien quiera profundizar.

### Delegación

El jugador puede delegar en asesores la economía, el comercio, la diplomacia menor o ejércitos concretos, con reglas configurables (“no endeudarse por encima de X”, “no romper alianzas”). Cada acción del asesor se registra y es reversible cuando sea posible.

### Accesibilidad

- Escalado de interfaz y de texto.
- Paletas para daltonismo (protanopía, deuteranopía, tritanopía) y modo de alto contraste.
- Patrones y símbolos además del color en los modos de mapa.
- Atajos configurables para todas las acciones frecuentes.
- Velocidades de juego lentas y pausas automáticas generosas.
- Subtítulos y textos para todo el audio con información.

### Localización

Español e inglés desde el slice, con el sistema preparado para más idiomas. Los nombres de lugares y personas tienen variantes (endónimo, exónimo en el idioma del jugador, nombre histórico de la época), seleccionables.

### Especificación detallada de la interfaz (v0.7, propuesto)

Base de `docs/specs/ui-panels.md`.

#### Anatomía del panel “¿por qué?”

```text
┌─ Precio del grano en Constantinopla ─────────────────────────────── 13,4 uc/t ▲ +49 % ─┐
│ Base 9,0  ·  Hace 1 año 9,3  ·  Media 52 semanas 10,1                                   │
│                                                                                         │
│  Mayores contribuyentes (últimas 12 semanas)                                            │
│  ▲ +2,9  Oferta local −38 %          Sequía en Tracia (anomalía −2)            [ir →]   │
│  ▲ +1,1  Existencias bajo objetivo   Graneros al 54 %                          [ir →]   │
│  ▲ +0,6  Demanda militar             Ejército de Adrianópolis (6.200 hombres)  [ir →]   │
│  ▼ −0,4  Importaciones               Grano de Caffa por mercaderes genoveses   [ir →]   │
│  ··· 4 contribuyentes menores (+0,2)                                                    │
│                                                                                         │
│  [Gráfica de 104 semanas con las contribuciones apiladas]                              │
│                                                                                         │
│  Qué puedes hacer: abrir los graneros · prohibir la exportación · negociar con Génova   │
└─────────────────────────────────────────────────────────────────────────────────────────┘
```

| Elemento | Regla |
| --- | --- |
| Encabezado | Valor actual, unidad, variación y periodo de la variación. |
| Referencias | Valor base, valor de hace un periodo largo y media móvil. |
| Contribuyentes | Los cinco mayores en valor absoluto, ordenados; el resto agregado en una línea. |
| Enlace | Cada contribuyente abre el “¿por qué?” de su causa (la causa de la causa). |
| Gráfica | Opcional; contribuciones apiladas en el tiempo. |
| Respuestas | Solo acciones posibles ahora, cada una con su previsión de efecto. |
| Incertidumbre | Si la variable es de otro país, el valor es un rango y se indica la fecha de la información. |

#### Tooltips anidados

| Nivel | Se abre con | Contenido | Longitud máxima |
| --- | --- | --- | --- |
| 1 | Pasar el cursor 300 ms | Valor, una línea de explicación y la mayor causa | 25 palabras |
| 2 | Mantener 800 ms o pulsar `Mayús` | Lista de contribuyentes con valores | 8 líneas |
| 3 | Clic en un término subrayado | Tooltip del término (glosario) o del contribuyente | 60 palabras |
| Fijado | `Ctrl` + clic o tecla `T` | Cualquier nivel queda fijo como ventana movible | — |

#### Composición de la pantalla (1920 × 1080)

| Zona | Posición | Contenido |
| --- | --- | --- |
| Barra superior | 0–48 px | Fecha, velocidad, tesoro, ingresos netos, legitimidad, estabilidad, agotamiento, alertas resumidas |
| Barra de alertas | Derecha, 48–600 px | Alertas agrupadas por prioridad (Anexo AO) |
| Panel principal | Izquierda, hasta 640 px de ancho | País, provincia, mercado, política… con historial de navegación |
| Mapa | Resto | Siempre visible; nunca queda tapado por completo |
| Selector de modos de mapa | Inferior derecha | Modos favoritos y búsqueda |
| Panel de detalle | Ventanas flotantes anclables | Comparaciones lado a lado, tooltips fijados |

A 1280 × 800 (Steam Deck) el panel principal se convierte en una hoja que ocupa el 50 % de la pantalla y la barra superior se reduce a iconos con cifras.

#### Atajos de teclado por defecto

| Tecla | Acción | Tecla | Acción |
| --- | --- | --- | --- |
| `Espacio` | Pausa / reanudar | `1`–`5` | Velocidad |
| `F1` | País | `F2` | Economía y presupuesto |
| `F3` | Política | `F4` | Diplomacia |
| `F5` | Guerra | `F6` | Tecnología |
| `F7` | Personajes | `F8` | Libro de estadísticas |
| `W` | “¿Por qué?” de lo que está bajo el cursor | `T` | Fijar tooltip |
| `Q` / `E` | Modo de mapa anterior / siguiente | `Ctrl` + `F` | Búsqueda universal |
| `Alt` + `←` / `→` | Atrás / adelante en paneles | `Ctrl` + `Z` | Deshacer órdenes dadas en pausa |
| `N` | Siguiente alerta | `Esc` | Cerrar panel / menú |

Todos son reconfigurables (F-QOL-09) y tienen equivalente con mando para Steam Deck.

#### Formato de cifras y fechas

| Elemento | Español | Inglés |
| --- | --- | --- |
| Miles y decimales | 12.345,6 | 12,345.6 |
| Cantidades grandes | 1,2 M (millones), 34 mil | 1.2M, 34k |
| Porcentajes | 12 % (con espacio fino) | 12% |
| Dinero | 465.000 uc o 930.000 hiperpirones (según preferencia) | 465,000 uc |
| Fechas | 14 de mayo de 1302 (o calendario cultural opcional) | 14 May 1302 |
| Rangos estimados | 4.000–7.000 | 4,000–7,000 |

El formato lo aplica la capa de localización (Fluent con funciones de número y fecha); el motor solo entrega enteros y punto fijo.

#### Reglas de delegación (asesores)

Las reglas del jugador se expresan como **límites y prioridades**, no como guiones:

| Asesor | Reglas configurables (ejemplos) |
| --- | --- |
| Económico | Deuda máxima (en % de ingresos), reserva mínima (meses), prioridades de inversión (lista ordenada), impuestos que no puede subir, prohibición de devaluar |
| Comercial | Mercados prioritarios, privilegios que no se pueden conceder, flota mercante mínima |
| Diplomático menor | Relaciones que mantener por encima de un valor, prohibición de romper tratados, matrimonios permitidos |
| General | Orden de campaña, provincias que no se pueden abandonar, bajas máximas aceptables, prohibición de devastar |

Cada acción de un asesor genera una entrada en su registro (F-ADV-05) con la regla que la justificó; las acciones reversibles se deshacen con un clic mientras no hayan producido efectos irreversibles.

## 19. Dirección de arte y audio

### Principios

- **El mapa es el protagonista:** el jugador pasa el 80 % del tiempo mirándolo. Debe ser bello, legible y rápido.
- **Sobriedad:** tipografía clara, composición precisa, formas simples. Se evita la estética genérica de IA (gradientes neón, cubos 3D, brillos, redes neuronales).
- **La época se ve:** el estilo cartográfico y la interfaz evolucionan con el tiempo.

### Estilo cartográfico por época (propuesto)

| Época | Estilo del mapa | Interfaz |
| --- | --- | --- |
| 1300–1500 | Pergamino, tintas sepia, rotulación caligráfica, ríos azul pálido, relieve sombreado a mano. | Marcos sobrios inspirados en manuscritos. |
| 1500–1750 | Grabado en cobre, cartelas, rosas de los vientos, colores a la acuarela. | Tipografía romana y cursiva de imprenta. |
| 1750–1900 | Cartografía topográfica, curvas de nivel, colores planos. | Tipografía de periódico y documentos oficiales. |
| 1900–1990 | Mapas de estado mayor, colores de atlas escolares. | Estética de informe técnico. |
| 1990+ | Cartografía digital limpia, datos superpuestos. | Interfaz de panel de datos. |

La transición es gradual y opcional: el jugador puede fijar un estilo.

### Ilustración

- Retratos de personajes: ilustración 2D con estilo propio (no fotorrealista), construida con capas por cultura, época, edad y vestimenta.
- Ilustraciones de eventos: escenas pintadas por época, reutilizables entre regiones mediante variantes.
- Iconografía: conjunto propio y coherente para bienes, edificios, tecnologías y acciones.
- Banderas y escudos: generados por reglas heráldicas y vexilológicas con datos históricos cuando existan.

### Audio

- Música adaptativa por región y época, con instrumentación histórica; capas que suben de intensidad en guerra o crisis.
- Paisaje sonoro discreto en el mapa (mar, ciudades, campamentos).
- Sonidos de interfaz breves y consistentes.

**Producción:** las ilustraciones, la música y los textos finales deben tener autoría y licencias claras. Los recursos generados con herramientas de IA, si se usan, deben revisarse por licencia, calidad y consistencia, y declararse según las normas de la tienda.

### Especificación de arte y audio para la vertical (v0.7, propuesto)

#### Inventario de recursos del slice

| Recurso | Cantidad | Formato y tamaño | Notas |
| --- | --- | --- | --- |
| Iconos de bienes | ≈ 45 | SVG fuente; atlas de 64 y 32 px | Silueta legible a 16 px; color por categoría |
| Iconos de edificios | ≈ 40 | Igual | Variantes por época en épocas posteriores |
| Iconos de tecnologías | ≈ 60 | Igual | Una metáfora visual por técnica |
| Iconos de leyes, acciones y alertas | ≈ 120 | Igual | Coherentes con el catálogo de alertas (Anexo AO) |
| Iconos de unidades y barcos | ≈ 25 | Igual + versión de mapa a 24 px | Contorno legible sobre cualquier color de país |
| Retratos modulares | 6 culturas × 3 edades × 2 sexos × 8–12 capas | PNG con capas, 512 × 640 | Fondo, cuerpo, cabeza, peinado, barba, tocado, vestido, insignias de rango |
| Ilustraciones de eventos | ≈ 40 | 1.280 × 720, pintadas | Reutilizables con variantes de color y detalle |
| Pantallas de carga | 4 | 1.920 × 1.080 | Mapas antiguos reinterpretados, no copiados |
| Texturas del mapa | Relieve, agua, papel, trama | 4.096 × 4.096 (slice) | Estilo de pergamino de la sección 19 |
| Escudos y banderas | 18 entidades + reglas para las generadas | SVG | Heráldica histórica cuando existe |

#### Paleta y tipografía por época (slice)

| Uso | Propuesta 1300–1500 | Regla |
| --- | --- | --- |
| Papel del mapa | Pergamino claro con variación sutil | Nunca más oscuro que el color de país más claro |
| Colores de país | 18 colores con separación perceptual (ΔE ≥ 20 entre vecinos) | Verificados con simulación de daltonismo |
| Tinta de bordes | Sepia oscuro para países, sepia medio para provincias | Grosor por jerarquía (3 / 1,5 / 0,75 px a zoom medio) |
| Tipografía de mapa | Romana humanista con versalitas para países | Licencia abierta o adquirida; cobertura de griego y latín extendido |
| Tipografía de interfaz | Sans serif muy legible en cifras tabulares | Cobertura completa de español, inglés, griego, cirílico y turco |

#### Música y sonido del slice

| Pieza | Duración | Uso | Instrumentación orientativa |
| --- | --- | --- | --- |
| Tema principal | 3 min | Menú, tráiler | Conjunto medieval mediterráneo + cuerdas |
| Paz, Mediterráneo griego | 3 × 4 min | Mapa en paz con país griego | Laúd, salterio, voces |
| Paz, Anatolia turca | 3 × 4 min | Mapa en paz con país turco | Ney, *saz*, percusión de marco |
| Paz, latinos (Venecia, Génova, francos) | 3 × 4 min | Mapa en paz con país latino | Vihuela, flautas, voces |
| Paz, Balcanes eslavos y Hungría | 2 × 4 min | Mapa en paz | Gusle, gaita, voces |
| Tensión | 2 × 3 min, en capas | Crisis, guerra cercana | Percusión y bordones añadidos a las capas de paz |
| Guerra | 2 × 3 min | Batallas seguidas por el jugador | Percusión, metales naturales |
| Peste | 1 × 3 min | Epidemia en el país | Bordón grave, silencio, campanas lejanas |
| Señales de alerta | ≈ 15 sonidos | Por prioridad de alerta | Distinguibles sin mirar la pantalla (F-AUD-03) |

La música se encarga a intérpretes de instrumentos históricos o se licencia con derechos claros; las reconstrucciones no pretenden ser música histórica exacta, sino una evocación respetuosa.

## 20. Modding y comunidad

### Qué se puede modificar

| Nivel | Contenido | Herramienta |
| --- | --- | --- |
| Datos | Países, culturas, religiones, bienes, edificios, tecnologías, personajes. | Archivos declarativos + validador. |
| Eventos y situaciones | Condiciones, efectos, variantes. | Lenguaje de condiciones; después, scripting. |
| Mapa | Localizaciones, provincias, terreno. | 101 Forge. |
| Interfaz | Textos, traducciones, iconos, estilos. | Archivos de localización y recursos. |
| Reglas | Parámetros de los sistemas (constantes de economía, guerra, etc.). | Archivos de parámetros. |

### Principios

- El contenido del juego base usa **los mismos formatos** que los mods. Si el estudio no puede hacer algo con datos, un modder tampoco.
- Validación estricta antes de cargar: un mod roto muestra errores claros en lugar de corromper la partida.
- Los mods no pueden acceder al sistema de archivos, la red ni el reloj.
- Compatibilidad: cada mod declara la versión del juego y sus dependencias; las partidas registran los mods usados.

### Comunidad

- Steam Workshop (1.0).
- Documentación pública de formatos y del lenguaje de condiciones.
- Canal de comunicación con la comunidad (Discord u otro) desde la página de Steam.
- Diarios de desarrollo periódicos para construir audiencia antes del lanzamiento.

### Especificación detallada de mods (v0.7, propuesto)

#### Estructura de un mod

```text
mi_mod/
├── mod.ron                 manifiesto: id, nombre, versión, versión del juego compatible,
│                           dependencias, conflictos, orden de carga, autores, licencia
├── data/                   mismos subdirectorios que games/epoch/data/ (entities, cultures…)
├── locale/es/, locale/en/  archivos Fluent
├── assets/                 iconos, retratos, mapas (formatos y tamaños validados)
└── README.md
```

#### Reglas de carga y combinación

| Operación | Sintaxis en datos | Resultado |
| --- | --- | --- |
| Añadir | Objeto con ID nuevo | Se añade al catálogo |
| Reemplazar | `Replace(id: "…", …)` | Sustituye el objeto completo; el validador avisa si otro mod también lo reemplaza |
| Parchear | `Patch(id: "…", set: { campo: valor }, add: { lista: […] }, remove: { lista: […] })` | Cambia campos concretos; varios mods pueden parchear el mismo objeto si no tocan los mismos campos |
| Eliminar | `Remove(id: "…")` | Solo si ningún otro objeto lo referencia tras aplicar todos los mods |

**Orden:** juego base → mods en el orden de carga resuelto por dependencias (orden topológico, empates por ID). El resultado se compila con el mismo `e101-content` que el juego base; un mod que no valida no se carga y el jugador ve el informe de errores con archivo y línea.

#### Seguridad y compatibilidad

- Los mods de datos no ejecutan código; 101 Script (Anexo AL) no tiene acceso al reloj, la red ni el sistema de archivos.
- Los recursos gráficos y de audio se validan por formato, tamaño y dimensiones antes de cargarse.
- Cada guardado registra los mods y sus versiones (Anexo AR); los logros se desactivan con mods que cambian reglas, no con mods solo visuales o de traducción (marcados en el manifiesto y verificados por el validador).

### Especificación del informe nocturno de 101 Lab (v0.7, propuesto)

| Sección del informe | Contenido |
| --- | --- |
| Resumen | Semáforo por métrica del Anexo F y del Anexo AW; métricas que cambiaron de rango respecto a la noche anterior |
| Historia | Distribuciones de fechas de situaciones clave por modo; mapa de calor de divergencia media |
| Salud del mundo | Invariantes, bancarrotas, guerras, duración de guerras, IA bloqueadas |
| Economía | Precios del grano por mercado (percentiles 10/50/90), inflación, deuda/ingresos por Estado |
| Población | Población total del slice, impacto y recuperación de la peste, migración neta por región |
| Balance | Supervivencia y tamaño de cada entidad (Anexo AW) |
| Rendimiento | Tick medio y p99 por sistema; memoria por siglo simulado |
| Diferencias | Lista de commits del día y métricas que movieron (comparación con las mismas semillas) |

El informe es un HTML estático con gráficas y un Parquet por campaña; un enlace “reproducir” lanza la campaña con su semilla y su versión en local.

---

# Parte V · Tecnología

## 21. Arquitectura de 101 Engine

```text
101 ENGINE  (workspace de Rust; nombres de crate definitivos de la sección 40)
│
├── Núcleo determinista (sin dependencias gráficas)
│     ├── e101-time       tiempo, calendarios, escalonamiento
│     ├── e101-rng        aleatoriedad por contador
│     ├── e101-store      tablas SoA, punto fijo, identificadores
│     ├── e101-commands   bus y diario de comandos
│     ├── e101-ledger     registro causal
│     ├── e101-map        (101 Map)     geografía, adyacencias, rutas, consultas espaciales
│     ├── e101-content    carga, validación y compilación de datos
│     ├── e101-script     (101 Script)  lenguaje de condiciones y efectos
│     ├── e101-sim        (101 Sim)     población, economía, política, diplomacia, guerra, ciencia, clima
│     ├── e101-history    (101 History) plausibilidad, situaciones, divergencia
│     ├── e101-ai         IA de países y personajes
│     └── e101-save       guardado, migraciones, hashes, repeticiones
│
└── Ejecutables y herramientas
      ├── e101-headless   simulación sin ventana
      ├── e101-lab        (101 Lab)     campañas masivas, informes, benchmarks
      ├── e101-client     render, ventana, entrada, UI, audio
      └── e101-forge      (101 Forge)   editores y validadores de contenido
```

**Regla de dependencias:** ningún crate del núcleo depende de `e101-client`, `e101-forge` ni de bibliotecas gráficas (grafo completo en la sección 40). El cliente lee el estado mediante **vistas de solo lectura** e **instantáneas**, y envía **comandos**; nunca modifica el estado directamente. *(En la v0.6 esta sección usaba nombres provisionales —`sim-core`, `map-data`…—; desde la v0.7 los únicos nombres válidos son los de prefijo `e101-`.)*

### Flujo de un tick

```text
1. Recoger comandos (jugador, IA, eventos) con marca de tick
2. Validar comandos contra el estado actual
3. Fase de lectura en paralelo: cada sistema calcula deltas
4. Ordenar deltas por clave estable y aplicarlos
5. Actualizar el registro causal y los índices derivados
6. Verificar invariantes (en modo de prueba) y calcular el hash de estado
7. Publicar una vista del estado para el cliente
```

### Calendario de sistemas dentro del tick (v0.7, propuesto)

El orden es **fijo y forma parte del contrato de determinismo**: cambiarlo cambia los hashes dorados y exige un ADR. Los sistemas de una misma fase leen el mismo estado y escriben deltas; las fases se aplican en orden.

| Fase | Sistema | Frecuencia | Lee | Escribe (deltas) |
| --- | --- | --- | --- | --- |
| 0 | Comandos | Diaria | Diario de comandos | Validación; deltas de órdenes |
| 1 | Clima y estación | Diaria (cambio de estación); anual (anomalías) | Calendario, semilla | Estado climático |
| 2 | Movimiento militar y naval | Diaria | Ejércitos, grafo de viaje | Posiciones, llegadas |
| 3 | Batallas y asedios | Diaria | Ejércitos en contacto, fortificaciones | Bajas, moral, progreso de asedio |
| 4 | Suministro militar | Diaria | Ejércitos, provincias | Consumo, desgaste |
| 5 | Epidemias | Semanal (escalonada por provincia) | Población, tráfico | S, I, R, fallecidos |
| 6 | Mercados y comercio | Semanal (escalonada por mercado) | Oferta, demanda, rutas | Precios, flujos, existencias |
| 7 | Producción y consumo | Mensual (escalonada por provincia); cosechas en su mes | Edificios, cohortes, precios | Bienes, ingresos, NV |
| 8 | Demografía y migración | Mensual (escalonada por provincia) | Cohortes, NV, seguridad | Nacimientos, muertes, flujos |
| 9 | Finanzas públicas | Mensual (escalonada por Estado) | Recaudación, gastos | Tesoro, deuda |
| 10 | Política | Mensual (escalonada por Estado) | Grupos, leyes, legitimidad | Presión, demandas, etapas de reformas |
| 11 | Diplomacia | Mensual (escalonada por Estado); tratados al vencer | Relaciones, tratados | Relaciones, vencimientos |
| 12 | Tecnología | Mensual (escalonada por Estado); adopción trimestral | Instituciones, contactos | Progreso, cuotas |
| 13 | Personajes | Mensual (salud y edad); diaria para muertes | Personajes | Muertes, nacimientos, sucesiones |
| 14 | 101 History | Mensual (escalonada por situación); divergencia anual | Estado agregado | Activación, etapas, sesgos |
| 15 | IA | Según capas (sección 17) | Mundo estimado | Comandos para el día siguiente |
| 16 | Registro causal e índices | Diaria | Deltas aplicados | Contribuciones, agregados |
| 17 | Invariantes y hash | Diaria (pruebas) / mensual (partida) | Estado | Informe, hash |

**Regla de la IA:** los comandos que la IA emite en el día *d* se marcan para el día *d + 1*. Así, la IA nunca ve los efectos de sus propios comandos dentro del mismo tick y el orden de los países no influye en el resultado.

### Separación simulación / presentación

La simulación avanza en sus propios hilos. El cliente renderiza a 60 FPS usando la última vista publicada e interpola lo que se mueve (ejércitos, flotas). Si la simulación va más lenta que la velocidad pedida, el reloj de juego se ralentiza; el render nunca se bloquea por la simulación.

### Registro causal (*causal ledger*)

Toda variable consultable se calcula como **valor base + suma de contribuciones con origen**.

| Campo | Ejemplo |
| --- | --- |
| Objetivo | Estabilidad de Castilla |
| Magnitud | −5 |
| Origen | Guerra con Aragón (entidad), impuesto extraordinario (ley) |
| Vigencia | Desde el día X hasta el fin de la guerra |
| Categoría | Militar / fiscal / religiosa |

- Para flujos agregados (precios, comercio) se guardan los **N mayores contribuyentes** por periodo.
- Detalle de los últimos meses en un búfer circular; más atrás, solo agregados. La memoria queda acotada en partidas de siglos.
- Interfaz, IA y 101 Lab consultan el mismo registro.

### Principios de ingeniería

- **Separar motor y contenido:** la lógica general no depende de que un evento concreto ocurra en 1453.
- **Headless first:** toda campaña puede simularse sin ventana ni GPU.
- **Comandos, no mutaciones.**
- **Datos orientados a memoria:** IDs estables y almacenamiento SoA.
- **Actualización incremental:** se recalcula solo lo afectado cuando es seguro.
- **Versionado de partidas:** instantáneas, migraciones y verificación de integridad.

## 22. Stack tecnológico recomendado

Estado comprobado en octubre de 2026. Cada elección debe revalidarse en la Fase 0 con la versión vigente, y toda versión concreta se fija en el repositorio para evitar actualizaciones accidentales.

### Qué construye 101 Engine y qué toma de terceros

| Pieza | Decisión | Motivo |
| --- | --- | --- |
| Núcleo de simulación | **Construir** | Es el corazón del producto: determinismo, registro causal y sistemas propios. Ningún motor lo trae. |
| Scheduler y modelo de datos | **Construir** | Requisitos de escalonamiento, SoA y orden estable muy específicos. |
| Pipeline de contenido y validadores | **Construir** sobre Serde | El formato de datos es propio y compartido con los mods. |
| Render del mapa | **Construir** sobre wgpu o sobre el motor elegido | El mapa es la pieza visual principal y necesita técnicas específicas. |
| UI del juego | **Adoptar** un framework y personalizar | Construir una UI desde cero es caro y arriesgado para un equipo pequeño. |
| Ventanas, entrada, audio, fuentes | **Adoptar** | Problemas resueltos por bibliotecas maduras. |
| Física, animación 3D, editor de escenas general | **No necesario** | Un juego de gran estrategia no lo requiere. |
| Red | **Adoptar** cuando llegue el multijugador | Steam Networking o QUIC. |

### Módulos internos de 101 Engine

| Módulo | Crate | Responsabilidad | Interfaz principal |
| --- | --- | --- | --- |
| `time` | `e101-time` | Día absoluto, calendarios de presentación, escalonamiento. | `Day`, `Calendar`, `Stagger`. |
| `store` | `e101-store` | Tablas SoA indexadas por ID estable; slotmaps para entidades dinámicas; punto fijo. | Lectura inmutable en paralelo; escritura solo en la fase de aplicación. |
| `commands` | `e101-commands` | Bus de comandos con marca de tick, validación y registro. | `Command`, `CommandLog`. |
| `systems` | `e101-sim` | Sistemas de simulación que leen el estado y emiten deltas. | `fn run(&State, &mut Deltas)`. |
| `apply` | `e101-sim` | Ordenación estable y aplicación de deltas; verificación de invariantes. | `Apply`, `Invariant`. |
| `ledger` | `e101-ledger` | Registro causal: contribuciones con origen, búfer circular, agregados. | `why(variable) -> Contributions`. |
| `query` | `e101-sim` | Vistas de solo lectura para el cliente, la IA y Lab. | `View`, `Snapshot`. |
| `rng` | `e101-rng` | Generador basado en contador. | `rng(seed, system, entity, day)`. |
| `content` | `e101-content` | Carga, validación y compilación de datos. | `ContentDb`. |
| `script` | `e101-script` | Lenguaje de condiciones y efectos (Anexo AL); después, máquina virtual de scripting. | `Condition`, `Effect`. |
| `save` | `e101-save` | Guardado, carga, migraciones, hashes, repeticiones. | `SaveFile`, `Replay`. |
| `history` | `e101-history` | Situaciones, divergencia, sesgos históricos. | `Situation`, `Divergence`. |
| `ai` | `e101-ai` | Decisiones de países y personajes con presupuesto de cómputo. | `Planner`, `Utility`. |
| `lab` | `e101-lab` | Ejecución masiva y exportación de resultados. | `Campaign`, `Report`. |

### Opciones para el cliente

| Opción | Descripción | Estado (oct. 2026) | Licencia y costes |
| --- | --- | --- | --- |
| **A. Cliente propio sobre wgpu** | Render, ventana (winit) y UI (egui u otra) montados a mano en Rust. | wgpu publica versiones mayores con frecuencia (serie 29 en 2026). | MIT/Apache; sin regalías. |
| **B. Bevy** | Motor de datos orientado a ECS, todo en Rust. | Bevy 0.20 (8 de octubre de 2026), aún antes de la 1.0, con cambios incompatibles en cada versión y guía de migración. | MIT/Apache; sin regalías. |
| **C. Fyrox** | Motor en Rust con editor integrado y UI propia. | Alcanzó la 1.0 en marzo de 2026 tras unos siete años de desarrollo, con estabilización de API. | MIT; sin regalías. |
| **D. Godot + Rust (GDExtension)** | Motor con editor y UI muy maduros; el núcleo Rust se integra como extensión mediante la biblioteca comunitaria godot-rust. | Godot 4.7.2 (agosto de 2026). Verificar la versión de godot-rust compatible. | MIT; sin regalías. |
| **E. Unity + núcleo Rust** | Motor comercial en C#; el núcleo se integra como biblioteca nativa. | Maduro. | Propietaria; sus condiciones han cambiado en el pasado (revisar las vigentes). |
| **F. Unreal + núcleo Rust** | Motor comercial en C++. | Maduro. | Propietaria; regalías sobre ingresos a partir de un umbral (revisar condiciones vigentes). |
| **G. Mapa en wgpu + UI web** | Mapa renderizado con wgpu; UI en HTML/CSS dentro de una vista web embebida, comunicada con el núcleo. | Tecnología web muy madura; la integración con el render nativo es la parte difícil. | Componentes libres; sin regalías. |

### Matriz de decisión ponderada (propuesta)

Puntuaciones de 1 a 5 basadas en el conocimiento actual; **deben confirmarse con el spike**. Los pesos reflejan lo que más importa a un juego de gran estrategia con equipo pequeño.

| Criterio (peso) | A | B | C | D | E | F | G |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Render del mapa 2D/3D (15) | 5 | 4 | 4 | 4 | 4 | 5 | 4 |
| UI densa de estrategia (20) | 2 | 3 | 3 | 5 | 4 | 3 | 5 |
| Herramientas y editor (10) | 2 | 2 | 4 | 5 | 5 | 5 | 3 |
| Estabilidad de API (10) | 3 | 2 | 4 | 4 | 4 | 4 | 4 |
| Integración con núcleo Rust (15) | 5 | 5 | 5 | 3 | 2 | 2 | 4 |
| Rendimiento (10) | 5 | 4 | 4 | 4 | 4 | 4 | 3 |
| Licencia y costes (5) | 5 | 5 | 5 | 5 | 3 | 3 | 5 |
| Multiplataforma y Steam Deck (5) | 4 | 4 | 4 | 5 | 5 | 4 | 4 |
| Productividad con agentes de IA (5) | 4 | 3 | 2 | 3 | 4 | 2 | 5 |
| Ecosistema y comunidad (5) | 3 | 4 | 2 | 5 | 5 | 4 | 4 |
| **Total sobre 100** | **74** | **71** | **76** | **85** | **77** | **72** | **82** |

**Lectura de la matriz:**

- **Godot + Rust (D)** gana por su UI y su editor, que son exactamente lo que más le cuesta a un equipo pequeño. Su riesgo es la frontera entre dos lenguajes: el núcleo vive en Rust y la presentación en el árbol de nodos de Godot.
- **Mapa en wgpu + UI web (G)** es la alternativa más interesante: HTML y CSS son ideales para paneles densos, tablas y tooltips anidados, y los agentes de IA son muy productivos con ellos. Su riesgo es componer la vista web sobre el render nativo con buen rendimiento.
- **Cliente propio (A)** es el más puro técnicamente, pero obliga a construir la UI y las herramientas.
- **Bevy (B)** y **Fyrox (C)** encajan con Rust, pero sus UI no están probadas en interfaces tan densas; Bevy además exige migraciones periódicas.
- **Unity (E)** y **Unreal (F)** aportan madurez, pero la integración con un núcleo Rust es incómoda y sus licencias añaden riesgo comercial.

**Recomendación:** spike comparativo entre **D** y **G**, con **A** como línea base porque el render del mapa en wgpu se reutiliza en G. Como el núcleo es independiente, la decisión es reversible.

### Bibliotecas de UI

| Biblioteca | Densidad y tablas | Tooltips anidados | Tematización | Licencia | Comentario |
| --- | --- | --- | --- | --- | --- |
| egui | Alta | Posible, manual | Limitada | MIT/Apache | Excelente para herramientas; apariencia difícil de pulir. |
| Slint | Media-alta | Posible | Buena (lenguaje declarativo) | Libre de regalías para escritorio con atribución visible (pantalla “Acerca de” o página de descarga); GPL-3.0; comercial | Buena opción nativa; revisar condiciones. |
| iced | Media | Manual | Buena | MIT | Arquitectura elegante; menos componentes. |
| UI de Godot | Muy alta | Sí | Muy buena, con editor visual | MIT | La más madura de la lista para juegos. |
| Bevy UI (widgets Feathers) | Media | Manual | En evolución | MIT/Apache | Mejora rápida, pero cambia entre versiones. |
| fyrox-ui | Media | Manual | Buena | MIT | Probada en el propio editor de Fyrox. |
| HTML/CSS en vista web | Muy alta | Sí | Total | Libre | Ideal para paneles; coste de integración y memoria. |

### Arquitectura de render del mapa

| Capa (orden de dibujo) | Contenido | Técnica |
| --- | --- | --- |
| 1. Terreno | Relieve, vegetación, nieve estacional. | Mapa de alturas y texturas mezcladas; sombreado de relieve. |
| 2. Agua | Mares, lagos, ríos. | Máscaras y animación sutil; ríos como líneas vectoriales con grosor por caudal. |
| 3. Color del modo de mapa | Político, cultura, economía, etc. | **Textura de IDs** + textura de colores por ID; cambio instantáneo de modo. |
| 4. Bordes | País, provincia, vasallos, frentes. | Detección de bordes por comparación de IDs en el shader; grosor por jerarquía. |
| 5. Estilo de época | Pergamino, grabado, atlas, digital. | Postproceso con texturas de papel, trama y paleta por época. |
| 6. Rutas y flechas | Comercio, suministro, movimientos. | Líneas instanciadas con grosor por volumen. |
| 7. Unidades e iconos | Ejércitos, flotas, ciudades, fortalezas. | Instancing; agrupación automática a poco zoom. |
| 8. Etiquetas | Países, regiones, ciudades, mares. | Fuentes SDF/MSDF curvadas sobre el eje del territorio. |
| 9. Niebla | Conocimiento geográfico e información. | Máscara por Estado. |
| 10. Interfaz | Paneles, tooltips, alertas. | Framework elegido. |

**Niveles de detalle:** a poco zoom se muestran macrorregiones, países y capitales; a zoom medio, provincias y ejércitos; a mucho zoom, ciudades, fortalezas, ríos menores y caminos. **Presupuesto de GPU:** el mapa debe mantener 60 FPS a 1080p en el PC de referencia con todas las capas activas en la escala S.

### Plan del spike de selección (tres semanas, Fase 1)

| Tarea idéntica para cada candidato | Métrica |
| --- | --- |
| Mapa de 400 provincias con textura de IDs y tres modos de mapa. | FPS; tiempo de cambio de modo. |
| Panel de provincia con una tabla de cohortes de 60 filas, ordenable. | Horas de desarrollo; fluidez. |
| Tooltip anidado de tres niveles conectado al registro causal. | Horas de desarrollo; claridad. |
| Etiquetas curvadas de países. | Calidad visual a varios zooms. |
| Integración con el núcleo: leer una vista y enviar un comando. | Líneas de código de pegamento; latencia. |
| Compilación y empaquetado para Windows y Linux. | Tiempo de compilación; tamaño del ejecutable. |
| Una tarea realizada íntegramente por un agente de IA. | Correcciones humanas necesarias. |

El resultado se registra en un ADR con las métricas medidas y la decisión.

### Decisiones clave del stack

| Área | Recomendación | Alternativas | Motivo |
| --- | --- | --- | --- |
| Lenguaje del núcleo | **Rust estable, edición 2024** | C++, C# | Rendimiento, seguridad de memoria, pruebas; la estrictez del compilador ayuda a revisar código de agentes. |
| Paralelismo | **Rayon** + scheduler propio | — | Paralelismo de datos maduro. |
| Datos de contenido | **RON** a mano; **CSV** para tablas grandes | TOML, YAML, JSON | RON representa bien estructuras de Rust; CSV se edita en hojas de cálculo. |
| Guardados | **postcard** o **bitcode** + **zstd** | rkyv para carga sin copia | bincode cesó su desarrollo en 2025 (RUSTSEC-2025-0141). |
| Scripting | Lenguaje de condiciones propio; después **Luau vía mlua** o **Rhai** | DSL completo propio | Decidir en la Fase 4 con eventos reales. |
| Localización | **Fluent** | gettext | Plurales y géneros correctos en español. |
| Audio | **kira** (o el del motor elegido) | rodio | Música adaptativa. |
| Herramientas | **egui** | — | Rápidas para Forge y Lab. |
| Análisis de Lab | **Parquet** + **Polars** o **DuckDB** | CSV | Rápido y columnar. |

### Bibliotecas por área (candidatas)

| Área | Candidatas | Nota |
| --- | --- | --- |
| Punto fijo | Tipos propios sobre `i64`; crate `fixed` | Tipos propios (`Money`, `Qty`, `Ratio`) son fáciles de auditar. |
| RNG | Generador basado en contador sobre `rand_core` | Derivar de (semilla, sistema, entidad, día). |
| Colecciones | `Vec` indexado por ID, `slotmap`, `indexmap`, `rustc-hash` | `slotmap` para entidades que nacen y mueren. |
| Grafos y rutas | `petgraph`, `pathfinding` | A* y Dijkstra. |
| Espacial | `rstar`, `geo`, `geojson` | Vecindad y pipeline geográfico. |
| Texto | `cosmic-text`, `glyphon` | Texto en GPU con Unicode completo. |
| Perfilado | `tracing`, Tracy, `puffin` | Tracy para análisis profundo; puffin dentro del juego. |
| Pruebas | `cargo-nextest`, `proptest`, `insta`, `divan` o `criterion` | Propiedades para invariantes. |
| Calidad | `clippy`, `rustfmt`, `cargo-deny` | `cargo-deny` vigila licencias y avisos. |
| Red (Post) | Steam Networking o `quinn` | Lockstep determinista. |
| Plataforma | `steamworks` | Logros, Workshop, nube. |

### Pipeline geográfico

Fuera del motor, con **QGIS** para edición manual y **Python** (GeoPandas, Shapely) o Rust (`geo`) para procesos automáticos: recortar costas, generar localizaciones, calcular adyacencias, rasterizar la textura de IDs. El resultado se compila a binario y se versiona.

### Integración continua

Caché de compilación, formato, lints, pruebas, `cargo-deny`, validación de datos, ejecuciones doradas de determinismo y benchmarks en un runner estable para comparar rendimiento entre commits.

## 23. Determinismo y reproducibilidad

**Definición:** misma versión del binario + mismos datos + misma semilla + mismos comandos ⇒ mismo estado, bit a bit, en cada tick.

| Fuente de no determinismo | Regla |
| --- | --- |
| Aritmética de punto flotante | Dinero, existencias, población y todo estado persistente en **enteros o punto fijo**. Flotantes solo en render y en cálculos intermedios convertidos de forma determinista. |
| Funciones de la plataforma | No usar en la lógica funciones trascendentes con flotantes (`exp`, `sin`, `pow`); usar tablas o implementaciones propias. |
| Orden de iteración | Prohibido iterar `HashMap`/`HashSet` de la biblioteca estándar en la simulación: su orden cambia entre ejecuciones. Usar vectores indexados, `BTreeMap` o hashers con semilla fija. |
| Paralelismo | Lectura en paralelo que produce **deltas**; aplicación ordenada por clave estable. Nada de reducciones paralelas de flotantes. |
| Aleatoriedad | RNG **basado en contador**: el número de una decisión se deriva de (semilla, sistema, entidad, día). No depende del orden de los hilos. |
| Tiempo real | La simulación nunca consulta el reloj del sistema. |
| Entrada | Toda entrada es un comando con marca de tick, registrado en el diario de comandos. |
| Scripts y mods | Sin acceso a reloj, red, sistema de archivos ni aleatoriedad propia. |

### Verificación

- **Hash de estado** al final de cada tick (o cada mes en partidas largas).
- **Ejecuciones doradas en CI:** escenarios fijos cuyo hash final se compara en cada cambio; los cambios intencionados se documentan.
- **Repeticiones:** semilla + diario de comandos reproducen cualquier partida, incluidos informes de errores.
- **Bisección:** el primer tick con hash distinto localiza el sistema responsable.
- **Lints propios** que impiden flotantes y `HashMap` en los crates del núcleo (`e101-sim`, `e101-ai`, `e101-history` y sus dependencias).

**Multijugador (Post):** el lockstep exige además determinismo **entre plataformas** (Windows, Linux, macOS; x86 y ARM). Las reglas anteriores lo hacen posible; debe verificarse con ejecuciones doradas en cada plataforma antes de prometerlo.

### Especificación del hash de estado (v0.7, propuesto)

| Aspecto | Decisión propuesta |
| --- | --- |
| Algoritmo | BLAKE3 de 256 bits (rápido, con implementación en Rust puro y paralelizable de forma determinista por bloques). |
| Qué se incluye | Todas las tablas del `State` serializadas en orden de ID con su formato canónico (enteros en little-endian, sin relleno), el día, la semilla y el contador de comandos. |
| Qué se excluye | Índices derivados reconstruibles (cachés de rutas, agregados de la interfaz) y el búfer detallado del registro causal (se incluye solo su resumen agregado). |
| Frecuencia | Cada tick en pruebas y ejecuciones doradas; cada mes en partidas normales; al guardar y al cargar. |
| Hash por sistema | Además del global, un hash por tabla (`population`, `economy`…) para que la bisección señale el sistema responsable sin repetir la simulación. |
| Estabilidad | El formato canónico se versiona; un cambio de formato exige migración y nueva línea base dorada. |

### Escenarios dorados iniciales

| Escenario | Duración | Qué protege |
| --- | --- | --- |
| `empty_300y` | 300 años sin sistemas activos | Tiempo, escalonamiento, scheduler |
| `economy_closed_100y` | 100 años, un mercado cerrado | Producción, consumo, precios, conservación |
| `slice_ai_only_50y` | 50 años de la vertical sin jugador | Integración de todos los sistemas |
| `war_two_states_10y` | Guerra entre dos Estados | Movimiento, batallas, asedios, paz |
| `plague_1347` | Peste inyectada en Caffa | Epidemias, demografía, economía de la escasez |
| `save_load_roundtrip` | Guardar en el año 30, cargar y seguir hasta el 60 | Formato de guardado y continuidad |
| `threads_1_vs_16` | Igual que `slice_ai_only_50y` con 1 y 16 hilos | Paralelismo determinista |

## 24. Datos históricos y pipeline

Los datos de 1300 no tienen la precisión de los actuales. El sistema registra procedencia, fecha, rango, incertidumbre y decisiones editoriales.

| Conjunto | Campos básicos |
| --- | --- |
| Territorio | Geometría, topografía, red, recursos, ciudades, clima, accesibilidad. |
| Entidades políticas | Nombre, gobierno, control, jerarquía, reclamaciones, tratados. |
| Demografía | Cohortes, ocupaciones, identidades, distribución, estimación temporal. |
| Economía | Producción, precios, acceso comercial, capital, ingresos, flujos. |
| Tecnología | Dependencias, institución, instrumentos, ventana, madurez. |
| Situaciones | Ventana, actores, condiciones, caducidad, variantes, fuentes. |
| Personajes | Dinastía, fechas, rasgos, cargos, reclamaciones. |
| Historiografía | Referencia, categoría, confianza, incertidumbre, notas. |

### Niveles de confianza

| Nivel | Significado | Ejemplo |
| --- | --- | --- |
| A | Documentado con fuentes concordantes. | Fecha de un tratado conocido. |
| B | Estimación académica con rango aceptado. | Población de una gran ciudad hacia 1400. |
| C | Extrapolación del equipo a partir de datos cercanos. | Población rural de una provincia poco documentada. |
| D | Valor de diseño sin base histórica directa. | Tecnología posterior a 2060. |

### Fuentes de datos candidatas

| Fuente | Uso | Licencia y advertencias |
| --- | --- | --- |
| Natural Earth | Costas, ríos, relieve base. | Dominio público. |
| HYDE 3.3 (Universidad de Utrecht) | Población histórica en cuadrícula de 5 minutos de arco (~85 km² en el ecuador), de 10.000 a. C. a 2023. | Acceso abierto; confirmar la licencia exacta antes de usarla en un producto comercial. |
| historical-basemaps (A. Ourednik) | Referencia de fronteras históricas. | GPL-3.0: usar solo como **referencia** de trabajo, no incluirlo en el juego. El autor advierte que es un trabajo en curso y que las fronteras premodernas son aproximadas. |
| Reconstrucciones climáticas (atlas de sequías, series paleoclimáticas) | Anomalías de clima por región. | Verificar licencia de cada conjunto. |
| Seshat y bases académicas de historia comparada | Capacidad estatal, instituciones. | Verificar licencia y condiciones de uso. |
| Bibliografía académica regional | Gobernantes, situaciones, economía. | Citar en la Biblia histórica; no copiar textos protegidos. |

### Pipeline

**Fuentes → extracción → normalización (fechas a día absoluto, unidades, IDs) → validación → compilación a binario → carga en el motor.** Cada paso es reproducible y versionado; los datos compilados nunca se editan a mano.

### Validadores

Referencias rotas, calendarios imposibles, provincias sin adyacencias válidas, ciclos en el grafo tecnológico, gobernantes con fechas solapadas, situaciones sin caducidad, efectos que violan la contabilidad o la soberanía, textos sin traducción.

## 25. Rendimiento y pruebas

### Presupuestos de diseño

| Indicador | Objetivo (escala S salvo indicación) |
| --- | --- |
| Tick diario medio | ≤ 10 ms |
| Tick diario p99 (incluye cierres mensuales) | ≤ 50 ms, gracias al escalonamiento |
| Velocidad máxima jugable | ≥ 20 días de juego por segundo |
| Renderizado del mapa | 60 FPS a 1080p, con la simulación en hilos separados |
| Campaña headless de 300 años | ≤ 20 min |
| Carga de partida | ≤ 10 s en escala S |
| Memoria | ≤ 2 GB en escala S; objetivo de escala L tras la Fase 1 |
| Sesiones largas | 760 años sin fugas de memoria ni cuentas negativas |

**Por qué estas cifras:** de 1300 a 2060 hay unos 277.600 días. Con 50 ms por tick, una campaña completa requeriría unas 3,9 horas de simulación pura. Con 10 ms de media, una campaña de 300 años (≈109.600 días) tarda unos 18 minutos, y 100 campañas tardan unas 2 horas en una máquina de 16 núcleos (una campaña por núcleo).

### Velocidades de juego

| Velocidad | Días de juego por segundo |
| --- | --- |
| 1 | 0,5 |
| 2 | 1 |
| 3 | 3 |
| 4 | 8 |
| 5 | 20 |
| Máxima | Limitada por CPU |

### PC de referencia (propuesto, a fijar en la Fase 0)

CPU de 8 núcleos de gama media de hace unos cuatro años, 16 GB de RAM, GPU integrada moderna o dedicada de gama de entrada, SSD. El juego debe funcionar bien en esta máquina; los objetivos de escala L pueden exigir más.

### Estrategia de pruebas

| Tipo | Qué verifica | Cuándo |
| --- | --- | --- |
| Unitarias | Funciones de cada sistema. | Cada commit. |
| Propiedades | Invariantes con entradas aleatorias (conservación, no negatividad). | Cada commit. |
| Instantáneas | Salidas de informes y estados pequeños. | Cada commit. |
| Ejecuciones doradas | Hash final de escenarios fijos. | Cada commit. |
| Benchmarks | Tiempo por tick y memoria. | Cada merge a la rama principal. |
| Campañas de 101 Lab | Distribuciones históricas y salud de la IA. | Cada noche. |
| Pruebas con jugadores | Legibilidad y diversión. | Mensual desde la Fase 2. |

## 26. Herramientas: 101 Forge y 101 Lab

### 101 Forge (editor de contenido)

| Módulo | Función |
| --- | --- |
| Editor de mapa | Ajustar localizaciones, provincias, terreno, ríos, estrechos. |
| Editor de entidades | Países, gobiernos, leyes, dinastías, personajes. |
| Editor de culturas y religiones | Taxonomías, rasgos, distribución por provincia. |
| Editor de economía | Bienes, edificios, modos de producción, rutas. |
| Editor de tecnologías | Grafo con prerrequisitos, ventanas y efectos. |
| Editor de situaciones | Condiciones, variantes, caducidad, fuentes. |
| Panel de validación | Errores y advertencias en tiempo real. |
| Vista previa | Simular unos años desde el editor y ver el efecto de un cambio. |

Forge usa egui y comparte las bibliotecas de contenido y validación con el juego, de modo que lo que valida el editor es exactamente lo que cargará el motor.

### 101 Lab (laboratorio de simulación)

| Función | Detalle |
| --- | --- |
| Campañas masivas | Cientos de partidas en paralelo con semillas distintas. |
| Distribuciones | Fecha y probabilidad de situaciones clave; tamaño de Estados por siglo. |
| Salud de la IA | Países bloqueados, bancarrotas, guerras sin sentido. |
| Economía | Precios, inflación, crecimiento, invariantes. |
| Divergencia | Índice medio por región y modo de campaña. |
| Rendimiento | Tiempo por tick y memoria por sistema. |
| Comparación de versiones | Mismas semillas con dos versiones del juego para medir el efecto de un cambio. |

Lab exporta resultados en Parquet y genera un informe HTML con gráficas tras cada ejecución nocturna.

---

# Parte VI · Producción y negocio

## 27. Desarrollo mediante agentes de IA

101 Agents Games usa agentes de IA para escribir código, preparar pruebas, estudiar documentación, procesar datos y construir herramientas. La dirección humana controla la arquitectura, los objetivos, la integración, la calidad y las decisiones de diseño. Los agentes de desarrollo no tienen relación con la IA que juega la partida.

| Rol de agente | Responsabilidad / salida esperada |
| --- | --- |
| Arquitectura | Interfaces de módulos, decisiones técnicas, perfiles de riesgo, revisión. |
| Motor y rendimiento | Scheduler, perfilado, benchmarks, concurrencia. |
| Gameplay y sistemas | Economía, guerra, IA, diplomacia, gobierno, población. |
| Contenido histórico | Datasets, fuentes, situaciones, incertidumbres, validaciones. |
| Interfaz y herramientas | Mapa, UI, Forge, utilidades internas. |
| QA y balance | Pruebas, campañas de Lab, reproducibilidad, regresiones. |
| Integración | CI, dependencias, formato, migraciones, entregables reproducibles. |

### Estructura del repositorio

La estructura definitiva está en la sección 40 (`101-engine/` con crates `e101-*`, `games/epoch/data/`, `docs/`, `tests/golden/`). Las reglas globales para agentes viven en **`AGENTS.md`** en la raíz (no en un `CONTEXT.md` global, como proponía la v0.5); cada crate tiene su `CONTEXT.md` con propósito, invariantes y límites.

### Reglas del flujo de trabajo

- Una tarea pequeña y verificable por cambio; contratos de interfaz antes de implementaciones paralelas.
- Cada PR incluye pruebas y una nota mínima de decisiones.
- CI con formato, lints, pruebas, validación de datos, ejecuciones doradas y benchmarks.
- No se aceptan cifras de rendimiento sin ejecutar escenarios comparables.
- El responsable humano resuelve conflictos de diseño y limita las refactorizaciones masivas.
- El repositorio puede reconstruirse y probarse sin depender de un agente ni de una conversación concretos.

### Lista de revisión de un PR

1. ¿Respeta las reglas de determinismo (sin flotantes ni `HashMap` en la simulación)?
2. ¿Mantiene los invariantes y tiene pruebas de propiedad si toca cantidades?
3. ¿Registra contribuciones en el registro causal si cambia variables visibles?
4. ¿Cambia el hash de alguna ejecución dorada? ¿Está justificado?
5. ¿Afecta al rendimiento? ¿Hay benchmark?
6. ¿Actualiza la documentación o un ADR si cambia una decisión?

### Contenido histórico con agentes

Los agentes pueden **proponer** datos históricos (gobernantes, poblaciones, situaciones), pero todo dato entra con nivel de confianza y fuente, y los de nivel A y B requieren verificación humana contra la fuente citada. Los agentes pueden equivocarse con nombres, fechas y relaciones; el validador y la revisión editorial son obligatorios.

## 28. Plan de desarrollo y calendario

Calendario orientativo para una persona con 20–30 horas por semana y uso intensivo de agentes de IA, empezando en noviembre de 2026.

| Fase | Periodo orientativo | Entregable | Puerta de salida (medible) | Si no se cumple |
| --- | --- | --- | --- | --- |
| 0 — Preproducción | Nov–dic 2026 | Este documento; modelo de datos; prototipo económico en hoja de cálculo o script; prototipo de mapa; PC de referencia. | El modelo económico simplificado es estable 200 años simulados; región de la vertical elegida. | Simplificar el modelo antes de escribir el motor. |
| 1 — Núcleo | Ene–mar 2027 | Calendario, scheduler, territorios, Estados, guardado, headless, render del mapa, spike de cliente. | Campaña vacía de 300 años en headless; hashes idénticos; mapa navegable; cliente elegido. | Revisar la arquitectura antes de añadir sistemas. |
| 2 — Economía y población | Abr–jun 2027 | Bienes, edificios, mercados, rutas, cohortes, presupuesto, registro causal. | 100 años sin violar invariantes; precios plausibles; “¿por qué?” funciona para precios. | Reducir bienes y variables; ampliar observabilidad. |
| 3 — Diplomacia y guerra | Jul–sep 2027 | Relaciones, tratados, ejércitos, logística, asedios, paz. | En 100 campañas de IA, todas las guerras terminan en estados válidos; ninguna IA bloqueada. | Simplificar combate o IA. |
| 4 — Historia, tecnología y personajes | Oct–dic 2027 | Situaciones, IA con objetivos, restauraciones, grafo tecnológico, dinastías, epidemias. | Distribuciones de situaciones clave en rangos acordados; ninguna tecnología fuera de límite. | Revisar pesos con Lab. |
| 5 — Vertical slice | Ene–abr 2028 | 18 entidades jugables, ~350 provincias, 1300–1600, UI completa, tutorial básico, ES/EN. | Pruebas con jugadores externos: entienden por qué ocurren las cosas y quieren seguir jugando. | Iterar UX y ritmo antes de expandir. |
| 6 — Expansión espacial y temporal | May 2028 – 2029 | Europa completa, Mediterráneo y Oriente Próximo (escala M); 1600–1900. | La misma partida cruza 1300–1900 sin romper la continuidad; rendimiento en escala M. | Limitar el alcance del lanzamiento. |
| 7 — Producto | 2029 en adelante | Mundo completo, siglo XX y XXI, 2060+, Workshop, pulido. | Objetivos de calidad, rendimiento (escala L) y contenido cumplidos. | Lanzar con alcance menor y ampliar después. |

**Primer contacto con jugadores:** desde la Fase 2, una sesión mensual con alguien externo que explique en voz alta por qué ocurre lo que ve.

### Calendario detallado de las primeras fases

| Mes | Trabajo principal | Hito |
| --- | --- | --- |
| Nov 2026 | Cerrar documento maestro; elegir región; prototipo económico en hoja de cálculo. | Región de la vertical decidida. |
| Dic 2026 | Workspace, CI, convenciones, tipos de punto fijo, RNG, día absoluto; prototipo de mapa (textura de IDs). | Primer hash determinista en CI. |
| Ene 2027 | Scheduler con escalonamiento; modelo de territorios y Estados; diario de comandos. | 300 años vacíos en headless. |
| Feb 2027 | Guardado/carga; pipeline geográfico para la región; spike de cliente (parte 1). | Mapa de la región navegable. |
| Mar 2027 | Spike de cliente (parte 2); modos de mapa; decisión de cliente. | ADR del cliente gráfico. |
| Abr 2027 | Bienes, edificios, producción y consumo; invariantes. | 50 años de economía sin errores. |
| May 2027 | Mercados, precios, rutas; registro causal para precios. | Panel “¿por qué sube este precio?”. |
| Jun 2027 | Cohortes, migración, nivel de vida; presupuesto del Estado. | Puerta de la Fase 2. |
| Jul 2027 | Relaciones y tratados; IA diplomática básica. | Alianzas que se forman y se rompen con sentido. |
| Ago 2027 | Ejércitos, movimiento, suministro, batallas. | Guerra completa entre dos IA. |
| Sep 2027 | Asedios, guerra naval básica, paz por cláusulas; 101 Lab v1. | Puerta de la Fase 3. |
| Oct 2027 | Personajes y dinastías; sucesiones. | Crisis sucesoria jugable. |
| Nov 2027 | Situaciones históricas del slice; 101 History. | Primeras distribuciones en Lab. |
| Dic 2027 | Tecnología, difusión, epidemias (peste negra). | Puerta de la Fase 4. |
| Ene–abr 2028 | Contenido completo del slice, UI, tutorial, localización, pruebas con jugadores. | Vertical slice. |

Estas fechas son una **guía para medir el avance**, no un compromiso. Si una fase se retrasa más de un 50 %, se revisa el alcance en lugar de acumular retraso. Las horas estimadas por fase y el presupuesto en efectivo hasta la vertical están en el Anexo AS.

## 29. Vertical slice: Mediterráneo oriental 1300–1600

### Por qué esta región

| Criterio | Mediterráneo oriental y Balcanes | Península ibérica | Italia |
| --- | --- | --- | --- |
| Divergencia histórica | Muy alta: ascenso otomano, 1453. | Alta: unión dinástica, 1492. | Media. |
| Economía y comercio | Alta: rutas venecianas y genovesas, mar Negro. | Media; el Atlántico exige un mapa mayor. | Muy alta. |
| Guerra y asedios | Muy alta: asedios, guerra naval, fortificaciones. | Alta. | Media. |
| Restauraciones y fragmentación | Alta. | Media. | Alta. |
| Epidemias | Alta: la peste negra pasa por la región en 1347. | Alta. | Alta. |
| Diversidad cultural y religiosa | Muy alta (exige más rigor editorial). | Alta. | Baja. |
| Coste de contenido | Alto. | Medio. | Medio. |

**Recomendación:** Mediterráneo oriental y Balcanes; Italia como alternativa más barata si el coste resulta excesivo.

### Extensión del mapa

Del Adriático al mar Caspio occidental (borde) y de los Cárpatos a Egipto (borde). Unas **350 provincias** jugables:

| Zona | Provincias aproximadas |
| --- | --- |
| Anatolia | 90 |
| Grecia, Tracia y Macedonia | 70 |
| Balcanes occidentales y centrales | 60 |
| Hungría y cuenca del Danubio | 45 |
| Islas del Egeo, Creta, Chipre | 30 |
| Costa del mar Negro y Crimea | 30 |
| Levante y Cilicia (borde) | 25 |

### Entidades jugables (18)

| Entidad | Capital | Gobernante en 1300 | Estilo de juego | Reto principal |
| --- | --- | --- | --- | --- |
| Imperio bizantino | Constantinopla | Andrónico II Paleólogo | Supervivencia, diplomacia, finanzas | Deuda, mercenarios, pérdida de Anatolia. |
| Beylik otomano | Söğüt | Osmán I | Expansión fronteriza | Crecer sin ser aplastado por vecinos mayores. |
| Beylik de Germiyan | Kütahya | Dinastía germiyánida | Potencia regional anatolia | Contener a vecinos y vasallos díscolos. |
| Karamán | Larende (Karaman) | Dinastía karamánida | Heredero aspirante del sultanato de Rum | Conquistar Konya y la Anatolia central. |
| Beylik de Karasi | Balıkesir | Dinastía de Karasi | Control de los Dardanelos | Sobrevivir entre otomanos y bizantinos. |
| Beylik de Menteşe | Milas | Dinastía de Menteşe | Piratería y comercio egeo | Equilibrar corso y comercio con Venecia. |
| Reino de Serbia | Skopie (corte itinerante) | Esteban Milutin | Expansión hacia el sur | Aprovechar la debilidad bizantina sin agotarse. |
| Imperio búlgaro | Tarnovo | Teodoro Svetoslav | Restauración | Recuperar poder frente a mongoles, serbios y bizantinos. |
| Despotado de Epiro | Arta | Tomás I Comneno Ducas | Estado griego rival de Bizancio | Independencia frente a Bizancio y los angevinos. |
| Tesalia | Neopatras | Constantino Ducas | Principado griego | Supervivencia entre Bizancio, Atenas y Epiro. |
| Principado de Acaya | Andravida | Isabel de Villehardouin | Feudalismo franco en Morea | Defenderse de la reconquista bizantina. |
| Ducado de Atenas | Tebas | Guido II de la Roche | Señorío franco | Peligro de mercenarios (Compañía Catalana). |
| República de Venecia | Venecia (núcleo fuera del mapa) y Candía | Dux Pietro Gradenigo | Imperio comercial marítimo | Rutas, colonias y rivalidad con Génova. |
| República de Génova | Pera y Caffa (núcleo fuera del mapa) | Gobierno de facciones | Comercio del mar Negro | Facciones internas y guerras con Venecia. |
| Reino de Hungría | Esztergom / Buda | Andrés III | Gran reino feudal | Crisis sucesoria inminente (1301). |
| Reino de Chipre | Nicosia | Enrique II de Lusignan | Reino cruzado insular | Azúcar, comercio levantino y presión mameluca. |
| Imperio de Trebisonda | Trebisonda | Alejo II | Pequeño imperio comercial | Ruta de Tabriz y presión turcomana. |
| Armenia cilicia | Sis | Dinastía hetúmida | Reino cristiano aliado de los mongoles | Resistir a los mamelucos. |

### Entidades no jugables o de borde

| Entidad | Rol |
| --- | --- |
| Sultanato mameluco | Gran potencia del borde sur; comercio de especias desde Alejandría. |
| Iljanato | Gran potencia del borde este; mercado de Tabriz. |
| Horda de Oro | Potencia del borde norte; mercado de Sarai; presión sobre Bulgaria. |
| República de Ragusa | Ciudad comercial bajo soberanía veneciana. |
| Banato de Bosnia | Señorío regional con fuerte autonomía. |
| Voivodatos valacos y moldavos | Entidades sociales que pueden convertirse en Estados (situación “Fundación de Valaquia”). |
| Caballeros Hospitalarios | Orden sin territorio propio en la región en 1300; pueden adquirirlo (Rodas, entre 1306 y 1310). |
| Compañía Catalana | Entidad emergente: compañía mercenaria **sin territorio** que puede ser contratada, rebelarse o conquistar un Estado. |

### Mercados del slice (~25)

Constantinopla, Tesalónica, Bursa, Konya, Esmirna-Focea, Antalya, Trebisonda, Sinope, Caffa, Tana (borde), Tarnovo, Skopie, Ragusa, Buda, Candía, Negroponte, Modón-Corón, Famagusta, Ayas (Cilicia), Tabriz (externo), Alejandría (externo), Sarai (externo), Venecia (externo), Génova (externo).

Los **mercados externos** representan el resto del mundo: tienen precios con su propia dinámica simplificada y capacidad limitada. Así llegan especias desde la India y paño desde Europa occidental sin simular el planeta.

**Datos cuantitativos de la vertical (v0.7):** el estado inicial de cada entidad (población, ingresos, ejército, flota, deuda, control, legitimidad, institucionalización) está en el Anexo AJ; los mercados con sus exportaciones, importaciones, precio inicial del grano y conexiones, en el Anexo AK; los rangos de balance que 101 Lab comprueba por entidad, en el Anexo AW; y los escenarios de aprendizaje del slice, en el Anexo AV.

### Situaciones del slice (selección)

Compañía Catalana en Oriente; crisis sucesoria húngara; guerras civiles bizantinas; ascenso del Imperio serbio; fundación de Valaquia y Moldavia; peste negra; guerras veneciano-genovesas; cruzadas tardías (Esmirna, Nicópolis, Varna); irrupción de Timur; interregno otomano; unión de las Iglesias; caída de Constantinopla; conquista de Morea; fortalezas hospitalarias y asedios de Rodas; guerras otomano-venecianas; Mohács; caída de Chipre; Liga Santa en el Mediterráneo. Cada una con las condiciones de la sección 07; ninguna con fecha fija.

### Personalidad de la IA por entidad (ejemplos)

| Entidad | Prioridades |
| --- | --- |
| Bizancio | Supervivencia, recuperar territorios cercanos, alianzas matrimoniales, mercenarios. |
| Otomanos | Expansión hacia tierras cristianas fronterizas, absorción de beyliks, paso a Europa. |
| Venecia | Proteger rutas y colonias, evitar guerras terrestres, aislar a Génova. |
| Serbia | Expansión hacia Macedonia y Grecia, prestigio imperial. |
| Hungría | Hegemonía en los Balcanes occidentales, contener a los otomanos cuando son amenaza. |
| Mamelucos | Control de las rutas de especias, eliminar a los cruzados residuales. |

### Demostraciones de aceptación

| Demostración | Criterio verificable |
| --- | --- |
| La IA juega 100 años sola. | 0 violaciones de invariantes; 0 IA bloqueadas; fronteras y economías plausibles. |
| El jugador provoca una alianza improbable (p. ej. Bizancio–Karamán). | Lab muestra cambios medibles en comercio y guerras frente a la línea base. |
| Se evita la caída de Constantinopla. | El motor no la fuerza después; las situaciones dependientes caducan o se transforman. |
| Se elimina Bulgaria. | Su restauración solo ocurre si existen condiciones sociales y políticas. |
| Se intenta investigar una tecnología imposible. | La interfaz enumera prerrequisitos faltantes y el límite de adelanto. |
| Se guarda y se carga. | El hash tras cargar coincide y la continuación produce los mismos hashes. |
| Un jugador externo juega 50 años. | Explica correctamente por qué ocurrieron tres sucesos importantes. |

## 30. Publicación, negocio y marca

### Plataforma y modelo (propuesto)

- **PC (Windows primero, Linux y macOS después)** mediante Steam. Publicar una aplicación en Steam Direct requiere una tarifa de 100 USD por producto (verificar condiciones vigentes).
- **Acceso anticipado** cuando el producto cubra al menos Europa, Mediterráneo y Oriente Próximo de 1300 a 1900 con calidad; el modelo de acceso anticipado encaja con un juego que crece por épocas.
- **Precio orientativo:** rango de juego independiente de estrategia (por ejemplo, 25–40 USD), a revisar con el mercado en su momento.
- **Contenido posterior:** expansiones por región (Asia, Américas, África) y por época, más inicios históricos adicionales.

### Construcción de audiencia

| Momento | Acción |
| --- | --- |
| Fase 2 | Diarios de desarrollo técnicos (determinismo, registro causal, mapa). |
| Fase 5 | Página de Steam con capturas reales y tráiler corto; lista de deseos. |
| Tras el slice | Demo de la vertical; participación en un festival de demos de Steam. |
| Acceso anticipado | Hoja de ruta pública y actualizaciones regulares. |

### Presupuesto (orden de magnitud, a cotizar)

| Partida | Notas |
| --- | --- |
| Herramientas y agentes de IA | Suscripciones mensuales; es el coste recurrente principal en las primeras fases. |
| Hardware de pruebas | Una máquina de referencia y acceso a otras plataformas. |
| Arte | Iconografía, retratos modulares, ilustraciones de eventos, logotipo. |
| Música y sonido | Encargo o licencia por época y región. |
| Revisión histórica | Consultoría puntual por región para contenido sensible y de nivel A. |
| Localización | Inglés como mínimo; más idiomas según demanda. |
| Legal | Registro de marca, revisión de licencias, términos de uso. |
| Marketing | Tráiler, materiales para prensa, festivales. |

### Objetivos de lanzamiento y métricas comerciales (v0.7, propuesto)

| Hito | Objetivo orientativo | Por qué importa | Si no se alcanza |
| --- | --- | --- | --- |
| Página de tienda publicada | Con la vertical jugable internamente (fin de la Fase 5) | La lista de deseos necesita tiempo para crecer | Retrasar la demo pública, no la página |
| Listas de deseos antes del festival de demos | 5.000–10.000 | Umbral orientativo para que el festival tenga efecto | Más diarios de desarrollo y contacto con creadores de contenido del género |
| Jugadores de la demo | 3.000–8.000 | Validación externa del bucle de juego | Revisar la primera hora (sección 18) antes de seguir |
| Retención de la demo (jugadores que superan 60 minutos) | ≥ 35 % | Señal de que el juego engancha tras el tutorial | Iterar el ritmo de los primeros 50 años |
| Listas de deseos al abrir el acceso anticipado | 25.000–50.000 | Orden de magnitud para un lanzamiento sostenible de estrategia independiente | Ampliar la fase de demo y comunidad |
| Valoración de usuarios en el primer mes | ≥ 80 % positiva | Visibilidad en la tienda | Priorizar estabilidad, rendimiento y legibilidad sobre contenido |

Las cifras son **orientativas** y deben contrastarse con datos públicos del mercado y con la evolución de la propia lista de deseos; no son promesas de ventas.

**Precio y contenido del acceso anticipado:** el precio se fija por el contenido disponible (Europa, Mediterráneo y Oriente Próximo, 1300–1900, Fase 6), dentro del rango de la sección 30; las expansiones regionales y temporales se anuncian en una hoja de ruta pública (Anexo H) sin fechas cerradas.

**Comunicación técnica como marketing:** los diarios de desarrollo sobre determinismo, registro causal, partidas de 760 años y trabajo con agentes de IA son un diferenciador; se publican con capturas reales y cifras medidas, nunca con promesas de sistemas que no existen todavía.

### Telemetría y privacidad (propuesto)

- **Desactivada por defecto** o con consentimiento explícito al primer arranque, según la normativa aplicable.
- Solo datos agregados de juego (duración de sesiones, países elegidos, fecha alcanzada, errores), nunca datos personales ni contenido de chat.
- Los informes de error adjuntan, con permiso, la semilla y el diario de comandos para reproducir el problema.
- Política de privacidad pública y opción de borrar los datos enviados.

### Marca

- **101 Agents Games** (estudio) y **101 Engine** (motor) están definidos.
- Antes de presencia pública: verificar disponibilidad y registrar la marca en las jurisdicciones relevantes; reservar dominio y cuentas en redes.
- El nombre del juego debe evocar historia en movimiento, ser pronunciable en español e inglés y estar libre como marca. Candidatos de trabajo: *Project Epoch*, *Nations Unwritten* (ninguno confirmado).
- Guía de identidad: logotipo final, variantes monocromáticas, horizontales, verticales y favicon; tipografías y paleta.

## 31. Riesgos

| Riesgo | Prob. | Impacto | Mitigación |
| --- | --- | --- | --- |
| Alcance de 760 años | Alta | Alto | Vertical por periodo; puertas de fase; lanzamiento por épocas. |
| El juego es profundo pero no divertido | Media | Muy alto | Bucles explícitos; pruebas con jugadores desde la Fase 2. |
| Datos históricos inciertos o erróneos | Alta | Medio | Niveles de confianza, fuentes, revisión regional; verificación humana de datos propuestos por agentes. |
| Motor propio demasiado ambicioso | Alta | Alto | Bibliotecas existentes; núcleo independiente; spike de cliente. |
| Economía inestable | Alta | Alto | Invariantes, prototipo previo, escenarios de estrés. |
| Pérdida de determinismo | Media | Alto | Reglas desde el primer commit; hashes y lints en CI. |
| IA descontrolada o guionizada | Media | Alto | Utilidades, requisitos duros, trazas, Lab. |
| Rendimiento en partidas largas | Media | Alto | SoA, escalonamiento, memoria acotada, perfilado. |
| Dependencias que cambian (Bevy, wgpu) | Alta | Medio | Aislar el cliente; fijar versiones; actualizar de forma planificada. |
| Contenido pobre después de 2060 | Alta | Medio | Expansión incremental. |
| Dependencia excesiva de *vibe coding* | Media | Alto | Pruebas, revisión, contexto por crate, ADR. |
| Agotamiento o dependencia de una sola persona | Media | Muy alto | Ritmo sostenible, repositorio autoexplicativo, colaboradores en fases de contenido. |
| Representación de contenido sensible | Media | Alto | Política de la sección 09 y revisión editorial. |
| Licencias de datos o similitud con otros juegos | Media | Alto | Auditoría con `cargo-deny`; datasets con licencia comprobada; contenido original. |
| Falsa precisión de los números de diseño | Media | Medio | Toda cifra lleva confianza (A–D); los valores de la v0.7 son iniciales y se calibran con Lab; ningún número de diseño se presenta como dato histórico. |

Cada riesgo tiene un **indicador de alerta temprana** y una acción predefinida en el Anexo AT.

## 32. Backlog inicial

| Orden | Tarea | Criterio de aceptación |
| --- | --- | --- |
| 01 | Workspace, CI y convenciones | `fmt`, `clippy`, `test`, `cargo-deny` en CI; lint que prohíbe `HashMap` y flotantes en los crates del núcleo. |
| 02 | Tipos base: punto fijo, día absoluto, IDs, RNG por contador | Pruebas de propiedad de aritmética y conversiones de fecha juliana/gregoriana. |
| 03 | Scheduler y cola de eventos | Escalonamiento mensual; 300 años vacíos con la misma secuencia de hashes en dos ejecuciones. |
| 04 | Territorios, Estados y relaciones | Invariantes de soberanía y conectividad tras 10.000 cambios aleatorios de frontera. |
| 05 | Headless, instantáneas y diario de comandos | Guardar, cargar y continuar produce los mismos hashes. |
| 06 | Pipeline geográfico de la región | Textura de IDs y adyacencias generadas de forma reproducible. |
| 07 | Render del mapa y selección | 60 FPS en escala S; cambio de modo de mapa instantáneo. |
| 08 | Spike de cliente | ADR con comparativa medida. |
| 09 | Registro causal (base) | Toda variable consultable devuelve sus contribuciones con origen. |
| 10 | Producción y consumo | Conservación de bienes durante 100 años. |
| 11 | Mercados, precios y rutas | Precios estables en escenario de referencia; tres contribuyentes por precio. |
| 12 | Población agregada | Respuesta a empleo y alimentos; número de cohortes acotado. |
| 13 | Presupuesto y deuda | Balance de deuda exacto; impagos con efectos. |
| 14 | Diplomacia, guerra y paz mínimas | 100 campañas: todo conflicto termina en estado válido. |
| 15 | Personajes y sucesión | Crisis sucesoria con pretendientes y guerra posible. |
| 16 | Situaciones declarativas | Ventana, caducidad y variantes; validador de referencias. |
| 17 | IA histórica y 101 Lab | Decisiones trazables; informe nocturno de distribuciones. |
| 18 | 101 Forge v1 | Edición de entidades y situaciones sin tocar el núcleo. |
| 19 | Prototipo jugable con tutorial | Jugador externo explica tres sucesos correctamente. |

---

# Parte VII · Diseño por épocas

Las épocas no son capítulos con reglas distintas: son **combinaciones típicas** de condiciones que el mismo motor produce. Esta parte describe cómo debe sentirse cada periodo cuando sus causas están presentes, qué sistemas ganan peso, qué crisis son características y qué condiciones empujan hacia la siguiente. Sirve como guía para el contenido, el balance y las pruebas de 101 Lab.

Cada sección sigue el mismo esquema:

1. **Identidad de la época:** qué fantasía ofrece al jugador.
2. **Qué pesa más:** sistemas dominantes.
3. **Mecánicas que se activan:** lo que aparece porque existen sus condiciones.
4. **Crisis características.**
5. **Tecnologías clave.**
6. **Fuerzas armadas representativas.**
7. **Condiciones de transición.**
8. **Contenido mínimo para la versión 1.0.**

### Cómo cambian los parámetros a lo largo de las épocas (v0.7)

Los parámetros no cambian por fecha: cambian cuando se adoptan las técnicas e instituciones que los modifican. Esta tabla muestra los **valores típicos** que deberían observarse en una región avanzada de cada periodo si la historia sigue su curso; 101 Lab los usa como referencia de calibración.

| Parámetro | 1300 | 1550 | 1800 | 1900 | 1960 | 2025 | Técnica o institución que lo mueve |
| --- | --- | --- | --- | --- | --- | --- | --- |
| D0 del control (días) | 15 | 25 | 40 | 90+ | ≈ ilimitado | ≈ ilimitado | Correo organizado, caminos, telégrafo, radio |
| Velocidad del mensajero (km/día) | 60–80 | 80–120 | 150 (correo de postas) | Instantáneo (telégrafo) | Instantáneo | Instantáneo | Postas, telégrafo |
| Coste de transporte terrestre / marítimo | 15× | 12× | 8× (caminos de peaje) | 2–3× (ferrocarril) | 2× | 2× | Caminos, canales, ferrocarril, camión |
| Ancho de frente en llanura (hombres por bando) | 8.000 | 15.000 | 40.000 | Frente continuo | Frente continuo | Disperso | Pólvora, organización, movilización de masas |
| Fracción movilizable máxima | 3 % | 4 % | 6 % | 12 % | 15 % | 1–3 % (profesional) | Leyes de ejército, conscripción |
| Mortalidad bruta (‰) | 36 | 34 | 28 | 20 | 10 | 8–10 | Saneamiento, medicina, vacunas, antibióticos |
| Natalidad bruta (‰) | 40 | 38 | 36 | 30 | 20 | 10–15 | Urbanización, educación, coste de crianza |
| Alfabetización adulta en regiones avanzadas | 5–10 % | 15–25 % | 35–55 % | 70–90 % | 95 % | 99 % | Imprenta, escuela pública |
| Tasa de difusión técnica | 0,02 | 0,05 | 0,05–0,08 | 0,15 | 0,25 | 0,40 | Imprenta, prensa, telégrafo, redes |
| Tipo de interés de la deuda soberana fiable | 8–12 % | 5–8 % | 4–6 % | 3–4 % | 4–6 % | 1–5 % | Bancos públicos, bonos, bancos centrales |
| Eficacia de recaudación típica | 0,35–0,50 | 0,45–0,60 | 0,60–0,75 | 0,75–0,85 | 0,85–0,90 | 0,85–0,95 | Catastro, burocracia, estadística |
| Institucionalización (I) de un Estado avanzado | 0,40 | 0,50 | 0,65 | 0,80 | 0,85 | 0,90 | Antigüedad de las instituciones, sucesión estable |
| Retraso de noticias entre capitales lejanas | Semanas–meses | Semanas | Días–semanas | Horas | Minutos | Segundos | Correo, telégrafo, radio, redes |

## 33. Baja Edad Media (1300–1500)

### Identidad de la época

Un mundo de **lealtades personales**, reinos compuestos, ciudades que compran su libertad, órdenes religiosas con ejércitos e imperios nómadas en retroceso. El jugador gobierna con nobles que pueden negarse a acudir, mercaderes que prestan con interés y una Iglesia que puede legitimarle o hundirle. La peste negra rompe el equilibrio a mitad de época y abre oportunidades a quien sepa aprovechar la escasez de mano de obra.

### Qué pesa más

| Sistema | Peso | Por qué |
| --- | --- | --- |
| Personajes y dinastías | Muy alto | La muerte de un rey puede desintegrar un reino. |
| Estamentos y privilegios | Muy alto | El poder real depende de la nobleza y el clero. |
| Control territorial | Alto | Comunicaciones lentas; el alcance del Estado es pequeño. |
| Agricultura y clima | Muy alto | La inmensa mayoría vive del campo; una mala cosecha es una crisis. |
| Comercio a larga distancia | Medio-alto | Pocas rutas muy valiosas (especias, seda, paño, alumbre). |
| Guerra | Alto | Estacional, de asedios y cabalgadas; ejércitos pequeños y caros. |

### Mecánicas que se activan

- **Levas feudales:** el rey pide tropas; los vasallos acuden según su lealtad, su contrato y su interés.
- **Compañías mercenarias** como entidades sin territorio que pueden ser contratadas o volverse contra su patrón.
- **Uniones personales** por matrimonio y herencia.
- **Ciudades con fueros** que negocian privilegios a cambio de dinero.
- **Cruzadas tardías y guerras santas** cuando una autoridad religiosa las convoca y existen intereses que las sostengan.
- **Arrendamiento de impuestos** como forma dominante de recaudación.

### Crisis características

| Crisis | Causas que la hacen probable | Consecuencias típicas |
| --- | --- | --- |
| Pandemia de peste | Rutas que unen la estepa con el Mediterráneo y el Atlántico. | Caída de población, salarios altos, crisis señorial, revueltas. |
| Crisis sucesoria | Extinción de dinastía, minorías, pretendientes extranjeros. | Guerras civiles, uniones personales, intervención exterior. |
| Revuelta campesina | Impuestos extraordinarios, servidumbre endurecida tras la peste. | Represión o concesiones; cambios en las leyes de tierra. |
| Cisma religioso | Papado bajo presión de una monarquía; elecciones disputadas. | Pérdida de autoridad religiosa; alineamientos diplomáticos. |
| Colapso de un imperio nómada | Disputas sucesorias, pérdida de rutas. | Fragmentación en kanatos; liberación de tributarios. |

### Tecnologías clave

Rotación trienal, molinos de agua y viento, papel, contabilidad por partida doble, letra de cambio, seguro marítimo, brújula y portulanos, coca y carraca, gafas, reloj mecánico, pólvora, bombardas, artillería de bronce, arcabuz temprano, imprenta de tipos móviles, astrolabio náutico, carabela, alto horno.

### Fuerzas armadas representativas

Caballería pesada, caballería ligera, arqueros a caballo, arqueros y ballesteros, infantería de picas y lanzas, milicias urbanas, máquinas de asedio, primeras bombardas, galeras y naves redondas.

### Condiciones de transición hacia la época siguiente

No hay fecha. La partida “entra” en la siguiente combinación cuando, en una parte significativa del mundo, se dan varias de estas condiciones: artillería capaz de derribar murallas medievales; navegación oceánica regular; imprenta extendida; ejércitos pagados permanentes; Estados con impuestos regulares sin necesidad de asambleas para cada guerra.

### Contenido mínimo para 1.0

Europa, Mediterráneo, Oriente Próximo y norte de África completos; peste, guerras sucesorias, cisma, revueltas campesinas, expansión otomana y unión ibérica como situaciones; 60–80 tecnologías tempranas; retratos y eventos para las culturas principales.

## 34. Edad Moderna temprana (1500–1750)

### Identidad de la época

Los océanos se conectan, la plata americana inunda los mercados, la pólvora transforma la guerra y los Estados aprenden a cobrar impuestos de forma regular para pagar ejércitos permanentes. La religión se fragmenta y se convierte en motivo de guerra; las monarquías compuestas intentan centralizarse frente a la resistencia de reinos, estamentos y ciudades. El jugador administra imperios con fronteras lejanas y deudas enormes.

### Qué pesa más

| Sistema | Peso | Por qué |
| --- | --- | --- |
| Finanzas públicas y crédito | Muy alto | La guerra se financia con deuda; la bancarrota es frecuente. |
| Comercio oceánico y colonias | Muy alto | Rutas intercontinentales y compañías comerciales. |
| Religión | Muy alto | Reformas, confesionalización, minorías y guerras religiosas. |
| Ejército permanente | Alto | Revolución militar: más soldados, más artillería, más fortificación. |
| Burocracia | Alto | Intendentes, consejos, registros y catastros. |
| Personajes | Medio-alto | Siguen importando, pero las instituciones pesan más. |

### Mecánicas que se activan

- **Compañías comerciales con flota y ejército propios**, concesiones de monopolio y accionistas.
- **Colonias de asentamiento y de explotación**, con poblamiento real, mestizaje, trabajo forzado y resistencia (siguiendo la política de contenido sensible).
- **Confesionalización:** el Estado define una religión oficial y gestiona minorías; posibles expulsiones y diásporas.
- **Absolutismo frente a constitucionalismo:** la Corona intenta gobernar sin asambleas; las asambleas intentan controlar el impuesto.
- **Fortificación abaluartada** que alarga los asedios y vuelve las guerras de desgaste.
- **Bolsas y bancos públicos** en las ciudades comerciales.

### Crisis características

| Crisis | Causas | Consecuencias |
| --- | --- | --- |
| Inflación por metales preciosos | Entrada masiva de plata. | Subida general de precios; pérdida de valor de rentas fijas. |
| Guerras de religión | Reforma emergente, príncipes con interés en romper. | Guerras civiles, paces confesionales, migraciones. |
| Bancarrota de la Corona | Guerras largas financiadas con deuda. | Ruina de banqueros; renegociación; pérdida de crédito. |
| Revuelta de reinos periféricos | Centralización fiscal y militar. | Secesiones, guerras civiles, pactos de autonomía. |
| Colapso demográfico americano | Epidemias en poblaciones sin exposición previa, guerra, trabajo forzado. | Pérdida masiva de población; reorganización del trabajo colonial. |
| Pequeña Edad de Hielo | Anomalías climáticas frías. | Malas cosechas, hambrunas, revueltas. |

### Tecnologías clave

Galeón, cartografía con proyecciones, artillería naval de costado, mosquete, bayoneta, fortificación abaluartada, telescopio, microscopio, cálculo, física newtoniana, banca pública, bolsa de valores, seguros, prensa periódica, correo postal regular, cultivos americanos en Eurasia (maíz, patata), canales con esclusas, máquinas de bombeo tempranas.

### Fuerzas armadas representativas

Tercios y formaciones de picas y arcabuces, infantería de línea con mosquete y bayoneta, caballería con armas de fuego, artillería de campaña, ingenieros de asedio; galeones, navíos de línea, fragatas.

### Condiciones de transición

Máquinas de vapor rentables; carbón accesible y barato; capital acumulado y mercados amplios; ideas ilustradas difundidas por la prensa; crisis fiscal que obliga a reformar la representación política.

### Contenido mínimo para 1.0

Exploración y colonización atlánticas; compañías comerciales; reformas religiosas emergentes; guerras de religión; plata americana; transición a ejércitos permanentes; 70–90 tecnologías.

## 35. Era de las revoluciones e industrialización (1750–1914)

### Identidad de la época

La máquina de vapor, el ferrocarril y la fábrica cambian lo que significa ser rico y poderoso. Las ideas de soberanía nacional, derechos y constitución convierten a los súbditos en ciudadanos, y a los ciudadanos en soldados de ejércitos masivos. Los imperios europeos se expanden por el mundo mientras dentro de sus fronteras surgen nacionalismos, movimientos obreros y partidos. El jugador gestiona una sociedad que cambia más rápido que sus instituciones.

### Qué pesa más

| Sistema | Peso | Por qué |
| --- | --- | --- |
| Industria y energía | Muy alto | El carbón y el vapor multiplican la producción. |
| Población y urbanización | Muy alto | Transición demográfica; ciudades enormes. |
| Política de masas | Muy alto | Partidos, sindicatos, prensa, elecciones, revoluciones. |
| Nacionalismo | Muy alto | Unificaciones, independencias, conflictos étnicos. |
| Imperialismo | Alto | Colonias, protectorados y esferas de influencia. |
| Ferrocarril y telégrafo | Alto | Cambian el alcance del Estado y la logística militar. |

### Mecánicas que se activan

- **Constituciones y parlamentos** con sufragio que se amplía o se restringe.
- **Partidos políticos** con programas, bases sociales y coaliciones.
- **Sindicatos, huelgas y legislación laboral.**
- **Conscripción masiva y reservas** movilizables por ferrocarril.
- **Mercados financieros** con bonos, acciones, crisis bursátiles y ciclos económicos.
- **Abolición** de la esclavitud y de la servidumbre como procesos políticos, con resistencias.
- **Emigración masiva** hacia regiones con tierra y salarios altos.

### Crisis características

| Crisis | Causas | Consecuencias |
| --- | --- | --- |
| Revolución política | Crisis fiscal, ideas ilustradas, élites excluidas. | Cambio de régimen, guerras revolucionarias. |
| Crisis financiera | Especulación, sobreinversión, crédito fácil. | Quiebras, desempleo, conflictividad. |
| Guerra de unificación | Nacionalismo con un Estado núcleo fuerte. | Nuevos Estados grandes; cambio del equilibrio de poder. |
| Pandemia de cólera | Ciudades sin saneamiento, transporte rápido. | Reformas sanitarias. |
| Hambruna | Monocultivo, plagas agrícolas, políticas de exportación. | Emigración masiva, agitación política. |
| Guerra colonial | Expansión imperial, resistencia local. | Conquista, resistencia prolongada, coste fiscal. |

### Tecnologías clave

Máquina de vapor, hiladora mecánica, telar mecánico, coque y hierro barato, acero Bessemer, ferrocarril, barco de vapor, telégrafo, fotografía, vacunación, anestesia, teoría microbiana, saneamiento urbano, fertilizantes químicos, electricidad industrial, motor de combustión, teléfono, fusil de retrocarga, ametralladora, artillería de retrocarga, acorazado.

### Fuerzas armadas representativas

Infantería con fusil, cazadores, caballería, artillería de campaña de retrocarga, ingenieros, ferrocarriles militares; navíos de vapor, acorazados, cruceros, torpederos.

### Condiciones de transición

Bloques de alianzas rígidas; carrera armamentista naval y terrestre; ametralladoras y artillería pesada que hacen la defensa dominante; industria capaz de abastecer guerras largas; crisis detonante entre potencias.

### Contenido mínimo para 1.0

Revoluciones políticas emergentes; industrialización con ferrocarril y fábricas; partidos y sindicatos; unificaciones nacionales; imperialismo con resistencia; 90–120 tecnologías.

## 36. Era de las guerras mundiales y los bloques (1914–1991)

### Identidad de la época

La guerra industrial total moviliza sociedades enteras: fábricas, mujeres en la industria, racionamiento, propaganda y economías planificadas. Las ideologías de masas compiten por el futuro, los imperios coloniales se disuelven y, tras la aparición de las armas nucleares, las grandes potencias se enfrentan sin combatir directamente. El jugador dirige un Estado moderno capaz de cosas enormes y de destruirse a sí mismo.

### Qué pesa más

| Sistema | Peso | Por qué |
| --- | --- | --- |
| Movilización industrial | Muy alto | La producción de guerra decide los conflictos largos. |
| Ideología y régimen | Muy alto | Democracias, autoritarismos y regímenes de partido único. |
| Frentes y operaciones combinadas | Muy alto | Tierra, mar y aire coordinados; la logística es decisiva. |
| Descolonización | Alto | Nuevos Estados y alineamientos. |
| Economía planificada frente a mercado | Alto | Modelos económicos distintos con fortalezas y debilidades. |
| Disuasión | Alto (desde 1945) | La amenaza nuclear limita la guerra directa entre potencias. |

### Mecánicas que se activan

- **Frentes y planes operacionales** delegables (patrón P-18).
- **Producción militar en líneas** con eficiencia (P-20) y **plantillas de división** (P-19).
- **Economía de guerra:** racionamiento, control de precios, reconversión industrial, trabajo femenino.
- **Propaganda y control de la información.**
- **Organizaciones internacionales** con votaciones, sanciones y misiones.
- **Guerra por delegación:** apoyo a bandos en conflictos ajenos.
- **Escalada nuclear** como mecánica de crisis con umbrales visibles.

### Crisis características

| Crisis | Causas | Consecuencias |
| --- | --- | --- |
| Guerra general entre potencias | Bloques rígidos, carrera armamentista, crisis detonante. | Movilización total, colapso de imperios, nuevas fronteras. |
| Gran depresión | Crisis financiera global, proteccionismo. | Desempleo masivo, radicalización política. |
| Revolución socialista | Guerra perdida, industrialización rápida, movimiento obrero organizado. | Economía planificada, guerra civil, nuevo bloque. |
| Pandemia de gripe | Movilización masiva y transporte rápido. | Mortalidad global elevada. |
| Crisis de descolonización | Metrópolis debilitadas, movimientos de independencia. | Nuevos Estados, guerras de independencia. |
| Crisis nuclear | Despliegue de armas cerca de un rival. | Negociación o escalada. |

### Tecnologías clave

Ametralladora moderna, tanque, aviación militar, portaaviones, submarino, radio, radar, motor a reacción, cohetes, antibióticos, fisión nuclear, energía nuclear civil, computación electrónica, transistor, satélites, televisión, plásticos, revolución verde agrícola, contenedores marítimos, circuitos integrados.

### Fuerzas armadas representativas

Divisiones de infantería, blindadas y motorizadas; artillería pesada; aviación de caza, bombardeo y transporte; marinas con portaaviones y submarinos; fuerzas aerotransportadas; misiles balísticos; fuerzas especiales.

### Condiciones de transición

Computadoras personales y redes extendidas; globalización del comercio por contenedores; fin de la confrontación de bloques o su transformación; mercados financieros integrados.

### Contenido mínimo para 1.0

Guerra general emergente con frentes; economía de guerra; regímenes ideológicos; descolonización; disuasión nuclear con escalada; 100–130 tecnologías.

## 37. Era digital y globalización (1991–2060)

### Identidad de la época

Un mundo interconectado en el que las cadenas de suministro cruzan continentes, la información viaja instantáneamente y el poder se mide tanto en semiconductores, datos y finanzas como en divisiones. El cambio climático, las migraciones, las pandemias y la automatización ponen a prueba a todos los Estados a la vez. El jugador gobierna con instituciones complejas, opinión pública volátil y problemas que no respetan fronteras.

### Qué pesa más

| Sistema | Peso | Por qué |
| --- | --- | --- |
| Cadenas de suministro globales | Muy alto | Dependencias críticas (energía, chips, alimentos). |
| Finanzas internacionales | Muy alto | Deuda soberana, crisis financieras, sanciones. |
| Información y ciberespacio | Alto | Desinformación, ciberataques, espionaje digital. |
| Clima y energía | Muy alto | Emisiones, fenómenos extremos, transición energética. |
| Demografía | Alto | Envejecimiento, migraciones, urbanización. |
| Organizaciones supranacionales | Alto | Integración regional, tribunales, acuerdos globales. |

### Mecánicas que se activan

- **Cadenas de suministro** con nodos críticos que pueden bloquearse por guerra, sanciones o desastres.
- **Ciberoperaciones y guerra de información** como herramientas de inteligencia.
- **Política climática:** emisiones, compromisos internacionales, costes de adaptación.
- **Automatización:** cambio en el empleo por sector y efectos sobre la desigualdad.
- **Migraciones climáticas y económicas.**
- **Opinión pública en tiempo real** con medios y redes como amplificadores.

### Crisis características

| Crisis | Causas | Consecuencias |
| --- | --- | --- |
| Crisis financiera global | Burbujas, apalancamiento, interconexión. | Recesión, rescates, deuda pública. |
| Pandemia global | Transporte masivo, densidad urbana. | Cierres, ruptura de cadenas, gasto sanitario. |
| Fenómenos climáticos extremos | Calentamiento acumulado. | Desastres, migraciones, presión fiscal. |
| Ruptura de una cadena crítica | Guerra, sanciones o desastre en un nodo. | Escasez, inflación, relocalización. |
| Conflicto regional con potencias implicadas | Rivalidades, recursos, identidades. | Sanciones, guerra por delegación, crisis energética. |

### Tecnologías clave

Internet, telefonía móvil, comercio electrónico, computación en la nube, energías renovables baratas, baterías, vehículos eléctricos, edición genética, vacunas de ARN, inteligencia artificial, robótica, semiconductores avanzados, satélites de órbita baja, almacenamiento energético masivo, fusión experimental.

### Fuerzas armadas representativas

Fuerzas profesionales reducidas, armas guiadas de precisión, drones, defensa antimisiles, guerra electrónica, fuerzas cibernéticas, satélites militares.

### Contenido mínimo para 1.0

Cadenas de suministro y sanciones; clima con emisiones; ciberoperaciones; organizaciones supranacionales; 80–100 tecnologías hasta 2060.

## 38. Más allá de 2060

### Identidad de la época

Un horizonte abierto en el que el jugador hereda los problemas y capacidades de su propia partida. No hay un futuro canónico: si el mundo de la partida llegó a 2060 con un clima estable y energía abundante, el futuro será distinto que si llegó fragmentado y empobrecido.

### Principios de diseño

- **Extrapolación conservadora:** las tecnologías posteriores a 2060 se diseñan como extensiones plausibles de las existentes (energía, materiales, biomedicina, computación, transporte, espacio cercano), con costes y riesgos.
- **Sin magia:** ninguna tecnología elimina por completo los límites físicos, económicos o sociales.
- **Problemas heredados:** clima, demografía, deuda, conflictos y desigualdad continúan.
- **Nuevas instituciones:** formas de gobierno y cooperación que la partida haya hecho posibles.

### Ejemplos de capacidades posibles

| Área | Ejemplos | Requisitos |
| --- | --- | --- |
| Energía | Fusión comercial, redes continentales | Décadas de investigación, inversión masiva, materiales. |
| Biomedicina | Terapias génicas generalizadas, longevidad aumentada | Instituciones sanitarias, regulación, financiación. |
| Computación | Automatización general de servicios | Energía abundante, semiconductores, adaptación social. |
| Espacio | Minería de asteroides, estaciones permanentes | Lanzamiento barato, cooperación o competencia sostenida. |
| Clima | Captura de carbono a gran escala, geoingeniería | Riesgos, acuerdos internacionales, financiación. |
| Sociedad | Renta básica, democracia digital, federaciones globales | Condiciones políticas y fiscales. |

### Contenido mínimo para 1.0

Un conjunto acotado de 30–50 tecnologías posteriores a 2060, crisis tardías derivadas de la partida y la posibilidad de continuar indefinidamente con rendimientos decrecientes de contenido nuevo.

---

# Parte VIII · Repositorio y agentes de IA

Esta parte convierte el documento en un **repositorio en el que trabajan agentes de IA** con reglas claras. Todo lo que aquí se describe se entrega también como un kit de archivos listo para copiar (`101-engine-starter`), de modo que el primer commit del repositorio ya incluya las instrucciones para agentes.

## 39. Nombre y organización del repositorio

### Decisión (propuesta)

| Elemento | Nombre | Motivo |
| --- | --- | --- |
| Organización en GitHub | `101-agents-games` | Coincide con el nombre del estudio; los nombres de organización pueden empezar por número. |
| Repositorio principal | `101-engine` | Monorepo con motor, juego y herramientas. El nombre del motor es estable; el del juego aún no. |
| Prefijo de crates de Rust | `e101-` (`e101-sim`, `e101-map`…) | Cargo no admite nombres de paquete que empiecen por número; la `e` de *engine* conserva el 101. |
| Carpeta del primer juego | `games/epoch/` | Nombre de trabajo; se renombra cuando se elija el título comercial. |
| Repositorio de datos pesados (opcional) | `101-engine-assets` | Arte y audio grandes, con almacenamiento de archivos grandes, para no inflar el monorepo. |

Antes de crear la organización hay que comprobar que el nombre esté libre y que no choque con marcas registradas.

> **Decisión vigente (24 de octubre de 2026, D-023):** el repositorio se crea como **`jairbonillacan-cmd/101Agents`**, **público** de momento para aprovechar los minutos gratuitos de CI de GitHub, e incluye también el sitio web en `website/`. La organización `101-agents-games` sigue siendo el destino previsto; GitHub permite transferir el repositorio conservando su historial. Los demás nombres de esta tabla (prefijo `e101-`, `games/epoch/`) no cambian.

### Por qué un monorepo

- Los agentes ven **todo el contexto** (motor, datos, herramientas, documentación) en un solo lugar.
- Un cambio de interfaz y sus consumidores se revisan en el mismo PR.
- El CI comprueba de una vez que motor, datos y herramientas siguen siendo compatibles.
- Si el motor se licencia o se separa más adelante, se puede extraer con su historia.

### Visibilidad y licencias

- ~~El repositorio es privado hasta el acceso anticipado.~~ Desde la D-023 el repositorio es **público**. Consecuencias: no se sube ningún secreto, dato personal ni conversación; la licencia es propietaria con código visible solo como referencia (D-024), sin permiso de uso, copia ni redistribución; los arreglos de seguridad se gestionan con los avisos privados de seguridad de GitHub.
- El código del motor y el contenido del juego llevan licencias decididas antes de publicar nada (Anexo B, A-14). Los formatos de datos para mods se documentan públicamente.
- `deny.toml` define las licencias de dependencias aceptadas (por ejemplo, MIT, Apache-2.0, BSD, Zlib) y rechaza las incompatibles.

## 40. Estructura del repositorio

```text
101-engine/
├── AGENTS.md                      reglas para agentes (fuente única)
├── CLAUDE.md                      remite a AGENTS.md
├── README.md
├── Cargo.toml                     workspace
├── rust-toolchain.toml            versión fija de Rust
├── deny.toml                      licencias y avisos de seguridad
├── .github/
│   ├── workflows/
│   │   ├── ci.yml                 check, golden, data, bench en cada PR
│   │   └── nightly-lab.yml        100 campañas por modo cada noche
│   ├── pull_request_template.md
│   ├── ISSUE_TEMPLATE/task.md
│   └── CODEOWNERS
├── crates/
│   ├── e101-time/                 día absoluto, calendarios, escalonamiento
│   ├── e101-store/                tablas SoA, punto fijo, IDs
│   ├── e101-commands/             bus y diario de comandos
│   ├── e101-ledger/               registro causal
│   ├── e101-rng/                  RNG por contador
│   ├── e101-sim/                  sistemas de simulación
│   ├── e101-history/              situaciones y divergencia
│   ├── e101-ai/                   IA de países y personajes
│   ├── e101-map/                  geografía y rutas
│   ├── e101-content/              carga, validación y compilación de datos
│   ├── e101-script/               condiciones y efectos
│   ├── e101-save/                 guardado, repeticiones, hashes
│   ├── e101-headless/             ejecutable sin ventana
│   ├── e101-lab/                  101 Lab
│   ├── e101-client/               cliente gráfico
│   └── e101-forge/                101 Forge
├── games/
│   └── epoch/
│       ├── data/                  RON y CSV (entities, cultures, religions, goods,
│       │                          buildings, techs, laws, units, history, map)
│       ├── locale/                es/, en/ (Fluent)
│       └── assets/                iconos, retratos, música (o enlace al repo de assets)
├── data-build/                    pipeline geográfico e histórico (Python + Rust)
├── tests/
│   └── golden/                    escenarios de determinismo y sus hashes
├── tools/
│   └── xtask/                     automatización (cargo xtask …)
└── docs/
    ├── master/                    documento maestro (este documento)
    ├── adr/                       decisiones de arquitectura
    ├── specs/                     especificaciones por sistema
    ├── agents/                    ROLES, WORKFLOW, PROMPTS, tasks/, journal/
    └── style/                     guía de código, de contenido y de contenido sensible
```

### Grafo de dependencias entre crates

```text
e101-time   e101-rng
     \        /
      e101-store ── e101-commands ── e101-ledger
            \             |              /
             \        e101-content ─ e101-script
              \           |
               e101-map   |
                  \       |
                   e101-sim ── e101-history ── e101-ai
                        |
                    e101-save
                        |
      ┌─────────────────┼──────────────────┐
 e101-headless      e101-lab          e101-client      e101-forge
```

**Regla:** las flechas solo van hacia abajo. Ningún crate de la mitad superior depende de `e101-client`, `e101-forge` ni de bibliotecas gráficas. Un lint del CI rechaza cualquier dependencia que viole el grafo.

### Workspace (referencia)

```toml
[workspace]
resolver = "3"
members = ["crates/*", "tools/xtask"]

[workspace.package]
edition = "2024"
license = "LicenseRef-101-Agents-Games-Proprietary"

[workspace.lints.clippy]
float_arithmetic = "deny"      # se relaja por crate solo en el cliente y las herramientas
unwrap_used = "warn"
```

Los valores exactos se fijan en la Fase 1; este fragmento solo ilustra la intención: edición 2024, lints compartidos y prohibición de aritmética flotante por defecto.

## 41. Archivos de instrucciones para agentes

El repositorio tiene **una sola fuente de reglas** para agentes: `AGENTS.md` en la raíz. Los agentes que buscan otro nombre de archivo (por ejemplo `CLAUDE.md`) encuentran uno breve que remite a `AGENTS.md`. Cada crate tiene además un `CONTEXT.md` con su propósito, invariantes y límites.

### Jerarquía de contexto

| Nivel | Archivo | Qué contiene |
| --- | --- | --- |
| Repositorio | `AGENTS.md` | Reglas globales, comandos, aprobaciones, seguridad. |
| Rol | `docs/agents/ROLES.md` | Qué rutas puede modificar cada rol y quién revisa. |
| Crate | `crates/<crate>/CONTEXT.md` | Propósito, invariantes, interfaz, trampas conocidas. |
| Tarea | Issue o `docs/agents/tasks/<id>.md` | Objetivo, archivos permitidos, criterios de aceptación. |
| Sesión | `docs/agents/journal/<issue>.md` | Plan, decisiones y problemas del agente que la ejecuta. |

### Contenido completo de `AGENTS.md`

~~~~markdown
# AGENTS.md — Instrucciones para agentes de IA en `101-engine`

Este archivo es la **fuente única de reglas** para cualquier agente de IA que trabaje en este repositorio. Léelo completo antes de cualquier tarea. Si otra instrucción del repositorio lo contradice, este archivo manda, salvo que la persona responsable diga otra cosa en la tarea.

## 1. Qué es este repositorio

`101-engine` es el monorepo de **101 Agents Games**. Contiene:

- **101 Engine**: un motor de simulación de gran estrategia histórica escrito en Rust.
- El contenido del primer juego (nombre de trabajo *Project Epoch*), en `games/epoch/`.
- Herramientas: 101 Forge (editor), 101 Lab (simulación masiva), pipeline de datos.

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
~~~~

### Contenido de `CLAUDE.md`

~~~~markdown
# CLAUDE.md

Las reglas para agentes de este repositorio están en **AGENTS.md**, en la raíz. Léelo completo antes de cualquier tarea; es la fuente única de reglas y prevalece sobre cualquier otra instrucción del repositorio.

Resumen de lo imprescindible:

- Determinismo: sin `f32`/`f64` en el estado, sin iterar `HashMap`, sin reloj, red ni aleatoriedad fuera de `e101-rng`.
- Trabaja solo en los archivos que permite la tarea.
- Ejecuta `cargo xtask check` y `cargo xtask golden` antes de abrir un PR.
- Mantén tu diario en `docs/agents/journal/<issue>.md`.
- Nunca hagas merge de tu propio PR.
~~~~

### Plantilla de `CONTEXT.md` por crate

~~~~markdown
# CONTEXT.md — <nombre del crate>

## Propósito

Una o dos frases: qué hace este crate y para qué existe.

## Responsabilidades

- …

## No es responsabilidad de este crate

- …

## Invariantes

- …

## Dependencias permitidas

- Crates internos: …
- Externos: … (cualquier otra requiere ADR)

## Interfaz pública

Tipos y funciones principales, con un enlace a la documentación generada.

## Cómo se prueba

- Pruebas unitarias: …
- Pruebas de propiedad: …
- Escenarios dorados: …

## Trampas conocidas

- …

## Rol propietario

`role:<rol>`
~~~~

## 42. Roles de agentes y propiedad del código

~~~~markdown
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
~~~~

### Revisión humana obligatoria

`CODEOWNERS` fija qué rutas exigen revisión de la persona responsable, independientemente del rol del agente:

~~~~text
# Sustituye @responsable por el usuario o equipo de GitHub real.
# Los roles de agentes se gestionan con etiquetas; CODEOWNERS fija la revisión humana obligatoria.

*                               @responsable
/docs/adr/                      @responsable
/crates/*/src/lib.rs            @responsable
/.github/                       @responsable
/tools/xtask/                   @responsable
/Cargo.toml                     @responsable
/deny.toml                      @responsable
/games/epoch/data/history/      @responsable
/games/epoch/data/entities/     @responsable
/tests/golden/                  @responsable
~~~~

## 43. Ciclo de vida de una tarea

~~~~markdown
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
~~~~

### Plantilla de tarea

~~~~markdown
---
name: Tarea
about: Tarea para una persona o un agente de IA
labels: status:draft
---

## Objetivo

<!-- Una frase verificable. -->

## Rol

role:<rol>

## Contexto

- Sección del documento maestro: <n>
- ADR relacionados: <ids>
- Tareas relacionadas: #<n>

## Archivos permitidos

- `<ruta>`

## Interfaz o contrato

<!-- Firmas, tipos o formato de datos que deben respetarse. -->

## Criterios de aceptación

- [ ] …
- [ ] …

## Pruebas requeridas

- [ ] …

## Fuera de alcance

- …

## Estimación

<!-- 2–6 horas de agente; si es más, dividir. -->
~~~~

### Plantilla de diario

~~~~markdown
# Diario de la tarea <issue> — <título>

- **Rol:** <rol>
- **Agente / sesión:** <identificador>
- **Rama:** agent/<rol>/<issue>-<descripcion>
- **Fecha de inicio:** <AAAA-MM-DD>

## Plan

1. …
2. …

## Decisiones

| Decisión | Motivo | Alternativas descartadas |
| --- | --- | --- |
| … | … | … |

## Problemas encontrados

- …

## Verificación

- [ ] `cargo xtask check`
- [ ] `cargo xtask golden`
- [ ] `cargo xtask bench` (si aplica)
- [ ] `cargo xtask data` (si aplica)

## Pendiente para otra tarea

- …
~~~~

### Ejemplo de tarea bien escrita

> **Objetivo:** implementar el ajuste semanal de precios con amortiguación y límite de cambio.  
> **Rol:** `role:sim`.  
> **Contexto:** sección 10, “Precios”; ADR 0009 (tipos de punto fijo).  
> **Archivos permitidos:** `crates/e101-sim/src/economy/prices.rs`, `crates/e101-sim/tests/prices.rs`, `tests/golden/economy_basic/`.  
> **Interfaz:** `fn run(state: &State, deltas: &mut Deltas)`; usa `Ratio` y `Money`.  
> **Criterios de aceptación:** el precio nunca cambia más del ±10 % por semana; nunca sale del rango 0,2–10 veces el base; cada cambio registra sus tres mayores contribuyentes en el ledger.  
> **Pruebas requeridas:** prueba de propiedad para los límites; escenario dorado de 50 años con hash estable.  
> **Fuera de alcance:** comercio entre mercados.

### Ejemplo de tarea mal escrita (y por qué)

> “Haz la economía.” No tiene objetivo verificable, ni archivos permitidos, ni criterios de aceptación, ni pruebas. Un agente que la reciba debe **preguntar** en lugar de empezar.

## 44. Ramas, commits, PR y revisión

### Ramas

| Rama | Uso |
| --- | --- |
| `main` | Siempre compila, pasa el CI y conserva los hashes dorados. Protegida. |
| `agent/<rol>/<issue>-<slug>` | Trabajo de agentes. |
| `human/<nombre>/<slug>` | Trabajo de personas. |
| `release/<versión>` | Ramas de publicación (a partir del acceso anticipado). |

Se trabaja con **ramas cortas** que se integran en `main` en pocos días. No hay ramas de larga duración por sistema.

### Commits

*Conventional Commits* en inglés (`feat`, `fix`, `test`, `docs`, `data`, `perf`, `refactor`, `chore`), con el crate o el área entre paréntesis.

### Pull requests

~~~~markdown
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
~~~~

### Etiquetas

| Grupo | Etiquetas |
| --- | --- |
| Rol | `role:architecture`, `role:engine`, `role:sim`, `role:history`, `role:ai`, `role:data`, `role:client`, `role:tools`, `role:qa`, `role:infra`, `role:l10n` |
| Estado | `status:draft`, `status:ready`, `status:in-progress`, `status:review`, `status:blocked`, `status:done` |
| Aprobación | `new-dependency`, `api-change`, `golden-change`, `perf-regression`, `needs-history-review`, `needs-sensitive-review`, `infra`, `needs-human` |
| Tipo | `feature`, `bug`, `perf`, `content`, `docs` |

### Protección de `main`

- CI obligatorio en verde.
- Al menos una aprobación del rol revisor y, si aplica, de la persona responsable.
- Historial lineal (fusión por *squash*).
- Nadie, persona ni agente, hace merge de su propio PR salvo emergencia documentada.

## 45. Comandos y automatización

`tools/xtask` concentra toda la automatización. Así los agentes usan siempre los mismos comandos, y el CI ejecuta exactamente lo mismo que un agente en local.

| Comando | Qué hace | Cuándo |
| --- | --- | --- |
| `cargo xtask check` | `fmt`, `clippy`, lints de determinismo y de grafo de dependencias, pruebas. | Antes de cada PR. |
| `cargo xtask test <crate>` | Pruebas de un crate. | Durante el desarrollo. |
| `cargo xtask golden` | Ejecuta escenarios dorados y compara hashes. | Antes de cada PR. |
| `cargo xtask golden --bless` | Actualiza hashes (requiere `golden-change`). | Solo con aprobación. |
| `cargo xtask golden --bisect <escenario>` | Localiza el primer tick divergente y el sistema responsable. | Al investigar desincronizaciones. |
| `cargo xtask bench` | Benchmarks comparados con `main`. | Cambios de simulación o rendimiento. |
| `cargo xtask bench --profile <escenario>` | Ejecuta con perfilado para Tracy. | Optimización. |
| `cargo xtask data` | Compila y valida el contenido. | Cambios de datos. |
| `cargo xtask lab --campaigns <n>` | Campañas cortas de 101 Lab con informe local. | Cambios de IA, historia o economía. |
| `cargo xtask docs` | Documentación de los crates. | Cambios de interfaz. |
| `cargo xtask new-crate <nombre>` | Crea un crate con `CONTEXT.md`, lints y estructura estándar. | Arquitectura. |
| `cargo xtask new-adr <título>` | Crea un ADR numerado desde la plantilla. | Arquitectura. |

### Integración continua

| Flujo | Disparador | Pasos |
| --- | --- | --- |
| `ci.yml` | Cada PR y cada push a `main` | `check`, `golden`, `data`, `cargo-deny`; `bench` si cambian crates de simulación. |
| `nightly-lab.yml` | Cada noche | 100 campañas por modo; informe HTML; alertas si una métrica del Anexo F sale de rango. |
| `release.yml` | Etiqueta de versión | Compilación para cada plataforma, empaquetado, subida a la tienda (a partir del acceso anticipado). |

## 46. Reglas de código y de datos para agentes

### Estilo de Rust

- `rustfmt` con la configuración del repositorio; `clippy` sin advertencias.
- Errores con tipos propios (`thiserror`) en bibliotecas; `anyhow` solo en ejecutables y herramientas.
- Sin `unwrap()` ni `expect()` en código de biblioteca salvo invariantes documentados.
- Documentación (`///`) en todo elemento público, con un ejemplo cuando sea útil.
- Nombres en inglés en el código; comentarios en inglés o español de forma consistente por crate.
- Funciones pequeñas; módulos por subsistema (`economy/prices.rs`, `economy/trade.rs`).

### Pruebas

| Tipo | Obligatoria cuando |
| --- | --- |
| Unitaria | Siempre. |
| Propiedad (`proptest`) | El cambio afecta a cantidades, dinero o población. |
| Instantánea (`insta`) | El cambio produce informes o textos estructurados. |
| Escenario dorado | El cambio afecta a la simulación. |
| Benchmark | El cambio afecta a un sistema con presupuesto de tiempo. |

### Datos

- Formato del Anexo E; IDs en inglés, estables y en minúsculas.
- Fuente y confianza en todo dato histórico.
- Textos visibles solo en `locale/`, nunca en los archivos de datos.
- `cargo xtask data` sin advertencias nuevas.

### Errores frecuentes de agentes y cómo evitarlos

| Error | Prevención |
| --- | --- |
| Inventar datos históricos plausibles pero falsos. | Confianza obligatoria; revisión humana de A/B; preferir C/D cuando hay duda. |
| “Arreglar” una prueba cambiando la expectativa en lugar del código. | Las pruebas doradas solo se actualizan con `golden-change` aprobado. |
| Refactorizar fuera del alcance de la tarea. | Archivos permitidos explícitos; PR rechazado si los excede. |
| Añadir dependencias para problemas pequeños. | `new-dependency` exige justificación y licencia. |
| Usar flotantes “solo esta vez”. | Lint de CI que lo impide en crates de simulación. |
| Silenciar lints con `allow`. | `allow` en crates de simulación requiere comentario y revisión. |
| Perder contexto entre sesiones. | Diario de la tarea y `CONTEXT.md` actualizados. |

## 47. Coordinación de varios agentes en paralelo

### Reglas

1. **Interfaz primero:** antes de que dos agentes trabajen a ambos lados de un límite, Arquitectura publica el contrato (tipos y firmas) con un ADR.
2. **Un crate, un agente:** dos agentes no modifican el mismo crate a la vez, salvo en módulos distintos indicados en las tareas.
3. **Worktrees separados:** cada agente trabaja en su propia copia de trabajo para evitar conflictos.
4. **Dependencias explícitas:** una tarea que necesita otra marca `status:blocked` y la enlaza.
5. **Integración frecuente:** las ramas viven pocos días; los conflictos grandes indican tareas mal divididas.

### Ejemplo de reparto en paralelo (Fase 2)

| Agente | Rol | Tarea | Depende de |
| --- | --- | --- | --- |
| 1 | Arquitectura | Contrato `Market`, `Good`, `Price` y ADR. | — |
| 2 | Simulación | Ajuste de precios. | 1 |
| 3 | Simulación | Producción y consumo. | 1 |
| 4 | Mapa y datos | Rutas y capacidades desde el pipeline geográfico. | — |
| 5 | Simulación | Comercio entre mercados. | 1, 2, 4 |
| 6 | QA | Pruebas de propiedad de conservación y escenario dorado económico. | 2, 3 |
| 7 | Cliente | Panel de mercado con “¿por qué?”. | 1, 2 |

### Supervisión humana

La persona responsable dedica una parte fija de su tiempo a **revisar y decidir**, no solo a escribir código:

| Actividad | Frecuencia |
| --- | --- |
| Preparar tareas para la semana (con Arquitectura). | Semanal |
| Revisar PR con etiquetas de aprobación. | Diaria |
| Leer el informe nocturno de 101 Lab. | Diaria |
| Revisar ADR propuestos. | Según llegan |
| Revisión de contenido histórico y sensible. | Semanal |

## 48. Plantillas, prompts y métricas

### Plantilla de ADR

~~~~markdown
# ADR <número>: <título>

- **Estado:** propuesto | aceptado | reemplazado por ADR <n> | rechazado
- **Fecha:** <AAAA-MM-DD>
- **Autoría:** <persona o agente y rol>
- **Relacionado con:** <sección del documento maestro, tareas, otros ADR>

## Contexto

Qué problema hay que resolver y qué restricciones existen.

## Decisión

Qué se decide, de forma concreta y verificable.

## Alternativas consideradas

| Alternativa | Ventajas | Inconvenientes |
| --- | --- | --- |
| … | … | … |

## Consecuencias

Qué cambia en el código, en los datos, en el rendimiento y en el trabajo futuro.

## Cómo se verifica

Pruebas, métricas o escenarios que demuestran que la decisión se cumple.
~~~~

### Biblioteca de prompts

~~~~markdown
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
~~~~

### Métricas del trabajo con agentes

| Métrica | Objetivo orientativo | Uso |
| --- | --- | --- |
| PR aceptados sin cambios mayores | ≥ 60 % | Calidad de las tareas y de los agentes. |
| PR que rompen el CI en `main` | 0 | Disciplina de verificación. |
| Tareas devueltas por falta de información | ≤ 15 % | Calidad de redacción de las tareas. |
| Tiempo medio de tarea a merge | ≤ 3 días | Fluidez del flujo. |
| Regresiones detectadas por Lab tras el merge | Tendencia a la baja | Cobertura de pruebas. |
| Datos históricos corregidos tras revisión | Seguimiento | Fiabilidad del contenido generado. |

Si una métrica empeora, se ajusta primero la redacción de tareas, el contexto (`CONTEXT.md`) o las pruebas, antes que el modelo o la herramienta.

### Kit inicial

El kit `101-engine-starter` contiene los archivos de esta parte listos para el primer commit:

| Archivo | Sección |
| --- | --- |
| `AGENTS.md`, `CLAUDE.md`, `README.md` | 41 |
| `docs/agents/ROLES.md` | 42 |
| `docs/agents/WORKFLOW.md`, `docs/agents/journal/TEMPLATE.md` | 43 |
| `.github/pull_request_template.md`, `.github/ISSUE_TEMPLATE/task.md`, `.github/CODEOWNERS` | 42–44 |
| `docs/adr/0000-template.md`, `docs/agents/PROMPTS.md` | 48 |
| `docs/agents/FAQ.md` | Anexo AC |
| `crates/CONTEXT.template.md` | 41 |

---

# Cierre

## 49. Conclusión y definición de éxito

El objetivo de 101 Agents Games no es copiar a otros juegos del género. Es una plataforma especializada para explorar siglos de historia política, militar, social, cultural y económica como un sistema continuo, legible y causal.

> **UNA FRASE QUE DEFINE EL JUEGO**  
> **La historia sigue siendo reconocible mientras sus causas sobreviven; cuando el jugador cambia esas causas, el mundo escribe consecuencias nuevas y plausibles.**

### Definición operativa de éxito para la primera gran prueba

- Un país puede existir, transformarse, desaparecer y reaparecer sin corromper el mapa ni su identidad.
- La economía explica el coste humano, material y fiscal de una guerra.
- Los cambios de época modifican instituciones y doctrinas por condiciones, no por un interruptor de calendario.
- Una IA autónoma simula muchas décadas sin quedar bloqueada.
- El jugador identifica por qué ocurrió un evento, una crisis, un avance o una derrota.
- 101 Engine ejecuta y verifica campañas de forma determinista sin depender del renderizador.

Cuando estas condiciones se cumplan en el Mediterráneo oriental entre 1300 y 1600, se podrán ampliar el mapa, los sistemas y los siglos sin perder el fundamento técnico.

---

## Anexo A · Inventario de entregables

| Artefacto | Descripción | Necesario antes de |
| --- | --- | --- |
| Documento técnico de 101 Engine | Componentes, API, formatos, concurrencia, determinismo, rendimiento. | Fase 1 |
| Plan de pruebas de 101 Lab | Escenarios, benchmarks, QA histórico, regresiones. | Fase 1 |
| GDD | Reglas, mecánicas, UX y objetivos de balance detallados. | Fase 2 |
| Especificación económica | Variables, ecuaciones, flujos, invariantes. | Fase 2 |
| Especificación militar | Organización, combate, suministros, doctrinas. | Fase 3 |
| Biblia histórica del slice | Entidades, gobernantes, situaciones, fuentes, confianza. | Fase 4 |
| Política de contenido sensible | Principios, revisión, opciones de presentación. | Fase 4 |
| Guía de arte | Estilos por época, retratos, iconografía, interfaz. | Fase 5 |
| Guía de identidad | Marca, logotipo, tipografías, paleta. | Presencia pública |
| Manual de modding | Formatos, condiciones, validación, herramientas. | Fase 6 |

## Anexo B · Registro de decisiones

### Decisiones tomadas o propuestas

| ID | Decisión | Estado |
| --- | --- | --- |
| D-001 | Estudio: 101 Agents Games. | Definido |
| D-002 | Motor: 101 Engine; prefijo 101 para la familia. | Definido |
| D-003 | Periodo continuo 1300–2060+, sin final obligatorio. | Definido |
| D-004 | Historia con inercia, no guion. | Definido |
| D-005 | Ningún modelo de lenguaje decide acciones de los países durante la partida. | Definido |
| D-006 | Rust (edición 2024) para el núcleo. | Propuesto |
| D-007 | Núcleo sin dependencias gráficas; el cliente envía comandos. | Propuesto |
| D-008 | Estado persistente en enteros o punto fijo; RNG por contador. | Propuesto |
| D-009 | Un jugador como prioridad. | Propuesto |
| D-010 | Población por cohortes agregadas. | Propuesto |
| D-011 | No usar bincode para guardados; evaluar postcard o bitcode. | Propuesto |
| D-012 | Render del mapa mediante textura de IDs de provincia. | Propuesto |
| D-013 | Español e inglés desde el slice, con Fluent. | Propuesto |
| D-014 | Contenido base en los mismos formatos que los mods. | Propuesto |
| D-015 | El diseño se describe por patrones; no se citan ni copian juegos comerciales. | Definido |
| D-016 | Unidad de cuenta interna fija (uc = 3,5 g de oro fino); las monedas del juego se valoran respecto a ella. | Propuesto (v0.7) |
| D-017 | Orden de sistemas dentro del tick fijo y parte del contrato de determinismo (sección 21); los comandos de la IA del día *d* se aplican en *d + 1*. | Propuesto (v0.7) |
| D-018 | Hash de estado BLAKE3 global y por tabla (sección 23). | Propuesto (v0.7) |
| D-019 | Todas las funciones de modificación de los modelos son tablas por tramos en datos, no fórmulas en código. | Propuesto (v0.7) |
| D-020 | Utilidad de la IA en puntos de utilidad (1 pu = 1 % de los ingresos anuales) y sesgo histórico máximo de +20 pu por acción. | Propuesto (v0.7) |
| D-021 | Los parámetros iniciales viven en `games/epoch/data/rules/` con ID estable (Anexo AI); cambiarlos exige una ejecución de Lab en el PR. | Propuesto (v0.7) |
| D-022 | Nombres de crate definitivos con prefijo `e101-`; `AGENTS.md` es la fuente única de reglas para agentes. | Propuesto (v0.7) |
| D-023 | Repositorio `jairbonillacan-cmd/101Agents`, público por ahora (minutos gratuitos de CI), con el sitio web en `website/`; transferencia futura a la organización `101-agents-games`. | Definido |
| D-024 | Licencia propietaria con código visible solo como referencia (`LICENSE`): todos los derechos reservados; contribuciones por invitación. Se puede abrir parcialmente más adelante (por ejemplo, el formato de mods). | Definido |

### Decisiones abiertas

| ID | Pregunta | Resolver antes de |
| --- | --- | --- |
| A-01 | Nombre comercial del juego. | Presencia pública |
| A-02 | Región de la vertical (propuesta: Mediterráneo oriental). | Fin de la Fase 0 |
| A-03 | PC de referencia. | Fin de la Fase 0 |
| A-04 | Política editorial y nivel de rigor histórico. | Fin de la Fase 0 |
| A-05 | Cliente gráfico (finalistas propuestos: Godot + Rust y mapa en wgpu + UI web; ver sección 22). | Fin de la Fase 1 |
| A-06 | UI del juego. | Fin de la Fase 1 |
| A-07 | Objetivos de partida, puntuación y crónica. | Fase 5 |
| A-08 | Multijugador y determinismo entre plataformas. | Antes de la Fase 3 |
| A-09 | Lenguaje de scripting. | Fase 4 |
| A-10 | Fechas de inicio adicionales. | Fase 6 |
| A-11 | Continuidad del jugador tras el colapso de su Estado (propuesta de la v0.7 en la sección 08: sucesor por orden de preferencia, con opción de “caída definitiva”). | Fase 4 |
| A-12 | Transición del clima histórico al simulado. | Fase 6 |
| A-13 | Alcance del contenido después de 2060. | Fase 7 |
| A-14 | Modelo de publicación, precio y financiación. | Fase 5 |
| A-15 | Uso de recursos generados por IA en arte y audio. | Fase 5 |

Cada cambio de estado se anota con fecha y motivo en un ADR. Una decisión definida solo se reabre con un ADR nuevo.

## Anexo C · Glosario

| Término | Definición |
| --- | --- |
| ADR | *Architecture Decision Record*: documento breve que registra una decisión y su motivo. |
| Año-sabio | Trabajo de investigación de una persona cualificada durante un año; unidad de coste de la tecnología (sección 14). |
| Agotamiento bélico | Variable derivada de bajas, impuestos, precios, ocupación, duración y deuda de guerra (sección 13). |
| Capacidad administrativa | Funcionarios cualificados × eficacia institucional × (1 − corrupción) (sección 11). |
| GE | Grano equivalente: kilogramo con el aporte calórico de 1 kg de trigo; unidad de las cestas de alimento (sección 09). |
| Institucionalización (I) | Índice de 0 a 1 que reduce el peso de los personajes en el Estado (sección 16). |
| NV | Nivel de vida: suma de las coberturas de las cestas de subsistencia, comodidad y lujo, de 0 a 3 (sección 09). |
| Plausibilidad | Puntuación de 0 a 1 de una situación histórica según ventana, precondiciones, modo y divergencia (sección 07). |
| Presión rebelde | Descontento × poder o capacidad de revuelta × falta de control de un grupo (sección 11). |
| pu | Punto de utilidad de la IA: valor del 1 % de los ingresos anuales del país (sección 17). |
| uc | Unidad de cuenta interna: el valor de 3,5 g de oro fino; no es una moneda del juego (sección 10). |
| Cohorte | Grupo de población que comparte provincia, ocupación, cultura, religión y estrato. |
| Determinismo | Las mismas entradas producen exactamente el mismo estado. |
| Divergencia | Distancia entre el estado simulado de una región y su trayectoria histórica. |
| ECS | *Entity Component System*: patrón de datos que separa entidades, componentes y sistemas. |
| Escalonamiento | Repartir cálculos periódicos entre varios días para evitar picos. |
| Headless | Ejecución de la simulación sin ventana ni GPU. |
| HTN | Planificación jerárquica de tareas: descompone un objetivo en subtareas. |
| Invariante | Condición que debe cumplirse siempre. |
| Lockstep | Multijugador en el que todos los equipos simulan lo mismo intercambiando solo comandos. |
| Punto fijo | Decimales representados con enteros y una escala fija. |
| Reconvergencia | Tendencia a volver hacia trayectorias históricas cuando sus causas reaparecen. |
| Registro causal | Estructura que guarda el origen de cada contribución a una variable. |
| SoA | *Structure of Arrays*: almacenamiento por columnas. |
| Spike | Prototipo corto para resolver una duda técnica. |
| Textura de IDs | Imagen en la que cada píxel guarda el ID de su provincia. |
| Tick | Un paso de simulación; normalmente, un día. |
| Vertical slice | Porción pequeña del juego con todos los sistemas funcionando juntos. |

## Anexo D · Referencias, fuentes de datos y comprobaciones

**Referencias de diseño:** el género de la gran estrategia histórica en general, descrito mediante patrones en la sección 02. Este documento no cita ni toma como modelo títulos comerciales concretos, y no se reutilizará código, datos, textos, interfaces ni recursos de ningún juego.

**Referencias técnicas:** Rust (edición 2024), wgpu, WGSL, winit, Rayon, Serde, RON, postcard, bitcode, rkyv, zstd, egui, Fluent, kira, petgraph, rstar, geo, cosmic-text, tracing, Tracy, puffin, cargo-nextest, proptest, insta, cargo-deny, Polars, DuckDB; opciones de cliente: Godot 4.7 con godot-rust, Bevy 0.20, Fyrox 1.0, Slint, iced, vista web embebida.

**Estado verificado en octubre de 2026:**
- Bevy 0.20 se publicó el 8 de octubre de 2026 con cambios incompatibles y guía de migración desde la 0.19; no hay compromiso público de versión 1.0.
- El equipo de bincode cesó el desarrollo de forma permanente (RUSTSEC-2025-0141), que recomienda alternativas como postcard, bitcode, rkyv y wincode.
- wgpu publica versiones mayores con frecuencia; la serie 29 era la vigente en 2026.
- Godot 4.7.2 se publicó el 18 de agosto de 2026; es MIT y sin regalías.
- Fyrox alcanzó la versión 1.0 en marzo de 2026.
- La licencia libre de regalías de Slint para escritorio exige mostrar una atribución (pantalla “Acerca de” o página de descarga) y excluye sistemas embebidos.
- historical-basemaps está bajo GPL-3.0 y su autor lo describe como trabajo en curso.
- HYDE 3.3 cubre de 10.000 a. C. a 2023 con resolución de 5 minutos de arco; su página de catálogo no indica la licencia exacta.

### Comprobaciones antes de implementar

- [ ] Revisar versión y estado de mantenimiento de cada biblioteca elegida.
- [ ] Comprobar licencias de bibliotecas (`cargo-deny`) y de cada dataset, y registrarlas.
- [ ] Definir el PC de referencia.
- [ ] Verificar la disponibilidad del nombre del juego y de las submarcas 101.
- [ ] Confirmar en la Biblia histórica los gobernantes y entidades de 1300 de la región elegida.
- [ ] Revisar las condiciones vigentes de Steam Direct.

## Anexo E · Formatos de datos (ejemplos)

Ejemplos ilustrativos del formato de contenido propuesto (RON). Los nombres de campos son provisionales y se fijarán en el documento técnico de 101 Engine. El contenido base y los mods usan exactamente estos formatos.

### Entidad política

```ron
Entity(
    id: "byzantium",
    names: {
        "es": "Imperio bizantino",
        "en": "Byzantine Empire",
        "self": "Basileia tōn Rhōmaiōn",
    },
    identity: "roman",
    government: "bureaucratic_monarchy",
    capital: "constantinople",
    dynasty: "palaiologos",
    ruler: "andronikos_ii",
    laws: ["succession_designation", "land_pronoia", "religion_state_orthodox", "army_mercenary"],
    currency: "hyperpyron",
    claims: [
        Claim(target: "region_bithynia", kind: Historical, strength: 80),
        Claim(target: "region_morea", kind: Historical, strength: 60),
    ],
    ai_personality: ["survival_first", "diplomatic", "fiscal_pressure"],
    sources: [Source(ref: "bib:ostrogorsky", confidence: A)],
)
```

### Cultura

```ron
Culture(
    id: "romaic_greek",
    names: { "es": "Griego (romeo)", "en": "Greek (Romaic)" },
    group: "hellenic",
    language: "medieval_greek",
    traits: ["urban_tradition", "written_bureaucratic", "maritime"],
    naming: NamingList(ref: "names/greek_medieval.csv"),
    place_names: PlaceNames(ref: "toponyms/greek.csv"),
    colors: (map: "#5B7DB1"),
)
```

### Situación histórica

```ron
Situation(
    id: "fall_of_the_imperial_city",
    window: (start: 1390, peak: (1440, 1470), end: 1520),
    roles: {
        "besieger": Role(requires: [
            Controls(region: "thrace", min_share: 70),
            Controls(region: "bithynia", min_share: 70),
            HasTech("large_bombards"),
        ]),
        "defender": Role(requires: [Owns(province: "constantinople")]),
    },
    preconditions: [
        Weighted(condition: Not(NavalAllyNear(role: "defender")), weight: 30),
        Weighted(condition: FortLevelBelow(province: "constantinople", level: "artillery_fort"), weight: 20),
    ],
    expires_if: [StrongPowerOwns(province: "constantinople")],
    transforms_into: "siege_of_imperial_city_generic",
    effects_on_ai: [RaisePriority(role: "besieger", goal: Capture("constantinople"), amount: 40)],
    variants: ["assault", "negotiated_surrender", "failed_siege_truce", "italian_intervention"],
    sources: [Source(ref: "bib:runciman_1453", confidence: A)],
)
```

### Edificio y modos de producción

```ron
Building(
    id: "grain_mill",
    category: Agriculture,
    jobs: { "artisans": 20, "peasants_free": 10 },
    modes: [
        Mode(id: "hand_mill", inputs: { "grain": 100 }, outputs: { "flour": 90 }, productivity: 1.0),
        Mode(id: "water_mill", requires_tech: "improved_water_mill", requires: [RiverInProvince],
             inputs: { "grain": 100 }, outputs: { "flour": 95 }, productivity: 2.5),
        Mode(id: "windmill", requires_tech: "windmill",
             inputs: { "grain": 100 }, outputs: { "flour": 95 }, productivity: 2.0),
    ],
)
```

### Tecnología

```ron
Technology(
    id: "movable_type_printing",
    branch: Communication,
    requires: ["paper", "fine_metallurgy", "screw_press"],
    historical_window: (start: 1440, end: 1480),
    max_lead_years: 40,
    stages: [Discovery, Prototype, Adoption, MassProduction],
    unlocks_modes: ["printing_press"],
    social_effects: [LiteracyGrowth(rate: 0.002), ReligiousReformPressure(amount: 10)],
)
```

### Reglas del formato

- Los IDs son en inglés, en minúsculas y estables; los textos visibles van en archivos de localización.
- Los porcentajes y cantidades se escriben como enteros o con decimales fijos; el compilador los convierte a punto fijo.
- Toda referencia a otro objeto se valida al compilar.
- Toda entrada histórica lleva fuente y nivel de confianza.

## Anexo F · Objetivos de calibración de 101 Lab

101 Lab ejecuta cientos de campañas sin jugador y compara los resultados con estos objetivos. Son **valores iniciales de diseño**: el equipo los revisará cuando haya datos. Un objetivo incumplido no se corrige forzando el resultado, sino ajustando las causas.

### Historia (vertical, sin jugador)

| Métrica | Modo estricto | Modo dinámico | Modo alternativo |
| --- | --- | --- | --- |
| Constantinopla cae ante una potencia anatolia entre 1430 y 1480 | 60–85 % de campañas | 35–70 % | Sin objetivo |
| Una potencia anatolia controla Bitinia antes de 1340 | ≥ 70 % | ≥ 50 % | Sin objetivo |
| Surge un Estado valaco antes de 1350 | ≥ 60 % | ≥ 40 % | Sin objetivo |
| La peste llega a la región entre 1340 y 1360 | ≥ 80 % | ≥ 70 % | ≥ 50 % |
| Entidades soberanas en el mapa en 1500 | 6–12 | 5–15 | 4–20 |
| Venecia conserva Creta en 1600 | ≥ 60 % | ≥ 40 % | Sin objetivo |

### Salud del mundo

| Métrica | Objetivo |
| --- | --- |
| IA bloqueadas (sin acciones válidas durante un año) | 0 |
| Violaciones de invariantes | 0 |
| Bancarrotas por Estado y siglo (mediana) | ≤ 1,5 |
| Guerras activas por década en el slice (mediana) | 3–8 |
| Duración media de una guerra | 1–6 años |
| Variación anual del precio del grano en años sin crisis | ≤ ±25 % |
| Población total del slice tras la peste respecto a antes | 50–80 % |
| Recuperación de la población anterior a la peste | Entre 80 y 200 años |
| Estados destruidos que se restauran alguna vez | 5–25 % |

### Rendimiento

| Métrica | Objetivo |
| --- | --- |
| Tick medio en escala S | ≤ 10 ms |
| Tick p99 | ≤ 50 ms |
| Campaña de 300 años | ≤ 20 min |
| Memoria tras 300 años | ≤ 2 GB y sin crecimiento lineal con el tiempo |

### Procedimiento

1. Cada noche, 100 campañas por modo con semillas distintas.
2. Informe HTML con distribuciones, comparación con la noche anterior y alertas cuando una métrica sale de su rango.
3. Un cambio que mueve una métrica fuera de rango requiere una nota en el PR explicando si es intencionado.

## Anexo G · Guía de estilo del contenido

### Voz y tono

- **Sobrio e informativo**, con el registro de un buen libro de divulgación histórica. Sin humor fuera de lugar ni lenguaje épico exagerado.
- Se nombra a los actores con precisión y sin juicios morales anacrónicos, pero sin suavizar la violencia o la injusticia cuando ocurren.
- Se evitan los anacronismos de vocabulario (“nación” en 1300 cuando no corresponde; “el Estado” en contextos feudales sin matizar).

### Longitud

| Tipo de texto | Longitud máxima |
| --- | --- |
| Título de evento | 6 palabras |
| Cuerpo de evento | 120 palabras |
| Opción de evento | 12 palabras |
| Tooltip de un modificador | 25 palabras |
| Entrada de enciclopedia | 400 palabras, con fuentes |

### Nombres

- Personas y lugares con su nombre de la época y la cultura, con el exónimo moderno entre paréntesis en la enciclopedia: “Edirne (Adrianópolis)”.
- Transliteraciones consistentes por idioma, documentadas en una tabla del proyecto.
- Los nombres cambian cuando cambia la cultura dominante de una provincia, conservando el historial.

### Lista de comprobación de sensibilidad

- ¿Las víctimas tienen voz y agencia en el texto?
- ¿Se evita presentar la violencia como recompensa o como algo deseable?
- ¿Se describe a culturas y religiones con respeto y precisión?
- ¿Hay una fuente para cada afirmación histórica concreta?
- ¿Revisó el texto alguien con conocimiento de la región?

### Traducción

- El español y el inglés se escriben a la vez, no uno a partir del otro, cuando sea posible.
- Los textos usan variables para nombres, cifras y géneros gramaticales (Fluent), nunca concatenaciones.
- Glosario compartido de términos del juego en ambos idiomas.

## Anexo H · Hoja de ruta posterior al lanzamiento

Propuesta orientativa; el orden se decidirá con datos de jugadores.

| Bloque | Contenido | Tipo |
| --- | --- | --- |
| Actualizaciones gratuitas | Balance, rendimiento, calidad de vida, más situaciones en regiones existentes. | Gratuito, continuo |
| Rutas de la seda | Asia central, Irán, India del norte, China Yuan y Ming; caravanas y nómadas. | Expansión regional |
| El océano Índico | India del sur, sudeste asiático, costa swahili, comercio monzónico. | Expansión regional |
| Mundo atlántico | Exploración, Américas con sistemas propios, colonización y sus consecuencias. | Expansión regional |
| África | Sahel, África occidental, central y austral con Estados y sociedades propias. | Expansión regional |
| Era de las revoluciones | Ilustración, revoluciones políticas, nacionalismo, primeras constituciones. | Expansión temporal |
| Era industrial | Vapor, ferrocarril, fábricas, movimientos obreros, imperialismo. | Expansión temporal |
| Siglo de las guerras mundiales | Guerra industrial total, ideologías de masas, aviación, frentes. | Expansión temporal |
| Era nuclear y digital | Bloques, descolonización, disuasión, globalización, redes. | Expansión temporal |
| Siglo XXI y más allá | Clima, energía, automatización, organizaciones supranacionales, 2060+. | Expansión temporal |
| Multijugador | Lockstep determinista, cooperativo y competitivo. | Actualización mayor |
| Forge público | Editor de escenarios y mapas para la comunidad. | Actualización mayor |

## Anexo I · Fichas de las entidades jugables de la vertical

Cada ficha resume la situación en 1300 y el diseño de juego de la entidad. Los datos históricos son material de trabajo y deben confirmarse en la Biblia histórica antes de convertirse en contenido.

### Imperio bizantino

- **Situación en 1300:** Andrónico II Paleólogo gobierna un imperio reducido a Constantinopla, Tracia, Macedonia, parte del Peloponeso e islas, que pierde rápidamente sus posesiones en Anatolia occidental ante los beyliks turcos.
- **Gobierno:** monarquía burocrática con tradición imperial romana; aristocracia terrateniente poderosa; Iglesia ortodoxa muy influyente.
- **Economía:** Constantinopla sigue siendo un gran mercado, pero el comercio está en manos de venecianos y genoveses, que pagan aduanas reducidas. El tesoro sufre una devaluación continuada del *hiperpirón*.
- **Ejército y flota:** dependencia de mercenarios. La flota imperial fue disuelta en la década de 1280 por razones de ahorro, lo que deja la defensa naval en manos de aliados italianos.
- **Retos:** deuda, pérdida de Anatolia, mercenarios peligrosos, guerras civiles dinásticas y dependencia comercial.
- **Oportunidades:** prestigio imperial, diplomacia matrimonial, posición estratégica de los estrechos, reconstrucción de la flota.
- **Situaciones asociadas:** Compañía Catalana, guerras civiles, unión de las Iglesias, caída de la ciudad imperial.
- **Ambiciones iniciales:** “Detener la pérdida de Bitinia”, “Reconstruir la flota”, “Sanear el *hiperpirón*”.
- **Personalidad de la IA:** supervivencia, diplomacia, contratación de mercenarios, alianzas matrimoniales.
- **Dificultad:** alta; recomendada para aprender el registro causal por la cantidad de problemas simultáneos.

### Beylik otomano

- **Situación en 1300:** Osmán I dirige un pequeño principado en el noroeste de Anatolia, en la frontera con las tierras bizantinas de Bitinia. En 1302 vencerá a un ejército bizantino en Bafeo.
- **Gobierno:** beylik fronterizo; poder personal del bey apoyado por guerreros de frontera, derviches y notables locales.
- **Economía:** pastoralismo, agricultura de valles, botín de frontera y tributo de aldeas conquistadas.
- **Ejército:** caballería ligera de frontera; pocos medios de asedio en los primeros años.
- **Retos:** vecinos mayores (Germiyan), ciudades bizantinas amuralladas imposibles de tomar sin asedios largos.
- **Oportunidades:** debilidad bizantina, atracción de guerreros de otros beyliks, cruce hacia Europa.
- **Situaciones asociadas:** conquista de Bitinia, cruce de los Dardanelos, interregno tras una derrota catastrófica, caída de la ciudad imperial.
- **Ambiciones iniciales:** “Tomar Bursa”, “Sumar a los guerreros de frontera”.
- **Personalidad de la IA:** expansión hacia tierras cristianas vecinas, absorción de beyliks, paciencia en asedios.
- **Dificultad:** media; crecimiento rápido si se gestiona bien el bloqueo de ciudades.

### Beylik de Germiyan

- **Situación en 1300:** el beylik más poderoso de Anatolia occidental, con capital en Kütahya. Varios de los futuros beyliks costeros nacen de comandantes de su órbita.
- **Gobierno:** beylik con vasallos y jefes de frontera semiautónomos.
- **Economía:** agricultura, ganadería y control de las rutas interiores hacia la costa egea, donde operan mercaderes italianos.
- **Retos:** mantener la lealtad de los jefes de frontera que fundan sus propios beyliks; rivalidad con Karamán.
- **Oportunidades:** convertirse en la potencia unificadora de Anatolia occidental en lugar de los otomanos.
- **Situaciones asociadas:** fragmentación de los beyliks, presión iljánida.
- **Ambiciones iniciales:** “Someter a los beyliks costeros”, “Contener a Karamán”.
- **Personalidad de la IA:** hegemonía regional, vasallaje, defensa frente a Karamán.
- **Dificultad:** media.

### Karamán

- **Situación en 1300:** principado de la Anatolia central-meridional que reclama la herencia del sultanato selyúcida de Rum y disputa Konya.
- **Gobierno:** beylik con fuerte apoyo turcomano.
- **Economía:** pastoralismo, rutas hacia el Mediterráneo y Cilicia.
- **Retos:** presión iljánida y mameluca; rivalidad con Germiyan y, más tarde, con los otomanos.
- **Oportunidades:** legitimidad como heredero de Rum; alianzas con potencias cristianas contra los otomanos.
- **Situaciones asociadas:** lucha por Konya, guerras con los otomanos.
- **Ambiciones iniciales:** “Tomar Konya”, “Ser reconocido heredero de Rum”.
- **Personalidad de la IA:** prestigio, rivalidad con el beylik más fuerte, alianzas oportunistas.
- **Dificultad:** media-alta.

### Beylik de Karasi

- **Situación en 1300:** principado del noroeste de Anatolia, en torno a Balıkesir, con acceso a la costa frente a los Dardanelos.
- **Economía y ejército:** guerreros de frontera, pequeña actividad naval.
- **Retos:** quedar atrapado entre otomanos y bizantinos; históricamente será absorbido por los otomanos a mediados del siglo XIV.
- **Oportunidades:** ser el primero en cruzar a Europa por los Dardanelos.
- **Ambiciones iniciales:** “Controlar la orilla asiática de los Dardanelos”.
- **Personalidad de la IA:** supervivencia, alianzas cambiantes.
- **Dificultad:** alta (pequeño y expuesto).

### Beylik de Menteşe

- **Situación en 1300:** principado costero del suroeste de Anatolia (Milas), con actividad naval y corsaria en el Egeo.
- **Economía:** comercio y corso; relaciones ambiguas con Venecia y con los Hospitalarios, que se instalarán en Rodas entre 1306 y 1310.
- **Retos:** represalias navales cristianas; competencia con otros beyliks costeros.
- **Oportunidades:** dominar el Egeo oriental; comerciar con todos.
- **Ambiciones iniciales:** “Dominar las islas cercanas”, “Acuerdo comercial con Venecia”.
- **Personalidad de la IA:** equilibrio entre corso y comercio.
- **Dificultad:** media.

### Reino de Serbia

- **Situación en 1300:** Esteban Milutin gobierna desde Skopie, tomada en 1282, y ha pactado con Bizancio casándose con la princesa Simonida (1299).
- **Gobierno:** monarquía de la dinastía Nemanjić; nobleza poderosa; Iglesia serbia autocéfala.
- **Economía:** minería de plata en auge con mineros sajones; comercio con Ragusa.
- **Retos:** conflictos dinásticos (Milutin y su hermano Dragutin), presión húngara al norte.
- **Oportunidades:** expansión hacia Macedonia y Grecia aprovechando la debilidad bizantina; título imperial.
- **Situaciones asociadas:** Imperio serbio, batalla decisiva frente a los otomanos.
- **Ambiciones iniciales:** “Asegurar Macedonia”, “Desarrollar las minas”.
- **Personalidad de la IA:** expansión hacia el sur, prestigio imperial.
- **Dificultad:** media.

### Imperio búlgaro

- **Situación en 1300:** Teodoro Svetoslav se impone en Tarnovo en 1300 tras años de dominio mongol, y busca restaurar el poder búlgaro.
- **Gobierno:** monarquía con boyardos poderosos; patriarcado de Tarnovo.
- **Economía:** agricultura del Danubio y comercio del mar Negro.
- **Retos:** presión de la Horda de Oro, rivalidad con Serbia y Bizancio por Tracia y Macedonia.
- **Oportunidades:** puertos del mar Negro; debilidad bizantina.
- **Situaciones asociadas:** guerras por Tracia, fragmentación en zaratos, conquista otomana.
- **Ambiciones iniciales:** “Recuperar los puertos del mar Negro”, “Paz con la Horda”.
- **Personalidad de la IA:** restauración, oportunismo frente a Bizancio.
- **Dificultad:** media.

### Despotado de Epiro

- **Situación en 1300:** Tomás I Comneno Ducas gobierna desde Arta, inicialmente bajo la regencia de su madre Ana.
- **Gobierno:** Estado griego heredero de las divisiones de 1204, rival de Constantinopla.
- **Retos:** presión angevina desde Italia, ambiciones bizantinas, clanes albaneses.
- **Oportunidades:** alianzas con Nápoles o con Bizancio según convenga; control del Jónico.
- **Ambiciones iniciales:** “Mantener la independencia”.
- **Personalidad de la IA:** equilibrio entre potencias.
- **Dificultad:** alta.

### Tesalia

- **Situación en 1300:** Constantino Ducas gobierna desde Neopatras un principado griego. La Compañía Catalana conquistará parte de la región en 1318.
- **Retos:** vecinos más fuertes (Bizancio, Atenas, Epiro), mercenarios.
- **Oportunidades:** llanuras fértiles; alianzas matrimoniales.
- **Ambiciones iniciales:** “Sobrevivir a los vecinos”.
- **Personalidad de la IA:** defensiva.
- **Dificultad:** alta.

### Principado de Acaya

- **Situación en 1300:** Isabel de Villehardouin gobierna el principado franco de Morea desde Andravida; en 1301 se casará con Felipe de Saboya. Los Anjou de Nápoles son señores feudales del principado.
- **Gobierno:** feudalismo franco con barones y castillos; población mayoritariamente griega ortodoxa.
- **Economía:** agricultura, puerto de Clarenza.
- **Retos:** reconquista bizantina desde Mistra; dependencia de Nápoles.
- **Oportunidades:** alianzas latinas; papel en las cruzadas tardías.
- **Ambiciones iniciales:** “Contener a Mistra”.
- **Personalidad de la IA:** defensa feudal, búsqueda de apoyos latinos.
- **Dificultad:** alta.

### Ducado de Atenas

- **Situación en 1300:** Guido II de la Roche gobierna desde Tebas. En 1311 la Compañía Catalana derrotará y matará a su sucesor en la batalla de Halmyros y se quedará con el ducado.
- **Retos:** contratar mercenarios sin perder el control; vecinos griegos.
- **Oportunidades:** riqueza de Tebas (seda); posición entre Morea y Tesalia.
- **Ambiciones iniciales:** “Expandirse hacia Tesalia”.
- **Personalidad de la IA:** expansión oportunista.
- **Dificultad:** media-alta (la Compañía es un peligro mortal si se gestiona mal).

### República de Venecia

- **Situación en 1300:** dux Pietro Gradenigo; la “serrata” del Gran Consejo (1297) ha cerrado la élite de gobierno. Venecia acaba de salir de una guerra con Génova (terminada en 1299).
- **Gobierno:** república oligárquica con consejos; muy estable.
- **Economía:** comercio marítimo de especias, seda, grano, sal; colonias en Creta, Negroponte, Modón y Corón; flotas comerciales públicas.
- **Retos:** revueltas en Creta, competencia genovesa, dependencia de las rutas levantinas.
- **Oportunidades:** dominar el comercio de Constantinopla; ampliar el imperio colonial.
- **Situaciones asociadas:** guerras veneciano-genovesas, guerras otomano-venecianas, conquista de Chipre.
- **Ambiciones iniciales:** “Asegurar las rutas del Egeo”, “Superar a Génova en el mar Negro”.
- **Personalidad de la IA:** comercio primero, evitar guerras terrestres, aislar a Génova.
- **Dificultad:** media; ideal para jugadores interesados en economía.

### República de Génova

- **Situación en 1300:** república dividida en facciones familiares que domina el comercio del mar Negro desde Pera y Caffa. Venció a Venecia en Curzola (1298). La familia Zaccaria explota el alumbre de Focea y tomará Quíos en 1304.
- **Gobierno:** república inestable; empresas privadas y familias gestionan colonias.
- **Economía:** comercio del mar Negro (grano, pieles, alumbre), banca.
- **Retos:** facciones internas, guerras con Venecia, relaciones tensas con Bizancio.
- **Oportunidades:** monopolios del alumbre y del grano póntico; préstamos a Estados.
- **Ambiciones iniciales:** “Controlar el comercio del mar Negro”, “Asegurar Quíos”.
- **Personalidad de la IA:** comercio agresivo, conflictos con Venecia, intervención en la política bizantina.
- **Dificultad:** media-alta (inestabilidad interna).

### Reino de Hungría

- **Situación en 1300:** Andrés III, último Árpád, morirá en enero de 1301, abriendo una guerra sucesoria entre pretendientes (Anjou, Bohemia, Baviera) que ganará Carlos Roberto de Anjou. Grandes oligarcas controlan regiones enteras.
- **Gobierno:** monarquía feudal con nobleza muy poderosa; dieta.
- **Economía:** agricultura, ganado, minas de oro y plata.
- **Retos:** crisis sucesoria inmediata, oligarcas, Croacia semiindependiente.
- **Oportunidades:** si se restaura la autoridad real, hegemonía en los Balcanes occidentales.
- **Situaciones asociadas:** crisis sucesoria, oligarcas, lucha contra los otomanos.
- **Ambiciones iniciales:** “Asegurar la sucesión”, “Someter a los oligarcas”.
- **Personalidad de la IA:** hegemonía regional, defensa frente a la amenaza otomana cuando aparezca.
- **Dificultad:** alta al principio.

### Reino de Chipre

- **Situación en 1300:** Enrique II de Lusignan gobierna un reino cruzado que, tras la caída de Acre (1291), se ha convertido en el gran puerto cristiano del Levante (Famagusta). En 1306 será desplazado del poder por su hermano Amalarico.
- **Economía:** comercio levantino, azúcar, refugio de mercaderes.
- **Retos:** amenaza mameluca, tensión con órdenes militares e italianos, conflictos dinásticos.
- **Oportunidades:** riqueza comercial; base para cruzadas tardías.
- **Ambiciones iniciales:** “Proteger Famagusta”.
- **Personalidad de la IA:** comercio, alianzas cristianas.
- **Dificultad:** media.

### Imperio de Trebisonda

- **Situación en 1300:** Alejo II gobierna un pequeño imperio griego en la costa sureste del mar Negro, enriquecido por la ruta hacia Tabriz.
- **Retos:** presión turcomana, conflictos con los genoveses, dependencia del Iljanato.
- **Oportunidades:** comercio de la seda persa; alianzas matrimoniales con vecinos.
- **Ambiciones iniciales:** “Defender la ruta de Tabriz”.
- **Personalidad de la IA:** supervivencia comercial y diplomática.
- **Dificultad:** media-alta.

### Armenia cilicia

- **Situación en 1300:** reino cristiano de la dinastía hetúmida, aliado de los mongoles, con el puerto de Ayas como salida de las rutas de Asia.
- **Retos:** invasiones mamelucas recurrentes; conflictos internos y religiosos.
- **Oportunidades:** apoyo mongol y latino; comercio.
- **Ambiciones iniciales:** “Resistir a los mamelucos”.
- **Personalidad de la IA:** alianzas defensivas.
- **Dificultad:** muy alta.

## Anexo J · Entidades de la primera expansión

La primera expansión (Fase 6) amplía el mapa a Europa, el Mediterráneo, Oriente Próximo y el norte de África (escala M). Estas fichas breves orientan el diseño; cada entidad tendrá una ficha completa como las del Anexo I cuando entre en producción.

### Península ibérica

| Entidad | Capital (1300) | Gobernante | Estilo de juego | Reto principal | Oportunidad |
| --- | --- | --- | --- | --- | --- |
| Corona de Castilla | Toledo / Burgos (corte itinerante) | Fernando IV (regencia) | Gran reino feudal | Minoría y nobleza turbulenta | Estrecho de Gibraltar; lana merina |
| Corona de Aragón | Barcelona / Zaragoza | Jaime II | Monarquía compuesta y marítima | Pactismo con las Cortes | Expansión mediterránea (Cerdeña, Sicilia) |
| Reino de Portugal | Lisboa | Dionisio I | Monarquía estable atlántica | Tamaño y vecino castellano | Navegación atlántica |
| Reino de Navarra | Pamplona | Juana I (con Felipe IV) | Unión personal | Depender de Francia | Recuperar autonomía |
| Emirato de Granada | Granada | Muhammad II | Supervivencia diplomática | Presión castellana | Comercio con Génova y el Magreb |
| Reino de Mallorca | Perpiñán / Palma | Jaime II de Mallorca | Reino insular vasallo | Absorción aragonesa | Comercio balear |

### Francia y Países Bajos

| Entidad | Capital | Gobernante | Estilo | Reto | Oportunidad |
| --- | --- | --- | --- | --- | --- |
| Reino de Francia | París | Felipe IV | Monarquía en centralización | Grandes vasallos y choque con el papado | Estado fiscal temprano |
| Ducado de Borgoña | Dijon | Roberto II | Gran vasallo | Lealtad a la Corona | Formar un Estado entre Francia y el Imperio |
| Ducado de Bretaña | Nantes / Vannes | Juan II | Vasallo autónomo | Presión francesa e inglesa | Neutralidad rentable |
| Condado de Flandes | Gante / Brujas | Guido de Dampierre (prisionero) | Ciudades textiles | Ocupación francesa | Revuelta urbana y alianza inglesa |
| Ducado de Brabante | Bruselas / Lovaina | Juan II | Principado comercial | Rivalidad con Flandes | Amberes |
| Henao y Holanda | Mons / La Haya | Juan II de Avesnes | Unión personal | Frisia rebelde | Comercio del mar del Norte |

### Islas británicas

| Entidad | Capital | Gobernante | Estilo | Reto | Oportunidad |
| --- | --- | --- | --- | --- | --- |
| Reino de Inglaterra | Londres / Westminster | Eduardo I | Monarquía con Parlamento | Guerras en Escocia y Gascuña | Lana y Parlamento como fuente de impuestos |
| Escocia | Scone (coronaciones) / Edimburgo | Guardianes del reino | Guerra de independencia | Ocupación inglesa | Restaurar la monarquía |
| Reinos gaélicos de Irlanda | Varios | Reyes locales | Resistencia y alianzas | Señores anglonormandos | Recuperar territorio |
| Señorío de las Islas | Islay | Señores de las Islas | Poder marítimo | Escocia e Inglaterra | Autonomía en las Hébridas |

### Sacro Imperio y Europa central

| Entidad | Capital | Gobernante | Estilo | Reto | Oportunidad |
| --- | --- | --- | --- | --- | --- |
| Austria (Habsburgo) | Viena | Alberto I | Casa con la corona de romanos | Elección imperial y rivales | Construir un patrimonio dinástico |
| Reino de Bohemia | Praga | Venceslao II | Rico por la plata | Mantener la corona polaca | Kutná Hora |
| Reino de Polonia | Cracovia | Venceslao II | Reunificación | Ducados piastas | Unión con Lituania (más tarde) |
| Baviera | Múnich / Landshut | Wittelsbach | Ducado dividido | Ramas rivales | Corona imperial |
| Brandeburgo | Spandau / Brandeburgo | Ascanios | Electorado del norte | Vecinos bálticos | Expansión hacia el Oder |
| Confederación suiza | Cantones de Uri, Schwyz y Unterwalden | Asambleas | Federación emergente | Habsburgo | Mercenariado y pasos alpinos |
| Hansa | Lübeck (dieta) | Ciudades | Organización comercial | Príncipes y Dinamarca | Monopolio del Báltico |
| Orden Teutónica | Marienburgo (desde 1309) | Gran maestre | Estado militar | Lituania y Polonia | Comercio de ámbar y grano |

### Italia

| Entidad | Capital | Gobernante | Estilo | Reto | Oportunidad |
| --- | --- | --- | --- | --- | --- |
| Milán | Milán | Mateo I Visconti | Señoría | Expulsión en 1302 | Dominar Lombardía |
| Florencia | Florencia | Priores | Comuna mercantil | Facciones güelfas | Banca europea |
| Estados Pontificios | Roma | Bonifacio VIII | Teocracia | Choque con Francia | Autoridad sobre la cristiandad latina |
| Reino de Nápoles | Nápoles | Carlos II de Anjou | Monarquía angevina | Guerra por Sicilia | Señorío sobre Acaya y reclamaciones orientales |
| Reino de Sicilia | Palermo | Federico III | Monarquía aragonesa | Ataques angevinos | Grano siciliano |
| Saboya | Chambéry | Amadeo V | Principado alpino | Vecinos mayores | Pasos alpinos y Piamonte |
| Verona | Verona | Della Scala | Señoría | Padua y Venecia | Hegemonía en el Véneto interior |
| Ferrara | Ferrara | Azzo VIII de Este | Señoría | Papado y Venecia | Estabilidad dinástica |

### Norte y este de Europa

| Entidad | Capital | Gobernante | Estilo | Reto | Oportunidad |
| --- | --- | --- | --- | --- | --- |
| Dinamarca | Roskilde / Vordingborg | Erico VI | Monarquía báltica | Nobleza y deuda | Control del Sund |
| Suecia | Estocolmo / Upsala | Birger Magnusson | Monarquía | Hermanos rivales | Finlandia |
| Noruega | Bergen / Oslo | Haakon V | Monarquía marítima | Dependencia hanseática | Uniones nórdicas |
| Gran Ducado de Lituania | Kernavė / Vilna (más tarde) | Vytenis | Pagano en expansión | Órdenes cruzadas | Tierras de la Rus |
| Nóvgorod | Nóvgorod | *Veche* | República de pieles | Suecia y la Orden | Comercio hanseático |
| Tver | Tver | Miguel Yaroslávich | Principado | Rivalidad con Moscú | Título de gran príncipe |
| Moscú | Moscú | Daniel | Principado menor | Tamaño | Favor de la Horda |
| Galitzia-Volinia | Leópolis / Vladímir | Yuri I | Reino de frontera | Vecinos poderosos | Comercio del Báltico al mar Negro |
| Horda de Oro | Sarai | Toqta | Kanato | Guerras internas | Tributo de la Rus y comercio de Caffa |

### Mundo islámico y Cáucaso

| Entidad | Capital | Gobernante | Estilo | Reto | Oportunidad |
| --- | --- | --- | --- | --- | --- |
| Sultanato mameluco | El Cairo | al-Nasir Muhammad | Sultanato militar | Facciones de emires | Especias, legitimidad califal |
| Iljanato | Tabriz / Soltaniyeh | Ghazan | Kanato reformista | Sucesiones, guerras con los mamelucos | Reformas fiscales, ruta de la seda |
| Georgia | Tiflis | Dividida bajo los iljánidas | Reino cristiano | Dominio mongol | Reunificación |
| Benimerines | Fez | Abu Yaqub Yusuf | Sultanato | Asedio de Tremecén | Estrecho y oro saheliano |
| Zayyaníes | Tremecén | — | Sultanato asediado | Benimerines | Rutas transaharianas |
| Hafsíes | Túnez | — | Sultanato | Divisiones dinásticas | Comercio con Italia y Aragón |
| Rasúlidas | Taiz / Zabid | al-Muayyad Dawud | Sultanato comercial | Rebeliones zaydíes | Comercio del mar Rojo |

## Anexo K · Catálogo de bienes y edificios por época

Los bienes aparecen cuando existe la tecnología o el contacto que los hace disponibles. La columna “Desde” es la época en la que suelen volverse relevantes, no una fecha de activación.

### Bienes

| Bien | Categoría | Desde | Uso principal |
| --- | --- | --- | --- |
| Grano | Alimento básico | 1300 | Alimentación, forraje, impuestos en especie |
| Arroz | Alimento básico | 1300 | Alimentación en Asia monzónica |
| Maíz | Alimento básico | 1300 (Américas) | Alimentación; se difunde a Eurasia tras el contacto |
| Patata | Alimento básico | 1300 (Andes) | Alta productividad en climas fríos tras su difusión |
| Ganado | Alimento | 1300 | Carne, cuero, tracción |
| Pescado | Alimento | 1300 | Alimentación, salazón |
| Frutas y hortalizas | Alimento | 1300 | Dieta urbana |
| Sal | Conservación | 1300 | Conservar alimentos; monopolio fiscal |
| Vino | Bebida | 1300 | Consumo, comercio, culto |
| Cerveza | Bebida | 1300 | Consumo del norte de Europa |
| Aceite de oliva | Alimento | 1300 | Alimentación, iluminación, jabón |
| Azúcar | Lujo | 1300 | Lujo; plantaciones |
| Especias | Lujo | 1300 | Lujo; comercio índico |
| Té | Lujo / bebida | 1300 (Asia) | Consumo; comercio global desde el siglo XVII |
| Café | Lujo / bebida | 1450 | Consumo urbano; cafés como espacios políticos |
| Cacao | Lujo | 1300 (Mesoamérica) | Bebida; moneda en Mesoamérica |
| Tabaco | Lujo | 1300 (Américas) | Consumo global tras el contacto |
| Madera | Material | 1300 | Construcción, barcos, combustible |
| Piedra | Material | 1300 | Construcción y fortificación |
| Ladrillo y cerámica | Material | 1300 | Construcción urbana |
| Hierro | Metal | 1300 | Herramientas, armas |
| Cobre | Metal | 1300 | Bronce, moneda, cables (más tarde) |
| Estaño | Metal | 1300 | Bronce |
| Plomo | Metal | 1300 | Munición, tuberías |
| Plata | Metal precioso | 1300 | Moneda |
| Oro | Metal precioso | 1300 | Moneda, lujo |
| Lana | Fibra | 1300 | Textiles |
| Lino | Fibra | 1300 | Textiles, velas |
| Algodón | Fibra | 1300 | Textiles; motor industrial |
| Seda | Fibra / lujo | 1300 | Textiles de lujo |
| Paño | Manufactura | 1300 | Vestido, comercio |
| Tejidos de algodón | Manufactura | 1300 | Vestido; industria temprana |
| Ropa | Manufactura | 1750 | Consumo masivo |
| Cuero | Manufactura | 1300 | Calzado, arneses, equipo |
| Papel | Manufactura | 1300 | Administración, libros |
| Libros | Manufactura | 1450 | Saber, alfabetización |
| Vidrio | Manufactura | 1300 | Ventanas, lentes, instrumentos |
| Alumbre | Química | 1300 | Mordiente textil |
| Tintes | Química | 1300 | Textiles |
| Salitre | Química | 1350 | Pólvora; fertilizante |
| Pólvora | Militar | 1350 | Armas de fuego |
| Armas blancas y armaduras | Militar | 1300 | Equipo |
| Armas de fuego | Militar | 1450 | Equipo |
| Artillería | Militar | 1400 | Asedio y campaña |
| Munición | Militar | 1500 | Consumo bélico |
| Barcos | Capital | 1300 | Comercio y guerra |
| Pertrechos navales | Material | 1300 | Brea, cáñamo, velas |
| Caballos | Animal | 1300 | Caballería, transporte |
| Herramientas | Capital | 1300 | Productividad |
| Muebles | Consumo | 1500 | Comodidad |
| Porcelana | Lujo | 1300 (China) | Lujo y comercio |
| Carbón | Energía | 1600 | Calefacción; industria |
| Coque | Energía | 1750 | Siderurgia |
| Acero | Metal | 1850 | Construcción, maquinaria, armas |
| Maquinaria | Capital | 1780 | Industria |
| Locomotoras y material ferroviario | Capital | 1830 | Transporte |
| Fertilizantes | Química | 1840 | Agricultura |
| Caucho | Material | 1850 | Neumáticos, aislantes |
| Petróleo | Energía | 1860 | Combustible |
| Electricidad | Energía (flujo) | 1880 | Industria, hogares |
| Productos químicos | Química | 1860 | Industria |
| Automóviles | Consumo / capital | 1910 | Transporte |
| Aviones | Capital | 1915 | Transporte, guerra |
| Electrodomésticos | Consumo | 1920 | Comodidad |
| Plásticos | Material | 1930 | Consumo, industria |
| Productos farmacéuticos | Salud | 1930 | Sanidad |
| Aluminio | Metal | 1890 | Aviación, consumo |
| Uranio | Energía | 1945 | Energía nuclear, armas |
| Electrónica | Manufactura | 1950 | Consumo, industria, defensa |
| Semiconductores | Manufactura estratégica | 1960 | Electrónica avanzada |
| Software y servicios digitales | Servicio | 1970 | Productividad |
| Telecomunicaciones | Servicio | 1880 | Información |
| Litio y tierras raras | Mineral estratégico | 1990 | Baterías, electrónica |
| Baterías | Manufactura | 1990 | Almacenamiento energético |
| Paneles solares y turbinas eólicas | Capital energético | 2000 | Energía renovable |
| Hidrógeno | Energía | 2020 | Industria y transporte |

### Edificios

| Edificio | Categoría | Desde | Modos de producción representativos |
| --- | --- | --- | --- |
| Campos | Agricultura | 1300 | Barbecho → rotación trienal → rotación cuatrienal → agricultura mecanizada → agricultura de precisión |
| Arrozales | Agricultura | 1300 | Inundación tradicional → variedades mejoradas → mecanización |
| Chinampas y andenes | Agricultura | 1300 (Américas) | Agricultura intensiva tradicional |
| Plantación | Agricultura | 1300 | Trabajo forzado (con sus costes) → trabajo asalariado → mecanización |
| Pastos y ranchos | Ganadería | 1300 | Trashumancia → cercados → ganadería industrial |
| Pesquería | Pesca | 1300 | Costera → altura → industrial |
| Molino | Transformación | 1300 | Manual → agua → viento → vapor → eléctrico |
| Mina | Extracción | 1300 | Superficial → galerías → bombas de vapor → mecanizada |
| Salinas | Extracción | 1300 | Evaporación → minería de sal → química |
| Aserradero | Extracción | 1300 | Manual → hidráulico → mecánico |
| Taller textil | Manufactura | 1300 | Gremial → doméstico disperso → manufactura → fábrica mecanizada |
| Forja | Manufactura | 1300 | Forja tradicional → alto horno → siderurgia de coque → acería |
| Curtiduría | Manufactura | 1300 | Tradicional → química |
| Astillero | Manufactura | 1300 | Galeras → naves de vela → buques de vapor → acero |
| Imprenta | Manufactura | 1450 | Tipos móviles → prensa mecánica → rotativa → digital |
| Vidriería | Manufactura | 1300 | Soplado → industrial |
| Fábrica de armas | Militar | 1400 | Armería → fábrica de armas de fuego → producción en serie |
| Fábrica | Manufactura | 1780 | Vapor → electricidad → cadena de montaje → automatización |
| Refinería | Energía | 1860 | Destilación → refinado moderno |
| Central eléctrica | Energía | 1880 | Carbón → hidroeléctrica → petróleo → nuclear → renovable |
| Planta química | Industria | 1850 | Química básica → petroquímica |
| Fábrica de automóviles | Industria | 1900 | Taller → cadena de montaje → robótica |
| Fábrica de semiconductores | Industria estratégica | 1960 | Generaciones de procesos |
| Centro de datos | Servicios | 1990 | Servidores → nube → computación especializada |
| Mercado y feria | Comercio | 1300 | Mercado local → feria → lonja → bolsa |
| Puerto | Comercio | 1300 | Muelle → puerto con almacenes → puerto de vapor → puerto de contenedores |
| Factoría comercial | Comercio | 1300 | *Fondaco* → factoría colonial → zona franca |
| Banco | Finanzas | 1300 | Cambistas → banca privada → banco público → banco central |
| Aduana | Estado | 1300 | Peaje → aduana → administración aduanera |
| Palacio y cancillería | Estado | 1300 | Corte → cancillería → ministerios |
| Tribunal | Estado | 1300 | Señorial → real → sistema judicial |
| Casa de la moneda | Estado | 1300 | Acuñación → moneda fiduciaria → banca central |
| Iglesia, mezquita, templo | Religión | 1300 | Local → catedral o gran mezquita → centro de peregrinación |
| Monasterio | Religión | 1300 | Comunidad → centro de saber → propiedades agrarias |
| Universidad o madrasa | Saber | 1300 | Escuela → universidad → universidad investigadora |
| Escuela | Educación | 1500 | Parroquial → pública → obligatoria |
| Hospital | Salud | 1300 | Hospicio → hospital → hospital moderno |
| Saneamiento | Salud | 1850 | Alcantarillado → agua potable → depuración |
| Castillo | Militar | 1300 | Castillo → fortaleza artillada |
| Murallas urbanas | Militar | 1300 | Medievales → abaluartadas → obsoletas |
| Fortaleza abaluartada | Militar | 1500 | Traza italiana → fortificación poligonal |
| Arsenal | Militar | 1300 | Arsenal → base naval |
| Cuartel | Militar | 1600 | Cuartel → base militar |
| Camino | Infraestructura | 1300 | Sendero → camino real → carretera → autopista |
| Puente | Infraestructura | 1300 | Madera → piedra → hierro → hormigón |
| Canal | Infraestructura | 1300 | Riego → navegación con esclusas → interoceánico |
| Ferrocarril | Infraestructura | 1830 | Vapor → electrificado → alta velocidad |
| Telégrafo y teléfono | Infraestructura | 1840 | Telégrafo → teléfono → fibra |
| Aeropuerto | Infraestructura | 1920 | Aeródromo → aeropuerto internacional |
| Red de datos | Infraestructura | 1990 | Cobre → fibra → redes móviles avanzadas |

## Anexo L · Catálogo de leyes

Cada categoría tiene opciones mutuamente excluyentes. Las opciones solo están disponibles cuando existen sus condiciones (instituciones, tecnologías, grupos de interés). Cambiar de opción requiere apoyo político suficiente (sección 11).

| Categoría | Opciones | Efecto principal | Quién la apoya o se opone |
| --- | --- | --- | --- |
| Sucesión | Primogenitura masculina; primogenitura con mujeres; elección por nobles; designación; rotación familiar; elección popular (moderna) | Estabilidad de la transmisión del poder | Nobleza prefiere elección; dinastía prefiere primogenitura |
| Régimen de la tierra | Feudo hereditario; concesión revocable (*pronoia*, *iqta*, *timar*); propiedad libre; propiedad comunal; propiedad eclesiástica protegida; reforma agraria | Quién controla la renta agraria y el reclutamiento | Nobleza, clero, campesinado |
| Servidumbre | Servidumbre plena; servidumbre limitada; campesinado libre | Mano de obra disponible, revueltas, movilidad | Terratenientes frente a campesinos |
| Esclavitud | Legal; restringida; prohibida en el territorio; prohibida y perseguida la trata | Trabajo forzado, legitimidad internacional, conflicto social | Plantadores frente a abolicionistas |
| Recaudación | En especie; en moneda; arrendamiento fiscal; recaudación directa; catastro; impuesto sobre la renta | Eficacia, corrupción, capacidad del Estado | Burocracia, nobleza, mercaderes |
| Política fiscal | Exenciones estamentales; impuesto universal; progresivo | Reparto de la carga | Estamentos privilegiados frente a los demás |
| Religión del Estado | Teocracia; religión oficial exclusiva; oficial con tolerancia; autonomía comunitaria; libertad religiosa; laicidad | Estabilidad con minorías, apoyo del clero | Clero, minorías religiosas |
| Ciudadanía y estatus cultural | Cultura única aceptada; varias aceptadas; integración por servicio; ciudadanía universal | Lealtad de minorías, asimilación | Grupos dominantes frente a minorías |
| Ejército | Levas feudales; mercenarios; milicias; ejército permanente profesional; conscripción; voluntariado profesional moderno | Coste, tamaño y lealtad del ejército | Nobleza, militares, población |
| Comercio | Privilegios a extranjeros; mercantilismo; monopolios estatales; proteccionismo; libre comercio | Ingresos aduaneros, industria local, relaciones exteriores | Mercaderes, industriales, consumidores |
| Gremios y trabajo | Gremios obligatorios; gremios voluntarios; libertad de oficio; derechos laborales; sindicatos legales | Productividad, innovación, conflicto laboral | Artesanos, empresarios, obreros |
| Justicia | Señorial; real; religiosa; codificada; independiente | Previsibilidad, poder de las élites | Nobleza, clero, burguesía |
| Representación | Ninguna; asamblea estamental; parlamento censitario; sufragio masculino; sufragio universal | Legitimidad, control del impuesto | Grupos excluidos frente a incluidos |
| Prensa e información | Censura previa; licencias; libertad de prensa; medios estatales; libertad con regulación | Opinión pública, difusión de ideas | Clero, intelectuales, gobierno |
| Educación | Religiosa; privada; pública; obligatoria | Alfabetización, ciencia, identidad nacional | Clero, Estado |
| Sanidad | Caridad religiosa; hospitales municipales; sanidad pública; seguro obligatorio | Mortalidad, coste fiscal | Clero, médicos, trabajadores |
| Bienestar | Ninguno; caridad; leyes de pobres; seguro social; Estado de bienestar | Pobreza, estabilidad, gasto | Trabajadores frente a contribuyentes |
| Moneda | Metálica; bimetálica; patrón oro; fiduciaria; banco central independiente | Inflación, crédito, crisis | Banqueros, deudores, acreedores |
| Migración | Libre; restringida; selectiva; cerrada | Población, mano de obra, tensiones | Empleadores, trabajadores locales |
| Policía y orden | Milicias locales; guardias reales; policía estatal; policía política | Orden, represión, libertades | Gobierno frente a oposición |
| Medio ambiente | Ninguna; protección de bosques; regulación de emisiones; neutralidad de carbono | Recursos, salud, coste industrial | Industria frente a afectados |

**Reglas de diseño:**

- Una ley puede existir **de iure** y no cumplirse **de facto** si el control territorial o la capacidad del Estado son bajos; el panel muestra ambos.
- Las leyes sobre trabajo forzado y persecución siguen la política de contenido sensible: sus costes humanos y sociales son visibles y relevantes.
- Las opciones modernas (sufragio, bienestar, medio ambiente) solo aparecen cuando existen las instituciones y los grupos que las demandan.

## Anexo M · Catálogo de unidades por época

Los valores son **relativos y orientativos** (escala 1–5) para orientar el balance; los números concretos se fijarán en la especificación militar.

### Tierra

| Unidad | Época | Choque | Fuego | Defensa | Movilidad | Coste | Notas |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Leva campesina | 1300–1500 | 1 | 1 | 2 | 2 | 1 | Barata, poco fiable. |
| Milicia urbana | 1300–1600 | 2 | 2 | 3 | 2 | 2 | Defiende bien su ciudad. |
| Caballería pesada | 1300–1550 | 5 | 0 | 3 | 3 | 5 | Decisiva en campo abierto; vulnerable a picas y fuego. |
| Caballería ligera | 1300–1900 | 3 | 1 | 2 | 5 | 3 | Exploración, persecución, saqueo. |
| Arqueros a caballo | 1300–1600 | 2 | 4 | 2 | 5 | 4 | Dominantes en la estepa. |
| Arqueros y ballesteros | 1300–1550 | 1 | 4 | 2 | 2 | 2 | Fuego a distancia. |
| Infantería de lanzas o picas | 1300–1700 | 3 | 0 | 5 | 2 | 2 | Frena a la caballería. |
| Infantería pesada de élite | 1300–1600 | 4 | 0 | 4 | 2 | 4 | Guardias, órdenes militares. |
| Arcabuceros | 1450–1650 | 1 | 4 | 2 | 2 | 3 | Necesitan protección de picas. |
| Tercio o formación mixta | 1500–1650 | 4 | 4 | 4 | 2 | 4 | Combinación de picas y fuego. |
| Infantería de línea | 1650–1860 | 3 | 4 | 3 | 3 | 3 | Mosquete y bayoneta. |
| Dragones | 1600–1900 | 3 | 3 | 2 | 4 | 3 | Infantería montada. |
| Artillería de asedio | 1400–1900 | 0 | 5 | 1 | 1 | 5 | Derriba murallas. |
| Artillería de campaña | 1600–1950 | 0 | 5 | 1 | 2 | 4 | Decisiva desde el siglo XVIII. |
| Infantería con fusil | 1850–1945 | 3 | 5 | 4 | 3 | 3 | Defensa dominante con trincheras. |
| Ametralladoras | 1880–1945 | 0 | 5 | 5 | 2 | 3 | Hace muy costosos los asaltos. |
| Blindados | 1916– | 5 | 4 | 4 | 4 | 5 | Ruptura y explotación. |
| Infantería mecanizada | 1939– | 4 | 4 | 4 | 4 | 4 | Acompaña a los blindados. |
| Artillería autopropulsada | 1940– | 0 | 5 | 2 | 4 | 4 | Apoyo móvil. |
| Fuerzas aerotransportadas | 1940– | 3 | 3 | 2 | 5 | 4 | Despliegue rápido, ligeras. |
| Fuerzas especiales | 1940– | 3 | 3 | 2 | 5 | 5 | Sabotaje y operaciones encubiertas. |
| Defensa aérea | 1915– | 0 | 4 | 3 | 2 | 3 | Protege frente a la aviación. |
| Lanzadores de misiles | 1950– | 0 | 5 | 1 | 3 | 5 | Ataques de precisión a distancia. |
| Drones | 2000– | 1 | 4 | 1 | 5 | 2 | Reconocimiento y ataque baratos. |

### Mar

| Unidad | Época | Fuego | Resistencia | Velocidad | Carga | Notas |
| --- | --- | --- | --- | --- | --- | --- |
| Galera | 1300–1700 | 2 | 2 | 3 | 1 | Depende de remeros y costas; ideal en el Mediterráneo. |
| Nave redonda / coca | 1300–1500 | 1 | 3 | 2 | 4 | Comercio y transporte. |
| Carraca | 1400–1600 | 2 | 4 | 2 | 4 | Grandes viajes. |
| Carabela | 1430–1600 | 1 | 2 | 4 | 2 | Exploración. |
| Galeaza | 1550–1700 | 4 | 4 | 2 | 2 | Galera artillada. |
| Galeón | 1550–1750 | 4 | 4 | 3 | 4 | Guerra y comercio oceánico. |
| Navío de línea | 1650–1860 | 5 | 5 | 3 | 2 | Combate en línea. |
| Fragata | 1650–1860 | 3 | 3 | 5 | 2 | Escolta y corso. |
| Buque de vapor | 1820–1900 | 3 | 3 | 4 | 4 | Independiente del viento. |
| Acorazado | 1860–1945 | 5 | 5 | 3 | 1 | Dominio naval industrial. |
| Crucero | 1880– | 4 | 3 | 4 | 1 | Protección de rutas. |
| Destructor | 1890– | 3 | 2 | 5 | 1 | Escolta, antisubmarino. |
| Submarino | 1900– | 4 | 2 | 3 | 0 | Guerra comercial. |
| Portaaviones | 1920– | 5 | 4 | 3 | 0 | Proyección aérea. |
| Buque anfibio | 1940– | 1 | 3 | 3 | 5 | Desembarcos. |
| Buque no tripulado | 2020– | 3 | 1 | 4 | 0 | Vigilancia y ataque. |

### Aire

| Unidad | Época | Función |
| --- | --- | --- |
| Reconocimiento | 1910– | Información y artillería. |
| Caza | 1915– | Superioridad aérea. |
| Bombardero táctico | 1915– | Apoyo al frente. |
| Bombardero estratégico | 1930– | Industria e infraestructura enemigas. |
| Transporte | 1930– | Logística y paracaidistas. |
| Avión de reacción | 1945– | Superioridad y ataque. |
| Helicóptero | 1950– | Movilidad y apoyo. |
| Alerta temprana | 1960– | Control del espacio aéreo. |
| Dron de gran altitud | 2000– | Vigilancia persistente. |

## Anexo N · Fichas culturales de la primera expansión

Complementan las 16 fichas de la vertical (sección 06). Mismo esquema: idioma, religión mayoritaria en 1300, núcleo territorial, rasgos y nota de diseño.

| Cultura | Idioma | Religión | Núcleo en 1300 | Rasgos | Nota de diseño |
| --- | --- | --- | --- | --- | --- |
| Castellano | Castellano | Católica | Castilla, Andalucía occidental | Tradición fronteriza, ganadería trashumante | La frontera con Granada sigue activa. |
| Leonés-asturiano | Asturleonés | Católica | León, Asturias | Tradición rural | Absorción progresiva por el castellano. |
| Gallego-portugués | Gallego-portugués | Católica | Galicia, Portugal | Tradición marítima | La rama portuguesa diverge con el reino. |
| Catalán | Catalán | Católica | Cataluña, Valencia, Baleares | Tradición mercantil, marítima, asambleas | Pactismo con la Corona. |
| Aragonés | Aragonés | Católica | Aragón | Asambleas, nobleza fuerte | Fueros y justicia mayor. |
| Vasco | Euskera | Católica | Vizcaya, Guipúzcoa, Navarra | Linajes, tradición marítima | Fueros y autonomía. |
| Andalusí | Árabe andalusí | Suní malikí | Granada | Tradición urbana, regadío | Cultura del último emirato peninsular. |
| Judío sefardí | Judeoespañol y lenguas locales | Judaísmo | Ciudades ibéricas | Diáspora, tradición escrita, mercantil | Vulnerable a persecuciones y expulsiones. |
| Francés | Francés antiguo | Católica | Norte de Francia | Tradición caballeresca, burocracia real | Núcleo de la monarquía capeta. |
| Occitano | Occitano | Católica | Sur de Francia | Tradición urbana, poesía cortés | Integrado en Francia tras la cruzada albigense. |
| Bretón | Bretón | Católica | Bretaña occidental | Tradición marítima | Ducado autónomo. |
| Flamenco | Neerlandés medio | Católica | Flandes | Tradición urbana, artesanía textil | Ciudades rebeldes frente a Francia. |
| Inglés | Inglés medio | Católica | Inglaterra | Asambleas, arquería | El francés sigue siendo lengua de la élite. |
| Anglonormando | Francés anglonormando | Católica | Élite de Inglaterra e Irlanda | Tradición caballeresca | Se asimila al inglés con el tiempo. |
| Escocés | Escocés de las tierras bajas | Católica | Lothian, costa este | Tradición fronteriza | Guerra de independencia. |
| Gaélico | Gaélico | Católica | Irlanda, Tierras Altas de Escocia | Linajes extensos | Clanes y señoríos. |
| Galés | Galés | Católica | Gales | Tradición oral, arquería | Conquistado recientemente por Inglaterra. |
| Alto alemán | Alto alemán medio | Católica | Sur y centro de Alemania | Tradición urbana, artesanía | Fragmentado en principados. |
| Bajo alemán | Bajo alemán | Católica | Norte de Alemania, Báltico | Tradición mercantil, marítima | Lengua de la Hansa. |
| Checo | Checo antiguo | Católica | Bohemia, Moravia | Minería, tradición urbana | Tensión con colonos alemanes. |
| Polaco | Polaco antiguo | Católica | Pequeña y Gran Polonia | Nobleza con asambleas | Reunificación en curso. |
| Lituano | Lituano | Pagana (báltica) | Lituania | Tradición fronteriza | Conversión aún no decidida. |
| Ruso antiguo | Ruso antiguo | Ortodoxa | Nóvgorod, Vladímir, Tver, Moscú | Tradición fronteriza, monacato | Bajo tributo de la Horda. |
| Rutenio | Ruteno | Ortodoxa | Galitzia-Volinia, Kiev | Tradición fronteriza | Entre Lituania, Polonia y la Horda. |
| Sueco | Sueco antiguo | Católica | Suecia | Tradición marítima | Expansión hacia Finlandia. |
| Danés | Danés antiguo | Católica | Dinamarca, Escania | Tradición marítima | Control del Sund. |
| Noruego | Nórdico antiguo | Católica | Noruega, islas del Atlántico | Tradición marítima | Dependencia comercial de la Hansa. |
| Finés | Finés | Católica y tradicional | Finlandia | Tradición rural | Bajo influencia sueca. |
| Toscano | Toscano | Católica | Florencia, Siena, Pisa | Tradición mercantil, urbana | Banca y literatura en lengua vulgar. |
| Lombardo | Lombardo | Católica | Milán y Lombardía | Tradición urbana | Señorías en ascenso. |
| Napolitano-siciliano | Napolitano, siciliano | Católica | Sur de Italia | Tradición rural, puertos | Guerra entre Anjou y Aragón. |
| Sardo | Sardo | Católica | Cerdeña | Tradición rural | Judicado de Arborea. |
| Árabe egipcio | Árabe | Suní; minoría copta | Egipto | Regadío, tradición urbana | Mayoría bajo una élite militar túrquica y circasiana. |
| Árabe levantino | Árabe | Suní; minorías cristianas, chiíes, drusas | Siria, Líbano, Palestina | Tradición urbana, mercantil | Frontera mameluca con el Iljanato. |
| Bereber (zenata, masmuda) | Lenguas bereberes | Suní malikí | Magreb | Linajes, pastoralismo | Base de las dinastías magrebíes. |
| Persa | Persa | Suní y chií | Irán | Tradición escrita y burocrática | Administración del Iljanato. |
| Kurdo | Kurdo | Suní; minorías yazidíes | Montes Zagros y Taurus | Linajes, montañeses | Emiratos autónomos. |
| Georgiano | Georgiano | Ortodoxa georgiana | Georgia | Tradición fronteriza, monacato | Reino dividido bajo dominio mongol. |
| Copto | Copto (litúrgico) y árabe | Copta | Egipto | Tradición escrita | Minoría con papel administrativo. |

## Anexo O · Especificación de pantallas (bocetos)

Bocetos de baja fidelidad para orientar el diseño de interfaz y las tareas del rol Cliente. Las proporciones son indicativas; el diseño final se hará con la herramienta de UI elegida en la Fase 1.

### Vista principal del mapa

```text
┌───────────────────────────────────────────────────────────────────────────────┐
│ [Escudo] Imperio bizantino  ₲ 1.240 (−35/mes)  Legit. 52%  Control 61%  ⚔ 1   │
│ 14 mar 1303 (juliano)   ▶ ▶▶ ▶▶▶   ⏸     [Alertas 3]  [Buscar…]  [☰]          │
├──────────┬────────────────────────────────────────────────────────┬───────────┤
│ Modos    │                                                        │ Alertas   │
│ ● Polít. │                                                        │ ! Tesoro  │
│ ○ Cultura│                  M A P A                               │   bajo    │
│ ○ Religión│                                                       │ ! Bitinia │
│ ○ Econom.│      (textura de IDs + estilo de época)                │   pierde  │
│ ○ Comerc.│                                                        │   control │
│ ○ Militar│                                                        │ i Peste en│
│ ○ Control│                                                        │   Caffa   │
│ ○ Diverg.│                                                        │           │
├──────────┴────────────────────────────────────────────────────────┴───────────┤
│ [País] [Gobierno] [Economía] [Mercado] [Ejército] [Diplomacia] [Ciencia]      │
│ [Corte] [Historia] [Estadísticas] [Enciclopedia]                              │
└───────────────────────────────────────────────────────────────────────────────┘
```

### Panel de provincia

```text
┌ Bitinia (Nicomedia) ─────────────────────────────────── [×] [📌] [←] [→] ┐
│ Propietario: Imperio bizantino   Control: 38% ▼  (¿por qué?)             │
│ Población: 84.300  ▼ −1,2%/año   Nivel de vida: bajo                     │
├──────────────────────────────────────────────────────────────────────────┤
│ Cohortes                         Personas  Cultura   Religión  Vida      │
│ Campesinos dependientes           51.200   Griego    Ortodoxa  Bajo      │
│ Pastores turcomanos                9.800   Turcomano Suní      Medio     │
│ Artesanos                          6.100   Griego    Ortodoxa  Medio     │
│ Clero y monjes                     2.300   Griego    Ortodoxa  Medio     │
│ …                                                                        │
├──────────────────────────────────────────────────────────────────────────┤
│ Edificios: Campos (rotación bienal) · Molino de agua · Castillo (II)     │
│ Producción: grano 1.900/mes · lana 210/mes                               │
│ Historial: 1299 incursiones · 1301 aldeas abandonadas                    │
└──────────────────────────────────────────────────────────────────────────┘
```

### Ventana “¿por qué?”

```text
┌ ¿Por qué baja el control de Bitinia? ────────────────────────────────────┐
│ Control objetivo: 31%    Control actual: 38%  → bajará ~0,4 puntos/mes   │
├──────────────────────────────────────────────────────────────────────────┤
│ Capacidad administrativa disponible            +55%                      │
│ Distancia: 9 días de viaje a Constantinopla    −12%                      │
│ Guarnición sin pagar (5 meses)                 −8%   [Ver tesoro →]      │
│ Incursiones de beyliks en los últimos 12 meses −10%  [Ver frontera →]    │
│ Población turcomana sin lealtad al imperio     −4%                       │
├──────────────────────────────────────────────────────────────────────────┤
│ Qué puedes hacer: pagar la guarnición (−300 ₲) · enviar tropas ·         │
│ conceder tierras a soldados (pronoia) · negociar con el beylik           │
└──────────────────────────────────────────────────────────────────────────┘
```

### Mercado

```text
┌ Mercado de Constantinopla ───────────────────────────────────────────────┐
│ Bien      Precio  Δ sem.  Oferta  Demanda  Principal causa del cambio    │
│ Grano     1,62    +8%     ▼       ▲        Sequía en Tracia (−40%)       │
│ Sal       0,95    0%      =       =        —                             │
│ Seda      7,40    −2%     ▲       =        Llegada de caravana de Tabriz │
│ Alumbre   3,10    +4%     ▼       ▲        Guerra en Focea               │
├──────────────────────────────────────────────────────────────────────────┤
│ Rutas principales: Caffa → (grano, pieles)  Venecia ← (paño)             │
│ Control comercial: Génova 46% · Venecia 31% · Bizancio 15% · otros 8%    │
└──────────────────────────────────────────────────────────────────────────┘
```

### Guerra

```text
┌ Guerra: Bizancio contra el beylik otomano ───────────────────────────────┐
│ Objetivo declarado: defender Bitinia      Puntuación: −18 (desfavorable) │
│ Agotamiento propio: 34%  (bajas 22%, impuestos 40%, precios 25%, …)       │
├──────────────────────────────────────────────────────────────────────────┤
│ Asedios activos: Nicea (sitiada por el enemigo) — progreso 12%           │
│   Bloqueo naval: no · Artillería enemiga: no · Comida: 14 meses           │
│ Ejércitos: 2 propios (4.100 hombres) · 3 enemigos (6.300 estimados)      │
├──────────────────────────────────────────────────────────────────────────┤
│ [Proponer paz]  [Pedir ayuda a aliados]  [Contratar mercenarios]         │
└──────────────────────────────────────────────────────────────────────────┘
```

### Diplomacia

```text
┌ Relaciones con la República de Génova ───────────────────────────────────┐
│ Confianza ▓▓▓▓░░ 62   Interés ▓▓▓▓▓░ 78   Agravio ▓░░░░░ 15              │
│ Amenaza ▓▓░░░░ 30     Afinidad ▓▓░░░░ 28  Dependencia ▓▓▓▓▓░ 81          │
├──────────────────────────────────────────────────────────────────────────┤
│ Tratados: privilegios comerciales (Ninfeo, 1261) · barrio de Pera        │
│ Lo que quieren: reducir aduanas · exclusividad del grano del mar Negro    │
│ Lo que sabemos: información de hace 9 días (embajada en Pera)            │
├──────────────────────────────────────────────────────────────────────────┤
│ [Negociar tratado]  [Pedir préstamo]  [Enviar regalo]  [Embajada]        │
└──────────────────────────────────────────────────────────────────────────┘
```

**Principios comunes de todas las pantallas:** toda cifra es clicable y lleva a su explicación; los paneles se pueden anclar y comparar; las acciones muestran su coste antes de confirmarse; ningún dato importante depende solo del color.

## Anexo P · Backlog de las Fases 0–2 en formato de tareas

Tareas listas para convertirse en issues con la plantilla de la sección 43. Cada una es pequeña (2–6 horas de agente) y tiene criterios verificables. Los identificadores `T-` son provisionales.

### Fase 0 · Preproducción

| ID | Rol | Tarea | Archivos | Criterios de aceptación |
| --- | --- | --- | --- | --- |
| T-001 | infra | Crear el repositorio con el kit `101-engine-starter`. | Raíz, `docs/`, `.github/` | Archivos del kit presentes; `main` protegida. |
| T-002 | infra | Workspace vacío con `rust-toolchain.toml`, lints compartidos y `deny.toml`. | `Cargo.toml`, `deny.toml` | `cargo build` en verde sin crates. |
| T-003 | infra | `tools/xtask` con `check` (fmt, clippy, test). | `tools/xtask/` | `cargo xtask check` funciona en CI y en local. |
| T-004 | infra | Flujo `ci.yml` que ejecuta `cargo xtask check`. | `.github/workflows/` | CI en verde en un PR de prueba. |
| T-005 | architecture | ADR 0001: monorepo y prefijo `e101-`. | `docs/adr/` | ADR aceptado. |
| T-006 | architecture | ADR 0002: reglas de determinismo. | `docs/adr/` | ADR con lista de prohibiciones y lints previstos. |
| T-007 | architecture | ADR 0003: tipos de punto fijo. | `docs/adr/` | Escalas y redondeo decididos. |
| T-008 | sim | Prototipo económico en hoja de cálculo o script (fuera del motor). | `docs/specs/prototypes/` | 200 años estables con 10 bienes y 5 mercados. |
| T-009 | data | Prueba del pipeline: costas y ríos de la región en una textura de IDs. | `data-build/` | Imagen generada de forma reproducible. |
| T-010 | history | Lista verificada de entidades y gobernantes de 1300 en la región. | `docs/specs/history/` | Fuente y confianza por fila; revisión humana. |

### Fase 1 · Núcleo

| ID | Rol | Tarea | Archivos | Criterios de aceptación |
| --- | --- | --- | --- | --- |
| T-101 | engine | Crate `e101-time`: día absoluto y conversión juliana/gregoriana. | `crates/e101-time/` | Pruebas de propiedad de ida y vuelta; fechas de referencia correctas. |
| T-102 | engine | Escalonamiento mensual por ID. | `crates/e101-time/` | Cada entidad se procesa una vez al mes; distribución uniforme. |
| T-103 | engine | Crate `e101-rng` con generador basado en contador. | `crates/e101-rng/` | Mismo resultado con cualquier orden de llamada; pruebas estadísticas básicas. |
| T-104 | engine | Tipos `Money`, `Qty`, `Ratio` en `e101-store`. | `crates/e101-store/src/fixed.rs` | Sin desbordamiento silencioso; pruebas de propiedad. |
| T-105 | engine | Tablas SoA con IDs estables y slotmaps. | `crates/e101-store/` | Inserción, borrado y lectura paralela probados. |
| T-106 | infra | Lint de determinismo (flotantes y `HashMap` en crates de simulación). | `tools/xtask/` | Un PR de prueba que los usa falla en CI. |
| T-107 | infra | Lint del grafo de dependencias entre crates. | `tools/xtask/` | Una dependencia prohibida falla en CI. |
| T-108 | engine | Crate `e101-commands`: bus y diario de comandos. | `crates/e101-commands/` | Orden estable; serialización del diario. |
| T-109 | engine | Fase de aplicación de deltas con orden estable. | `crates/e101-sim/src/apply.rs` | Resultado idéntico con 1 y con 16 hilos. |
| T-110 | engine | Hash de estado por tick. | `crates/e101-save/` | Hash estable entre ejecuciones. |
| T-111 | qa | Primer escenario dorado: 300 años vacíos. | `tests/golden/empty_300y/` | Hash idéntico en dos ejecuciones y en CI. |
| T-112 | engine | Guardado y carga con postcard o bitcode y zstd. | `crates/e101-save/` | Cargar y continuar produce los mismos hashes. |
| T-113 | data | Modelo de territorios: localizaciones, provincias, adyacencias. | `crates/e101-map/` | Invariantes de conectividad. |
| T-114 | data | Carga y validación de entidades desde RON. | `crates/e101-content/` | Errores claros con archivo y línea. |
| T-115 | sim | Soberanía y control efectivo básicos. | `crates/e101-sim/src/politics/` | 10.000 cambios aleatorios de frontera sin violar invariantes. |
| T-116 | tools | `e101-headless` ejecuta N años y escribe un resumen. | `crates/e101-headless/` | Campaña de 300 años en headless. |
| T-117 | client | Spike A: mapa con textura de IDs y tres modos (wgpu). | `crates/e101-client/` (rama de spike) | Métricas del plan del spike. |
| T-118 | client | Spike D: mismo mapa y panel en Godot con Rust. | Rama de spike | Métricas del plan del spike. |
| T-119 | client | Spike G: mismo mapa con UI web embebida. | Rama de spike | Métricas del plan del spike. |
| T-120 | architecture | ADR de elección del cliente con métricas. | `docs/adr/` | Decisión aceptada. |

### Fase 2 · Economía y población

| ID | Rol | Tarea | Archivos | Criterios de aceptación |
| --- | --- | --- | --- | --- |
| T-201 | architecture | Contrato `Good`, `Market`, `Price`, `Building`, `Mode`. | `docs/adr/`, interfaces | ADR aceptado. |
| T-202 | data | Formato RON de bienes, edificios y modos. | `crates/e101-content/`, `games/epoch/data/` | 20 bienes y 25 edificios cargan sin errores. |
| T-203 | sim | Producción con proporciones fijas. | `crates/e101-sim/src/economy/production.rs` | El insumo limitante se identifica y se registra. |
| T-204 | sim | Consumo por cestas de estrato. | `crates/e101-sim/src/economy/consumption.rs` | Orden de prioridad respetado; sustitución por categoría. |
| T-205 | sim | Ajuste semanal de precios. | `crates/e101-sim/src/economy/prices.rs` | Límites ±10 % y 0,2–10 × base. |
| T-206 | data | Rutas y capacidades desde el pipeline. | `data-build/`, `crates/e101-map/` | Rutas reproducibles con capacidad por tipo. |
| T-207 | sim | Comercio entre mercados con ajuste parcial. | `crates/e101-sim/src/economy/trade.rs` | Conservación de bienes; flujos acotados. |
| T-208 | engine | Crate `e101-ledger`: contribuciones con origen. | `crates/e101-ledger/` | `why(variable)` devuelve contribuciones ordenadas. |
| T-209 | sim | Registro de precios en el ledger (tres mayores contribuyentes). | `crates/e101-sim/src/economy/` | Pruebas de que la suma explica el cambio. |
| T-210 | sim | Cohortes: natalidad, mortalidad, migración. | `crates/e101-sim/src/population/` | Conservación de población; tasas en rangos. |
| T-211 | sim | Fusión de cohortes por umbral. | `crates/e101-sim/src/population/merge.rs` | Número de cohortes acotado en 300 años. |
| T-212 | sim | Presupuesto del Estado: impuestos y gasto. | `crates/e101-sim/src/state_finance/` | Balance exacto. |
| T-213 | sim | Deuda con acreedores e impago. | `crates/e101-sim/src/state_finance/debt.rs` | Balance de deuda exacto entre actores. |
| T-214 | qa | Pruebas de propiedad de conservación de bienes, dinero y población. | `tests/` | Fallan si se introduce una fuga deliberada. |
| T-215 | qa | Escenario dorado económico de 100 años. | `tests/golden/economy_100y/` | Hash estable. |
| T-216 | tools | 101 Lab v0: 20 campañas y CSV de precios. | `crates/e101-lab/` | Informe local generado. |
| T-217 | client | Panel de mercado con “¿por qué?”. | `crates/e101-client/` | Muestra los tres contribuyentes de cada precio. |
| T-218 | client | Panel de provincia con cohortes. | `crates/e101-client/` | Tabla ordenable de 60 filas fluida. |
| T-219 | history | Datos económicos iniciales del slice (producción por provincia). | `games/epoch/data/` | Fuente y confianza; revisión humana. |
| T-220 | qa | Primera prueba con jugador externo y acta. | `docs/playtests/` | Acta con hallazgos y tareas derivadas. |

## Anexo Q · Catálogo ampliado de situaciones históricas

Complementa la muestra de la sección 07. Ninguna situación tiene fecha fija: la ventana indica cuándo es plausible, y las condiciones deciden si ocurre. “Consecuencias típicas” describe lo que suele producir, no lo que obliga a producir.

### 1300–1500

| Situación | Ventana | Condiciones | Consecuencias típicas |
| --- | --- | --- | --- |
| Revuelta de las ciudades flamencas | 1300–1330 | Ciudades textiles ocupadas por un rey extranjero; gremios armados. | Derrota de la caballería ante milicias; autonomía urbana. |
| Supresión de una orden militar | 1305–1320 | Orden rica sin misión activa; monarca endeudado con ella. | Confiscación de bienes; traspaso a otra orden. |
| Papado en Aviñón | 1305–1380 | Papa elegido bajo presión de una monarquía fuerte; Roma insegura. | Papado alineado con esa monarquía; pérdida de prestigio. |
| Gran hambruna | 1310–1330 | Varios años fríos y lluviosos seguidos en regiones densamente pobladas. | Mortalidad alta, abandono de tierras marginales. |
| Guerra civil castellana | 1350–1370 | Rey enfrentado a la nobleza y a un hermano bastardo con apoyos exteriores. | Cambio de dinastía, intervención de potencias vecinas. |
| Revueltas tras la peste | 1350–1400 | Escasez de mano de obra y leyes que congelan salarios. | Revueltas campesinas y urbanas; cambios en la servidumbre. |
| Guerra de Chioggia | 1370–1390 | Rivalidad veneciano-genovesa por rutas; aliados regionales. | Agotamiento de ambos; reordenación del comercio. |
| Batalla decisiva en los Balcanes | 1370–1400 | Potencia otomana en expansión frente a coalición balcánica. | Vasallaje de los Estados balcánicos. |
| Cruzada de socorro | 1390–1450 | Potencia otomana amenazante; Hungría y potencias occidentales dispuestas. | Gran batalla; victoria o desastre cruzado. |
| Ascenso de los Médici | 1400–1440 | Banca dominante en una república con facciones. | Gobierno informal de una familia banquera. |
| Guerra hussita | 1415–1440 | Reformador ejecutado; nobleza y ciudades descontentas. | Cruzadas fallidas; compromiso religioso. |
| Revueltas campesinas en Escandinavia | 1430–1440 | Impuestos para guerras extranjeras en una unión de reinos. | Debilitamiento de la unión. |
| Paz de Lodi y equilibrio italiano | 1450–1460 | Agotamiento tras guerras entre Estados italianos; amenaza exterior. | Liga italiana y equilibrio de poder. |
| Guerra de las Dos Rosas | 1450–1490 | Rey débil, nobleza armada tras una guerra perdida en el exterior. | Cambio dinástico; nobleza diezmada. |
| Caída de Granada | 1480–1500 | Emirato dividido frente a coronas unidas. | Fin del último Estado musulmán peninsular. |

### 1500–1750

| Situación | Ventana | Condiciones | Consecuencias típicas |
| --- | --- | --- | --- |
| Conquista de un imperio americano | 1510–1540 | Contacto transatlántico; aliados locales enemigos del imperio; epidemias. | Colapso del imperio; virreinato; catástrofe demográfica. |
| Guerras de Italia | 1494–1559 | Potencias con reclamaciones sobre Estados italianos ricos y divididos. | Dominio extranjero de Italia; revolución militar. |
| Revuelta de las Comunidades | 1515–1525 | Rey extranjero, impuestos para fines exteriores, ciudades con tradición de autonomía. | Derrota o concesiones; fortalecimiento de la Corona. |
| Guerra de los campesinos | 1520–1530 | Reforma religiosa reciente, presión señorial. | Represión; cambios en la religión del territorio. |
| Sitio de Viena | 1525–1690 | Potencia otomana en Hungría frente a los Habsburgo. | Frontera estabilizada o colapso de Europa central. |
| Guerra de los Ochenta Años | 1560–1650 | Provincias ricas con religión distinta a la del soberano; impuestos. | Independencia de una república comercial. |
| Batalla naval decisiva en el Mediterráneo | 1560–1580 | Coalición cristiana frente a flota otomana en expansión. | Freno simbólico; equilibrio naval. |
| Unión de coronas ibéricas | 1570–1600 | Rey sin heredero directo y pretendiente vecino fuerte. | Unión personal; tensiones posteriores. |
| Época de los Disturbios | 1598–1620 | Extinción dinástica en un gran Estado; intervención vecina. | Nueva dinastía o fragmentación. |
| Guerra de los Treinta Años | 1610–1650 | Imperio dividido religiosamente; potencias exteriores interesadas. | Devastación; soberanía de los príncipes; nuevo equilibrio. |
| Guerra civil inglesa | 1630–1660 | Rey sin apoyo del Parlamento para impuestos; conflicto religioso. | Ejecución del rey o compromiso; república temporal. |
| Crisis general del siglo XVII | 1620–1690 | Clima frío, guerras, presión fiscal. | Revueltas simultáneas en varios Estados. |
| Cierre de un país al comercio exterior | 1600–1650 | Gobierno central fuerte que teme la influencia extranjera. | Aislamiento selectivo prolongado. |
| Cambio de dinastía en China | 1630–1680 | Rebeliones campesinas, crisis fiscal, invasión del norte. | Nueva dinastía conquistadora. |
| Guerra de Sucesión española | 1700–1715 | Rey sin heredero con reinos codiciados por dos casas. | Reparto de territorios; nueva dinastía. |
| Gran Guerra del Norte | 1700–1721 | Potencia báltica dominante frente a coalición de vecinos. | Nueva potencia en el Báltico. |

### 1750–1914

| Situación | Ventana | Condiciones | Consecuencias típicas |
| --- | --- | --- | --- |
| Guerra global entre potencias coloniales | 1750–1765 | Rivalidad colonial y europea simultánea. | Reparto colonial; deuda que provoca crisis posteriores. |
| Reparto de un Estado débil | 1770–1800 | Estado con nobleza dividida rodeado de potencias absolutistas. | Desaparición del Estado; movimientos de restauración. |
| Independencia de colonias atlánticas | 1770–1830 | Élites coloniales sin representación, metrópoli endeudada. | Nuevas repúblicas; guerras de independencia. |
| Revolución política en una gran monarquía | 1780–1800 | Bancarrota, asamblea convocada, ideas ilustradas. | Fin del antiguo régimen; guerras revolucionarias. |
| Imperio continental de un general | 1795–1815 | Revolución, guerras exteriores, general victorioso. | Hegemonía temporal; códigos legales; nacionalismos. |
| Revolución haitiana | 1790–1805 | Colonia de plantación con mayoría esclavizada; metrópoli en crisis. | Independencia y abolición. |
| Primavera de los pueblos | 1840–1850 | Crisis económica, nacionalismos, liberalismo. | Revoluciones simultáneas; reformas o represión. |
| Gran hambruna | 1840–1850 | Dependencia de un cultivo afectado por una plaga. | Mortalidad y emigración masivas. |
| Rebelión masiva en un imperio asiático | 1850–1865 | Crisis dinástica, presión extranjera, movimiento religioso. | Decenas de millones de muertes; debilitamiento del Estado. |
| Restauración y modernización acelerada | 1860–1880 | Presión exterior que demuestra el atraso militar; élites reformistas. | Industrialización y reforma desde arriba. |
| Guerra civil por la esclavitud | 1850–1870 | Federación dividida entre economías libre y esclavista. | Secesión o abolición. |
| Reparto colonial de África | 1880–1900 | Potencias industriales con medicina tropical y armas modernas. | Colonización casi total; resistencia. |
| Guerra entre potencias asiáticas y europeas | 1895–1910 | Potencia asiática modernizada frente a imperio europeo en Asia. | Cambio en el equilibrio mundial. |

### 1914–2060

| Situación | Ventana | Condiciones | Consecuencias típicas |
| --- | --- | --- | --- |
| Guerra general europea | 1900–1930 | Bloques rígidos, crisis detonante, planes de movilización rápidos. | Guerra larga; colapso de imperios. |
| Pandemia de gripe | 1915–1925 | Movilización masiva y transporte rápido. | Mortalidad global elevada. |
| Revolución en un imperio agotado | 1915–1925 | Guerra perdida, hambre, movimiento revolucionario organizado. | Nuevo régimen; guerra civil. |
| Gran depresión | 1925–1940 | Crisis financiera en la mayor economía, proteccionismo. | Desempleo masivo; radicalización. |
| Ascenso de un régimen expansionista | 1925–1945 | Humillación tras una guerra, crisis económica, movimiento de masas. | Rearme, agresiones, nueva guerra general. |
| Segunda guerra general | 1935–1950 | Régimen expansionista, potencias que no lo contienen a tiempo. | Destrucción masiva; nuevo orden mundial. |
| Partición tras la independencia | 1945–1950 | Colonia con identidades religiosas enfrentadas. | Nuevos Estados; migraciones y violencia. |
| Guerra de Corea o equivalente | 1945–1960 | País dividido entre bloques. | Guerra por delegación; frontera fortificada. |
| Crisis de los misiles | 1955–1970 | Despliegue de armas nucleares cerca de un rival. | Negociación o escalada nuclear. |
| Fin de un bloque | 1980–2000 | Estancamiento económico, reformas, movimientos nacionales. | Disolución; nuevos Estados. |
| Crisis financiera global | 1995–2030 | Burbujas, apalancamiento, interconexión. | Recesión mundial; rescates. |
| Pandemia global moderna | 2000–2040 | Movilidad masiva, zoonosis. | Cierres, vacunas rápidas, cambios sociales. |
| Ruptura de cadenas de suministro | 2010–2060 | Concentración de producción crítica, conflicto o desastre. | Escasez, relocalización industrial. |
| Puntos de inflexión climáticos | 2030–2060+ | Emisiones acumuladas elevadas. | Desastres más frecuentes, migraciones, conflictos. |

## Anexo R · Catálogo de tecnologías por época

Lista de trabajo del grafo tecnológico. Las ramas son las de la sección 14: Agricultura (AGR), Energía y materiales (ENE), Manufactura (MAN), Transporte y navegación (TRA), Comunicación e información (COM), Militar (MIL), Ciencias y medicina (CIE) e Instituciones y saber (INS). La época indica la ventana histórica aproximada; los prerrequisitos son orientativos.

### 1300–1500

| Tecnología | Rama | Prerrequisitos | Efecto principal |
| --- | --- | --- | --- |
| Rotación trienal | AGR | Arado pesado | Más cereal en tierras húmedas. |
| Regadío de norias y acequias | AGR | Carpintería, hidráulica | Agricultura intensiva en climas secos. |
| Molino de agua mejorado | ENE | Carpintería | Más harina y energía para batanes y forjas. |
| Molino de viento de pivote | ENE | Carpintería | Energía sin ríos. |
| Batán hidráulico | MAN | Molino de agua | Paño más barato. |
| Papel | COM | Contacto con productores | Administración y registros más baratos. |
| Contabilidad por partida doble | INS | Aritmética comercial, papel | Empresas y finanzas mejor gestionadas. |
| Letra de cambio | INS | Contabilidad, red de mercaderes | Comercio a distancia sin mover metal. |
| Seguro marítimo | INS | Letra de cambio | Menor riesgo comercial. |
| Brújula y portulanos | TRA | Navegación costera | Navegación invernal y en mar abierto. |
| Timón de codaste | TRA | Carpintería naval | Barcos mayores y más maniobrables. |
| Coca | TRA | Timón de codaste | Más carga. |
| Carraca | TRA | Coca, vela latina | Viajes largos. |
| Gafas | CIE | Vidrio de calidad | Prolonga la vida laboral de letrados y artesanos. |
| Reloj mecánico | MAN | Metalurgia fina | Organización del trabajo urbano. |
| Pólvora | MIL | Salitre, química práctica | Base de las armas de fuego. |
| Bombardas | MIL | Pólvora, fundición | Artillería de asedio temprana. |
| Artillería de bronce | MIL | Bombardas, metalurgia del cobre | Asedios rápidos. |
| Arcabuz | MIL | Pólvora, metalurgia | Infantería de fuego. |
| Armadura de placas | MIL | Metalurgia | Caballería e infantería más resistentes. |
| Alto horno | ENE | Energía hidráulica, metalurgia | Hierro barato. |
| Imprenta de tipos móviles | COM | Papel, metalurgia fina, prensas | Difusión del saber; presión religiosa. |
| Astrolabio náutico | TRA | Astronomía | Navegación oceánica. |
| Carabela | TRA | Carraca, vela latina | Exploración atlántica. |
| Universidad | INS | Clero letrado, ciudades | Capacidad científica e institucional. |
| Banca de depósito | INS | Letra de cambio | Crédito y préstamos al Estado. |
| Perspectiva lineal | CIE | Geometría | Arte, cartografía y arquitectura. |

### 1500–1750

| Tecnología | Rama | Prerrequisitos | Efecto principal |
| --- | --- | --- | --- |
| Cultivos americanos en Eurasia | AGR | Contacto transatlántico | Más calorías por hectárea (maíz, patata). |
| Nueva agricultura (forrajes, cercados) | AGR | Rotación trienal | Más ganado y productividad. |
| Galeón | TRA | Carraca, artillería naval | Guerra y comercio oceánico. |
| Artillería naval de costado | MIL | Artillería de bronce, galeón | Combate naval en línea. |
| Fortificación abaluartada | MIL | Artillería, geometría | Defensa contra artillería. |
| Mosquete | MIL | Arcabuz | Mayor alcance y potencia. |
| Llave de chispa | MIL | Metalurgia fina | Armas más fiables. |
| Bayoneta | MIL | Mosquete | Fin de las picas. |
| Proyección cartográfica | TRA | Matemáticas, astronomía | Navegación oceánica más segura. |
| Telescopio | CIE | Lentes | Astronomía, navegación. |
| Microscopio | CIE | Lentes | Biología. |
| Cálculo | CIE | Álgebra | Física y ingeniería. |
| Física mecánica | CIE | Cálculo, astronomía | Ingeniería y balística. |
| Banco público | INS | Banca de depósito | Deuda pública más barata. |
| Bolsa de valores | INS | Banca, compañías por acciones | Capital para grandes empresas. |
| Compañía por acciones | INS | Bolsa, seguros | Compañías comerciales. |
| Correo postal regular | COM | Caminos, administración | Mayor alcance del Estado. |
| Prensa periódica | COM | Imprenta, correo | Opinión pública temprana. |
| Canal con esclusas | TRA | Hidráulica | Transporte interior barato. |
| Bomba de vapor atmosférica | ENE | Física, metalurgia | Desagüe de minas. |
| Medición de la longitud | TRA | Relojería de precisión | Navegación precisa. |
| Inoculación | CIE | Observación médica | Menor mortalidad por viruela. |

### 1750–1914

| Tecnología | Rama | Prerrequisitos | Efecto principal |
| --- | --- | --- | --- |
| Máquina de vapor de Watt | ENE | Bomba de vapor, metalurgia | Energía para fábricas. |
| Hiladora mecánica | MAN | Mecánica | Hilo barato. |
| Telar mecánico | MAN | Hiladora, vapor | Tejidos industriales. |
| Fundición con coque | ENE | Carbón | Hierro barato en masa. |
| Pudelado | ENE | Coque | Hierro forjado industrial. |
| Máquinas herramienta | MAN | Metalurgia de precisión | Piezas intercambiables. |
| Ferrocarril | TRA | Vapor, hierro | Transporte terrestre masivo. |
| Barco de vapor | TRA | Vapor | Navegación independiente del viento. |
| Hélice | TRA | Barco de vapor | Barcos oceánicos de vapor. |
| Telégrafo | COM | Electricidad básica | Comunicación instantánea. |
| Cable submarino | COM | Telégrafo, gutapercha | Comunicación intercontinental. |
| Fotografía | COM | Química | Prensa ilustrada, cartografía. |
| Vacunación | CIE | Inoculación | Fin de las epidemias de viruela. |
| Anestesia | CIE | Química | Cirugía moderna. |
| Teoría microbiana | CIE | Microscopio | Saneamiento, antisepsia. |
| Saneamiento urbano | CIE | Teoría microbiana, ingeniería | Menor mortalidad urbana. |
| Fertilizantes químicos | AGR | Química | Más rendimiento agrícola. |
| Acero Bessemer | ENE | Coque | Acero barato. |
| Dinamo | ENE | Electromagnetismo | Electricidad industrial. |
| Bombilla eléctrica | ENE | Dinamo | Iluminación. |
| Motor de combustión interna | ENE | Petróleo, metalurgia | Automóvil, tractor. |
| Teléfono | COM | Electricidad | Comunicación de voz. |
| Refrigeración | MAN | Termodinámica | Conservación y comercio de alimentos. |
| Fusil de retrocarga | MIL | Metalurgia de precisión | Fuego rápido. |
| Ametralladora | MIL | Fusil de retrocarga | Defensa dominante. |
| Artillería de retrocarga | MIL | Acero | Artillería moderna. |
| Acorazado | MIL | Acero, vapor | Dominio naval. |
| Pólvora sin humo | MIL | Química | Mayor alcance y ocultación. |
| Estadística oficial | INS | Censo, burocracia | Mejor capacidad del Estado. |
| Sociedad anónima moderna | INS | Bolsa | Grandes empresas industriales. |

### 1914–1991

| Tecnología | Rama | Prerrequisitos | Efecto principal |
| --- | --- | --- | --- |
| Tanque | MIL | Motor de combustión, acero | Ruptura de frentes. |
| Avión militar | MIL | Motor de combustión | Reconocimiento y combate aéreo. |
| Portaaviones | MIL | Aviación, acero | Proyección aérea naval. |
| Submarino moderno | MIL | Motor diésel, baterías | Guerra comercial. |
| Radio | COM | Electromagnetismo | Comunicación de masas y militar. |
| Radar | MIL | Radio | Defensa aérea. |
| Motor a reacción | TRA | Aerodinámica, metalurgia | Aviación rápida. |
| Cohetes | MIL | Química, aerodinámica | Misiles y espacio. |
| Antibióticos | CIE | Microbiología | Menor mortalidad por infecciones. |
| Síntesis de amoníaco | AGR | Química | Fertilizantes y explosivos en masa. |
| Plásticos | MAN | Petroquímica | Consumo e industria. |
| Cadena de montaje | MAN | Máquinas herramienta | Producción en masa. |
| Fisión nuclear | CIE | Física atómica | Armas y energía nuclear. |
| Energía nuclear civil | ENE | Fisión | Electricidad sin carbón. |
| Computadora electrónica | COM | Electrónica | Cálculo y criptografía. |
| Transistor | COM | Física del estado sólido | Electrónica barata. |
| Circuito integrado | COM | Transistor | Computación masiva. |
| Satélite artificial | COM | Cohetes | Comunicaciones, observación. |
| Televisión | COM | Radio, electrónica | Opinión pública de masas. |
| Revolución verde | AGR | Fertilizantes, genética vegetal | Menos hambrunas. |
| Contenedor marítimo | TRA | Logística | Comercio global barato. |
| Anticonceptivos modernos | CIE | Química médica | Transición demográfica más rápida. |
| Misil balístico | MIL | Cohetes, guía inercial | Disuasión. |
| Computadora personal | COM | Microprocesador | Productividad de oficina. |
| Redes de computadoras | COM | Computadora, telecomunicaciones | Base de internet. |

### 1991–2060

| Tecnología | Rama | Prerrequisitos | Efecto principal |
| --- | --- | --- | --- |
| Internet comercial | COM | Redes | Comercio y comunicación globales. |
| Telefonía móvil | COM | Electrónica, satélites | Conectividad universal. |
| Teléfono inteligente | COM | Telefonía móvil, microprocesador | Servicios digitales masivos. |
| Computación en la nube | COM | Internet, centros de datos | Servicios escalables. |
| Energía solar barata | ENE | Semiconductores | Electricidad renovable. |
| Energía eólica marina | ENE | Materiales compuestos | Electricidad renovable. |
| Baterías de litio | ENE | Química de materiales | Vehículos eléctricos, almacenamiento. |
| Vehículo eléctrico | TRA | Baterías | Transporte sin combustibles fósiles. |
| Secuenciación genómica barata | CIE | Biotecnología, computación | Medicina personalizada. |
| Edición genética | CIE | Secuenciación | Terapias y agricultura. |
| Vacunas de ARN | CIE | Biotecnología | Respuesta rápida a pandemias. |
| Inteligencia artificial | COM | Computación masiva, datos | Automatización de tareas cognitivas. |
| Robótica avanzada | MAN | IA, sensores | Automatización industrial y de servicios. |
| Drones | MIL | Electrónica, baterías | Reconocimiento y ataque baratos. |
| Satélites de órbita baja en constelación | COM | Lanzamiento barato | Conectividad global. |
| Lanzadores reutilizables | TRA | Cohetes | Acceso barato al espacio. |
| Almacenamiento energético masivo | ENE | Baterías, redes | Estabilidad de redes renovables. |
| Hidrógeno verde | ENE | Electrólisis, renovables | Descarbonización industrial. |
| Captura de carbono | ENE | Química, energía barata | Mitigación climática. |
| Fusión experimental | ENE | Física de plasma, superconductores | Camino hacia la fusión comercial. |

### Después de 2060 (diseñadas, conservadoras)

| Tecnología | Rama | Prerrequisitos | Efecto principal |
| --- | --- | --- | --- |
| Fusión comercial | ENE | Fusión experimental, materiales | Energía abundante. |
| Redes continentales superconductoras | ENE | Superconductores | Menos pérdidas, energía compartida. |
| Terapias génicas generalizadas | CIE | Edición genética | Mayor esperanza de vida sana. |
| Automatización general de servicios | MAN | IA, robótica | Cambio profundo en el empleo. |
| Minería espacial | TRA | Lanzadores reutilizables, robótica | Metales raros. |
| Estaciones orbitales permanentes | TRA | Lanzadores reutilizables | Industria espacial. |
| Geoingeniería solar | ENE | Climatología, aviación | Enfriamiento con riesgos internacionales. |
| Agricultura vertical a gran escala | AGR | Energía barata, robótica | Alimentos con menos tierra. |

## Anexo S · Entidades de las expansiones mundiales

Fichas breves de las entidades principales de las expansiones posteriores (Anexo H). En estas regiones el diseño debe aportar **sistemas propios** (tributo, redes de intercambio, calendarios, formas de guerra y de legitimidad) y no versiones empobrecidas de los europeos.

### Asia central, Irán e India (en torno a 1300)

| Entidad | Capital | Gobernante | Estilo | Reto | Oportunidad |
| --- | --- | --- | --- | --- | --- |
| Kanato de Chagatai | Almalik (corte nómada) | Duwa | Kanato nómada | Guerras con Yuan e Iljanato | Ruta de la seda |
| Kanato ogodeí | Corte nómada | Kaidu (muere en 1301) | Kanato en guerra | Absorción por Chagatai | Liderazgo de la estepa |
| Kartíes de Herat | Herat | Dinastía kartí | Vasallo urbano | Iljanato | Reconstrucción de Jorasán |
| Sultanato de Delhi | Delhi | Alauddin Khalji | Sultanato militar | Invasiones mongolas | Conquista del Decán |
| Kakatiya | Warangal | Prataparudra | Reino hindú | Expediciones de Delhi | Comercio del golfo de Bengala |
| Yadava | Devagiri | Ramachandra | Reino del Decán | Delhi | Riqueza agrícola |
| Hoysala | Dwarasamudra | Ballala III | Reino del sur | Delhi, Pandya | Templos y comercio |
| Pandya | Madurai | Maravarman Kulasekara I | Reino tamil | Disputas sucesorias | Comercio con el mundo árabe |
| Ganga orientales | Orissa | Dinastía ganga | Reino costero | Delhi y Bengala | Comercio marítimo |
| Reino ahom | Valle del Brahmaputra | Dinastía ahom | Reino montañés | Vecinos | Aislamiento defensivo |

### Asia oriental y sudeste asiático

| Entidad | Capital | Gobernante | Estilo | Reto | Oportunidad |
| --- | --- | --- | --- | --- | --- |
| Dinastía Yuan | Dadu (Pekín) | Temür Kan | Imperio burocrático-mongol | Tensiones entre élite mongola y población han | Mayor economía del mundo |
| Goryeo | Kaesong | Chungnyeol | Monarquía vasalla | Injerencia Yuan | Autonomía futura |
| Japón (Kamakura) | Kamakura / Kioto | Regencia Hōjō | Shogunato | Deuda tras las invasiones mongolas | Comercio con China |
| Đại Việt | Thăng Long | Trần Anh Tông | Monarquía | Champa | Expansión hacia el sur |
| Champa | Vijaya | Jaya Sinhavarman III | Reinos marítimos | Đại Việt | Comercio marítimo |
| Imperio jemer | Angkor | Indravarman III | Monarquía | Declive y presión tai | Herencia monumental |
| Sukhothai | Sukhothai | Loe Thai | Reino tai | Vasallos que se separan | Budismo theravada |
| Lan Na | Chiang Mai | Mangrai | Reino tai | Vecinos | Comercio interior |
| Majapahit | Trowulan | Kertarajasa | Reino javanés | Consolidación | Talasocracia del archipiélago |
| Samudera Pasai | Pasai | Sultanes | Sultanato portuario | Vecinos javaneses | Comercio y difusión del islam |

### África

| Entidad | Capital | Gobernante | Estilo | Reto | Oportunidad |
| --- | --- | --- | --- | --- | --- |
| Imperio de Malí | Niani (tradicional) | Mansa (a confirmar) | Imperio del oro | Sucesiones | Comercio transahariano, peregrinación |
| Kanem | Njimi | Mai | Imperio saheliano | Nómadas y rivales | Rutas hacia Libia y Egipto |
| Ciudades hausa | Kano, Katsina | Reyes urbanos | Ciudades-Estado | Vecinos mayores | Artesanía y comercio |
| Reino de Benín | Edo | Oba | Monarquía urbana | Vecinos | Arte y comercio regional |
| Ifé | Ifé | Ooni | Centro religioso yoruba | Ascenso de Oyo | Prestigio ritual |
| Etiopía salomónica | Corte itinerante | Wedem Arad | Imperio cristiano | Sultanatos musulmanes | Expansión hacia el sur |
| Sultanato de Ifat | Ifat | Dinastía walashma | Sultanato | Etiopía | Comercio con el mar Rojo |
| Kilwa | Kilwa Kisiwani | Sultanes | Ciudad-Estado swahili | Rivales costeros | Oro de Zimbabue |
| Mogadiscio | Mogadiscio | Sultanes | Ciudad-Estado | Vecinos | Comercio índico |
| Gran Zimbabue | Gran Zimbabue | Reyes shona | Reino | Agotamiento de recursos | Oro y ganado |

### Américas

| Entidad | Centro | Situación | Sistemas propios a diseñar |
| --- | --- | --- | --- |
| Azcapotzalco (tepanecas) | Cuenca de México | Potencia dominante emergente | Tributo, alianzas matrimoniales, mercados regionales. |
| Culhuacán | Cuenca de México | Prestigio tolteca | Legitimidad por linaje. |
| Texcoco (acolhuas) | Cuenca de México | Señorío en ascenso | Leyes y poesía cortesana. |
| Grupo mexica | Cuenca de México | Pueblo migrante sin tierra propia | Mercenariado, fundación de ciudad. |
| Tlaxcallan | Altiplano oriental | Confederación de señoríos | Gobierno colegiado, guerra ritual. |
| Purépecha | Pátzcuaro | Señoríos en unificación | Metalurgia del cobre, Estado centralizado. |
| Mayapán | Yucatán | Liga política | Comercio marítimo de sal, cacao y algodón. |
| Reinos de los altos de Guatemala | Altos | K'iche' y vecinos | Guerra y alianzas entre linajes. |
| Chimú | Chan Chan | Reino costero | Grandes obras de irrigación; metalurgia. |
| Cusco | Cusco | Señorío local | Reciprocidad, trabajo por turnos, caminos. |
| Reinos aymaras | Altiplano | Lupaca, Colla | Ganadería de camélidos, archipiélagos verticales. |
| Muiscas | Altiplano colombiano | Zipa y zaque | Sal, oro, mercados. |
| Cahokia y misisipianos | Valle del Misisipi | Cacicazgos en declive | Montículos, maíz, redes de intercambio. |
| Pueblos ancestrales | Suroeste | Migraciones por sequía | Agricultura de secano, asentamientos en altura. |

## Anexo T · Plan de pruebas por sistema

Casos de prueba mínimos que el rol QA debe mantener. Cada fila se convierte en una o varias pruebas automáticas; los escenarios dorados viven en `tests/golden/`.

### Núcleo y determinismo

| ID | Caso | Tipo | Resultado esperado |
| --- | --- | --- | --- |
| QA-CORE-01 | Ejecutar 300 años vacíos dos veces con la misma semilla. | Dorado | Misma secuencia de hashes. |
| QA-CORE-02 | Ejecutar con 1, 4 y 16 hilos. | Dorado | Mismo hash final. |
| QA-CORE-03 | Guardar en el año 50, cargar y continuar hasta el 100. | Dorado | Mismo hash que sin interrupción. |
| QA-CORE-04 | Reproducir una partida desde semilla y diario de comandos. | Dorado | Estado idéntico en cada tick registrado. |
| QA-CORE-05 | Conversión juliana/gregoriana en fechas límite (1582, años bisiestos). | Unitaria | Fechas correctas. |
| QA-CORE-06 | Escalonamiento: cada entidad procesada exactamente una vez al mes. | Propiedad | Ninguna omitida ni repetida. |
| QA-CORE-07 | Migración de un guardado de la versión anterior. | Integración | Carga sin pérdida de datos. |

### Economía

| ID | Caso | Tipo | Resultado esperado |
| --- | --- | --- | --- |
| QA-ECO-01 | Conservación de bienes con producción, consumo y comercio aleatorios. | Propiedad | Existencias cuadran siempre. |
| QA-ECO-02 | Conservación del dinero sin acuñación. | Propiedad | Masa monetaria constante. |
| QA-ECO-03 | Límites de precio ante shocks extremos de oferta. | Propiedad | Nunca fuera de ±10 % semanal ni de 0,2–10 × base. |
| QA-ECO-04 | Producción con un insumo ausente. | Unitaria | Producción cero y causa registrada. |
| QA-ECO-05 | Comercio con ruta bloqueada. | Unitaria | Flujo cero; precios divergen. |
| QA-ECO-06 | Impago de deuda. | Integración | Acreedores pierden exactamente lo adeudado. |
| QA-ECO-07 | 100 años de economía de referencia. | Dorado | Hash estable; precios en rango. |

### Población y sociedad

| ID | Caso | Tipo | Resultado esperado |
| --- | --- | --- | --- |
| QA-POP-01 | Conservación de población con nacimientos, muertes y migración. | Propiedad | Totales cuadran. |
| QA-POP-02 | Hambruna simulada (cobertura del 60 % durante un año). | Integración | Mortalidad y emigración suben de forma visible. |
| QA-POP-03 | Fusión de cohortes durante 300 años. | Integración | Número de cohortes por provincia acotado. |
| QA-POP-04 | Asimilación en ambos sentidos. | Unitaria | Una élite minoritaria puede asimilarse a la mayoría. |

### Política y diplomacia

| ID | Caso | Tipo | Resultado esperado |
| --- | --- | --- | --- |
| QA-POL-01 | 10.000 cambios aleatorios de frontera. | Propiedad | Ninguna provincia sin dueño ni con dos dueños. |
| QA-POL-02 | Extinción de dinastía. | Integración | Se abre una crisis sucesoria con pretendientes válidos. |
| QA-POL-03 | Rebelión que triunfa. | Integración | Cambian leyes o régimen según el programa del bando. |
| QA-DIP-01 | Tratado con cláusulas contradictorias. | Unitaria | El validador lo rechaza. |
| QA-DIP-02 | Coalición frente a un país agresivo. | Lab | La coalición se forma en un porcentaje medible de campañas. |

### Guerra

| ID | Caso | Tipo | Resultado esperado |
| --- | --- | --- | --- |
| QA-WAR-01 | Batalla con fuerzas idénticas. | Propiedad | Resultado simétrico salvo por la aleatoriedad acotada. |
| QA-WAR-02 | Asedio sin artillería ni bloqueo a ciudad costera abastecida. | Unitaria | El asedio no progresa; la interfaz lo explica. |
| QA-WAR-03 | Ejército mayor que la capacidad de suministro. | Unitaria | Desgaste según la fórmula. |
| QA-WAR-04 | 100 campañas de IA. | Lab | Todas las guerras terminan en estados válidos. |

### Historia, tecnología y epidemias

| ID | Caso | Tipo | Resultado esperado |
| --- | --- | --- | --- |
| QA-HIS-01 | Situación con caducidad tras divergencia. | Unitaria | La situación se transforma o desaparece. |
| QA-HIS-02 | Distribuciones de situaciones clave. | Lab | Dentro de los rangos del Anexo F. |
| QA-SCI-01 | Investigar una tecnología sin prerrequisitos. | Unitaria | Bloqueada con explicación. |
| QA-SCI-02 | Adelanto mayor que el límite. | Unitaria | Coste infinito; no se descubre. |
| QA-EPI-01 | Cuarentena total de una provincia. | Unitaria | Sin importación de casos; comercio reducido. |

### Interfaz y contenido

| ID | Caso | Tipo | Resultado esperado |
| --- | --- | --- | --- |
| QA-UX-01 | Toda variable visible tiene explicación en el ledger. | Integración | Ninguna variable sin contribuciones. |
| QA-UX-02 | Textos sin traducción. | Validación | Cero en español e inglés. |
| QA-UX-03 | Modos de mapa con daltonismo simulado. | Manual | Información distinguible sin color. |
| QA-DAT-01 | Referencias rotas en datos. | Validación | Cero. |
| QA-DAT-02 | Datos A/B sin fuente. | Validación | Cero. |

## Anexo U · Glosario histórico

Términos de época que aparecen en el documento o en el contenido. Las definiciones son breves y orientadas al diseño; la enciclopedia del juego las ampliará con fuentes.

| Término | Definición |
| --- | --- |
| Ayllu | Unidad social andina basada en el parentesco y la reciprocidad. |
| Bey / beylik | Señor turco y su principado. |
| Boyardo | Noble de alto rango en la Rus, Bulgaria y los principados rumanos. |
| Calpulli | Unidad territorial y social nahua con tierras comunales. |
| Casus belli | Motivo que justifica una guerra. |
| Condotiero | Jefe de una compañía mercenaria contratada por Estados italianos. |
| Despotado | Principado bizantino o posbizantino gobernado por un déspota (título de alta dignidad). |
| Dieta | Asamblea de estamentos en Europa central. |
| Dux | Jefe de Estado electo de Venecia y Génova. |
| Encomienda | Concesión de tierras o personas a cambio de servicios (en órdenes militares y, más tarde, en América). |
| Estamento | Orden social con derechos propios (nobleza, clero, ciudades, campesinos). |
| *Fondaco* | Edificio de mercaderes extranjeros que servía de almacén, residencia y oficina. |
| Fuero | Conjunto de privilegios y normas propias de una ciudad o territorio. |
| Gazi | Guerrero de frontera en el mundo islámico. |
| Hiperpirón | Moneda de oro bizantina, devaluada progresivamente. |
| *Iqta* | Concesión revocable de rentas a cambio de servicio militar en el mundo islámico. |
| Jenízaros | Infantería profesional otomana reclutada mediante levas de niños cristianos. |
| Kan / kanato | Gobernante mongol o túrquico y su Estado. |
| Mamelucos | Soldados de origen esclavo que formaron una élite militar gobernante. |
| Mansa | Título del soberano de Malí. |
| *Millet* | Comunidad religiosa con autonomía jurídica en el Imperio otomano. |
| Oba | Título del rey de Benín. |
| Oligarca | En Hungría, gran noble que controlaba regiones casi como soberano. |
| *Pronoia* | Concesión bizantina de rentas fiscales a cambio de servicio militar. |
| Señorío | Dominio territorial con poderes sobre tierras y personas. |
| Serrata | Cierre del Gran Consejo de Venecia a un grupo fijo de familias (1297). |
| Sultanato | Estado gobernado por un sultán. |
| Tanistry | Sucesión gaélica en la que se elige al heredero entre los parientes. |
| *Timar* | Concesión otomana de rentas a un jinete a cambio de servicio. |
| Tributo | Pago periódico de un territorio subordinado a una potencia. |
| *Veche* | Asamblea popular de Nóvgorod y Pskov. |
| Voivoda | Señor militar y gobernador en los Balcanes y Europa oriental. |
| Zaque y zipa | Gobernantes de las dos grandes confederaciones muiscas. |

## Anexo V · Bibliografía de trabajo

Obras de referencia para iniciar la Biblia histórica de la vertical y de la primera expansión. Es una lista de partida: cada dato del juego debe citar la obra concreta que lo respalda, y la lista se ampliará con fuentes regionales y en otros idiomas.

| Tema | Obra |
| --- | --- |
| Bizancio | George Ostrogorsky, *History of the Byzantine State*. |
| Bizancio tardío | Donald M. Nicol, *The Last Centuries of Byzantium, 1261–1453*. |
| Política de Andrónico II | Angeliki E. Laiou, *Constantinople and the Latins: The Foreign Policy of Andronicus II*. |
| Caída de Constantinopla | Steven Runciman, *The Fall of Constantinople 1453*. |
| Origen otomano | Cemal Kafadar, *Between Two Worlds: The Construction of the Ottoman State*. |
| Imperio otomano clásico | Halil İnalcık, *The Ottoman Empire: The Classical Age 1300–1600*. |
| Balcanes medievales | John V. A. Fine Jr., *The Late Medieval Balkans*. |
| Venecia | Frederic C. Lane, *Venice: A Maritime Republic*. |
| Hungría medieval | Pál Engel, *The Realm of St Stephen: A History of Medieval Hungary*. |
| Cruzadas tardías y Levante | Kenneth M. Setton, *The Papacy and the Levant (1204–1571)*. |
| Mongoles y Occidente | Peter Jackson, *The Mongols and the West*. |
| Sistema mundial antes de 1500 | Janet L. Abu-Lughod, *Before European Hegemony: The World System A.D. 1250–1350*. |
| Peste negra | Ole J. Benedictow, *The Black Death 1346–1353: The Complete History*. |
| Mediterráneo | David Abulafia, *The Great Sea: A Human History of the Mediterranean*. |

Antes de citar una obra en el juego hay que confirmar la edición utilizada y las páginas concretas.

## Anexo W · Ejemplo completo de una tarea resuelta por un agente

Este anexo muestra, de principio a fin, cómo debe trabajar un agente en `101-engine` con una tarea real del backlog (T-205, ajuste semanal de precios). El código es **ilustrativo**: las firmas exactas dependerán de los ADR de tipos y de almacenamiento, pero la forma de trabajar es la que se espera.

### 1. La tarea (issue)

~~~~markdown
## Objetivo
Implementar el ajuste semanal de precios con amortiguación y límite de cambio.

## Rol
role:sim

## Contexto
- Documento maestro: sección 10, "Precios".
- ADR 0003 (tipos de punto fijo), ADR 0011 (contrato Market/Good/Price).

## Archivos permitidos
- crates/e101-sim/src/economy/prices.rs
- crates/e101-sim/src/economy/mod.rs (solo para registrar el sistema)
- crates/e101-sim/tests/prices.rs
- tests/golden/economy_basic/

## Interfaz
fn run(state: &State, deltas: &mut Deltas)

## Criterios de aceptación
- [ ] El precio nunca cambia más de ±10 % por semana.
- [ ] El precio nunca sale del rango 0,2–10 veces el precio base.
- [ ] Cada cambio registra en el ledger sus contribuyentes (oferta y demanda).
- [ ] Sin flotantes; orden de iteración estable.

## Pruebas requeridas
- [ ] Prueba de propiedad para los límites.
- [ ] Escenario dorado de 50 años con hash estable.

## Fuera de alcance
Comercio entre mercados (T-207).
~~~~

### 2. Primera entrada del diario

~~~~markdown
# Diario de la tarea T-205 — Ajuste semanal de precios

- Rol: sim
- Rama: agent/sim/T-205-weekly-prices

## Plan
1. Leer AGENTS.md, CONTEXT.md de e101-sim y e101-store, sección 10 y ADR 0003/0011.
2. Escribir una función pura `adjust(price, base, supply, demand) -> Money`.
3. Escribir pruebas de propiedad para `adjust` antes de conectarla al sistema.
4. Implementar `run` iterando mercados y bienes por ID en orden.
5. Registrar contribuciones de oferta y demanda en el ledger.
6. Añadir el escenario dorado economy_basic de 50 años.
7. Ejecutar check, golden y bench.

## Decisiones
| Decisión | Motivo | Alternativas descartadas |
| --- | --- | --- |
| Separar `adjust` como función pura | Probarla sin construir un State completo | Probar solo a través de `run` |
| Oferta mínima de 1 unidad en el denominador | Evitar división por cero cuando la oferta es nula | Precio máximo directo si oferta = 0 |
~~~~

### 3. Código

```rust
//! Weekly price adjustment. See master document §10 ("Precios").
//!
//! price(t+1) = price(t) × (1 + clamp(k × imbalance, −x, +x)),
//! bounded to [0.2, 10] × base price.

use e101_ledger::{Contribution, Origin};
use e101_store::fixed::{Money, Qty, Ratio};
use e101_store::{GoodId, MarketId, State};

use crate::deltas::Deltas;

/// Damping factor k = 0.10.
pub const DAMPING: Ratio = Ratio::from_basis_points(1_000);
/// Maximum weekly change x = ±10 %.
pub const MAX_STEP: Ratio = Ratio::from_basis_points(1_000);
/// Lower bound: 0.2 × base price.
pub const MIN_FACTOR: Ratio = Ratio::from_basis_points(2_000);
/// Upper bound: 10 × base price.
pub const MAX_FACTOR: Ratio = Ratio::from_basis_points(100_000);

/// Pure price update. Deterministic and side-effect free.
pub fn adjust(price: Money, base: Money, supply: Qty, demand: Qty) -> Money {
    let denominator = supply.max(Qty::ONE);
    let imbalance = Ratio::from_quotient(demand - supply, denominator);
    let step = (imbalance * DAMPING).clamp(-MAX_STEP, MAX_STEP);
    let raw = price.scale(Ratio::ONE + step);
    raw.clamp(base.scale(MIN_FACTOR), base.scale(MAX_FACTOR))
}

/// System entry point. Reads state, writes only deltas.
pub fn run(state: &State, deltas: &mut Deltas) {
    let today = state.time.today();
    for market in state.markets.ids() {
        // Staggered: each market updates on its own weekday.
        if !state.time.is_weekly_slot(market.stagger_key(), today) {
            continue;
        }
        for good in state.goods.ids() {
            update_one(state, deltas, market, good);
        }
    }
}

fn update_one(state: &State, deltas: &mut Deltas, market: MarketId, good: GoodId) {
    let supply = state.economy.supply(market, good);
    let demand = state.economy.demand(market, good);
    let price = state.economy.price(market, good);
    let base = state.goods.base_price(good);

    let new_price = adjust(price, base, supply, demand);
    if new_price == price {
        return;
    }

    deltas.economy.set_price(market, good, new_price);
    deltas.ledger.record(
        state.ledger_key_price(market, good),
        [
            Contribution::new(Origin::Supply { market, good }, supply.into()),
            Contribution::new(Origin::Demand { market, good }, demand.into()),
        ],
    );
}
```

### 4. Pruebas

```rust
use e101_sim::economy::prices::{adjust, MAX_FACTOR, MIN_FACTOR};
use e101_store::fixed::{Money, Qty, Ratio};
use proptest::prelude::*;

proptest! {
    #[test]
    fn weekly_change_is_bounded(
        price in 1_000i64..10_000_000,
        supply in 0i64..1_000_000,
        demand in 0i64..1_000_000,
    ) {
        let base = Money::from_raw(price);
        let p = Money::from_raw(price);
        let next = adjust(p, base, Qty::from_raw(supply), Qty::from_raw(demand));
        let upper = p.scale(Ratio::from_basis_points(11_000));
        let lower = p.scale(Ratio::from_basis_points(9_000));
        prop_assert!(next <= upper && next >= lower);
    }

    #[test]
    fn price_stays_within_base_band(
        base in 1_000i64..1_000_000,
        factor_bp in 1_000i64..200_000,
        supply in 0i64..1_000_000,
        demand in 0i64..1_000_000,
    ) {
        let base = Money::from_raw(base);
        let p = base.scale(Ratio::from_basis_points(factor_bp));
        let next = adjust(p, base, Qty::from_raw(supply), Qty::from_raw(demand));
        prop_assert!(next >= base.scale(MIN_FACTOR) && next <= base.scale(MAX_FACTOR));
    }
}

#[test]
fn balanced_market_keeps_price() {
    let base = Money::from_units(10);
    let next = adjust(base, base, Qty::from_units(500), Qty::from_units(500));
    assert_eq!(next, base);
}
```

### 5. Verificación local

```text
$ cargo xtask check
fmt ............ ok
clippy ......... ok
determinism .... ok   (no floats, no HashMap iteration in sim crates)
dep-graph ...... ok
tests .......... ok   (e101-sim: 148 passed)

$ cargo xtask golden
economy_basic (50y) ... new scenario, hash recorded (requires golden-change)
empty_300y ............ ok

$ cargo xtask bench
economy/prices ........ 0.41 ms/tick (budget 1.0 ms)  ok
```

*(Salida ilustrativa.)*

### 6. Pull request

~~~~markdown
## Resumen
Añade el sistema de ajuste semanal de precios con amortiguación (k = 0,10),
límite de cambio (±10 %) y banda de 0,2–10 × precio base. Registra oferta y
demanda como contribuciones en el ledger.

## Tarea y diario
- Tarea: #205
- Diario: docs/agents/journal/T-205.md
- Rol: sim

## Verificación
- [x] cargo xtask check
- [x] cargo xtask golden — nuevo escenario economy_basic (etiqueta golden-change)
- [x] cargo xtask bench — 0,41 ms/tick, dentro del presupuesto

## Determinismo y contabilidad
- [x] Sin f32/f64
- [x] Sin iteración de HashMap
- [x] Cambios visibles registrados en el ledger

## No incluido / pendiente
- El comercio entre mercados (T-207) aún no reduce las diferencias de precio.
- Las contribuciones de “sequía” o “bloqueo” llegarán cuando existan esos sistemas;
  por ahora el ledger solo distingue oferta y demanda.
~~~~

### 7. Revisión

| Revisor | Comentario | Respuesta del agente |
| --- | --- | --- |
| Arquitectura | `Qty::ONE` como mínimo de oferta debe estar documentado en el ADR 0011. | Añadida nota en el ADR (permitido por la tarea tras confirmación). |
| QA | Falta un caso con oferta cero y demanda alta. | Añadida prueba `zero_supply_hits_upper_step`. |
| Persona responsable | Aprobado el nuevo escenario dorado. | Etiqueta `golden-change` aprobada; hash registrado. |

### 8. Lo que este ejemplo enseña

- El agente **planifica antes de programar** y deja rastro de sus decisiones.
- La lógica difícil se aísla en **funciones puras** fáciles de probar.
- El sistema **no escribe en el estado**: solo produce deltas.
- Las pruebas de propiedad expresan los **criterios de aceptación** literalmente.
- El PR dice con claridad **qué no está hecho**.

## Anexo X · Referencia de la interfaz del núcleo (borrador)

Borrador de los tipos y funciones públicos del núcleo de 101 Engine. Sirve para que Arquitectura redacte los primeros ADR y para que los agentes entiendan la forma del código antes de que exista. **Todo es provisional** hasta que los ADR correspondientes se acepten.

### Tiempo (`e101-time`)

```rust
/// Absolute day number since the engine epoch (proleptic Gregorian).
#[derive(Copy, Clone, Debug, PartialEq, Eq, PartialOrd, Ord, Hash)]
pub struct Day(pub i32);

pub enum CalendarKind { Gregorian, Julian, Hijri, Byzantine }

pub struct DisplayDate { pub year: i32, pub month: u8, pub day: u8, pub calendar: CalendarKind }

impl Day {
    pub fn from_gregorian(year: i32, month: u8, day: u8) -> Day;
    pub fn from_julian(year: i32, month: u8, day: u8) -> Day;
    pub fn to_display(self, calendar: CalendarKind) -> DisplayDate;
    pub fn weekday(self) -> u8;
}

/// Staggering: which day of the period an entity is processed.
pub trait StaggerKey { fn stagger_key(&self) -> u64; }
pub fn is_monthly_slot(key: u64, today: Day) -> bool;
pub fn is_weekly_slot(key: u64, today: Day) -> bool;
```

### Punto fijo e identificadores (`e101-store`)

```rust
/// Money in the smallest accounting unit (1/10_000 of a unit).
#[derive(Copy, Clone, Debug, PartialEq, Eq, PartialOrd, Ord)]
pub struct Money(i64);

/// Physical quantity (goods, people) with 3 implied decimals.
#[derive(Copy, Clone, Debug, PartialEq, Eq, PartialOrd, Ord)]
pub struct Qty(i64);

/// Dimensionless ratio in basis points (10_000 = 1.0).
#[derive(Copy, Clone, Debug, PartialEq, Eq, PartialOrd, Ord)]
pub struct Ratio(i32);

impl Money {
    pub const ZERO: Money;
    pub fn from_units(units: i64) -> Money;
    pub fn from_raw(raw: i64) -> Money;
    pub fn scale(self, r: Ratio) -> Money;          // rounds half to even
    pub fn checked_add(self, other: Money) -> Option<Money>;
}

impl Ratio {
    pub const ONE: Ratio;
    pub const fn from_basis_points(bp: i32) -> Ratio;
    pub fn from_quotient(num: Qty, den: Qty) -> Ratio; // saturating
}

/// Typed, stable identifier. Index into SoA tables.
pub struct Id<T> { index: u32, _marker: PhantomData<T> }

pub type ProvinceId = Id<Province>;
pub type EntityId   = Id<PoliticalEntity>;
pub type MarketId   = Id<Market>;
pub type GoodId     = Id<Good>;
pub type CohortId   = Id<Cohort>;   // backed by a generational slotmap
pub type ArmyId     = Id<Army>;     // backed by a generational slotmap
```

### Estado y vistas

```rust
/// Full simulation state. Only `apply` gets `&mut State`.
pub struct State {
    pub time: TimeState,
    pub map: MapTables,
    pub entities: EntityTables,
    pub population: CohortTables,
    pub economy: EconomyTables,
    pub politics: PoliticsTables,
    pub military: MilitaryTables,
    pub history: HistoryTables,
    pub ledger: Ledger,
}

/// Read-only snapshot for the client, AI and Lab.
pub struct View<'a> { state: &'a State }

impl<'a> View<'a> {
    pub fn province(&self, id: ProvinceId) -> ProvinceView<'a>;
    pub fn why(&self, key: LedgerKey) -> Explanation;
    pub fn entity(&self, id: EntityId) -> EntityView<'a>;
}
```

### Comandos y deltas (`e101-commands`, `e101-sim`)

```rust
/// Every external input to the simulation.
pub enum Command {
    SetLaw { entity: EntityId, category: LawCategory, option: LawOptionId },
    SetBudget { entity: EntityId, line: BudgetLine, amount: Money },
    MoveArmy { army: ArmyId, path: Vec<ProvinceId> },
    ProposeTreaty { from: EntityId, to: EntityId, clauses: Vec<Clause> },
    ChooseEventOption { event: EventInstanceId, option: u8 },
    // …
}

pub struct StampedCommand { pub day: Day, pub issuer: Issuer, pub seq: u32, pub command: Command }

/// Changes produced by systems during the read phase.
pub struct Deltas {
    pub economy: EconomyDeltas,
    pub population: PopulationDeltas,
    pub politics: PoliticsDeltas,
    pub military: MilitaryDeltas,
    pub ledger: LedgerDeltas,
}

/// A simulation system.
pub trait System: Send + Sync {
    fn name(&self) -> &'static str;
    fn run(&self, state: &State, deltas: &mut Deltas);
}

/// Merge per-thread deltas in stable key order, then apply.
pub fn apply(state: &mut State, deltas: Vec<Deltas>) -> Result<(), InvariantViolation>;
```

### Registro causal (`e101-ledger`)

```rust
pub struct LedgerKey { pub variable: VariableKind, pub subject: SubjectId }

pub enum Origin {
    Law(LawOptionId),
    Event(EventInstanceId),
    War(WarId),
    Supply { market: MarketId, good: GoodId },
    Demand { market: MarketId, good: GoodId },
    Climate(ClimateAnomalyId),
    Character(CharacterId),
    // …
}

pub struct Contribution { pub origin: Origin, pub amount: i64, pub since: Day, pub until: Option<Day> }

pub struct Explanation { pub base: i64, pub contributions: Vec<Contribution>, pub total: i64 }

impl Ledger {
    pub fn record(&mut self, key: LedgerKey, contributions: impl IntoIterator<Item = Contribution>);
    pub fn why(&self, key: LedgerKey) -> Explanation;
    pub fn top(&self, key: LedgerKey, n: usize) -> Vec<Contribution>;
}
```

### Aleatoriedad (`e101-rng`)

```rust
/// Counter-based deterministic randomness.
pub fn rng(seed: u64, system: SystemTag, entity: u64, day: Day) -> CounterRng;

impl CounterRng {
    pub fn next_u64(&mut self) -> u64;
    pub fn ratio(&mut self, min: Ratio, max: Ratio) -> Ratio;
    pub fn chance(&mut self, p: Ratio) -> bool;
}
```

### Guardado y repeticiones (`e101-save`)

```rust
pub struct SaveFile { pub header: SaveHeader, pub state: State, pub command_log: Vec<StampedCommand> }

pub struct SaveHeader {
    pub engine_version: SemVer,
    pub content_hash: [u8; 32],
    pub mods: Vec<ModRef>,
    pub seed: u64,
    pub day: Day,
    pub state_hash: [u8; 32],
}

pub fn save(file: &SaveFile, out: &mut impl Write) -> Result<(), SaveError>;
pub fn load(input: &mut impl Read) -> Result<SaveFile, LoadError>;
pub fn state_hash(state: &State) -> [u8; 32];
pub fn replay(initial: &State, log: &[StampedCommand], until: Day) -> State;
```

### Contenido (`e101-content`)

```rust
pub struct ContentDb { /* compiled, validated, read-only */ }

pub fn compile(root: &Path) -> Result<ContentDb, Vec<ContentError>>;

pub struct ContentError { pub file: PathBuf, pub line: u32, pub message: String, pub severity: Severity }
```

### Convenciones

- Los nombres de tipos y funciones están en inglés.
- Ningún tipo público del núcleo expone flotantes.
- Las colecciones públicas se iteran siempre en orden de ID.
- Los errores son tipos propios; el núcleo no hace `panic!` ante datos inválidos, solo ante invariantes internos rotos.

## Anexo Y · Plan de producción de contenido

Volúmenes orientativos de contenido y capacidad de revisión necesaria. El cuello de botella no será generar texto o datos con agentes, sino **verificarlos**: el plan se dimensiona por la capacidad de revisión humana.

### Volumen de la vertical (1300–1600)

| Tipo de contenido | Cantidad orientativa | Generación | Revisión |
| --- | --- | --- | --- |
| Provincias | ~350 | Pipeline geográfico + ajuste manual | Muestreo del 20 % |
| Entidades políticas | 18 jugables + ~12 no jugables | Agente de Historia | 100 % humana (confianza A/B) |
| Gobernantes y personajes iniciales | ~150 | Agente de Historia | 100 % humana |
| Dinastías | ~40 | Agente de Historia | 100 % humana |
| Culturas | 16 | Agente + persona | 100 % humana |
| Religiones y confesiones | ~10 | Agente + persona | 100 % humana |
| Bienes | 20 | Diseño | Diseño |
| Edificios y modos | ~25 edificios, ~60 modos | Diseño + agente | Diseño |
| Tecnologías | ~30 | Diseño + agente | Diseño |
| Leyes | ~60 opciones | Diseño | Diseño |
| Situaciones históricas | 30–50 | Agente de Historia + diseño | 100 % humana |
| Eventos | ~300 | Agente de Historia | 100 % humana; sensibles con revisión específica |
| Entradas de enciclopedia | ~250 | Agente | Muestreo del 30 % + todas las sensibles |
| Textos de interfaz | ~3.000 cadenas | Agente de Cliente + l10n | Revisión de estilo |
| Palabras totales (ES + EN) | ~120.000 por idioma | Agentes | Edición humana |
| Retratos modulares | 16 culturas × capas | Artista | Dirección de arte |
| Ilustraciones de eventos | ~40 | Artista | Dirección de arte |
| Iconos | ~200 | Artista | Dirección de arte |
| Música | 6–8 piezas | Compositor | Dirección |

### Capacidad de revisión

| Recurso | Capacidad orientativa | Implicación |
| --- | --- | --- |
| Persona responsable (revisión de datos A/B) | 6–8 horas por semana | ~40–60 registros verificados por semana. |
| Revisor histórico externo | Sesiones puntuales por región | Validar situaciones y contenido sensible antes del slice. |
| Editor de textos | Por lotes | Unificar estilo de eventos y enciclopedia. |

Con estas cifras, la verificación de unos 600 registros históricos de alta confianza requiere del orden de **10 a 15 semanas** de revisión distribuidas a lo largo de las Fases 4 y 5. Por eso el contenido se produce **por lotes regionales** y se revisa a medida que llega, no al final.

### Flujo de un lote de contenido

1. **Investigación:** el agente de Historia reúne fuentes y propone datos con confianza.
2. **Borrador:** genera los archivos RON y los textos en ambos idiomas.
3. **Validación automática:** `cargo xtask data` sin errores.
4. **Revisión histórica:** la persona responsable o un revisor externo verifica los datos A/B.
5. **Revisión de estilo:** guía del Anexo G.
6. **Prueba en Lab:** comprobar que el lote no rompe las distribuciones del Anexo F.
7. **Merge** y registro del lote en el historial de contenido.

### Riesgos de contenido

| Riesgo | Mitigación |
| --- | --- |
| Datos plausibles pero falsos generados por agentes | Fuente obligatoria; verificación humana de A/B; preferir C/D ante la duda. |
| Estilo inconsistente entre lotes | Guía de estilo, editor por lotes, ejemplos de referencia. |
| Sesgo hacia regiones con más fuentes en inglés | Bibliografía regional y revisores de cada área. |
| Volumen de revisión subestimado | Medir el ritmo real en la Fase 4 y ajustar el alcance del slice. |

## Anexo Z · Catálogo de escenarios de prueba y de laboratorio

Escenarios con nombre estable que usan el CI, las ejecuciones doradas y 101 Lab. Cada uno vive en `tests/golden/<nombre>/` o en `crates/e101-lab/scenarios/<nombre>/`.

| Escenario | Tipo | Duración | Qué comprueba |
| --- | --- | --- | --- |
| `empty_300y` | Dorado | 300 años | Calendario, scheduler y hash sin sistemas. |
| `threads_1_4_16` | Dorado | 50 años | Mismo resultado con distinto número de hilos. |
| `save_reload_mid` | Dorado | 100 años | Guardar y cargar a mitad sin cambiar el resultado. |
| `economy_basic` | Dorado | 50 años | Producción, consumo y precios estables. |
| `economy_shock_drought` | Dorado | 10 años | Respuesta a una sequía (Anexo F y ejemplo de la sección 10). |
| `trade_blockade` | Dorado | 10 años | Divergencia de precios y peajes bajo bloqueo. |
| `population_famine` | Dorado | 20 años | Mortalidad y emigración por hambruna. |
| `cohort_merge_300y` | Dorado | 300 años | Número de cohortes acotado. |
| `debt_default` | Dorado | 20 años | Impago y pérdidas exactas de los acreedores. |
| `succession_extinct` | Dorado | 30 años | Crisis sucesoria tras la extinción de una dinastía. |
| `rebellion_success` | Dorado | 30 años | Cambio de leyes tras una rebelión victoriosa. |
| `war_two_ai` | Dorado | 30 años | Guerra completa entre dos IA con paz válida. |
| `siege_unsupplied` | Dorado | 5 años | Asedio sin artillería ni bloqueo que no progresa. |
| `plague_routes` | Dorado | 30 años | Propagación de la peste por rutas comerciales. |
| `tech_lead_limit` | Dorado | 200 años | Ninguna tecnología supera el límite de adelanto. |
| `slice_strict_300y` | Lab | 300 años × 100 | Distribuciones del modo histórico estricto. |
| `slice_dynamic_300y` | Lab | 300 años × 100 | Distribuciones del modo dinámico. |
| `slice_alternative_300y` | Lab | 300 años × 100 | Diversidad de resultados. |
| `slice_sandbox_300y` | Lab | 300 años × 100 | Sin sesgos históricos; salud del mundo. |
| `ai_health_100y` | Lab | 100 años × 100 | IA bloqueadas, bancarrotas, guerras absurdas. |
| `perf_scale_s` | Benchmark | 50 años | Presupuestos de la escala S. |
| `perf_scale_m` | Benchmark | 20 años | Escalado a la escala M. |
| `perf_scale_l` | Benchmark | 10 años | Escalado a la escala L. |
| `memory_760y` | Benchmark | 760 años | Memoria acotada en la partida completa. |

## Anexo AA · Eventos de ejemplo de la vertical

Quince eventos escritos según la guía de estilo (Anexo G) para fijar el tono, la longitud y la forma de describir efectos. Las condiciones y los efectos son orientativos; las cifras finales saldrán del balance en 101 Lab. Todos los efectos se registran en el ledger con el evento como origen.

### EV-001 · La paga de los catalanes

- **Entidad:** poseedor de Constantinopla que ha contratado a la Compañía Catalana.
- **Condiciones:** la Compañía lleva tres meses o más sin cobrar; el tesoro no cubre la deuda.
- **Texto:** Los capitanes de la Compañía se presentan en palacio. Han vencido a los turcos en Anatolia, dicen, y el imperio les debe meses de soldada. Sus hombres viven sobre el terreno y los campesinos de Tracia ya se quejan de saqueos. Si no reciben el pago, no responden de lo que hagan.
- **Opciones:**
  - *Pagar con lo que haya en el tesoro.* → Tesoro baja; lealtad de la Compañía sube; sin dinero para la flota.
  - *Devaluar la moneda para pagarles.* → Paga inmediata; inflación en los meses siguientes; mercaderes descontentos.
  - *Ofrecerles tierras en lugar de dinero.* → Sin coste inmediato; la Compañía gana una base propia; riesgo de Estado dentro del Estado.
  - *Negarse y ordenar su disolución.* → Ahorro; alta probabilidad de que la Compañía se rebele.
- **Nota de diseño:** muestra la mecánica de mercenarios como entidad con contrato, lealtad y riesgo de rebelión (F-WAR-17).

### EV-002 · Los monasterios exentos

- **Entidad:** Estado ortodoxo con déficit y monasterios con grandes propiedades exentas.
- **Condiciones:** déficit durante dos años; monasterios con más del 15 % de la tierra de varias provincias.
- **Texto:** Los recaudadores informan de que buena parte de las mejores tierras pertenecen a monasterios que no pagan impuestos. El tesorero propone gravarlas, aunque sea temporalmente. El patriarca advierte de que tocar los bienes de Dios dividirá a los fieles.
- **Opciones:**
  - *Gravar las tierras monásticas.* → Más ingresos; legitimidad baja entre el clero; posible enfrentamiento con el patriarca.
  - *Pedir una contribución voluntaria.* → Ingresos modestos; relación con el clero intacta.
  - *Dejar las exenciones como están.* → Sin cambios; el déficit continúa.
- **Nota de diseño:** ejemplo de privilegio estamental negociable (P-06).

### EV-003 · Guerreros en la frontera

- **Entidad:** beylik fronterizo con victorias recientes.
- **Condiciones:** al menos una victoria contra un vecino cristiano en el último año; prestigio alto.
- **Texto:** Grupos de jinetes llegan desde otros beyliks atraídos por las noticias de botín. Piden servir bajo tu estandarte a cambio de tierras en la frontera. Su número fortalecería tus campañas, pero no todos obedecen con facilidad.
- **Opciones:**
  - *Aceptarlos y asignarles tierras de frontera.* → Más caballería; menor control en la frontera.
  - *Aceptar solo a los que juren lealtad personal.* → Menos tropas, más fieles.
  - *Rechazarlos.* → Sin cambios; los vecinos podrían recibirlos.
- **Nota de diseño:** la expansión fronteriza atrae población militar y erosiona el control (P-07).

### EV-004 · Un derviche pide tierras

- **Entidad:** beylik con población rural cristiana recién incorporada.
- **Condiciones:** provincia conquistada en los últimos cinco años.
- **Texto:** Un derviche respetado pide una aldea abandonada para fundar una hospedería. Promete atender a viajeros, alimentar a los pobres y atraer a nuevos pobladores. Los notables locales dudan, pero la gente del camino ya habla de él.
- **Opciones:**
  - *Concederle la aldea.* → Repoblación lenta; conversión gradual en la provincia; prestigio religioso.
  - *Concederla con impuestos.* → Algo de ingreso; menor efecto repoblador.
  - *Negarse.* → Sin cambios.
- **Nota de diseño:** conversión y asimilación como procesos lentos con causas materiales (sección 06).

### EV-005 · Plata en las montañas

- **Entidad:** reino con montañas mineras sin explotar.
- **Condiciones:** tecnología de minería en galerías; contacto comercial con mineros extranjeros.
- **Texto:** Mineros llegados del norte aseguran que las montañas esconden vetas de plata. Piden permiso para establecerse, con sus propias leyes y una parte de lo que extraigan. Los nobles de la región temen perder el control de sus tierras.
- **Opciones:**
  - *Concederles privilegios mineros.* → Nueva mina; más plata en unos años; comunidad extranjera autónoma.
  - *Explotar las minas con mineros del reino.* → Producción menor y más lenta; sin privilegios extranjeros.
  - *Dejar las montañas como están.* → Sin cambios.
- **Nota de diseño:** diáspora con privilegios propios y efecto económico diferido.

### EV-006 · Los embajadores del kan

- **Entidad:** Estado tributario o vecino de un kanato de la estepa.
- **Condiciones:** la Horda es más fuerte; hay tributo pendiente o disputas fronterizas.
- **Texto:** Una embajada del kan llega a la corte con exigencias claras: tributo, rehenes y libre paso para sus jinetes. Rechazarla supone arriesgar una incursión. Aceptarla, una humillación ante los nobles.
- **Opciones:**
  - *Pagar el tributo.* → Tesoro baja; seguridad en la frontera; legitimidad baja entre la nobleza.
  - *Ofrecer un matrimonio en lugar de tributo.* → Vínculo dinástico; posible reclamación futura del kan.
  - *Rechazar la embajada.* → Riesgo alto de incursión; prestigio entre los nobles.

### EV-007 · Revuelta en la isla

- **Entidad:** potencia colonial con una isla de población distinta a la dominante.
- **Condiciones:** impuestos altos en la colonia; nobleza local excluida del gobierno.
- **Texto:** Los señores locales de la isla se han levantado contra el gobernador. Exigen conservar sus tierras y reducir las cargas. La flota puede sofocar la revuelta, pero el comercio de la isla se resentirá durante años.
- **Opciones:**
  - *Enviar la flota y reprimir.* → Coste militar; control recuperado; agravio duradero.
  - *Negociar privilegios con los rebeldes.* → Paz rápida; menos ingresos; precedente para otras colonias.
  - *Contratar a señores rivales para combatirlos.* → Bajo coste; guerra civil local.

### EV-008 · Una isla para una familia

- **Entidad:** Estado con islas que no puede defender.
- **Condiciones:** piratería activa cerca de una isla propia; familia mercantil extranjera con flota.
- **Texto:** Una familia de mercaderes extranjeros ofrece defender una isla amenazada por los piratas. A cambio pide gobernarla durante unos años y quedarse con sus rentas. Sus galeras son mejores que las tuyas.
- **Opciones:**
  - *Conceder la isla por diez años.* → Isla defendida; pérdida de rentas; posible pérdida permanente.
  - *Conceder solo la defensa, no las rentas.* → Probable rechazo; si aceptan, coste moderado.
  - *Rechazar la oferta.* → La isla sigue expuesta.
- **Nota de diseño:** inspirado en concesiones a familias genovesas en el Egeo; la entrega puede volverse permanente.

### EV-009 · El rey ha muerto sin hijos

- **Entidad:** monarquía hereditaria cuya dinastía se extingue.
- **Condiciones:** muerte del gobernante sin herederos directos.
- **Texto:** El último rey de la casa ha muerto sin hijos varones. Tres pretendientes reclaman la corona: un príncipe extranjero apoyado por el papado, un rey vecino con lazos de sangre y un candidato de los grandes nobles. Cada uno trae aliados y enemigos.
- **Opciones:**
  - *Apoyar al candidato del papado.* → Apoyo religioso exterior; nobles divididos.
  - *Apoyar al rey vecino.* → Unión personal posible; resistencia nacional.
  - *Apoyar al candidato de los nobles.* → Rey débil; nobles más fuertes.
- **Nota de diseño:** abre la situación “crisis sucesoria” con pretendientes reales del mundo simulado.

### EV-010 · Una orden busca hogar

- **Entidad:** potencias cercanas a islas del Egeo.
- **Condiciones:** una orden militar sin territorio propio en la región; islas mal defendidas.
- **Texto:** Los caballeros de una orden militar buscan una isla donde establecer su sede. Tienen soldados veteranos, galeras y el respaldo de reinos lejanos, pero ninguna tierra propia. Su elección cambiará el equilibrio del mar.
- **Opciones (si la isla es tuya):**
  - *Venderles la isla.* → Ingreso grande; vecino cristiano fuerte.
  - *Ofrecerles una alianza a cambio de protección.* → Defensa naval; menor soberanía.
  - *Negarse.* → Riesgo de que la tomen por la fuerza.

### EV-011 · Ratas en el puerto

- **Entidad:** cualquier Estado con un puerto conectado a una zona de epidemia.
- **Condiciones:** epidemia activa en un puerto con tráfico directo.
- **Texto:** Llegan noticias de una enfermedad terrible en los puertos del mar Negro. Los marineros cuentan que la gente muere en pocos días. Varias naves de esa ruta esperan para atracar con sus cargas de grano.
- **Opciones:**
  - *Prohibir la entrada a esas naves.* → Menos riesgo de contagio; escasez y subida del grano.
  - *Imponer cuarentena antes de desembarcar.* → Riesgo moderado; retrasos comerciales (requiere la medida disponible).
  - *Dejarlas atracar.* → Comercio normal; riesgo alto.
- **Nota de diseño:** las medidas sanitarias reducen el comercio (sección 15).

### EV-012 · Un pretendiente en la corte

- **Entidad:** Estado con un vecino en crisis sucesoria.
- **Condiciones:** pretendiente exiliado de un Estado vecino.
- **Texto:** Un príncipe exiliado del reino vecino pide asilo y apoyo. Asegura que el pueblo lo espera y que, una vez en el trono, será tu aliado fiel. Su presencia ya irrita a quienes gobiernan su país.
- **Opciones:**
  - *Darle asilo y apoyo militar.* → Motivo de guerra; posible aliado futuro.
  - *Darle asilo sin apoyo.* → Moneda de cambio diplomática.
  - *Entregarlo a sus enemigos.* → Mejores relaciones con el vecino; prestigio dañado.

### EV-013 · Pan para la capital

- **Entidad:** Estado con una gran ciudad dependiente de grano importado.
- **Condiciones:** cobertura de alimentos de la capital por debajo del 80 %.
- **Texto:** El precio del pan se ha disparado y las panaderías cierran antes de mediodía. Los gremios piden que el Estado intervenga. Los mercaderes advierten de que fijar precios solo hará que el grano se esconda.
- **Opciones:**
  - *Abrir los graneros públicos.* → Precios bajan a corto plazo; reservas agotadas.
  - *Fijar un precio máximo.* → Descontento de mercaderes; riesgo de mercado negro.
  - *Prohibir la exportación de grano.* → Más oferta interna; agravio de socios comerciales.
  - *No intervenir.* → El mercado se ajusta; mortalidad y descontento entre los pobres.

### EV-014 · Rebaja de aduanas

- **Entidad:** Estado con fuerte presencia de mercaderes extranjeros.
- **Condiciones:** dependencia comercial alta de una república mercantil.
- **Texto:** Los mercaderes de la república piden reducir las aduanas a la mitad a cambio de un préstamo y de su apoyo naval. Tus propios mercaderes protestan: ya no pueden competir.
- **Opciones:**
  - *Aceptar el acuerdo.* → Préstamo y apoyo naval; menos ingresos aduaneros; mercaderes locales arruinados.
  - *Contraofertar una rebaja menor.* → Negociación con resultado incierto.
  - *Rechazarlo.* → Relaciones tensas; la república puede buscar otro socio.

### EV-015 · Concilio para la unión

- **Entidad:** Estado ortodoxo bajo amenaza militar grave.
- **Condiciones:** pérdida de territorio reciente; potencias latinas dispuestas a ayudar a cambio de la unión de las Iglesias.
- **Texto:** El papado ofrece convocar un concilio para unir las Iglesias. A cambio, promete ayuda militar contra tus enemigos. El clero y el pueblo rechazan la idea: muchos prefieren perder la ciudad antes que la fe.
- **Opciones:**
  - *Aceptar la unión.* → Ayuda militar posible; legitimidad baja entre clero y pueblo; posible revuelta.
  - *Negociar sin comprometerse.* → Tiempo ganado; ayuda poco probable.
  - *Rechazar la unión.* → Clero satisfecho; aislamiento diplomático.
- **Nota de diseño:** se presenta sin juzgar a ninguna confesión; las consecuencias dependen de la situación militar y social.

## Anexo AB · Rasgos de personajes y personalidades de la IA

### Rasgos de personajes

Los rasgos afectan a dos cosas: el **rendimiento** del personaje en su cargo y los **pesos** de la IA cuando ese personaje decide. Ningún rasgo es solo positivo.

| Rasgo | Rendimiento | Sesgo de decisión | Contrapartida |
| --- | --- | --- | --- |
| Prudente | Menos desastres militares | Evita guerras arriesgadas | Pierde oportunidades |
| Audaz | Mejor en ofensiva | Acepta más riesgo | Más derrotas graves |
| Ambicioso | Más iniciativa | Busca expansión y títulos | Conflictos con vecinos y familia |
| Contento | Estabilidad | Prefiere el statu quo | Poca iniciativa |
| Piadoso | Apoyo del clero | Favorece la religión oficial | Menos tolerancia |
| Escéptico | Más pragmatismo | Menos peso religioso | Desconfianza del clero |
| Justo | Más legitimidad | Respeta leyes y pactos | Menos margen para trampas útiles |
| Cruel | Represión eficaz | Usa la fuerza | Agravio y rebeliones |
| Clemente | Menos agravio | Perdona rebeldes | Puede parecer débil |
| Codicioso | Más ingresos personales | Prioriza el dinero | Corrupción |
| Generoso | Lealtad de la corte | Reparte recursos | Gasto |
| Austero | Gasto bajo | Recorta | Descontento de las élites |
| Derrochador | Prestigio de la corte | Gasta en lujo | Deuda |
| Erudito | Mejor en ciencia y administración | Financia el saber | Menos interés militar |
| Guerrero | Mejor mando | Busca gloria militar | Guerras innecesarias |
| Cobarde | Evita el campo de batalla | Huye del riesgo | Prestigio bajo |
| Diplomático | Mejores tratados | Prefiere negociar | Puede ceder demasiado |
| Intrigante | Mejor en conjuras e inteligencia | Usa medios encubiertos | Desconfianza |
| Ingenuo | — | Confía en los demás | Víctima de engaños |
| Paranoico | Detecta conjuras | Purga a sospechosos | Pierde aliados leales |
| Carismático | Más lealtad y reclutamiento | — | Dependencia personal |
| Tímido | — | Evita confrontaciones | Pierde apoyos |
| Testarudo | Resiste presiones | No cambia de plan | Persiste en errores |
| Pragmático | Se adapta | Cambia de alianza si conviene | Menos confianza ajena |
| Vengativo | — | Recuerda agravios | Guerras de revancha |
| Tolerante | Estabilidad con minorías | Protege diversidad | Rechazo de ortodoxos |
| Fanático | Moral religiosa alta | Guerra santa, persecución | Rebeliones de minorías |
| Reformista | Impulsa leyes nuevas | Cambia instituciones | Oposición de élites |
| Tradicionalista | Apoyo de élites tradicionales | Bloquea reformas | Estancamiento |
| Constructor | Infraestructura más barata | Invierte en obras | Gasto |
| Mercantil | Mejor en comercio | Favorece a los mercaderes | Descontento de la nobleza |
| Estratega | Mejores planes de campaña | — | — |
| Administrador | Más control efectivo | Prioriza la gestión | Menos atención exterior |
| Enfermizo | Rendimiento irregular | — | Riesgo de muerte o regencia |
| Robusto | Vida más larga | — | — |
| Melancólico | Rendimiento bajo en crisis | Evita decisiones | Parálisis en momentos clave |

Los rasgos de figuras históricas se proponen a partir de las fuentes y se marcan con nivel de confianza, igual que cualquier otro dato.

### Componentes de personalidad de la IA

La personalidad de un país combina varios componentes con pesos. Los pesos salen de la identidad, la geografía, el régimen y el gobernante, y cambian con el tiempo.

| Componente | Prioridades | Ejemplos en 1300 |
| --- | --- | --- |
| Supervivencia | Alianzas defensivas, evitar guerras perdidas, conservar el núcleo | Bizancio, Trebisonda, Armenia cilicia |
| Expansión fronteriza | Conquistas cercanas, botín, absorber vecinos débiles | Beylik otomano, Menteşe |
| Hegemonía regional | Vasallos, influencia, impedir rivales | Germiyan, Hungría, Serbia |
| Comercio primero | Rutas, privilegios, colonias, evitar guerras terrestres | Venecia, Génova |
| Prestigio imperial | Títulos, ciudades simbólicas, legitimidad | Serbia, Bulgaria, Karamán |
| Defensa de la fe | Proteger correligionarios, guerra santa con condiciones | Mamelucos, órdenes militares |
| Oportunista | Atacar a quien esté en crisis | Beyliks, ducados francos |
| Equilibrador | Unirse contra el más fuerte | Repúblicas italianas, potencias medias |
| Restauración | Recuperar territorios e identidades perdidas | Bizancio, Bulgaria |
| Revanchista | Recuperar lo perdido en la última guerra | Cualquier derrotado reciente |
| Aislacionista | Pocos compromisos exteriores | Estados insulares o montañosos |
| Mercenario | Vender servicios militares | Compañía Catalana, compañías italianas |
| Reformista | Leyes nuevas, centralización | Monarcas con burocracia en crecimiento |
| Tradicionalista | Conservar privilegios y leyes | Estados dominados por estamentos |
| Colonizador | Asentamientos lejanos y rutas oceánicas | Potencias atlánticas (épocas posteriores) |

**Regla:** los componentes nunca empujan a acciones imposibles. Una IA con “Prestigio imperial” no ataca Constantinopla sin artillería ni flota; acumula capacidades o busca la ciudad por otra vía (matrimonio, vasallaje, crisis interna).

## Anexo AC · Preguntas frecuentes para agentes

**¿Puedo usar `f64` en un cálculo intermedio si el resultado es entero?**  
No en los crates de simulación. Usa los tipos de punto fijo; si necesitas una función que no existe (por ejemplo, una raíz o una exponencial), pide una implementación por tablas en `e101-store` mediante una tarea de Motor.

**El orden de iteración de mi `BTreeMap` no coincide con el orden por ID. ¿Es un problema?**  
Es determinista, pero puede producir resultados distintos a los esperados por otros sistemas. Itera por ID salvo que la tarea indique otra cosa.

**Una prueba dorada falla tras mi cambio y creo que el nuevo resultado es correcto.**  
No actualices el hash. Explica en el PR por qué cambia, añade la etiqueta `golden-change` y espera la aprobación humana.

**Necesito una biblioteca externa pequeña.**  
Abre una tarea o comenta en la tuya con nombre, licencia, mantenimiento y alternativa sin dependencia. Etiqueta `new-dependency`. No la añadas antes de la aprobación.

**La tarea me pide algo que contradice el documento maestro.**  
Detente y pregunta. El documento maestro y los ADR prevalecen sobre una tarea, salvo que la persona responsable lo confirme.

**No encuentro una fuente fiable para un dato histórico.**  
Usa confianza C o D, explica tu razonamiento en el diario y en el campo de notas del dato. No inventes una fuente.

**¿Puedo reorganizar módulos para que el código quede más limpio?**  
Solo dentro de los archivos permitidos y si la tarea lo contempla. Las refactorizaciones grandes son tareas propias.

**Mi cambio necesita tocar otro crate.**  
Anótalo en el diario y pregunta. Si es una interfaz pública, hace falta un ADR del rol de Arquitectura.

**¿Cómo registro algo en el ledger si mi sistema cambia una variable de forma indirecta?**  
Registra la contribución en el sistema que produce el delta, con el origen más específico disponible. Si no hay un `Origin` adecuado, pide añadirlo mediante una tarea de Arquitectura.

**El benchmark empeora un 3 %. ¿Es aceptable?**  
Por debajo del 5 % es aceptable si lo indicas en el PR. Por encima, etiqueta `perf-regression` y justifica o corrige.

**¿Puedo escribir los textos del juego directamente en los archivos de datos?**  
No. Los textos van en `games/epoch/locale/` con claves; los datos solo contienen claves.

**¿Qué hago si dos agentes necesitan el mismo archivo?**  
El segundo marca su tarea como `status:blocked` y enlaza la del primero. Arquitectura decide si se divide el archivo o se secuencian las tareas.

**¿Puedo probar algo con datos reales de la red durante una prueba?**  
No. Las pruebas no acceden a la red. Usa datos de prueba incluidos en el repositorio.

**¿Cómo sé si un contenido es sensible?**  
Si trata esclavitud, trata de personas, violencia masiva, persecución religiosa o étnica, o representación de culturas minoritarias, lo es. Sigue la guía y etiqueta `needs-sensitive-review`.

**Terminé antes de lo previsto. ¿Puedo seguir con la siguiente tarea?**  
Sí, si está en `status:ready` y es de tu rol. Abre un PR por tarea; no mezcles tareas en un mismo PR.

## Anexo AD · Fichas de religiones y confesiones

Cada confesión se define con los rasgos doctrinales de la sección 06. Las fichas describen la situación de 1300 y la forma de modelarla; no valoran las creencias.

| Confesión | Familia | Autoridad | Clero | Relación con el Estado | Préstamo con interés | Notas de diseño |
| --- | --- | --- | --- | --- | --- | --- |
| Católica latina | Cristianismo | Centralizada (papado) | Célibe | Iglesia de Estado con autonomía | Restringido | Papado como actor diplomático; órdenes religiosas y militares. |
| Ortodoxa de Constantinopla | Cristianismo | Sinodal (patriarcado) | Casado (bajo), célibe (obispos) | Estrecha con el emperador | Restringido | Monacato fuerte; relación con el Estado imperial. |
| Ortodoxas autocéfalas (serbia, búlgara) | Cristianismo | Sinodal nacional | Casado (bajo) | Iglesia de Estado | Restringido | Identidad política ligada a la Iglesia. |
| Armenia apostólica | Cristianismo | Catolicosado | Casado (bajo) | Ligada al reino y a la diáspora | Restringido | Redes de diáspora comercial. |
| Copta | Cristianismo | Patriarcado de Alejandría | Casado (bajo) | Minoría tolerada | Restringido | Papel administrativo en Egipto. |
| Etíope | Cristianismo | Vinculada al patriarcado copto | Casado (bajo) | Iglesia de Estado | Restringido | Monarquía salomónica como legitimadora. |
| Iglesia del Oriente | Cristianismo | Catolicosado | Casado | Minoría en Asia | Restringido | Presente de Mesopotamia a China. |
| Suní (hanafí, malikí, shafií, hanbalí) | Islam | Descentralizada (ulemas; califato simbólico) | Sin clero ordenado | Ley religiosa integral o parcial | Prohibido (con instrumentos alternativos) | Escuelas jurídicas por región; órdenes sufíes como redes. |
| Chií duodecimana | Islam | Ulemas | Sin clero ordenado | Minoritaria en 1300 | Prohibido | Puede volverse religión de Estado. |
| Ismailí | Islam | Imamato | Sin clero ordenado | Comunidades dispersas | Prohibido | Redes clandestinas tras la caída de sus fortalezas. |
| Zaydí | Islam | Imamato | Sin clero ordenado | Estado en Yemen | Prohibido | Rivalidad con los rasúlidas. |
| Ibadí | Islam | Imamato electivo | Sin clero ordenado | Estado en Omán | Prohibido | Tradición marítima. |
| Judaísmo rabínico | Judaísmo | Local (rabinos, comunidades) | Rabinos | Minoría con autonomía comunitaria | Permitido con no correligionarios | Diásporas; vulnerabilidad a persecuciones. |
| Hinduismo (shivaísta, vishnuista) | Religiones de la India | Local (templos, linajes de maestros) | Brahmanes | Templos patrocinados por reyes | Variable | Estructura social ligada a la religión. |
| Jainismo | Religiones de la India | Comunidades monásticas | Monjes | Minoría mercantil | Permitido | Comerciantes y banqueros. |
| Budismo theravada | Budismo | Sangha nacional | Monjes célibes | Estrecha con la monarquía | Permitido | Legitimidad real por patrocinio de la sangha. |
| Budismo mahayana | Budismo | Escuelas y monasterios | Monjes | Variable | Permitido | Monasterios con tierras y comercio. |
| Budismo vajrayana | Budismo | Escuelas con linajes | Monjes y lamas | Poder político directo (Tíbet) | Permitido | Relación con los kanes mongoles. |
| Confucianismo | Asia oriental | Funcionarios letrados | Sin clero | Ideología del Estado | Permitido | Exámenes y burocracia. |
| Sintoísmo | Asia oriental | Santuarios locales | Sacerdotes | Ligado a la corte imperial | Permitido | Coexiste con el budismo. |
| Tengrismo | Tradicional | Chamanes | Chamanes | Ligado al kan | — | En retroceso ante el islam en los kanatos occidentales. |
| Paganismo báltico | Tradicional | Sacerdotes locales | Sacerdotes | Religión del gran duque | — | Conversión aún abierta en Lituania. |
| Religiones mesoamericanas | Tradicional | Templos de cada ciudad | Sacerdotes | Teocrática o ligada a la nobleza | — | Calendarios, ritual y guerra relacionados. |
| Religión andina | Tradicional | Santuarios y oráculos | Sacerdotes | Ligada a linajes y huacas | — | Pachacamac como centro de peregrinación. |

## Anexo AE · Potencias de referencia por época

Fichas breves de las potencias que el modo histórico estricto suele producir en cada época. Sirven para que la IA, los nombres y las identidades estén preparados si una entidad parecida surge en la partida.

| Época | Potencia de referencia | Rasgos de juego | Componentes de IA típicos |
| --- | --- | --- | --- |
| 1450–1600 | Imperio otomano | Imperio burocrático-militar, *timar*, jenízaros, *millet* | Expansión, prestigio imperial, defensa de la fe |
| 1450–1600 | Monarquía Hispánica | Monarquía compuesta, plata americana, tercios | Defensa de la fe, colonizador, hegemonía |
| 1450–1600 | Francia | Monarquía centralizadora | Equilibrador, hegemonía |
| 1450–1600 | Polonia-Lituania | Unión con nobleza fuerte y rey electivo | Supervivencia, tradicionalista |
| 1450–1600 | Moscovia | Autocracia en expansión | Expansión, restauración (tierras de la Rus) |
| 1450–1600 | Persia safávida | Imperio con religión de Estado chií | Prestigio, defensa de la fe |
| 1450–1600 | Imperio mogol | Imperio con nobleza de servicio | Expansión, tolerancia variable |
| 1450–1600 | Ming | Burocracia confuciana | Aislacionista, defensa |
| 1450–1600 | Songhai | Imperio saheliano | Hegemonía regional |
| 1450–1600 | Tawantinsuyu | Imperio andino de reciprocidad | Expansión, integración |
| 1600–1800 | Provincias Unidas | República comercial | Comercio primero |
| 1600–1800 | Gran Bretaña | Monarquía parlamentaria naval | Comercio, colonizador, equilibrador |
| 1600–1800 | Monarquía de los Habsburgo | Monarquía compuesta danubiana | Supervivencia, defensa de la fe |
| 1600–1800 | Prusia | Estado militar-burocrático | Expansión, reformista |
| 1600–1800 | Rusia imperial | Autocracia modernizadora | Expansión, reformista |
| 1600–1800 | Qing | Imperio conquistador con burocracia | Hegemonía, aislacionista |
| 1600–1800 | Japón Tokugawa | Shogunato con cierre selectivo | Aislacionista, tradicionalista |
| 1600–1800 | Confederación maratha | Confederación militar | Expansión, oportunista |
| 1800–1914 | Reino Unido | Potencia industrial y naval | Comercio, colonizador |
| 1800–1914 | Imperio alemán | Potencia industrial unificada | Hegemonía, reformista |
| 1800–1914 | Estados Unidos | República federal en expansión | Expansión continental, aislacionista |
| 1800–1914 | Imperio del Japón | Modernización acelerada | Expansión, reformista |
| 1800–1914 | Imperio ruso | Autocracia en tensión | Expansión, tradicionalista |
| 1800–1914 | México | República federal tras la independencia | Supervivencia, reformista |
| 1800–1914 | Imperio del Brasil | Monarquía americana | Estabilidad, comercio |
| 1914–1991 | Unión Soviética | Régimen de partido único con economía planificada | Hegemonía, ideológico |
| 1914–1991 | Estados Unidos | Superpotencia democrática | Hegemonía, comercio |
| 1914–1991 | República Popular China | Régimen de partido único | Restauración, hegemonía regional |
| 1914–1991 | India | Democracia poscolonial | Equilibrador, no alineado |
| 1991–2060 | Unión Europea (como organización) | Integración regional | Comercio, normativo |
| 1991–2060 | China | Potencia manufacturera | Hegemonía regional, comercio |
| 1991–2060 | Estados Unidos | Potencia tecnológica y financiera | Hegemonía, comercio |
| 1991–2060 | India | Potencia demográfica emergente | Equilibrador |
| 1991–2060 | Brasil, México, Indonesia, Nigeria | Potencias regionales | Comercio, hegemonía regional |

## Anexo AF · Las primeras cuatro semanas del repositorio

Plan detallado para arrancar `101-engine` con agentes desde el primer día. Corresponde al inicio de la Fase 0 y al principio de la Fase 1.

| Semana | Día | Trabajo | Responsable | Resultado |
| --- | --- | --- | --- | --- |
| 1 | 1 | Crear la organización y el repositorio; subir el kit `101-engine-starter`. | Persona | Repositorio con `AGENTS.md` y plantillas. |
| 1 | 1 | Configurar protección de `main`, etiquetas y CODEOWNERS. | Persona | Reglas activas. |
| 1 | 2 | Copiar el documento maestro a `docs/master/`. | Persona | Contexto disponible para agentes. |
| 1 | 2–3 | T-002 y T-003: workspace vacío y `xtask check`. | Agente infra | `cargo xtask check` en verde. |
| 1 | 3–4 | T-004: CI. | Agente infra | CI en verde en un PR de prueba. |
| 1 | 4–5 | T-005 a T-007: ADR de monorepo, determinismo y punto fijo. | Agente arquitectura + persona | Tres ADR aceptados. |
| 2 | 1–2 | T-101: `e101-time`. | Agente engine | Calendario con pruebas. |
| 2 | 1–2 | T-103: `e101-rng`. | Agente engine (en paralelo) | RNG con pruebas. |
| 2 | 3–5 | T-104: tipos de punto fijo. | Agente engine | `Money`, `Qty`, `Ratio` con pruebas de propiedad. |
| 2 | 3–5 | T-106 y T-107: lints de determinismo y dependencias. | Agente infra | Lints activos en CI. |
| 3 | 1–3 | T-105: tablas SoA. | Agente engine | Almacenamiento con IDs estables. |
| 3 | 1–3 | T-008: prototipo económico fuera del motor. | Agente sim + persona | 200 años estables. |
| 3 | 4–5 | T-102: escalonamiento. | Agente engine | Distribución uniforme probada. |
| 3 | 4–5 | T-010: lista verificada de entidades de 1300. | Agente history + persona | Tabla con fuentes. |
| 4 | 1–3 | T-108 y T-109: comandos y aplicación de deltas. | Agente engine | Mismo resultado con 1 y 16 hilos. |
| 4 | 3–4 | T-110 y T-111: hash de estado y primer escenario dorado. | Agente engine + QA | `empty_300y` estable. |
| 4 | 5 | Revisión de las cuatro semanas: métricas de agentes, ajustes en `AGENTS.md`. | Persona | Lecciones aprendidas en un ADR o en el propio AGENTS.md. |

**Criterio de éxito del primer mes:** el repositorio compila, el CI impide romper el determinismo, existe el primer escenario dorado y al menos un 60 % de los PR de agentes se aceptaron sin cambios mayores.

## Anexo AG · Índice de especificaciones por sistema

El documento maestro orienta; cada sistema necesita una especificación propia en `docs/specs/` antes de implementarse. Esta tabla lista las especificaciones previstas, su rol propietario, la fase en la que deben estar aceptadas y su contenido mínimo.

| Especificación | Rol | Antes de | Contenido mínimo |
| --- | --- | --- | --- |
| `time.md` | engine | Fase 1 | Época del día absoluto, calendarios, reglas de escalonamiento, casos límite. |
| `fixed-point.md` | engine | Fase 1 | Escalas, redondeo, desbordamiento, operaciones permitidas. |
| `store.md` | engine | Fase 1 | Tablas, IDs, slotmaps, ciclo de vida de entidades. |
| `commands.md` | engine | Fase 1 | Lista de comandos, validación, orden, diario. |
| `apply-and-invariants.md` | engine | Fase 1 | Fase de aplicación, ordenación de deltas, lista de invariantes. |
| `save-format.md` | engine | Fase 1 | Cabecera, compresión, versionado, migraciones, hash. |
| `map-pipeline.md` | data | Fase 1 | Fuentes, procesos, textura de IDs, adyacencias, reproducibilidad. |
| `content-format.md` | data | Fase 1 | Esquemas RON y CSV, validadores, errores. |
| `ledger.md` | architecture | Fase 2 | Claves, orígenes, retención, agregados, consultas. |
| `economy.md` | sim | Fase 2 | Bienes, edificios, modos, precios, comercio, consumo, moneda, ecuaciones y parámetros. |
| `population.md` | sim | Fase 2 | Cohortes, tasas, migración, movilidad, fusión, asimilación. |
| `state-finance.md` | sim | Fase 2 | Impuestos, gastos, deuda, acreedores, impago. |
| `politics.md` | sim | Fase 3 | Gobiernos, grupos de interés, leyes, legitimidad, control, rebeliones. |
| `diplomacy.md` | sim | Fase 3 | Relaciones, tratados por cláusulas, vasallaje, información imperfecta. |
| `military.md` | sim | Fase 3 | Unidades, movimiento, suministro, batallas, asedios, guerra naval, paz. |
| `ai.md` | ai | Fase 3 | Niveles, utilidades, personalidades, presupuesto de cómputo, observabilidad. |
| `characters.md` | sim | Fase 4 | Personajes, rasgos, dinastías, sucesión, regencias, facciones. |
| `history.md` | history | Fase 4 | Situaciones, roles, caducidad, divergencia, modos de campaña. |
| `technology.md` | sim | Fase 4 | Grafo, etapas, difusión, adopción, límite de adelanto. |
| `climate-epidemics.md` | sim | Fase 4 | Anomalías climáticas, desastres, modelo de epidemias, medidas. |
| `culture-religion.md` | sim | Fase 4 | Taxonomías, rasgos, procesos culturales y religiosos. |
| `ui-map.md` | client | Fase 1 | Capas de render, modos de mapa, niveles de detalle, estilos de época. |
| `ui-panels.md` | client | Fase 2 | Pantallas, navegación, tooltips, “¿por qué?”, accesibilidad. |
| `localization.md` | l10n | Fase 2 | Claves, Fluent, glosario, topónimos. |
| `lab.md` | tools | Fase 2 | Escenarios, métricas, informes, comparación de versiones. |
| `forge.md` | tools | Fase 4 | Editores, validación en tiempo real, vista previa. |
| `modding.md` | data | Fase 6 | Formatos públicos, carga, compatibilidad, Workshop. |
| `multiplayer.md` | architecture | Antes de prometerlo | Lockstep, determinismo entre plataformas, red. |

**Plantilla de especificación:** objetivo; alcance y fuera de alcance; modelo (entidades, variables, ecuaciones); parámetros iniciales; invariantes; interacción con otros sistemas; registro causal; interfaz de usuario; pruebas y escenarios; preguntas abiertas.

**Punto de partida de cada especificación en la v0.7:**

| Especificación | Base en este documento |
| --- | --- |
| `population.md` | Sección 09, “Especificación detallada de población” |
| `economy.md`, `state-finance.md` | Sección 10, “Especificación detallada de economía” |
| `politics.md` | Sección 11, “Especificación detallada de gobierno y política” |
| `diplomacy.md` | Sección 12, “Especificación detallada de diplomacia” |
| `military.md` | Sección 13, “Especificación detallada militar” |
| `technology.md` | Sección 14, “Especificación detallada de tecnología” |
| `climate-epidemics.md` | Sección 15, “Especificación detallada de clima, epidemias y exploración” |
| `characters.md` | Sección 16, “Especificación detallada de personajes y dinastías” |
| `ai.md` | Sección 17, “Especificación detallada de la IA de países” |
| `history.md` | Sección 07, “Especificación detallada de 101 History”, y sección 08 |
| `culture-religion.md` | Sección 06, “Especificación detallada de cultura y religión” |
| `map-pipeline.md` | Sección 04, “Especificación detallada del mapa” |
| `ui-panels.md` | Sección 18, “Especificación detallada de la interfaz”, y Anexo AO |
| `apply-and-invariants.md` | Sección 21 (calendario del tick) y Anexo AM |
| `save-format.md` | Sección 23 (hash) y Anexo AR |
| `content-format.md`, `modding.md` | Anexos E y AL; sección 20 |
| `lab.md` | Sección 26 (informe nocturno), Anexos F, Z y AW |
| Parámetros de todas | Anexo AI |

## Anexo AH · Lista de comprobación para cerrar la vertical

Antes de declarar terminada la Fase 5, todos los puntos deben estar marcados o tener una excepción documentada.

### Simulación

- [ ] 0 violaciones de invariantes en 100 campañas de 300 años por modo.
- [ ] 0 IA bloqueadas en `ai_health_100y`.
- [ ] Distribuciones del Anexo F dentro de rango en los cuatro modos.
- [ ] Tick medio ≤ 10 ms y p99 ≤ 50 ms en escala S en el PC de referencia.
- [ ] Memoria acotada en `memory_760y`.
- [ ] Guardar, cargar y continuar con hash idéntico.

### Contenido

- [ ] 18 entidades jugables con ficha completa, fuentes y revisión humana.
- [ ] 30–50 situaciones con condiciones, caducidad y variantes.
- [ ] ~300 eventos revisados con la guía de estilo.
- [ ] Contenido sensible revisado por una persona con conocimiento de la región.
- [ ] Español e inglés completos; 0 cadenas sin traducir.
- [ ] Enciclopedia con fuentes para todas las entidades, culturas y religiones del slice.

### Interfaz

- [ ] Todas las variables visibles responden a “¿por qué?”.
- [ ] Modos de mapa legibles con daltonismo simulado.
- [ ] Tutorial de la primera hora probado con tres jugadores nuevos.
- [ ] Navegación completa por teclado en las pantallas principales.
- [ ] 60 FPS a 1080p con todas las capas.

### Pruebas con jugadores

- [ ] Al menos diez sesiones con jugadores externos.
- [ ] La mayoría explica correctamente tres sucesos de su partida.
- [ ] La mayoría quiere seguir jugando al terminar la sesión.
- [ ] Hallazgos convertidos en tareas y priorizados.

### Producción

- [ ] Backlog de la Fase 6 preparado en formato de tareas.
- [ ] Métricas de agentes revisadas y `AGENTS.md` actualizado.
- [ ] ADR al día; ninguna decisión importante solo en conversaciones.
- [ ] Licencias de dependencias y datasets auditadas.
- [ ] Página de tienda y materiales de presentación preparados (si se decide publicar la demo).

## Anexo AI · Tabla de parámetros globales

Fuente única de los parámetros iniciales citados en las especificaciones de la v0.7. En el repositorio vive en `games/epoch/data/rules/*.ron`; **cualquier cambio de valor** se hace en datos, se justifica en el PR con una ejecución de 101 Lab y, si mueve una métrica del Anexo F, se anota. Los ID son estables y los mods pueden sobrescribirlos.

### Población

| ID | Valor inicial | Unidad | Sección |
| --- | --- | --- | --- |
| `pop.birth_rate_per_adult` | 72,7 | ‰ anual por adulto | 09 |
| `pop.mortality.children` | 55 | ‰ anual | 09 |
| `pop.mortality.adults` | 16 | ‰ anual | 09 |
| `pop.mortality.elders` | 85 | ‰ anual | 09 |
| `pop.aging.child_to_adult` | 1/180 | fracción mensual | 09 |
| `pop.aging.adult_to_elder` | 1/420 | fracción mensual | 09 |
| `pop.cohort.create_threshold` | 50 | personas | 09 |
| `pop.cohort.merge_threshold` | max(100; 0,3 % de la provincia) | personas | 09 |
| `pop.cohort.max_per_province.S/M/L` | 70 / 50 / 40 | cohortes | 09 |
| `pop.migration.alpha` | 0,02 | fracción mensual | 09 |
| `pop.migration.threshold` | 0,10 | atractivo | 09 |
| `pop.migration.cap_free` | 1 % | mensual por cohorte | 09 |
| `pop.migration.max_days` | 30 | días de viaje | 09 |
| `pop.refugees.security_trigger` | 0,30 | seguridad | 09 |
| `pop.refugees.cap` | 10 % | mensual | 09 |
| `pop.refugees.return_chance` | 2 % | mensual | 09 |
| `pop.refugees.productivity_malus` | −30 % durante 12 meses | — | 09 |
| `pop.mobility.cap` | 0,5 % | mensual por cohorte | 09 |
| `pop.literacy.convergence` | 1/240 | fracción mensual | 09 |
| `pop.urban.threshold` | 30 % no agrario o 10.000 hab. | — | 09 |
| `pop.urban.overcap_mortality` | +10 % por cada 10 % de exceso | — | 09 |
| `cul.assimilation.base` | 0,0012 | fracción mensual | 06 |
| `cul.hybrid.min_years` | 80 | años de convivencia al 30–70 % | 06 |
| `rel.conversion.base` | 0,0003 | fracción mensual | 06 |
| `rel.reform.thresholds` | 40 / 60 / 80 | presión de reforma | 06 |

### Economía y finanzas

| ID | Valor inicial | Unidad | Sección |
| --- | --- | --- | --- |
| `eco.unit_of_account` | 3,5 g de oro fino | uc | 10 |
| `eco.price.k` | 0,10 | por semana | 10 |
| `eco.price.max_change` | ±10 % | por semana | 10 |
| `eco.price.stock_weight` | 0,25 | — | 10 |
| `eco.price.min_max` | 0,2× / 10× precio base | — | 10 |
| `eco.stock.grain_weeks` | 26 | semanas de consumo tras la cosecha | 10 |
| `eco.trade.partial_adjust` | 20 % | por semana | 10 |
| `eco.transport.sea` | 0,0008 | uc por t·km | 10 |
| `eco.transport.river` | 0,0032 | uc por t·km | 10 |
| `eco.transport.road` | 0,012 | uc por t·km | 10 |
| `eco.transport.pack` | 0,020 | uc por t·km | 10 |
| `eco.invest.hurdle` | interés + riesgo + 3 % | anual | 10 |
| `eco.invest.max_share` | 30 % del capital | trimestral | 10 |
| `eco.tax_farm.price` | 0,70–0,85 × recaudación esperada | — | 10 |
| `eco.tax_farm.extra_pressure` | 1,10–1,40 | — | 10 |
| `eco.debt.risk_per_debt_ratio` | 2 % por unidad de deuda/ingresos | anual | 10 |
| `eco.debt.risk_per_default` | 6 % por impago recordado | anual | 10 |
| `eco.debt.default_half_life` | 15 | años | 10 |
| `eco.coin.detection.urban` | 1/6 | fracción mensual | 10 |
| `eco.coin.detection.rural` | 1/18 | fracción mensual | 10 |
| `eco.coin.gresham_outflow` | 5 % | mensual | 10 |
| `eco.price_level.adjust` | 1/36 | fracción mensual | 10 |
| `eco.gold_silver_ratio.start` | 11 | — | 10 |

### Gobierno y política

| ID | Valor inicial | Unidad | Sección |
| --- | --- | --- | --- |
| `gov.power.weights` | 0,35 / 0,20 / 0,25 / 0,20 | riqueza / número / organización / control institucional | 11 |
| `gov.reform.majority_factor` | 1,2 | — | 11 |
| `gov.reform.sovereign_authority` | 0,15–0,45 | — | 11 |
| `gov.legitimacy.base` | 50 | 0–100 | 11 |
| `gov.control.convergence` | 0,05 | mensual | 11 |
| `gov.control.D0.1300` | 15 | días | 11 |
| `gov.control.insecure_multiplier` | ×2 (inseguro) / ×4 (enemigo) | — | 11 |
| `gov.province.cost` | 1 + 0,02 × miles de hab. + 0,5 si urbana | capacidad | 11 |
| `gov.corruption.base` | 0,10 | — | 11 |
| `gov.corruption.convergence` | 0,02 | mensual | 11 |
| `gov.rebel.thresholds` | 20 / 45 / 70 | presión | 11 |
| `gov.civil_war.province_share` | 25 % | — | 11 |
| `gov.repression.grievance` | +15, semivida 10 años | — | 11 |

### Diplomacia

| ID | Valor inicial | Unidad | Sección |
| --- | --- | --- | --- |
| `dip.trust.reversion` | 1 % | mensual hacia 50 | 12 |
| `dip.grievance.half_life` | 10 (20 con reclamación) | años | 12 |
| `dip.aggression.per_province` | 0,1 | agresividad | 12 |
| `dip.aggression.half_life` | 10 | años | 12 |
| `dip.coalition.threat_trigger` | 60 | amenaza | 12 |
| `dip.coalition.dissolve` | < 40 durante 2 años | amenaza media | 12 |
| `dip.peace.harsh_threshold` | 80 | puntos de coste | 12 |
| `dip.peace.revanche_years` | 50 | años | 12 |
| `dip.vassal.rebel_margin` | 15 | pu | 12 |
| `dip.news.factor` | 1,0 / 0,7 / 0,5 / 0,05 / ≈0 | sin red / embajada / correo / telégrafo / redes | 12 |
| `dip.estimate.base_error` | ±40 % | — | 12 |
| `dip.retry.cooldown` | 6 | meses | 17 |

### Guerra

| ID | Valor inicial | Unidad | Sección |
| --- | --- | --- | --- |
| `war.frontage.plain` | 8.000 | hombres por bando | 13 |
| `war.frontage.hills / forest / mountain / ford` | 5.000 / 3.000 / 1.500 / 800 | hombres por bando | 13 |
| `war.fire.coefficient` | 0,0008 | — | 13 |
| `war.shock.coefficient` | 0,0012 | — | 13 |
| `war.random.range` | 0,85–1,15 | — | 13 |
| `war.morale.retreat / rout` | 30 / 10 | moral | 13 |
| `war.pursuit.coefficient` | 0,003 (×3 contra desbandada) | — | 13 |
| `war.attrition.base / slope / cap` | 2 % / 6 % / 15 % | mensual | 13 |
| `war.camp_disease` | 1 % por mes inmóvil | mensual | 13 |
| `war.levy.service_days` | 40–90 | días/año | 13 |
| `war.levy.dissolve` | 10 % | semanal fuera de plazo sin paga | 13 |
| `war.merc.mutiny.start` | 3 meses de atraso | — | 13 |
| `war.merc.mutiny.base / step` | 10 % / +10 % | mensual | 13 |
| `war.siege.breach_progress` | 10 | progreso acumulado | 13 |
| `war.siege.artillery_vs_medieval` | 1/3 | — | 13 |
| `war.siege.artillery_vs_bastion` | 1/6 | — | 13 |
| `war.navy.control_ratio` | 3:1 | — | 13 |
| `war.navy.galley_autonomy` | 7–10 días; −5 %/semana fuera | — | 13 |
| `war.navy.storm.summer / winter` | 1–3 % / 5–12 % | mensual | 13 |
| `war.occupation.control_growth` | +5 % mensual hasta 0,5 × objetivo | — | 13 |

### Tecnología, clima y epidemias

| ID | Valor inicial | Unidad | Sección |
| --- | --- | --- | --- |
| `tech.lead.N.1300_1500` | 25 | años | 14 |
| `tech.lead.N.1500_1750 / 1750_1914 / 1914_1991 / 1991_2060` | 30 / 20 / 12 / 10 | años | 14 |
| `tech.lead.cost_curve` | 1 + 0,5 × (años/10)² (1,0 desde 1914) | — | 14 |
| `tech.diffusion.rate` | 0,02 / 0,05 / 0,15 / 0,40 | manuscrito / imprenta / telégrafo / redes | 14 |
| `tech.adoption.r` | 0,15 | trimestral | 14 |
| `tech.adoption.seed` | 1 % | — | 14 |
| `tech.sage_year.cost.1300` | 8–15 | uc | 14 |
| `clim.weight.strict / dynamic / alt / sandbox` | 0,85 / 0,60 / 0,30 / 0 | — | 15 |
| `clim.noise.spatial_corr / temporal_corr` | 0,6 / 0,3 | — | 15 |
| `epi.plague.beta / gamma / cfr` | 1,60 / 0,90 / 50–60 % | semanal | 15 |
| `epi.plague.immunity_loss` | 10 % | anual | 15 |
| `epi.plague.spark` | 0,0008 × tráfico × clima | semanal | 15 |
| `epi.quarantine.import_reduction` | 70 % | — | 15 |
| `epi.lazaretto.beta_reduction` | 20 % | — | 15 |

### Personajes, historia e IA

| ID | Valor inicial | Unidad | Sección |
| --- | --- | --- | --- |
| `chr.skill.mean` | 8 | 0–20 | 16 |
| `chr.regency.age` | 16 (por cultura) | años | 16 |
| `chr.regency.authority` | ×0,6 | — | 16 |
| `chr.usurpation.base` | 0,3 % | mensual | 16 |
| `chr.weight.formula` | 1 − 0,8 × I | — | 16 |
| `chr.historical_template.p` | 0,9 / 0,6 / 0,25 / 0 | estricto / dinámico / alternativo / sandbox | 16 |
| `hist.activation / maintenance` | 0,60 / 0,40 | plausibilidad | 07 |
| `hist.mode_factor` | 1,2 / 1,0 / 0,6 / 0 | — | 07 |
| `hist.divergence.cutoff` | 60 | divergencia | 07 |
| `hist.bias.cap` | +20 | pu por acción | 07 |
| `ai.pu.definition` | 1 % de los ingresos anuales | — | 17 |
| `ai.discount.base / long / short` | 0,10 / 0,05 / 0,20 | anual | 17 |
| `ai.plan.hysteresis` | 15 % | — | 17 |
| `ai.war.threshold` | +5 a +25 | pu | 17 |
| `ai.reserve.months.peace / war` | 3 / 6 | meses | 17 |
| `ai.budget.share_of_tick` | ≤ 25 % | — | 17 |

## Anexo AJ · Estado inicial cuantitativo de la vertical (1300)

Valores **de trabajo** para construir el escenario de 1300 y para que 101 Lab tenga un punto de partida. Confianza C salvo indicación; la Biblia histórica debe sustituirlos por estimaciones con fuente antes de la Fase 5. Población en miles de personas; ingresos en uc anuales; el ejército es la fuerza movilizable en una campaña, no el total teórico.

| Entidad | Provincias en el slice | Población (miles) | Ingresos (uc/año) | Ejército movilizable | Flota | Deuda (uc) | Control medio | Legitimidad | Institucionalización (I) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Imperio bizantino | 70 | 1.800 (1.200–2.500) | 465.000 (B en el orden de magnitud) | 4.000–6.000 (mercenarios y guarniciones) | 0–5 galeras | 120.000 | 55 % | 55 | 0,50 |
| Beylik otomano | 6 | 60 (30–120) | 12.000 | 1.500–3.000 (más voluntarios de frontera atraídos por el botín) | — | 0 | 70 % | 65 | 0,10 |
| Beylik de Germiyan | 14 | 250 | 60.000 | 6.000–9.000 | — | 0 | 55 % | 60 | 0,20 |
| Karamán | 12 | 220 | 50.000 | 6.000–8.000 | — | 0 | 55 % | 60 | 0,20 |
| Beylik de Karasi | 5 | 70 | 15.000 | 2.000–3.000 | 6 barcas de corso | 0 | 60 % | 60 | 0,12 |
| Beylik de Menteşe | 5 | 80 | 22.000 | 2.000–3.000 | 20 barcas de corso | 0 | 60 % | 60 | 0,12 |
| Reino de Serbia | 28 | 700 | 150.000 (plata de Brskovo) | 12.000–16.000 | — | 10.000 | 50 % | 65 | 0,30 |
| Imperio búlgaro | 22 | 600 | 80.000 | 8.000–12.000 | — | 15.000 | 45 % | 50 | 0,30 |
| Despotado de Epiro | 10 | 200 | 35.000 | 3.000–5.000 | 2 galeras | 5.000 | 50 % | 55 | 0,35 |
| Tesalia | 8 | 150 | 30.000 | 2.500–3.500 | — | 0 | 50 % | 50 | 0,30 |
| Principado de Acaya | 10 | 180 | 40.000 | 2.000–3.000 (≈ 600 caballeros) | 2 galeras | 10.000 | 55 % | 55 | 0,35 |
| Ducado de Atenas | 6 | 120 | 35.000 | 1.500–2.500 | — | 0 | 60 % | 60 | 0,35 |
| República de Venecia (posesiones del slice; núcleo externo) | 9 | 250 en el slice | 400.000 (Estado completo) | 2.000 en guarniciones | 30–60 galeras movilizables | 400.000 (deuda consolidada al 5 %) | 75 % | 75 | 0,60 |
| República de Génova (Pera, Caffa; núcleo externo) | 4 | 60 en el slice | 300.000 (Estado completo) | 1.000 en guarniciones | 30–50 galeras | 200.000 | 65 % | 50 (facciones) | 0,45 |
| Reino de Hungría | 45 | 2.000 | 250.000 | 15.000–25.000 | — | 0 | 40 % | 45 (crisis inminente) | 0,30 |
| Reino de Chipre | 10 | 120 | 120.000 (azúcar y Famagusta) | 2.500–3.500 | 6 galeras | 10.000 | 70 % | 55 | 0,45 |
| Imperio de Trebisonda | 6 | 200 | 70.000 | 2.500–3.500 | 4 galeras | 5.000 | 60 % | 55 | 0,45 |
| Armenia cilicia | 10 | 300 | 80.000 (Ayas) | 5.000–7.000 | 2 galeras | 20.000 (tributo mongol) | 55 % | 50 | 0,40 |

**Entidades de borde (valores para sus mercados externos y su IA simplificada):** sultanato mameluco (ingresos ≈ 2–3 millones de uc; ejército de élite de 10.000–15.000 mamelucos), Iljanato (en crisis fiscal en vías de reforma), Horda de Oro (tributos de la Rus; caballería masiva), Ragusa, Bosnia, voivodatos valacos, Hospitalarios y Compañía Catalana (≈ 6.500 personas, sin territorio; disponible desde 1302 si se cumple su situación).

**Comprobaciones de coherencia del escenario:**

- La suma de poblaciones del slice (≈ 7,4 millones en las 18 entidades, más los bordes) debe quedar dentro del rango que proponga la Biblia histórica para la región; si no, se ajustan las provincias, no los totales nacionales.
- La relación ingresos/población de cada entidad debe estar entre 0,1 y 0,6 uc por habitante y año para los Estados agrarios, y puede superarla para los comerciales (Venecia, Génova, Chipre) por aduanas y monopolios.
- El ejército movilizable no puede superar el 3 % de la población en Estados agrarios con levas ni el 1 % en Estados que dependen de mercenarios, salvo en los beyliks fronterizos (hasta un 5 % de jinetes de frontera).

## Anexo AK · Mercados de la vertical

| Mercado | Controlador en 1300 | Población urbana (miles, C) | Exporta | Importa | Grano inicial (uc/t) | Conexiones principales |
| --- | --- | --- | --- | --- | --- | --- |
| Constantinopla | Bizancio | 100 (B) | Seda, manufacturas de lujo, servicios | Grano, pescado, sal, pieles, esclavos (sistema de población) | 10,5 | Pera, Tesalónica, Bursa, Caffa, Venecia (ext.), Génova (ext.) |
| Pera (Gálata) | Génova (barrio autónomo) | 15 | Comercio de tránsito | — | 10,5 (comparte con Constantinopla) | Caffa, Quíos, Génova (ext.) |
| Tesalónica | Bizancio | 40 | Grano de Macedonia, vino, paño | Especias, sal | 8,5 | Constantinopla, Skopie, Negroponte, Ragusa |
| Bursa (Prusa) | Bizancio (hasta su posible caída) | 15 | Seda en bruto, fruta | Grano | 9,0 | Constantinopla, Nicea, Konya |
| Konya | Karamán / disputa | 25 | Lana, alfombras, caballos | Especias, paño | 7,5 | Antalya, Bursa, Ayas, Tabriz (ext.) |
| Esmirna-Focea | Bizancio, genoveses (Focea) y beyliks | 20 | Alumbre, grano, frutos secos | Paño | 8,5 | Quíos, Constantinopla, Venecia (ext.) |
| Antalya | Beyliks del sur | 10 | Madera, grano | Especias | 8,0 | Chipre, Alejandría (ext.), Konya |
| Trebisonda | Trebisonda | 40 | Seda (tránsito), plata, avellanas | Paño, vino | 9,5 | Tabriz (ext.), Caffa, Sinope, Constantinopla |
| Sinope | Beylik de Candar / disputa | 10 | Madera, pescado | Grano | 9,0 | Caffa, Trebisonda, Constantinopla |
| Caffa | Génova | 20 | Grano, pescado salado, pieles, cera, personas esclavizadas (sistema de población) | Paño, vino, sal | 6,5 | Tana, Sarai (ext.), Constantinopla, Trebisonda |
| Tana (borde) | Venecia y Génova, bajo la Horda | 8 | Grano, pescado, pieles | Paño | 6,0 | Sarai (ext.), Caffa |
| Tarnovo | Bulgaria | 15 | Grano, ganado, miel | Sal, paño | 7,0 | Constantinopla, Vidin, Mesembria |
| Skopie | Serbia | 15 | Plata, ganado | Paño, sal | 7,5 | Tesalónica, Ragusa |
| Ragusa | Ragusa (bajo Venecia) | 8 | Servicios comerciales, plata de tránsito | Grano | 10,0 | Venecia (ext.), Skopie, Tesalónica |
| Buda | Hungría | 10 | Grano, ganado, cobre, oro (Kremnica, más tarde) | Paño, especias | 6,0 | Viena (borde), Belgrado, Venecia (ext.) |
| Candía | Venecia | 25 | Vino, grano, queso | Paño, madera | 8,5 | Venecia (ext.), Negroponte, Modón-Corón, Alejandría (ext.) |
| Negroponte | Venecia y señores lombardos | 10 | Grano, seda | Paño | 8,5 | Tesalónica, Atenas, Candía |
| Modón-Corón | Venecia | 6 | Escala de galeras, vino | Grano | 9,0 | Venecia (ext.), Candía, Acaya |
| Famagusta | Chipre | 30 | Azúcar, algodón, tránsito de especias | Grano, madera | 9,0 | Ayas, Alejandría (ext.), Venecia (ext.), Génova (ext.) |
| Ayas | Armenia cilicia | 15 | Tránsito de especias y seda, algodón | Grano, paño | 8,5 | Tabriz (ext.), Famagusta, Konya |
| Tabriz (externo) | Iljanato | 200 (C) | Seda, especias, perlas | Paño, plata | Externo | Trebisonda, Ayas |
| Alejandría (externo) | Mamelucos | 100 (C) | Especias, azúcar, lino | Madera, metales, paño, esclavos militares | Externo | Famagusta, Candía, Venecia (ext.) |
| Sarai (externo) | Horda de Oro | 75 (C) | Pieles, cera, grano, personas esclavizadas | Paño, plata | Externo | Tana, Caffa |
| Venecia (externo) | Venecia | 100 (B) | Paño, vidrio, servicios, plata | Especias, seda, grano, alumbre | Externo | Candía, Modón-Corón, Constantinopla, Ragusa |
| Génova (externo) | Génova | 60 (B) | Paño, servicios financieros | Alumbre, grano, especias | Externo | Pera, Caffa, Quíos, Famagusta |

Los mercados externos tienen precios con su propia dinámica (un recorrido aleatorio acotado alrededor de su precio base, alimentado por la anomalía climática de su macrorregión) y una **capacidad de absorción** por bien, para que no puedan comprar ni vender cantidades ilimitadas.

## Anexo AL · Especificación de 101 Script: condiciones y efectos (borrador)

101 Script es el lenguaje **declarativo** con el que el contenido base y los mods expresan condiciones (cuándo ocurre algo) y efectos (qué cambia). No es un lenguaje de programación general: no tiene bucles abiertos, variables mutables, acceso al reloj, a la red ni a archivos, ni aleatoriedad propia. Se escribe en RON, como el resto del contenido, y se compila a un árbol validado. La decisión sobre un lenguaje de scripting completo (Luau o Rhai) sigue abierta (A-09) y, si se toma, se apoyará en esta misma capa de efectos.

### Tipos

| Tipo | Representación | Ejemplo |
| --- | --- | --- |
| `Bool` | Verdadero o falso | `true` |
| `Int` | Entero de 64 bits | `12` |
| `Ratio` | Puntos básicos (10.000 = 1,0) | `Ratio(0.25)` en el texto; 2.500 internamente |
| `Money` | uc con 4 decimales | `Money(1200)` |
| `Qty` | Cantidad con 3 decimales | `Qty(350.5)` |
| `Day` | Fecha absoluta | `Date(1302, 5, 14)` |
| `Years` / `Months` | Duración | `Years(10)` |
| Identificadores | Tipados | `Entity("byzantium")`, `Province("constantinople")`, `Culture("romaic_greek")` |
| Ámbitos | Sujetos de evaluación | `ThisEntity`, `ThisProvince`, `Role("besieger")`, `Ruler(ThisEntity)` |

Los tipos no se mezclan sin conversión explícita: comparar `Money` con `Ratio` es un error de compilación.

### Gramática (EBNF simplificada sobre RON)

```text
condition   = all | any | not | compare | predicate | weighted | in_window ;
all         = "All(" condition { "," condition } ")" ;
any         = "Any(" condition { "," condition } ")" ;
not         = "Not(" condition ")" ;
compare     = "Compare(" value "," op "," value ")" ;
op          = "Lt" | "Le" | "Eq" | "Ge" | "Gt" | "Ne" ;
weighted    = "Weighted(condition:" condition ", weight:" int ")" ;
in_window   = "InWindow(start:" year ", end:" year ")" ;
value       = const | var | "Add(" value "," value ")" | "Sub(" … ")" | "Mul(" … ")"
            | "Div(" … ")" | "Min(" … ")" | "Max(" … ")" | "Clamp(" value "," value "," value ")"
            | "Count(" scope_set "," condition ")" | "Sum(" scope_set "," var ")" ;
var         = "Var(" scope "," path ")" ;            (* p. ej. Var(ThisEntity, "treasury") *)
scope_set   = "ProvincesOf(" scope ")" | "ProvincesIn(" region ")" | "NeighborsOf(" scope ")"
            | "EntitiesIn(" region ")" | "CohortsIn(" scope ")" | "Vassals(" scope ")" ;
effect      = "Effects([" effect_item { "," effect_item } "])" ;
```

### Predicados más usados (catálogo inicial)

| Predicado | Significado |
| --- | --- |
| `Owns(province)` / `Controls(province)` | Soberanía / control de hecho |
| `Controls(region, min_share)` | Cuota de provincias controladas en una región |
| `HasTech(tech, stage)` | Técnica en la etapa indicada o superior |
| `HasLaw(category, option)` | Ley vigente |
| `AtWar(with)` / `AtWarAny` | Estado de guerra |
| `RelationAbove(with, dimension, value)` | Dimensión de relación |
| `RulerAge(op, years)` / `RulerHasTrait(trait)` | Gobernante |
| `HeirExists` / `Regency` | Sucesión |
| `CultureShare(province, culture, op, ratio)` | Composición cultural |
| `ReligionShare(scope, religion, op, ratio)` | Composición religiosa |
| `PriceAbove(market, good, multiple_of_base)` | Precios |
| `TreasuryBelow(months_of_expenses)` | Finanzas |
| `ThreatAbove(from, value)` | Amenaza percibida |
| `FortLevelBelow(province, level)` | Fortificación |
| `NavalAllyNear(role)` | Presencia naval aliada a ≤ 10 días |
| `SituationActive(id)` / `SituationStage(id, stage)` | Estado de otras situaciones |
| `Chance(ratio, key)` | Azar determinista con el RNG por contador; `key` obligatoria para que el resultado no dependa del orden |

### Efectos permitidos

Todo efecto produce **deltas** que pasan por la misma validación e invariantes que los de los sistemas, y registra su origen en el registro causal.

| Efecto | Qué hace | Restricciones |
| --- | --- | --- |
| `AddContribution(target, var, amount, duration)` | Añade una contribución con origen a una variable visible (legitimidad, agravio, eficacia…) | Solo variables declaradas como “contribuibles”; magnitud limitada por variable |
| `TransferMoney(from, to, amount)` | Mueve dinero entre actores | Conservación exacta; falla si no hay fondos |
| `TransferGoods(market_or_stock, to, good, qty)` | Mueve bienes | Conservación exacta |
| `DestroyGoods(stock, good, qty, cause)` | Destruye bienes (incendio, saqueo) | Requiere causa |
| `MovePeople(from_cohort, to_province, qty, origin)` | Mueve personas | Conservación exacta; respeta la condición jurídica |
| `ChangeCohortAttribute(cohort, attr, delta)` | Cambia cultura, religión u ocupación de una parte de una cohorte | A través de la tabla de transición (sección 09) |
| `ProposeLaw(entity, category, option)` | Inicia el proceso de reforma | No aplica la ley directamente |
| `ChangeRelation(a, b, dimension, delta)` | Modifica una dimensión diplomática | Límites por dimensión |
| `SpawnCharacter(template, dynasty, location)` | Crea un personaje | Plantilla validada; fechas coherentes |
| `SpawnArmy(entity, composition, location, origin)` | Crea una fuerza (rebeldes, compañía) | Las personas salen de cohortes reales |
| `StartSituation(id)` / `AdvanceStage(id)` | Control de situaciones | Solo desde 101 History o eventos de la misma situación |
| `Notify(target, alert_id, params)` | Lanza una alerta | Catálogo del Anexo AO |
| `QueueEvent(event_id, target, delay)` | Programa un evento | Retraso mínimo de un día |

**Prohibido por diseño:** crear dinero de la nada (la acuñación pasa por el sistema monetario), crear personas sin nacimiento ni migración, fijar valores directamente (`Set`) sobre variables simuladas, modificar el mapa físico, leer el estado real de otro país desde la IA (solo `Estimated(...)`).

### Límites de compilación

| Límite | Valor |
| --- | --- |
| Profundidad del árbol | 16 |
| Nodos por condición | 512 |
| Conjuntos iterados (`Count`, `Sum`) | ≤ 2 anidados; tamaño máximo 5.000 elementos |
| Efectos por evento u opción | 32 |
| Coste estimado por evaluación | ≤ 50 µs en el PC de referencia (el compilador lo estima y avisa) |

### Ejemplo: EV-001 “La paga de los catalanes” en 101 Script

```ron
Event(
    id: "ev_catalan_pay",
    situation: Some("catalan_company_east"),
    scope: Role("employer"),
    trigger: All([
        SituationStage("catalan_company_east", "employed"),
        Compare(Var(Role("company"), "pay_arrears_months"), Ge, Int(3)),
        Compare(Var(ThisEntity, "treasury"), Lt, Var(Role("company"), "arrears_amount")),
    ]),
    mean_time_to_happen: Months(1),
    options: [
        Option(id: "pay_what_we_have",
            effects: Effects([
                // paga parcial: todo el tesoro disponible por encima de la reserva mínima
                TransferMoney(ThisEntity, Role("company"), Var(ThisEntity, "treasury_above_reserve")),
                AddContribution(Role("company"), "mercenary_loyalty", Int(8), Months(6)),
            ])),
        Option(id: "debase_to_pay",
            effects: Effects([
                ProposeLaw(ThisEntity, "coinage", "debase_10pct"),
                QueueEvent("ev_catalan_paid_in_debased_coin", ThisEntity, Days(30)),
            ])),
        Option(id: "grant_lands",
            effects: Effects([
                // la cesión de tierras crea una base propia: riesgo de Estado dentro del Estado
                QueueEvent("ev_catalan_land_grant_choice", ThisEntity, Days(1)),
                AddContribution(Role("company"), "mercenary_loyalty", Int(15), Years(2)),
            ])),
        Option(id: "order_disbandment",
            effects: Effects([
                AddContribution(Role("company"), "mercenary_loyalty", Int(-40), Years(1)),
                AddContribution(ThisEntity, "legitimacy@army", Int(-4), Years(1)),
            ])),
    ],
    loc_key: "ev_catalan_pay",
    sources: [Source(ref: "bib:catalan_company", confidence: B)],
)
```

### Mensajes de error (ejemplos)

```text
error[S012]: tipos incompatibles en Compare
  --> data/history/events/catalan.ron:9:17
   |
 9 |   Compare(Var(Role("company"), "pay_arrears_months"), Ge, Money(2)),
   |                                                           ^^^^^^^^ se esperaba Int, se encontró Money
   = ayuda: los meses de atraso son un entero; usa Int(2)

error[S031]: efecto prohibido en contenido: Set sobre variable simulada
  --> mods/mi_mod/events/oro.ron:22:9
   = nota: las variables simuladas solo cambian con efectos con origen (AddContribution, TransferMoney…)
```

## Anexo AO · Catálogo de alertas y notificaciones

| ID | Alerta | Prioridad | Disparador | Pausa por defecto | Acción sugerida |
| --- | --- | --- | --- | --- | --- |
| AL-001 | Declaración de guerra contra ti | Crítica | Comando de guerra recibido | Sí | Abrir guerra |
| AL-002 | Muerte del gobernante | Crítica | Muerte de tu gobernante | Sí | Abrir sucesión |
| AL-003 | Rebelión abierta | Crítica | Presión > 70 en un grupo | Sí | Abrir política |
| AL-004 | Impago inminente | Crítica | Tesoro < servicio de la deuda del próximo mes | Sí | Abrir presupuesto |
| AL-005 | Capital sitiada | Crítica | Asedio en tu capital | Sí | Abrir asedio |
| AL-006 | Epidemia en tu territorio | Alta | Primer caso en una provincia propia | Sí | Modo de mapa de epidemias |
| AL-007 | Ejército enemigo cruza la frontera | Alta | Ejército hostil entra en provincia propia | Opcional | Centrar mapa |
| AL-008 | Batalla terminada | Alta | Fin de una batalla con un ejército propio | Opcional | Informe de batalla |
| AL-009 | Asedio terminado | Alta | Rendición o asalto | Opcional | Informe |
| AL-010 | Propuesta de tratado | Alta | Propuesta recibida | Sí | Negociación |
| AL-011 | Tratado a punto de vencer | Media | 3 meses antes del vencimiento | No | Diplomacia |
| AL-012 | Mercenarios sin paga | Alta | Atraso ≥ 2 meses | Opcional | Presupuesto |
| AL-013 | Motín | Crítica | Motín de una compañía | Sí | Ejército |
| AL-014 | Hambruna | Alta | Cobertura < 0,7 en una provincia con > 10.000 hab. | Opcional | Provincia |
| AL-015 | Precio disparado | Media | Precio de un bien básico > 1,5 × base | No | “¿Por qué?” del precio |
| AL-016 | Demanda de un grupo de interés | Media | Agitación (presión > 20) | No | Política |
| AL-017 | Movimiento organizado | Alta | Presión > 45 | Opcional | Política |
| AL-018 | Conjura descubierta | Alta | Descubrimiento | Sí | Corte |
| AL-019 | Heredero nacido | Baja | Nacimiento | No | Dinastía |
| AL-020 | Heredero menor de edad | Media | El gobernante enferma con heredero < 16 | No | Dinastía |
| AL-021 | Regencia iniciada | Alta | Inicio de regencia | Sí | Corte |
| AL-022 | Situación histórica activada | Media | Activación visible para ti | Opcional | Panel de situación |
| AL-023 | Etapa de situación | Media | Cambio de etapa | No | Panel de situación |
| AL-024 | Coalición contra ti | Alta | Formación de coalición | Sí | Diplomacia |
| AL-025 | Vasallo inquieto | Media | Utilidad de independencia > seguir + 5 | No | Vasallos |
| AL-026 | Vasallo rebelde | Alta | Rebelión de vasallo | Sí | Guerra |
| AL-027 | Técnica descubierta | Baja | Descubrimiento propio | No | Tecnología |
| AL-028 | Técnica conocida pero no adoptada | Baja | 10 años con cuota < 5 % | No | “¿Por qué?” de la adopción |
| AL-029 | Ruta cortada | Media | Ruta comercial con volumen > umbral bloqueada | No | Comercio |
| AL-030 | Flota perdida en tormenta | Media | Pérdida > 20 % | No | Flota |
| AL-031 | Ejército sin suministro | Alta | Desgaste > 5 % mensual | Opcional | Ejército |
| AL-032 | Leva a punto de disolverse | Media | Fin del plazo de servicio | No | Ejército |
| AL-033 | Reforma aprobada / rechazada | Media | Decisión de la institución | No | Política |
| AL-034 | Implantación detenida | Alta | Presión de perjudicados > 70 | Opcional | Política |
| AL-035 | Bancarrota de un acreedor | Media | Quiebra de un acreedor tuyo o de quien te debe | No | Presupuesto |
| AL-036 | Devaluación detectada | Media | Valor percibido de tu moneda cae > 5 % | No | Moneda |
| AL-037 | Emigración masiva | Media | Pérdida > 2 % de una provincia en un mes | No | Provincia |
| AL-038 | Refugiados llegan | Media | Llegada > 5 % de la población local | No | Provincia |
| AL-039 | Terremoto | Alta | Terremoto en provincia propia | Opcional | Provincia |
| AL-040 | Mala cosecha prevista | Media | Anomalía climática −2 o peor en tu macrorregión | No | Clima |
| AL-041 | Identidad proclamable | Media | Condiciones de proclamación cumplidas | Opcional | Decisión |
| AL-042 | Restauración posible | Baja | Movimiento de restauración activo en tu territorio | No | Política |
| AL-043 | Asesor actuó | Baja | Acción de un asesor | No | Registro del asesor |
| AL-044 | Asesor bloqueado por una regla | Media | Una regla impidió una acción necesaria | No | Configuración del asesor |
| AL-045 | Recordatorio del jugador | Según el jugador | Fecha programada | Según el jugador | — |

**Reglas:** las alertas de la misma clase en el mismo mes se agrupan (“3 precios disparados”); cada alerta enlaza a su “¿por qué?”; ninguna alerta crítica se puede silenciar del todo, solo quitarle la pausa; el jugador puede crear filtros por prioridad y por región.

## Anexo AM · Traza de un día de simulación

Traza comentada del **14 de julio de 1302** en la vertical, con el calendario de la sección 21. Sirve como referencia para la especificación `apply-and-invariants.md` y como modelo del registro de depuración (F-DEV-01).

```text
[día 1302-07-14 | tick 4.577 | semilla 0x5EED_0101]
fase 0  comandos         3 recibidos (jugador: 1; IA: 2, emitidos el día 13)
                          · byzantium  SetBudget(line: mercenaries, +1.500 uc/mes)       válido
                          · ottoman    MoveArmy(army#41, [nicaea_rural, prusa_rural])     válido
                          · venice     ProposeTreaty(→ byzantium, [Truce(10y), …])       válido
fase 1  clima             sin cambio de estación (verano); anomalía anual ya fijada (Tracia: humedad −2)
fase 2  movimiento        army#41 llega a prusa_rural (3,9 días); flota genovesa#7 en Mármara
fase 3  batallas          ninguna; asedio de Prusa: progreso 0,00 (sin máquinas), comida estimada 13,6 meses
fase 4  suministro        army#41 consume 1,4 t grano y 9 t forraje; capacidad local 2,1 t → sin desgaste
fase 5  epidemias         (semanal; hoy no toca a ninguna provincia del slice)
fase 6  mercados          hoy toca a 4 mercados (escalonamiento): constantinople, caffa, tarnovo, famagusta
                          · constantinople/grain: oferta 610 t, demanda 1.020 t, existencias 58 %
                            presión 0,672 + 0,105 → cambio +7,8 % → 12,46 uc/t
                            ledger: [sequía Tracia +2,1][existencias +0,4][ejército de Adrianópolis +0,3]
                          · caffa/grain: margen hacia Constantinopla 3,9 uc/t → flujo 140 t (capacidad libre)
fase 7  producción        hoy cierran mes 11 provincias; cosecha de cereal en thrace_* (multiplicador 0,65)
fase 8  demografía        11 provincias; nicaea_city: −88 personas (detalle en el registro)
fase 9  finanzas          cierre mensual de 1 Estado (karasi): ingresos 1.180 uc, gastos 1.090 uc
fase 10 política          byzantium/clergy: legitimidad 61 → 60 (prosperidad −0,6; impuesto extraordinario −0,4)
fase 11 diplomacia        tratado venice→byzantium registrado como propuesta pendiente (AL-010 al jugador)
fase 12 tecnología        progreso de 'compass_portolan' en genoa +0,4 años-sabio (difusión desde venice)
fase 13 personajes        sin muertes; salud de andronikos_ii 58
fase 14 history           'catalan_company_east' plausibilidad 0,90 (activa, etapa 'negotiation')
fase 15 IA                14 decisiones (presupuesto usado: 1,7 ms de 2,5 ms)
                          · ottoman: mantener bloqueo de Prusa (utilidad +37 frente a +11)
                          · catalan_company: aceptar contrato si adelanto ≥ 4 meses (estimado: 3,5) → esperar
fase 16 ledger            212 contribuciones nuevas; 9 agregados actualizados
fase 17 invariantes/hash  OK (bienes, dinero, deuda, población, no negatividad)
                          hash global 7c1e…a90f · population 33ab… · economy 91d0… · military 0e4f…
```

**Qué enseña la traza:** el comando del jugador (más presupuesto para mercenarios) no tiene efecto hasta el cierre mensual de Bizancio; los comandos de la IA del día 13 se ejecutan hoy; el precio del grano en Constantinopla se explica con tres contribuyentes; la decisión de la Compañía depende de una estimación que el jugador puede cambiar ofreciendo medio mes más de adelanto.

## Anexo AN · Partida de ejemplo comentada: Bizancio, 1300–1330

Una partida **hipotética** en modo histórico dinámico, escrita para mostrar cómo encajan los sistemas. No es un guion: otra semilla o decisiones distintas producirían otra historia. Las cifras provienen de las especificaciones de la v0.7.

### 1300–1302: el presupuesto como primer enemigo

- **Situación de partida (Anexo AJ):** 465.000 uc de ingresos, 470.000 de gastos, sin flota, mercenarios caros, exenciones aduaneras para Venecia y Génova.
- **Decisión 1 (enero de 1300):** el jugador intenta gravar las tierras monásticas (sección 11). La previsión dice que se aprobaría, pero que la legitimidad del clero bajaría unos 25 puntos. Opta por la **reforma parcial** (solo grandes monasterios): +12.000 uc anuales, −9 de legitimidad del clero.
- **Consecuencia (1301):** la guerra con Venecia (heredada) sigue; la flota veneciana saquea dos islas. El agotamiento llega a 48 (bajas 6, impuestos extraordinarios 14, precio del grano 9, ocupación 11, duración 8).
- **Decisión 2 (1302):** acepta la tregua veneciana sin una de las islas reclamadas (ejemplo de la sección 12). Agravio con Venecia: 55. Se libera presupuesto para Anatolia.

### 1302–1305: la frontera de Bitinia y la llegada de los catalanes

- **Derrota en la frontera (1302):** un ejército de 2.000 hombres mal pagados pierde ante 4.500 jinetes otomanos y voluntarios de frontera (sección 13). La seguridad de Bitinia cae a 0,45; empieza la emigración hacia Constantinopla (sección 09).
- **La situación catalana se activa** (plausibilidad 0,90; Anexo AM). El jugador ofrece 4 meses de adelanto (≈ 26.000 uc, pagados con un préstamo genovés al 14 %, sección 10). La Compañía acepta.
- **1303–1304:** la Compañía vence dos veces en Anatolia; la amenaza turca en el panel diplomático baja de 72 a 58. Pero su paga cuesta ≈ 6.500 uc al mes y el tesoro solo cubre dos tercios.
- **Decisión 3 (1304):** el jugador elige **devaluar el hiperpirón un 10 %** para pagar (EV-001). El mercado de Constantinopla detecta la devaluación en unos cuatro meses (sección 10); el precio del grano en hiperpirones sube un 11 %, la legitimidad de los mercaderes baja 6 y la de los pobres urbanos 4.

### 1305–1311: el contrato se rompe

- **1305:** los atrasos vuelven a acumularse (3 meses). La lealtad de la Compañía cae de 52 a 28 en un año (atrasos −30, victorias +9, afinidad religiosa −3). Un evento ofrece **tierras en lugar de dinero**; el jugador lo rechaza para no crear un Estado dentro del Estado.
- **1306–1307:** con 4 meses de atraso y lealtad < 20, la Compañía se convierte en entidad independiente (sección 13) y saquea Tracia. El forrajeo libre sube el agravio de los campesinos tracios +10 al mes y baja sus existencias un 50 %; el precio del grano en Constantinopla llega a 14,8 uc/t.
- **1308–1311:** la Compañía se desplaza hacia Tesalia y Atenas buscando patrón. Su IA (personalidad “mercenaria”) calcula que conquistar un ducado vale más que vender sus servicios. En esta semilla, vence al duque de Atenas (1311) y se convierte en una entidad territorial. La crónica registra el cambio sin que exista un evento “batalla de 1311”: lo produjeron el contrato, la lealtad y las utilidades.

### 1311–1320: reconstruir la flota

- **Decisión 4:** el jugador fija una ambición “Reconstruir la flota”. El asesor económico (reglas: deuda ≤ 40 % de ingresos, sin devaluaciones) propone 4 galeras al año (600 uc cada una, 45 de mantenimiento mensual) financiadas con la renegociación del privilegio aduanero genovés.
- **Negociación con Génova (1313):** el jugador ofrece confirmar el barrio de Pera a cambio de reducir la exención del 100 % al 50 %. La aceptación genovesa es −6 (interés comercial alto, pero agravio por la devaluación de 1304). Añade un **préstamo** al 9 % con las aduanas como garantía: la aceptación sube a +8 y Génova firma. Ingresos aduaneros: +14.000 uc al año.
- **1316:** con 14 galeras, Bizancio controla el Mármara en verano (fuerza 3:1 frente a las barcas de Karasi). Las incursiones costeras de Karasi caen un 60 %; el control de Bitinia costera sube de 41 % a 52 %.

### 1320–1330: guerra civil y Bursa

- **1320:** el emperador tiene 61 años y su nieto, coemperador, forma una facción con la aristocracia joven de Tracia (fuerza 0,58 frente a la del emperador; sección 16). La situación “guerras civiles bizantinas” pasa a la etapa 2.
- **Decisión 5 (1321):** el jugador concede al nieto el gobierno de Tracia occidental para evitar la guerra. La presión aristocrática baja de 52 a 30, pero el control de esa región pasa a depender de la lealtad del nieto (44) y la recaudación de Tracia cae un 25 %.
- **Mientras tanto, en Bitinia:** la IA otomana mantiene desde 1317 el bloqueo de Prusa (Bursa) con fortines (sección 17). Con la flota bizantina ocupada en el Mármara y la recaudación en caída, el jugador no puede romper el bloqueo por tierra. La comida de la ciudad se agota en 1326; la probabilidad mensual de rendición supera el 50 % y la ciudad se rinde.
- **Crónica de la partida (1330):** Bizancio conserva Tracia y Macedonia, tiene flota propia y una deuda del 38 % de sus ingresos; ha perdido Bitinia interior y Atenas está en manos de una compañía catalana. El índice de divergencia de la región es 18: **reconocible, pero no idéntico** a la historia real (en la que Bizancio no reconstruyó una flota comparable). El jugador puede abrir cada eslabón en el registro causal.

### Qué demuestra la partida

| Pilar | Evidencia en la partida |
| --- | --- |
| Causalidad explicable | Cada desenlace (rebelión catalana, caída de Bursa) se puede rastrear hasta decisiones y números concretos. |
| Historia condicional | La compañía conquista Atenas porque las utilidades y la ocasión lo permiten, no por fecha; con otra paga no habría ocurrido. |
| Profundidad sistémica | Una devaluación afecta a precios, legitimidad, crédito con Génova y una negociación nueve años después. |
| Agencia | La flota reconstruida cambia el control costero y la economía del Mármara. |
| Legibilidad | Todas las cifras de esta narración están visibles para el jugador en paneles “¿por qué?”. |

## Anexo AP · Matriz de interacción entre sistemas

Cada fila es una **dependencia causal** que debe existir en el código y aparecer en el registro causal. Sirve para revisar que ningún sistema quede aislado (la “prueba de causalidad” de la sección 10) y para que los agentes sepan qué contrato tocan al cambiar una variable.

| De | A | Variable que transmite el efecto | Sección |
| --- | --- | --- | --- |
| Clima | Producción | Multiplicador de cosecha | 15 → 10 |
| Clima | Guerra | Duración del invierno, estado de caminos | 15 → 13 |
| Clima | Epidemias | Factor climático del reservorio; estacionalidad | 15 |
| Producción | Mercados | Oferta | 10 |
| Mercados | Población | Precio de las cestas → cobertura → NV | 10 → 09 |
| Población | Producción | Trabajadores en plazas | 09 → 10 |
| Población | Política | NV → legitimidad por prosperidad; agravio | 09 → 11 |
| Población | Guerra | Reserva movilizable | 09 → 13 |
| Población | Tecnología | Alfabetización → absorción y personas cualificadas | 09 → 14 |
| Población | Gobierno | Letrados → capacidad administrativa | 09 → 11 |
| Gobierno | Finanzas | Control efectivo → recaudación | 11 → 10 |
| Gobierno | Guerra | Control → reclutamiento; leyes de ejército | 11 → 13 |
| Gobierno | Población | Leyes de condición jurídica, religión y tierra → movilidad, migración | 11 → 09 |
| Finanzas | Guerra | Paga → moral y lealtad mercenaria | 10 → 13 |
| Finanzas | Política | Impuestos extraordinarios → legitimidad | 10 → 11 |
| Finanzas | Diplomacia | Deuda con extranjeros → dependencia | 10 → 12 |
| Moneda | Mercados | Valor percibido → nivel de precios | 10 |
| Moneda | Política | Inflación → legitimidad de mercaderes y pobres urbanos | 10 → 11 |
| Comercio | Epidemias | Tráfico entre provincias | 10 → 15 |
| Comercio | Tecnología | Contacto → difusión | 10 → 14 |
| Comercio | Diplomacia | Interés y dependencia | 10 → 12 |
| Guerra | Población | Bajas, refugiados, devastación | 13 → 09 |
| Guerra | Producción | Edificios dañados, campos devastados, trabajadores movilizados | 13 → 10 |
| Guerra | Mercados | Demanda militar, rutas cortadas, bloqueos | 13 → 10 |
| Guerra | Política | Victorias y derrotas → legitimidad; agotamiento → presión | 13 → 11 |
| Guerra | Diplomacia | Puntuación bélica, agravio, amenaza | 13 → 12 |
| Guerra | Epidemias | Tifus y disentería en campamentos; movimiento de tropas | 13 → 15 |
| Diplomacia | Comercio | Exenciones, aranceles, barrios, embargos | 12 → 10 |
| Diplomacia | Guerra | Alianzas, derecho de paso, coaliciones | 12 → 13 |
| Personajes | Gobierno | Capacidad de los cargos × peso personal | 16 → 11 |
| Personajes | Diplomacia | Matrimonios, reclamaciones, rasgos en la IA | 16 → 12 |
| Personajes | Guerra | Mando de ejércitos | 16 → 13 |
| Religión | Política | Legitimidad religiosa; política religiosa | 06 → 11 |
| Religión | Economía | Préstamo con interés, diezmo, propiedad eclesiástica | 06 → 10 |
| Tecnología | Producción | Modos de producción | 14 → 10 |
| Tecnología | Guerra | Unidades, artillería, fortificación | 14 → 13 |
| Tecnología | Gobierno | Tecnología de registros → eficacia institucional | 14 → 11 |
| Tecnología | Información | Correo, imprenta, telégrafo → factor de red | 14 → 12 |
| 101 History | IA | Sesgo histórico acotado | 07 → 17 |
| IA | Todos | Comandos (los mismos que el jugador) | 17 |
| Epidemias | Población | Mortalidad, huida | 15 → 09 |
| Epidemias | Mercados | Cuarentenas → tráfico; caída de demanda y oferta | 15 → 10 |
| Epidemias | Personajes | Muerte de personajes | 15 → 16 |

**Comprobación automática:** `cargo xtask causality-check` genera un escenario por fila, perturba la variable de origen y verifica que la de destino cambia en el sentido esperado y que el registro causal contiene la contribución. Una fila sin prueba es un error del CI desde la Fase 3.

## Anexo AQ · Protocolo de pruebas con jugadores

### Perfiles y calendario

| Fase | Sesiones al mes | Perfiles | Formato |
| --- | --- | --- | --- |
| 2–3 | 1 | Jugador veterano de gran estrategia | Remota, 60 min, pensar en voz alta |
| 4 | 2 | Veterano + aficionado a la historia | Remota, 90 min |
| 5 (vertical) | 4 | Veteranos, aficionados, un jugador nuevo en el género | Remota o presencial, 2 h; partida libre de 50 años |
| Acceso anticipado | Continuo | Comunidad | Telemetría con consentimiento + encuestas |

### Guion de una sesión de la vertical (2 horas)

| Minuto | Actividad | Qué se mide |
| --- | --- | --- |
| 0–5 | Presentación; consentimiento de grabación; sin explicar el juego | — |
| 5–65 | Primera hora con el tutorial de la sección 18; el observador no ayuda | Tiempo hasta la primera consulta de “¿por qué?” sin indicación; errores de navegación |
| 65–95 | Juego libre hasta completar 50 años | Decisiones tomadas; pausas; paneles más usados |
| 95–110 | Entrevista: “Explica tres cosas importantes que pasaron y por qué” | Exactitud de las explicaciones (rúbrica) |
| 110–120 | Cuestionario | Escalas de abajo |

### Rúbrica de explicación (por suceso)

| Puntuación | Criterio |
| --- | --- |
| 0 | No sabe por qué ocurrió. |
| 1 | Da una causa genérica (“mala suerte”, “la IA es agresiva”). |
| 2 | Da una causa correcta del sistema. |
| 3 | Da la cadena de dos o más causas, coherente con el registro causal. |

**Objetivo de la vertical (AH):** la mayoría de jugadores obtiene ≥ 2 en al menos tres sucesos.

### Cuestionario (escala de 1 a 7)

1. Entendía qué estaba pasando en mi país.
2. Cuando algo cambiaba, sabía dónde mirar para entender por qué.
3. Mis decisiones tenían consecuencias que podía ver.
4. El mundo se sentía histórico y a la vez abierto.
5. La interfaz me dejaba encontrar la información sin perderme.
6. Quiero seguir jugando esta partida.
7. Recomendaría el juego a alguien que disfruta del género.

Más tres preguntas abiertas: lo más confuso, lo más memorable, lo que cambiarías primero.

### Métricas de la sesión

| Métrica | Objetivo de la vertical |
| --- | --- |
| Tiempo hasta la primera consulta espontánea de “¿por qué?” | < 20 minutos |
| Consultas de “¿por qué?” por hora de juego | ≥ 10 |
| Abandonos del tutorial | < 20 % |
| Puntuación media de las preguntas 1–3 | ≥ 5 |
| Puntuación media de la pregunta 6 | ≥ 5,5 |
| Errores de navegación graves (no encuentra un panel tras 2 minutos) | ≤ 2 por sesión |

### Tratamiento de los hallazgos

Cada hallazgo se registra con la sesión, el minuto, la cita literal y una propuesta; se agrupa por tema y se convierte en tareas con la etiqueta `playtest`. Un hallazgo que aparece en tres sesiones o más pasa a prioridad alta automáticamente. Las grabaciones se borran a los 90 días salvo consentimiento explícito para conservarlas.

## Anexo AR · Formato de guardado (borrador)

### Estructura del archivo

```text
┌──────────────────────────────────────────────┐
│ Cabecera fija (64 bytes)                     │  magia "E101SAVE", versión del formato, banderas
├──────────────────────────────────────────────┤
│ Cabecera extendida (postcard)                │  versión del motor, hash del contenido, mods,
│                                              │  semilla, día, hash del estado, metadatos de la
│                                              │  partida (país, modo, reglas), miniatura opcional
├──────────────────────────────────────────────┤
│ Índice de secciones                          │  nombre, desplazamiento, tamaño, hash por sección
├──────────────────────────────────────────────┤
│ Secciones del estado (zstd por sección)      │  time, map_dynamic, entities, population, economy,
│                                              │  politics, diplomacy, military, characters,
│                                              │  history, ledger_summary, ai_memory
├──────────────────────────────────────────────┤
│ Diario de comandos (opcional, zstd)          │  para repeticiones e informes de error
└──────────────────────────────────────────────┘
```

| Aspecto | Decisión propuesta |
| --- | --- |
| Serialización | postcard o bitcode (D-011), con formato canónico por sección |
| Compresión | zstd nivel 3 para autoguardados (rápido), nivel 9 para guardados manuales |
| Integridad | Hash BLAKE3 por sección y global; la carga verifica antes de usar |
| Versionado | Número de formato entero; cada cambio incompatible añade una **migración** `vN → vN+1` en `e101-save` |
| Compatibilidad con mods | La cabecera lista mods y versiones; si faltan, se avisa y se ofrece cargar sin ellos solo si el validador lo permite |
| Autoguardado | Rotativo: mensual (últimos 3), anual (últimos 5), por década (todos); configurable |
| Tamaño estimado | Escala S: 15–40 MB comprimido tras 300 años; escala L: 150–400 MB (objetivo a medir en la Fase 1) |
| Tiempo | Guardado ≤ 2 s y carga ≤ 10 s en escala S (sección 25) |

### Migraciones

```rust
/// Each migration is a pure function from one format version to the next.
pub trait Migration {
    const FROM: u32;
    const TO: u32;
    fn migrate(input: RawSave) -> Result<RawSave, MigrationError>;
}
```

- Las migraciones se prueban con un **corpus de guardados** de cada versión publicada (`tests/saves/`).
- Una migración nunca inventa estado simulado: si un sistema nuevo necesita datos, los inicializa con valores neutros documentados y lo anota en la cabecera (“migrado desde v12”).
- Los guardados migrados no son válidos para logros si la migración cambió reglas de juego.

## Anexo AS · Esfuerzo y presupuesto estimados hasta la vertical

### Horas por fase (una persona, 25 horas semanales de media)

| Fase | Semanas | Horas humanas | Dedicación humana principal | Trabajo principal de agentes |
| --- | --- | --- | --- | --- |
| 0 — Preproducción | 8 | 200 | Diseño, documento, prototipo económico, decisiones | Prototipo en script, revisión de licencias, borradores de especificaciones |
| 1 — Núcleo | 13 | 325 | Arquitectura, revisión de PR, spike de cliente | Crates base, CI, pipeline geográfico, render del mapa |
| 2 — Economía y población | 13 | 325 | Especificaciones, revisión, calibración | Sistemas, pruebas de propiedad, Lab v0 |
| 3 — Diplomacia y guerra | 13 | 325 | Diseño militar y diplomático, pruebas con jugadores | Sistemas, IA básica, escenarios dorados |
| 4 — Historia, tecnología, personajes | 13 | 325 | Biblia histórica (verificación), situaciones | Datos propuestos con fuente, sistemas, Lab v1 |
| 5 — Vertical | 17 | 425 | UX, contenido, revisión editorial, pruebas | UI, eventos, localización, pulido |
| **Total** | **77 (≈ 18 meses)** | **≈ 1.925** | — | — |

**Reparto de las horas humanas previsto:** revisión de código y de PR 35 %; diseño y especificaciones 25 %; verificación histórica y editorial 20 %; pruebas y calibración 15 %; gestión y comunicación 5 %. Si la revisión supera el 45 % durante dos meses, las tareas de agentes son demasiado grandes o están mal definidas (sección 43).

### Presupuesto orientativo en efectivo hasta la vertical (USD, a cotizar)

| Partida | Mínimo | Máximo | Notas |
| --- | --- | --- | --- |
| Herramientas y agentes de IA (18 meses) | 2.700 | 9.000 | 150–500 al mes según uso |
| PC de referencia y dispositivos de prueba | 1.500 | 3.000 | Incluye un equipo portátil de tipo Steam Deck para la verificación |
| Iconografía (≈ 300 iconos) | 3.000 | 10.000 | Estilo propio coherente |
| Sistema modular de retratos (6 culturas, 3 edades, variantes) | 8.000 | 25.000 | La pieza de arte más cara del slice |
| Ilustraciones de eventos (≈ 40 escenas) | 6.000 | 16.000 | Reutilizables por variantes |
| Logotipo e identidad | 1.500 | 5.000 | Antes de la presencia pública |
| Música (30–45 minutos para el slice) | 6.000 | 20.000 | Encargo o licencias |
| Diseño de sonido | 1.000 | 4.000 | Interfaz y ambientes |
| Consultoría histórica regional | 3.000 | 8.000 | Contenido sensible y datos de nivel A |
| Revisión de la localización al inglés (≈ 120.000 palabras) | 6.000 | 14.000 | Si los textos se escriben en ambos idiomas, solo revisión |
| Legal (marca, licencias, términos) | 2.500 | 7.000 | Marca en las jurisdicciones principales |
| Steam Direct | 100 | 100 | Por producto |
| Tráiler y materiales de prensa | 2.000 | 8.000 | Para la página de tienda y el festival de demos |
| **Total** | **≈ 43.000** | **≈ 129.000** | Sin salarios; el tiempo de la persona responsable no se incluye |

**Cómo reducirlo:** retratos más simples en el slice (silueta + heráldica), música licenciada en lugar de encargada, iconografía generada con revisión humana estricta (si A-15 lo permite) y consultoría histórica solo para lo sensible. **Cómo no reducirlo:** la revisión histórica de contenido sensible y la revisión legal de licencias no se recortan.

## Anexo AT · Riesgos con indicadores de alerta temprana

| Riesgo (sección 31) | Indicador | Umbral de alerta | Acción al superarlo |
| --- | --- | --- | --- |
| Alcance de 760 años | Retraso acumulado de fase | > 50 % de la duración prevista | Revisar alcance del lanzamiento (sección 28) |
| Profundo pero no divertido | Pregunta 6 del cuestionario (Anexo AQ) | Media < 4,5 en dos meses seguidos | Congelar sistemas nuevos; iterar bucles y ritmo |
| Datos históricos erróneos | Errores encontrados en revisión por cada 100 datos propuestos por agentes | > 8 | Reducir lotes; exigir fuente directa por dato |
| Motor demasiado ambicioso | Horas de infraestructura frente a horas de juego | > 60 % durante la Fase 2 | Reutilizar bibliotecas; posponer optimizaciones |
| Economía inestable | Escenarios de estrés fuera de rango (Anexo F) | > 2 métricas en tres noches seguidas | Volver al prototipo de la Fase 0 con el cambio aislado |
| Pérdida de determinismo | Desincronizaciones en `threads_1_vs_16` | > 0 | Bloquear merges hasta corregir |
| IA descontrolada o guionizada | Métricas de salud de la IA (sección 17) | Cualquier alerta durante una semana | Tarea de diagnóstico con prioridad alta |
| Rendimiento | Tick medio en escala S | > 12 ms | Perfilado obligatorio antes de nuevas features |
| Dependencias que cambian | Versiones mayores pendientes en dependencias del cliente | > 2 | Planificar migración en una tarea dedicada |
| *Vibe coding* | PR de agentes aceptados sin cambios mayores | < 50 % durante un mes | Revisar tamaño y redacción de tareas; actualizar `AGENTS.md` |
| Agotamiento personal | Horas semanales reales | > 35 durante 4 semanas o < 10 durante 4 semanas | Reducir alcance o pausar; no compensar con más agentes |
| Contenido sensible | Textos sensibles sin revisión regional | > 0 en una versión pública | Retirar el contenido de la versión |
| Licencias | Dependencias o datasets sin licencia registrada | > 0 | Bloquear el uso hasta registrarla |

## Anexo AU · Trazabilidad: features → especificación → pruebas

Muestra para las features MVP y Slice más críticas. La tabla completa vive en `docs/specs/TRACEABILITY.md` y el CI comprueba que toda feature MVP o Slice tenga al menos una prueba enlazada.

| Feature | Tier | Especificación | Pruebas y escenarios |
| --- | --- | --- | --- |
| F-CORE-01 Calendario continuo | MVP | `time.md` | Conversión juliana/gregoriana (propiedades), `empty_300y` |
| F-CORE-04 Guardado determinista | MVP | `save-format.md` (Anexo AR) | `save_load_roundtrip` |
| F-MAP-01 Mapa de provincias | MVP | `ui-map.md`, `map-pipeline.md` | Benchmark de FPS; validación de textura de IDs |
| F-POP-01 Cohortes | MVP | `population.md` (sección 09) | Conservación con fusión; tope de cohortes |
| F-POP-02 Natalidad, mortalidad, migración | MVP | `population.md` | `pop_stability_200y`, `famine_response` |
| F-POP-11 Refugiados | Slice | `population.md` | Refugiados acotados |
| F-ECO-01 Cadena con conservación | MVP | `economy.md` (sección 10) | `economy_closed_100y` |
| F-ECO-02 Mercados y precios | MVP | `economy.md` | `harvest_shock`, `transport_gradient` |
| F-ECO-05 Presupuesto y deuda | MVP | `state-finance.md` | `default_creditors` |
| F-ECO-06 Moneda | Slice | `economy.md` | `debasement_detection` |
| F-ECO-15 Arrendamiento fiscal | Slice | `state-finance.md` | `tax_farm_tradeoff` |
| F-GOV-02 Grupos de interés | Slice | `politics.md` (sección 11) | `power_sums_to_one` |
| F-GOV-03 Leyes | Slice | `politics.md` | `reform_cannot_skip` |
| F-GOV-05 Control efectivo | MVP | `politics.md` | `overextension_bites` |
| F-GOV-06 Rebeliones | Slice | `politics.md` | `rebellion_has_program`, `civil_war_resolves` |
| F-DIP-02 Tratados por cláusulas | Slice | `diplomacy.md` (sección 12) | `treaty_consistency` |
| F-DIP-05 Coaliciones | Slice | `diplomacy.md` | `coalition_forms` |
| F-DIP-06 Información imperfecta | Slice | `diplomacy.md` | `information_lag` |
| F-DIP-10 Vasallos con IA | Slice | `diplomacy.md` | `vassal_opportunism` |
| F-WAR-01 Ejércitos | MVP | `military.md` (sección 13) | `battle_symmetry`, `terrain_matters` |
| F-WAR-03 Asedios | MVP | `military.md` | `siege_without_artillery` |
| F-WAR-04 Logística | Slice | `military.md` | `supply_ceiling` |
| F-WAR-07 Paz por cláusulas | MVP | `diplomacy.md`, `military.md` | `peace_terminates` |
| F-WAR-13 Agotamiento emergente | Slice | `military.md` | `war_exhaustion_composed` |
| F-WAR-17 Mercenarios | Slice | `military.md` | `mercenary_arrears` |
| F-SCI-01 Grafo tecnológico | Slice | `technology.md` (sección 14) | `graph_acyclic`, `knowledge_without_adoption` |
| F-SCI-03 Límite de adelanto | Slice | `technology.md` | `no_tech_beyond_lead` |
| F-ENV-01 Clima | Slice | `climate-epidemics.md` (sección 15) | `climate_correlation` |
| F-ENV-02 Epidemias | Slice | `climate-epidemics.md` | `plague_final_size`, `plague_1347` |
| F-ENV-10 Medidas sanitarias | Slice | `climate-epidemics.md` | `quarantine_tradeoff` |
| F-CHR-01 Gobernantes y herederos | Slice | `characters.md` (sección 16) | `succession_always_resolves`, `life_expectancy` |
| F-CHR-08 Regencias | Slice | `characters.md` | `regency_risk_bounds` |
| F-NAR-01 Situaciones | Slice | `history.md` (sección 07) | `situation_expiry`, `bias_capped` |
| F-NAR-03 Divergencia | Slice | `history.md` | `divergence_monotone_with_conquest` |
| F-UX-02 “¿Por qué?” | Slice | `ui-panels.md` (sección 18) | Prueba de cobertura: toda variable visible tiene explicación |
| F-PLT-01 Headless y Lab | MVP | `lab.md` | Informe nocturno generado |

## Anexo AV · Escenarios de aprendizaje

Escenarios cortos (F-MOD-02) que enseñan un sistema cada uno. Usan la misma simulación que la partida completa, con un estado inicial preparado y un objetivo.

| Escenario | Entidad | Duración | Enseña | Objetivo | Por qué es buen ejemplo |
| --- | --- | --- | --- | --- | --- |
| 1. Pan para la capital | Bizancio, 1305 | 2 años | Mercados, existencias, “¿por qué?” de precios | Mantener el grano de Constantinopla < 1,4 × base | Sequía, Génova y graneros en tensión |
| 2. La paga de los catalanes | Bizancio, 1303 | 3 años | Finanzas, mercenarios, devaluación | Conservar la lealtad de la Compañía > 40 sin superar una deuda del 50 % | Contrato, crédito y moneda |
| 3. Los fortines de Bursa | Beylik otomano, 1315 | 12 años | Asedios por bloqueo, suministro, paciencia | Tomar Prusa sin perder más del 30 % del ejército | Asedio sin artillería |
| 4. Dos señores, un rey | Hungría, 1301 | 10 años | Sucesión, pretendientes, concesiones a magnates | Asegurar un rey reconocido por la mayoría de los magnates | Crisis sucesoria pura |
| 5. Aduanas del Bósforo | Génova (Pera), 1310 | 5 años | Diplomacia por cláusulas, comercio, flota | Mantener la exención aduanera y el control del comercio del mar Negro | Negociación con poder naval |
| 6. Ratas en el puerto | Venecia (Candía), 1347 | 3 años | Epidemias y medidas sanitarias | Mantener la población de Candía > 75 % con el comercio > 60 % | La cuarentena tiene costes |

Cada escenario termina con una **pantalla de explicación**: qué hiciste, qué produjo cada efecto y qué habría pasado con otra decisión (comparando con una simulación paralela determinista con la decisión alternativa).

## Anexo AW · Objetivos de balance por entidad de la vertical

Rangos que 101 Lab comprueba en el **modo histórico dinámico, sin jugador** (100 campañas por noche). Su función es garantizar que cada entidad sea **viable pero con su peso histórico**: ninguna está condenada y ninguna es invencible.

| Entidad | Métrica | Rango objetivo |
| --- | --- | --- |
| Imperio bizantino | Conserva Constantinopla en 1400 | 55–85 % |
| Imperio bizantino | Conserva Constantinopla en 1500 | 25–55 % |
| Beylik otomano | Es la mayor potencia de Anatolia en 1400 (por ingresos) | 35–65 % |
| Beylik otomano | Tiene provincias en Europa antes de 1380 | 40–70 % |
| Germiyan | Sobrevive como Estado independiente hasta 1400 | 20–50 % |
| Karamán | Controla Konya en 1350 | 50–80 % |
| Karasi | Sobrevive como independiente hasta 1360 | 10–35 % |
| Menteşe | Sobrevive como independiente hasta 1400 | 25–55 % |
| Serbia | Alcanza ≥ 40 provincias en algún momento antes de 1370 | 30–60 % |
| Bulgaria | Sobrevive como independiente hasta 1400 | 30–60 % |
| Epiro y Tesalia | Al menos uno conserva su independencia hasta 1350 | 30–60 % |
| Acaya | Conserva Andravida hasta 1400 | 30–60 % |
| Atenas | Cambia de dinastía o de dueño antes de 1350 | 50–85 % |
| Venecia | Conserva Creta en 1600 | 40–75 % (Anexo F: ≥ 40 % en dinámico) |
| Génova | Conserva Caffa en 1450 | 40–70 % |
| Hungría | Sufre una guerra sucesoria entre 1301 y 1310 | 60–90 % |
| Chipre | Conserva su independencia hasta 1500 | 40–70 % |
| Trebisonda | Sobrevive hasta 1450 | 40–70 % |
| Armenia cilicia | Sobrevive hasta 1380 | 25–55 % |
| Compañía Catalana | Obtiene un territorio propio antes de 1320 | 20–50 % |

**Regla de ajuste:** si una entidad cae por debajo de su rango, se revisan sus **causas** (ingresos, ejército inicial, personalidad de la IA, geografía de sus provincias), nunca se le da una bonificación oculta. Los cambios se documentan en el PR con las métricas antes y después.

> **Documento vivo · versión 0.7 · 24 de octubre de 2026**
