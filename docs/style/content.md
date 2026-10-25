# Guía de Estilo de Contenido Histórico y Narrativo

Esta guía define los criterios de redacción, consistencia historiográfica, toponimia y restricciones de formato para todo el contenido textual y narrativo del proyecto `101Agents`. Es de obligado cumplimiento tanto para redactores humanos como para agentes de inteligencia artificial.

Las directrices aquí presentadas se fundamentan en el **Anexo G ("Guía de estilo del contenido")** del [`Documento Maestro v0.7`](../master/101_Agents_Games_Documento_Maestro_v0.7.md) y se complementan con las disposiciones de datos de la **Sección 9 de [`AGENTS.md`](../../AGENTS.md)**.

---

## 1. Principio Fundamental: Historia Condicional

En el diseño de `101Agents`, **nada ocurre por fecha fija; todo ocurre por condiciones**. El contenido narrativo (eventos, situaciones históricas, descripciones de facciones y entradas enciclopédicas) no actúa como un guion predeterminado que fuerza a los actores a replicar la historia real, sino como una respuesta contextual a las dinámicas materiales, políticas y sociales emergentes de la simulación. Los textos deben reflejar este principio causal con naturalidad.

---

## 2. Voz y Tono Editorial

El tono de los textos es la tarjeta de presentación de la experiencia de juego:

- **Sobriedad y rigor divulgativo:** El registro emula el estilo de una monografía o tratado de alta divulgación histórica contemporánea. Debe primar la claridad expositiva, la precisión terminológica y el equilibrio narrativo.
- **Sin humor anacrónico ni grandilocuencia:** Queda vetado el uso de chistes internos, referencias a la cultura popular contemporánea, sarcasmo o ironía fuera de lugar. Asimismo, se debe evitar el dramatismo épico hiperbólico y los tropos novelescos melodramáticos.
- **Sin anacronismos morales:** Los personajes, órdenes religiosas, facciones y dinastías deben presentarse en función de sus propios marcos mentales, intereses y cosmovisiones contemporáneas. No se juzga el pasado desde la moral del siglo XXI, pero tampoco se justifica la opresión como una fatalidad benevolente.
- **Sin edulcorar la realidad:** Cuando un evento o situación involucre violencia, injusticia, sometimiento, masacres o hambrunas, los hechos se describen de manera directa, objetiva y verídica, sin recurrir a eufemismos evasivos ni al recreamiento morboso.

### 2.1. Anacronismos Léxicos e Institucionales Prohibidos
Es imperativo evitar la extrapolación hacia el pasado de categorías políticas, jurídicas y sociales que no existían en las épocas simuladas:
- **"Nación" o "pueblo nacional":** Inapropiado para contextos como el siglo XIV. Términos como "nación francesa" o "patriotismo turco" en 1300 son falsedades conceptuales. Úsese "comunidad", "súbditos", "linaje", "reino" o "gentes de lengua romance/griega/eslava".
- **"El Estado" (sin matizar):** En periodos medievales o tempranomodernos no existía la maquinaria estatal weberiana abstracta. Se debe hablar de "la corona", "el gobernante", "el fisco real", "la corte", "los señores de la tierra" o "el régimen señorial".
- **"Economía nacional" / "Producto Interior Bruto":** En su lugar, utilícese "recaudación del tesoro", "cosechas provinciales", "comercio de las plazas" o "tributos".
- **"Frontera lineal":** En 1300 las fronteras eran marcas, franjas porosas y zonas de soberanías solapadas, no líneas aduaneras cartográficas modernas.

---

## 3. Restricciones Cuantitativas de Longitud

Para preservar la ergonomía visual, la jerarquía de lectura y la adaptabilidad a pantallas compactas (como Steam Deck a 1280 × 800), se aplican límites de palabras estrictos e infranqueables:

| Tipo de Texto | Límite Máximo | Finalidad y Criterio de Redacción |
| :--- | :--- | :--- |
| **Título de evento** | **6 palabras** | Breve, evocador y descriptivo. Sin signos de exclamación innecesarios. |
| **Cuerpo de evento** | **120 palabras** | Expone la situación, el conflicto nuclear y la causa inmediata sin digresiones. |
| **Opción de evento** | **12 palabras** | Indica con claridad la postura o acción que toma el jugador. |
| **Tooltip de modificador** | **25 palabras** | Explica el origen del efecto y su consecuencia funcional en una o dos frases. |
| **Entrada de enciclopedia** | **400 palabras** | Resumen histórico contextualizado, con mención explícita a fuentes consultadas. |

Todo texto que exceda estos límites será rechazado por los validadores automáticos y en las revisiones editoriales de los pull requests.

---

## 4. Toponimia y Onomástica

La denominación de lugares y personas debe conjugar la autenticidad histórica con la usabilidad:

- **Uso preferente de endónimos contemporáneos:** Las provincias, asentamientos y personajes se introducen con la denominación propia de la cultura y época gobernante (ej. *Konstantinoupolis*, *Edirne*, *Kütahya*, *Bursa*).
- **Exónimos modernos en la enciclopedia:** Para asegurar la accesibilidad geográfica del jugador, las entradas enciclopédicas y tooltips de búsqueda deben incluir el exónimo moderno convencional entre paréntesis:
  > *Ejemplo:* "Edirne (Adrianópolis)", "Nicea (İznik)".
- **Transliteración normalizada:** Las transliteraciones desde alfabetos no latinos (griego bizantino, árabe, cirílico, turco otomano) deben seguir una tabla de transliteración académica consistente y documentada en el repositorio.
- **Toponimia dinámica:** Cuando una provincia cambia de cultura dominante o de régimen soberano de manera estable, su nombre toponímico debe actualizarse a la variante cultural correspondiente, manteniendo siempre el historial previo en el registro de la provincia para garantizar la trazabilidad causal.

---

## 5. Integridad de Datos e Historiografía

Conforme a la Sección 9 de [`AGENTS.md`](../../AGENTS.md) y la Sección 46 del Documento Maestro:

### 5.1. Identificadores Semánticos
- Todos los identificadores (`ID`) de entidades, bienes, eventos, culturas y religiones se redactan en **inglés técnico**, en minúsculas y con guiones bajos (`snake_case`), manteniéndose estables e inmutables (ej. `province_byzantium_thrace`, `event_crown_succession_crisis`).

### 5.2. Fuentes y Grados de Confianza
Todo dato histórico cuantitativo o cualitativo incorporado a los catálogos del juego debe ir acompañado de su bibliografía de respaldo y de una clasificación explícita de confianza:
- **Grado A (Certeza histórica contrastada):** Fuentes primarias coincidentes o consenso arqueológico y documental indiscutible. Requiere revisión humana especializada (`needs-history-review`).
- **Grado B (Consenso historiográfico amplio):** Estimaciones mayoritarias en la literatura académica reciente. Requiere verificación humana (`needs-history-review`).
- **Grado C (Hipótesis razonable o dato controvertido):** Fuentes divergentes o extrapolaciones arqueológicas indirectas. Debe detallarse la justificación en las notas del archivo y en el diario de la tarea.
- **Grado D (Aproximación por modelado o analogía regional):** Carencia de registros directos; cifra estimada por densidad poblacional y paralelismo productivo. Se debe consignar abiertamente la falta de fuentes directas.

> [!CAUTION]
> **Prohibición absoluta:** Jamás se deben inventar gobernantes, batallas, fechas o censos para "rellenar" un hueco documental. Ante la ausencia de datos, utilícese el grado D y documente el procedimiento analógico.

### 5.3. Separación Tajante entre Datos y Textos de Interfaz
- Queda **estrictamente prohibido** escribir cadenas de texto o descripciones traducibles dentro de los archivos de definición de datos (`.ron`, `.csv` en `games/epoch/data/`).
- Los archivos de datos contienen únicamente referencias a claves semánticas (ej. `title_key: "event-byz-civil_war-title"`). Las cadenas legibles residen exclusivamente bajo el árbol de directorios de localización (`games/epoch/locale/`).

---

## 6. Proceso de Redacción y Localización Bilingüe Simultánea

- **Redacción en paralelo:** Los textos no se redactan en un idioma para ser traducidos posteriormente mediante traductores automáticos de baja fidelidad. En la medida de lo posible, las versiones en **español** e **inglés** se conciben simultáneamente respetando el mismo registro histórico en ambas lenguas.
- **Uso estricto de Project Fluent (`.ftl`):** Todo texto dinámico debe emplear las variables del sistema Fluent (`$count`, `$character_name`, `$province`), contemplando las variantes de concordancia gramatical, plurales y género de cada idioma.
- **Prohibición de concatenación en código:** Jamás se construirán oraciones mediante sumas de cadenas (`"El ejército de " + actor + " avanzó hacia..."`). La lógica de género y orden gramatical corresponde íntegramente a las plantillas de localización.
- **Glosario compartido:** Toda terminología institucional y de simulación (bienes, cargos de corte, tipos de vasallaje, nociones de legitimidad) debe alinearse rigurosamente con el glosario terminológico bilingüe central del proyecto.
