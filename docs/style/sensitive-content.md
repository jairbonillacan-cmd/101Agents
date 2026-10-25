# Guía de Tratamiento de Contenido Histórico Sensible

Esta guía establece las directrices éticas, arquitectónicas y de diseño para la representación y simulación de sucesos históricos trágicos, traumáticos o de explotación humana dentro de `101Agents`. Su aplicación es obligatoria en todos los crates de simulación, bases de datos históricas, cadenas narrativas y representaciones visuales.

Las políticas aquí detalladas sintetizan y desarrollan los preceptos establecidos en la **Sección 09 ("Población y sociedad" - subsección Contenido histórico sensible)** y el **Anexo G ("Guía de estilo del contenido" - subsección Lista de comprobación de sensibilidad)** de [`docs/master/101_Agents_Games_Documento_Maestro_v0.7.md`](../master/101_Agents_Games_Documento_Maestro_v0.7.md), en estrecha coordinación con la **Sección 9 y 10 de [`AGENTS.md`](../../AGENTS.md)**.

---

## 1. Ámbito de Aplicación

La historia de la humanidad está atravesada por fenómenos de opresión estructural, coacción violenta y sufrimiento colectivo. En `101Agents`, dichos fenómenos se simulan como realidades históricas ineludibles, sin censurarlas ni instrumentalizarlas de manera lúdica irresponsable. Esta política abarca específicamente:
- **Esclavitud, trata de personas y trabajo forzado:** Sistemas esclavistas antiguos y coloniales, levas forzosas, servidumbre hereditaria y cautiverio bélico.
- **Colonización y desposesión territorial:** Desplazamiento forzado de comunidades autóctonas, despojo de tierras y asimilación coercitiva.
- **Violencia masiva y crímenes bélicos:** Saqueos destructivos, asedios con inanición provocada, masacres y represalias punitivas contra poblaciones civiles.
- **Persecuciones étnicas y religiosas:** Pogromos, procesos inquisitoriales, expulsiones forzadas (como las de comunidades judías o moriscas) y desmantelamiento forzoso de minorías.
- **Diásporas y segregación:** Marginación legal de grupos protegidos o discriminados bajo marcos confesionales o estamentales.

---

## 2. Principios Rectores Innegociables (§09)

Todo sistema, dato o evento que interactúe con el ámbito sensible debe someterse a seis principios rectores:

### 2.1. Sistemas, no Recompensas
El juego nunca presenta el sufrimiento ajeno, la servidumbre o la violencia masiva como una bonificación unilateral, aséptica y deseable para el jugador. 
- Todo régimen de explotación genera **costes patentes y consecuencias sistémicas**: erosión de la legitimidad, resistencia activa, fricción institucional, inestabilidad social, costes permanentes de vigilancia y represión, y empobrecimiento a largo plazo de la base productiva.
- Nunca existirá una decisión de gobierno que proporcione beneficios de producción inmediatos sin que el sistema registre y visibilice el gravamen social correspondiente.

### 2.2. Personas, no Mercancías
- Queda **terminantemente prohibido** modelar seres humanos o poblaciones esclavizadas como bienes comerciales fungibles en el mercado.
- La trata humana, la captura bélica y los desplazamientos coactivos **no tienen icono de producto en el panel de mercado, ni cotización de compraventa por fletes como si fuesen grano o madera**.
- Toda persona se representa exclusivamente como parte de la demografía mediante el sistema de cohortes de población, asignando la condición jurídica correspondiente (`legal_status: Enslaved`).

### 2.3. Agencia de los Afectados
Las poblaciones víctimas de abusos nunca son decorados estáticos o receptáculos pasivos:
- El modelo demográfico les dota de agencia intrínseca: mecanismos continuos de resistencia cotidiana, redes de solidaridad comunitaria, intentos periódicos de huida hacia zonas de refugio o soberanías tolerantes, capacidad de insurrección armada y acumulación de agravio histórico contra el régimen opresor.
- La memoria histórica del agravio permanece viva en las cohortes receptoras y en sus comunidades de origen tras generaciones.

### 2.4. Dignidad sin Caricaturas
- Las culturas, comunidades originarias y minorías perseguidas se representan con absoluto respeto a su dignidad histórica e identidad propia.
- Se utilizan siempre **endónimos** (nombres propios asignados por la propia comunidad) y descripciones etnográficas rigurosas, desterrando estereotipos despectivos, simplificaciones coloniales o representaciones exóticas degradantes.

### 2.5. Revisión Humana Especializada
- Cualquier cambio en el código de simulación, conjunto de datos o guion de eventos que afecte a materias sensibles requiere de forma obligatoria la etiqueta `needs-sensitive-review`.
- Ningún pull request con esta etiqueta puede integrarse al repositorio sin la revisión y aprobación formal de especialistas humanos designados.

### 2.6. Opciones de Presentación y Respeto al Jugador
- La simulación matemática subyacente es rigurosa, completa e inalterable, garantizando la fidelidad histórica de los cómputos.
- No obstante, la interfaz ofrece configuraciones de accesibilidad para regular la crudeza descriptiva de los textos o de las representaciones artísticas, permitiendo a los jugadores adaptar la experiencia estética sin pervertir ni adulterar la dinámica sistémica de la partida.

---

## 3. Modelado Demográfico y Mecánico en el Motor (§09)

En la arquitectura del 101 Engine (`crates/e101-sim`), los colectivos bajo opresión se modelan dentro de la estructura formal de cohortes descrita en la Sección 09 del Documento Maestro:

### 3.1. Condición Jurídica (`legal_status`)
- La condición jurídica es un atributo estructural de la cohorte, no una profesión u ocupación:
  ```rust
  pub enum LegalStatus {
      Free,
      Dependent,
      Enslaved,
      Privileged,
  }
  ```
- **Invariante demográfico:** Las cohortes con distinta condición jurídica tienen claves de identidad incompatibles y **tienen estrictamente prohibido fusionarse** entre sí, preservando siempre la trazabilidad estadística de su estatus.

### 3.2. Dinámica de la Cohorte `Enslaved`
- **Ingresos y nivel de vida:** Una cohorte en estado `Enslaved` percibe un ingreso personal de cero (`0 Money`). La entidad o cohorte explotadora asume exclusivamente la cobertura de la cesta de subsistencia biológica básica. El nivel de vida resultante (`living_standard`) se muestra de forma transparente e inequívoca en la interfaz para que el jugador aprecie el estado de depauperación de dicha población.
- **Acumulación de agravio (`grievance`):** Cada mes de simulación, la cohorte acumula agravio contra la autoridad política y sus explotadores, modulado por la dureza de las leyes aplicables, la escasez material y el grado de represión física presente en la provincia.
- **Evasión y huida:** A diferencia de las cohortes libres que operan bajo reglas de migración económica atractiva ordinaria, las personas sometidas a cautiverio o esclavitud cuentan con una probabilidad mensual de **huida clandestina**, canalizada hacia provincias fronterizas seguras, núcleos urbanos libres o territorios de refugio con alta tolerancia cultural/religiosa. Estas huidas se registran en el ledger bajo `Origin::Flight`.

### 3.3. Transiciones Jurídicas y Contabilidad Causal
- **Manumisión y redención de cautivos:** La emancipación de cohortes, el rescate de cautivos de guerra y las leyes generales de abolición constituyen transformaciones institucionales de la condición jurídica.
- Toda liberación altera formalmente el campo `legal_status` hacia `Free` o `Dependent`, generando el correspondiente registro causal en el ledger con su costo compensatorio o político, y alterando de inmediato las relaciones de lealtad y apoyo hacia los grupos de interés del reino.

---

## 4. Lista de Comprobación de Sensibilidad (Anexo G)

Antes de enviar cualquier modificación de código, datos o eventos que involucre temáticas sensibles, se debe verificar y responder afirmativamente a las **cinco preguntas fundamentales** del Anexo G:

1. **¿Las víctimas tienen voz y agencia activa en el texto y en las mecánicas?**  
   *Comprobación:* El texto no puede presentar a los oprimidos como meros recursos pasivos o daños colaterales; debe evidenciar su perspectiva, sus respuestas de supervivencia y su resistencia.
2. **¿Se evita presentar la violencia, la servidumbre o el sometimiento como una recompensa o bonificación deseable?**  
   *Comprobación:* Verificar que no existan ventajas unilaterales desprovistas de costes sociales, demográficos, de legitimidad o de riesgo de insurrección.
3. **¿Se describe a las culturas, comunidades y confesiones involucradas con respeto, rigor y ausencia de estereotipos?**  
   *Comprobación:* Asegurarse del empleo de endónimos, fuentes históricas rigurosas y la supresión de tropos moralistas o paternalistas contemporáneos.
4. **¿Existe una fuente historiográfica contrastada para cada afirmación o dato cuantitativo incorporado?**  
   *Comprobación:* Toda cifra demográfica, tributaria o de bajas debe referenciar bibliografía académica reconocida con su respectivo grado de confianza.
5. **¿Ha sido revisado el contenido por personas con conocimiento histórico y contextual de la región y periodo tratados?**  
   *Comprobación:* Requisito ineludible de validación humana a través de la etiqueta correspondiente en el repositorio.

---

## 5. Flujo de Trabajo, Etiquetas y Tolerancia Cero

Para salvaguardar la integridad del proyecto frente al público general:

- **Etiqueta obligatoria:** Todo pull request o tarea que interactúe con el catálogo de población sensible, redacte eventos de crisis humanitarias o altere mecánicas de coacción debe portar la etiqueta:
  ```text
  needs-sensitive-review
  ```
- **Prohibición de auto-merge:** Ningún agente de IA ni colaborador individual puede aprobar o mezclar por su cuenta ramas marcadas con esta etiqueta. Se requiere la firma expresa de la persona responsable del estudio.
- **Tolerancia cero:** Queda rotundamente prohibida cualquier concesión a la apología de genocidios, trivialización de crímenes históricos o implementación de mecánicas que busquen el entretenimiento basado en la humillación o exterminio de grupos humanos. Las propuestas que vulneren estas directrices serán rechazadas de inmediato y acarrearán la invalidación de la sesión de trabajo.
