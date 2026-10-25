# Guía de Localización, Formato de Cifras y Presentación Causal

Esta guía técnica y editorial define los estándares para la gestión multilingüe, las normas de representación numérica y cronológica, la arquitectura de cadenas dinámicas mediante Project Fluent y las reglas de diseño para los paneles explicativos causales y tooltips de `101Agents`.

Las pautas aquí desarrolladas se fundamentan en la **Sección 18 ("Interfaz, mapa y accesibilidad" - subsecciones Formato de cifras y fechas, Localización, Tooltips anidados, Anatomía del panel "¿por qué?")** de [`docs/master/101_Agents_Games_Documento_Maestro_v0.7.md`](../master/101_Agents_Games_Documento_Maestro_v0.7.md).

---

## 1. Estrategia Multilingüe y Desacoplamiento Técnico

El diseño de internacionalización del proyecto persigue la máxima pureza técnica y fidelidad cultural:

- **Idiomas base desde el vertical slice:** El juego se desarrolla de forma nativa en **español** e **inglés**, redactándose ambas versiones en paralelo para garantizar la misma calidad de registro histórico. La arquitectura del sistema está completamente desacoplada y preparada para la incorporación fluida de idiomas adicionales (griego, turco, francés, alemán, etc.) sin modificaciones en el código de simulación.
- **Desacoplamiento radical del motor:** Los crates de simulación (`e101-sim`, `e101-store`) ignoran las convenciones gramaticales y tipográficas humanas. El motor opera y entrega exclusivamente tipos primarios: números enteros, identificadores semánticos y tipos de punto fijo (`FixedI64`, `Money`, `Qty`, `Ratio`).
- **Responsabilidad de la capa de presentación:** La traducción, la concordancia de género gramatical, la selección de formas de plural y el formateo de números, monedas y fechas corresponden con exclusividad a la capa de localización alimentada por **Project Fluent** (`.ftl`).

> [!IMPORTANT]
> **Prohibición de concatenación en Rust:** Jamás se deben construir frases mediante concatenación de fragmentos de texto en código Rust (`format!("{}: {} ducados", actor, valor)`). Todas las cadenas legibles deben generarse a través de mensajes de Fluent parametrizados con variables semánticas.

---

## 2. Normas de Formateo Numérico, Monetario y Cronológico (§18)

Las convenciones tipográficas y matemáticas se adaptan a las normas ortotipográficas de cada lengua conforme a la tabla oficial de la Sección 18:

| Concepto | Español (`es`) | Inglés (`en`) | Notas y Criterio de Uso |
| :--- | :--- | :--- | :--- |
| **Separador de miles y decimales** | `12.345,6` | `12,345.6` | En español se utiliza punto para millares y coma para la fracción decimal; en inglés, coma y punto respectivamente. |
| **Grandes magnitudes** | `1,2 M`, `34 mil` | `1.2M`, `34k` | En español se escribe con espacio entre el dígito y la abreviatura/palabra; en inglés se presenta compacto sin espacio. |
| **Porcentajes** | `12 %` | `12%` | En español se incluye obligatoriamente un espacio fino o de no separación entre la cifra y el símbolo `%`; en inglés va unido. |
| **Valores monetarios** | `465.000 uc`<br>`930.000 hiperpirones` | `465,000 uc` | La unidad de cuenta general es `uc`. Cuando el jugador activa la visualización histórica contextual por país, se muestra la divisa histórica (ej. hiperpirones bizantinos). |
| **Fechas históricas** | `14 de mayo de 1302` | `14 May 1302` | Redacción natural por idioma. Opcionalmente se puede habilitar la vista de calendarios culturales coetáneos en la interfaz. |
| **Intervalos de incertidumbre** | `4.000–7.000` | `4,000–7,000` | Se utiliza el guion medio (`–` / en-dash) sin espacios alrededor para delimitar rangos estimados o de inteligencia parcial. |

---

## 3. Criterios de Selección Onomástica y Toponímica

Para conjugar rigor y personalización en la lectura del mapa y los documentos, el sistema ofrece tres variantes seleccionables de nombres de lugares y personajes:
1. **Endónimo cultural coetáneo:** La denominación histórica empleada por la comunidad y gobierno local de la época (ej. *Konstantinoupolis*, *Edirne*, *Kallipolis*). Es la opción configurada por defecto.
2. **Exónimo moderno en la lengua del jugador:** Traducción o adaptación convencional al idioma en que se está ejecutando el juego (ej. *Constantinopla*, *Adrianópolis*, *Galípoli* en español; *Constantinople*, *Adrianople*, *Gallipoli* en inglés).
3. **Nombre histórico de la época:** Variante documental predominante en los tratados diplomáticos internacionales del periodo de partida.

Los archivos de localización deben proveer las variantes pertinentes cuando el término difiera de su grafía estándar.

---

## 4. Convenciones de Project Fluent (`.ftl`)

La localización de `101Agents` utiliza la sintaxis declarativa de Project Fluent de Mozilla:

### 4.1. Nombres de Claves Semánticas
Las claves deben ser descriptivas y reflejar la jerarquía del módulo o subsistema:
```text
<subsistema>-<categoria>-<nombre_del_elemento>-<variante>
```
*Ejemplos:*
- `market-price-grain-header = Precio del grano`
- `event-succession-dead_king-title = El rey ha muerto sin hijos`
- `ui-common-action-confirm = Confirmar orden`

### 4.2. Variables Semánticas y Concordancia
Se prohíben cadenas estáticas rígidas que fuercen estructuras gramaticales anglosajonas en otros idiomas:
```fluent
# Mensaje correcto con variables y selectores
pop-migration-flight =
    { $count ->
        [one] Una persona ha huido
       *[other] { $count } personas han huido
    } desde { $origin_province } hacia { $dest_province }.
```

### 4.3. Tratamiento de Género y Rangos
Cuando se introduzcan personajes o cargos institucionales, se debe contemplar la concordancia de género mediante selectores:
```fluent
character-title-ruler =
    { $gender ->
        [female] Reina { $name }
       *[male] Rey { $name }
    }
```

---

## 5. Restricciones de Interfaz y Tooltips Anidados (§18)

La densidad de información del juego exige jerarquizar la lectura visual para evitar la saturación cognitiva:

### 5.1. Jerarquía de Tooltips Anidados
La interfaz implementa un sistema escalonado de consulta de datos según la intención del jugador:

| Nivel de Tooltip | Activación por Usuario | Contenido Visible | Límite Máximo Estricto |
| :--- | :--- | :--- | :--- |
| **Nivel 1 (Resumen)** | Pasar el cursor durante 300 ms | Valor actual, una línea de descripción inmediata y la mayor causa individual. | **25 palabras** |
| **Nivel 2 (Desglose)** | Mantener el cursor 800 ms o pulsar tecla `Mayús` | Lista desglosada de los principales factores contribuyentes con sus respectivos valores cuantitativos. | **8 líneas de texto** |
| **Nivel 3 (Profundidad)** | Clic sobre un término subrayado dentro de un tooltip previo | Definición enciclopédica del término (glosario) o desglose causal detallado de dicho contribuyente. | **60 palabras** |
| **Fijado (Ventana flotante)** | Combinación `Ctrl` + clic o pulsar la tecla `T` | Convierte cualquier tooltip en una ventana flotante anclada y reposicionable para contrastar datos. | Sin límite de tiempo |

---

## 6. Anatomía del Panel Causal "¿Por Qué?" (§18)

El panel "¿Por qué?" es el núcleo pedagógico e interactivo de `101Agents`. Permite desentrañar cualquier valor de la simulación mediante la trazabilidad registrada en el ledger.

### 6.1. Estructura Obligatoria de Presentación
Todo panel "¿Por qué?" debe estructurarse conforme al esquema estandarizado:

1. **Encabezado unificado:**
   - Nombre de la variable analizada y ámbito geográfico/institucional.
   - Valor actual con su unidad de medida y símbolo de tendencia (`▲`, `▼`, `―`).
   - Variación neta y periodo evaluado (ej. `13,4 uc/t ▲ +49 %`).
2. **Línea de referencias históricas:**
   - Valor base sin modificadores temporales.
   - Valor de hace un ciclo largo (ej. "Hace 1 año").
   - Media móvil de referencia (ej. "Media 52 semanas").
3. **Bloque de factores contribuyentes:**
   - Muestra **los 5 mayores contribuyentes en valor absoluto**, clasificados por orden de impacto decreciente.
   - Si existen factores adicionales menores, se agrupan en una única línea de cierre: `··· N contribuyentes menores (+X,X)`.
   - Cada contribuyente muestra su valor, la causa subyacente y un enlace interactivo `[ir →]` que abre el "¿Por qué?" de la causa antecedente (la causa de la causa).
4. **Gráfica de series temporales (opcional/desplegable):**
   - Gráfico de áreas o líneas apiladas con la evolución temporal de las contribuciones.
5. **Menú de respuestas operativas viables:**
   - Solo se listan acciones que el jugador puede ejecutar material y legalmente en el turno actual para influir sobre la variable, cada una con la estimación de su impacto previsto.
6. **Gestión de la incertidumbre:**
   - Si la variable pertenece a una provincia o reino extranjero fuera de la red de control o información plena del jugador, el valor se presenta como un intervalo estimado (`4.000–7.000`) indicando la fecha de antigüedad del reporte.

---

## 7. Glosario Oficial Compartido (Español – Inglés)

Los siguientes términos nucleares de la simulación deben traducirse y emplearse de forma unívoca en todo el código de localización y en la documentación:

| Término en Español | Término en Inglés | Ámbito / Definición Funcional |
| :--- | :--- | :--- |
| **Registro causal** | *Causal log* / *Ledger* | Historial auditable de contribuciones que originan cada cambio. |
| **Unidad de cuenta (`uc`)** | *Unit of account (`uc`)* | Medida estándar de poder adquisitivo y valor monetario abstracto. |
| **Población en cohortes** | *Pop cohorts* | Segmento demográfico caracterizado por ubicación, cultura, credo y estado legal. |
| **Condición jurídica** | *Legal status* | Categoría estamental de derechos (`Free`, `Dependent`, `Enslaved`, `Privileged`). |
| **Nivel de vida (NV)** | *Living standard (LS)* | Grado de satisfacción de las cestas de subsistencia, confort y lujo (0,00 a 3,00). |
| **Agravio** | *Grievance* | Tensión acumulada por una cohorte frente al régimen de gobierno. |
| **Control efectivo** | *Effective control* | Capacidad real del gobernante para ejercer soberanía fiscal y judicial en una provincia. |
| **Legitimidad** | *Legitimacy* | Reconocimiento moral y formal del derecho del gobernante a ejercer el mando. |
| **Agotamiento bélico** | *War exhaustion* | Desgaste material, humano y psicológico acumulado durante un conflicto. |
| **Presupuesto de tiempo** | *Time budget* | Tiempo máximo asignado en milisegundos a un sistema durante el tick de simulación. |
| **Escenario dorado** | *Golden scenario* | Escenario de prueba determinista contra el que se validan hashes bit a bit. |
| **Grado de confianza** | *Confidence level* | Calificación historiográfica de una fuente de datos (grados A, B, C o D). |
