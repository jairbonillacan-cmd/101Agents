# Guía de Estilo y Reglas de Código en Rust

Esta guía establece los estándares de ingeniería de software, arquitectura interna y reglas de codificación para el desarrollo en Rust dentro del proyecto `101Agents` (101 Engine y herramientas asociadas). Su cumplimiento es estricto y obligatorio para todos los colaboradores y agentes de inteligencia artificial.

Las directrices aquí expuestas sintetizan y formalizan lo establecido en la **Sección 46 ("Reglas de código y de datos para agentes")** y el **Anexo AC ("Preguntas frecuentes para agentes")** de [`docs/master/101_Agents_Games_Documento_Maestro_v0.7.md`](../master/101_Agents_Games_Documento_Maestro_v0.7.md), en estrecha concordancia con la **Sección 3 de [`AGENTS.md`](../../AGENTS.md)**.

---

## 1. Alcance y Crates Afectados

Las restricciones de determinismo, aislamiento y contabilidad aplican directamente a todos los crates de simulación y lógica central del motor:
- `e101-time`: Medición del tiempo de simulación y granularidad temporal por ticks/días/meses.
- `e101-store`: Almacenamiento columnar y tipos numéricos de punto fijo (`FixedI64`, `Money`, `Qty`, `Ratio`).
- `e101-commands`: Definición, serialización y validación de comandos emitidos.
- `e101-ledger`: Contabilidad exacta de bienes y registro causal de modificaciones.
- `e101-rng`: Generador de números pseudoaleatorios determinista con saltos.
- `e101-sim`: Núcleo de simulación y orquestación de sistemas.
- `e101-history`: Registro histórico y comparación de divergencias.
- `e101-map`: Topología, distancias y grafo geográfico.
- `e101-content`: Definiciones de catálogo de entidades, culturas, religiones y tecnologías.
- `e101-script`: Evaluación condicional declarativa.
- `e101-save`: Serialización binaria y restauración fiel del estado bit a bit.
- `e101-ai`: Lógica de evaluación y toma de decisiones de actores no jugadores.

---

## 2. Principios Inviolables de Determinismo

El principio rector del motor es el **determinismo absoluto**: mismo binario + mismos datos + misma semilla + misma secuencia de comandos reproducen siempre el mismo estado bit a bit. Para garantizarlo, se establecen las siguientes prohibiciones y obligaciones:

### 2.1. Prohibición de Punto Flotante en Simulación
- Queda **terminantemente prohibido** el uso de tipos de coma flotante nativos (`f32`, `f64`) en cualquier estructura del estado persistente, en cálculos intermedios de sistemas de simulación o en la contabilidad del ledger.
- Se deben emplear exclusivamente los tipos de punto fijo implementados en `e101-store::fixed`:
  - `Money`: Precisión monetaria en unidades de cuenta (`uc`).
  - `Qty`: Precisión para existencias de bienes, inventarios y demografía (3 decimales implícitos).
  - `Ratio`: Puntos básicos (`pb`, donde 10.000 pb equivale al 100,00 %).
- Si un cálculo requiere funciones matemáticas continuas o no lineales (como funciones exponenciales, logaritmos o raíces), está prohibido recurrir a aproximaciones de punto flotante de la librería estándar. La solución mandatoria es el uso de **tablas precalculadas por tramos lineales** en punto fijo (`e101-store`).

### 2.2. Colecciones y Orden de Iteración Determinista
- Queda **prohibido** el uso de `std::collections::HashMap` o `std::collections::HashSet` en el estado o en la lógica de simulación. Estas colecciones dependen del azar en su semilla de dispersión por defecto y carecen de un orden de iteración reproducible.
- Las alternativas canónicas son:
  - Vectores densos indexados por identificador numérico continuo o slotmaps generacionales (ej. `SlotMap<EntityId, T>`).
  - `std::collections::BTreeMap` y `std::collections::BTreeSet` cuando se requiere ordenamiento determinista por clave.
  - `IndexMap` e `IndexSet` cuando se requiere preservar estrictamente el orden de inserción.
- **Regla de iteración:** Toda iteración sobre entidades, provincias o transacciones debe ejecutarse siempre en orden determinista (por identificador único estable `ID`), evitando cualquier dependencia implícita del diseño interno de la memoria o de punteros.

### 2.3. Aislamiento Radical del Entorno
- La lógica de simulación vive en una caja cerrada y pura. Queda **prohibido** invocar:
  - El reloj del sistema operativo (`std::time::SystemTime`, `std::time::Instant`).
  - Llamadas a la red o sockets.
  - Accesos directos al sistema de archivos (`std::fs`) durante la ejecución de los sistemas.
  - Lectura de variables de entorno (`std::env`).
- Cualquier dato externo, catálogo o mapa debe haber sido cargado y validado en la fase de inicialización o suministrado a través de comandos y contextos inmutables.

### 2.4. Generador Pseudoaleatorio Restringido
- Queda **prohibido** el uso de `rand::thread_rng()` o cualquier generador no controlado.
- La única aleatoriedad permitida se obtiene invocando:
  ```rust
  e101_rng::rng(seed, system, entity, day)
  ```
- Este generador garantiza reproducibilidad independiente del orden de paralelización entre subsistemas o entidades distintas.

### 2.5. Prohibición de Código Inseguro
- El uso de `unsafe` está prohibido en todo el repositorio.
- Excepción: Solo se admite bajo un *Architecture Decision Record* (ADR) formalmente aprobado por el rol de Arquitectura, acompañado de pruebas exhaustivas y documentación matemática de las invariantes de seguridad de memoria.

---

## 3. Arquitectura de Sistemas y Flujo de Mutación

El motor implementa una arquitectura basada en desacoplamiento estricto entre lectura de estado y aplicación de modificaciones:

### 3.1. Firma Canónica de Sistemas
Los sistemas de simulación ejecutan su fase de cálculo sin mutar directamente la memoria compartida del juego:
```rust
pub fn run(state: &State, deltas: &mut Deltas)
```
- **Invariante:** Ningún sistema escribe de forma directa en `State`.
- Los cálculos generan "deltas" (cambios propuestos) que son evaluados, verificados y aplicados atómicamente por la fase de aplicación del motor.

### 3.2. Registro Causal Obligatorio (Ledger)
- La contabilidad de recursos y población es exacta y conservativa: ningún bien, persona o cantidad de moneda aparece o desaparece sin una regla registrada.
- Todo delta que modifique una variable visible para el usuario debe invocar el registro causal del ledger:
  ```rust
  deltas.ledger.record(target_entity, variable, delta_value, origin);
  ```
- El campo `origin` debe identificar con exactitud el subsistema o causa (ej. `Origin::MarketTrade`, `Origin::Famine`, `Origin::Birth`). Si no existe un identificador de origen adecuado en el enum `Origin`, debe solicitarse su incorporación al rol de Arquitectura mediante un ADR previo.

---

## 4. Estándares de Calidad y Ergonomía del Código

### 4.1. Formateo y Lints
- Todo el código debe estar formateado con `rustfmt` conforme al archivo de configuración del repositorio.
- El análisis estático con `clippy` debe pasar con cero advertencias:
  ```bash
  cargo xtask check
  ```
- Queda prohibido silenciar advertencias con directivas `#[allow(...)]` en los crates de simulación, salvo en situaciones excepcionales justificadas con comentario técnico y aprobadas en revisión de PR.

### 4.2. Tratamiento de Errores
- **Crates y bibliotecas internas:** Emplear tipos de error fuertemente tipados definidos mediante `thiserror`. No propagar cadenas genéricas.
- **Herramientas de soporte y ejecutables (`tools/xtask`, scripts):** Se permite el uso de `anyhow` para simplificar el reporte de errores en consola.
- **Pánicos:** Prohibido el uso de `.unwrap()` o `.expect()` en código de producción de bibliotecas, a menos que se trate de un invariante interno rigurosamente documentado con un comentario que explique por qué la condición es imposible de incumplir.

### 4.3. Nombres y Documentación
- **Identificadores y API:** Todo el código (tipos, structs, enums, funciones, variables, nombres de archivos y módulos) se redacta en **inglés técnico**.
- **Comentarios:** Los comentarios y explicaciones técnicas internas pueden redactarse en inglés o español, manteniendo estricta coherencia dentro de cada crate individual.
- **Documentación de API:** Todo elemento público (`pub`) debe contar con comentarios de documentación (`///`) que describan:
  - Su propósito y comportamiento.
  - Parámetros y valores de retorno.
  - Invariantes y condiciones de error.
  - Un ejemplo de uso (`# Examples`) siempre que sea aplicable.
- **Modularidad:** Funciones breves y cohesivas; organización de archivos por subsistemas semánticos (ej. `economy/prices.rs`, `economy/trade.rs`).

---

## 5. Estrategia y Pirámide de Pruebas

Toda modificación debe estar respaldada por pruebas automatizadas verificables antes de someterse a revisión:

| Tipo de Prueba | Obligatoriedad | Herramienta / Comando |
| :--- | :--- | :--- |
| **Unitaria** | Obligatoria en todo cambio o adición de función/método. | `cargo xtask test <crate>` |
| **Propiedad** | Obligatoria ante cambios que afecten bienes, dinero, demografía o balances contables. | `proptest` |
| **Instantánea** | Obligatoria para formatos serializados, salidas textuales, reportes y árboles de datos. | `insta` |
| **Escenarios Dorados** | Obligatoria ante cualquier alteración de la lógica de simulación. Verifica determinismo y hashes. | `cargo xtask golden` |
| **Rendimiento** | Obligatoria cuando se toquen sistemas críticos con presupuesto de tiempo asignado. | `cargo xtask bench` |

---

## 6. Errores Comunes de Agentes y Cómo Evitarlos (Resumen §46)

La experiencia con agentes de IA en el repositorio ha identificado patrones de fallo recurrentes. La siguiente tabla resume la prevención obligatoria:

| Error Común | Medida Preventiva Obligatoria |
| :--- | :--- |
| **Inventar datos históricos plausibles pero ficticios.** | Todo dato debe incluir fuentes y nivel de confianza. Preferir grados C o D si existe duda razonable. Verificación humana requerida para grados A y B. |
| **"Arreglar" una prueba alterando la expectativa.** | Prohibido alterar hashes de pruebas doradas. Requiere la etiqueta `golden-change` y aprobación humana explícita. |
| **Refactorizar código fuera del alcance asignado.** | Trabajar estrictamente sobre los archivos permitidos en la tarea. Cambios no autorizados invalidan el PR. |
| **Añadir dependencias externas para funciones simples.** | Exige trámite previo con etiqueta `new-dependency`, justificando licencia, peso y necesidad real. |
| **Introducir números flotantes de manera puntual.** | Prohibido sin excepciones en simulación. Los lints de CI bloquean el commit. Emplear `Money`, `Qty` o `Ratio`. |
| **Desactivar lints con `#[allow(...)]` para pasar el CI.** | Corregir la causa raíz del lint. Los `allow` no autorizados serán rechazados en el proceso de revisión. |
| **Pérdida de contexto entre sesiones de trabajo.** | Actualizar el diario de la tarea (`docs/agents/journal/<issue>.md`) y consultar el `CONTEXT.md` del crate antes de operar. |

---

## 7. Preguntas Frecuentes Operativas para Agentes (Resumen Anexo AC)

A continuación se condensan las directrices del Anexo AC para resolver dudas operativas inmediatas:

1. **¿Puedo usar `f64` en un cálculo intermedio si el resultado final se redondea a entero?**  
   *No.* En los crates de simulación el uso de flotantes está vetado incluso de forma temporal. Emplea aritmética de punto fijo o solicita una tabla de interpolación a través de una tarea de motor.

2. **El orden de iteración de mi `BTreeMap` no coincide con el orden por ID. ¿Es problemático?**  
   Aunque `BTreeMap` es determinista respecto a sus claves, otros sistemas pueden depender del orden por identificador numérico de entidad. La regla general es iterar siempre ordenando por `EntityId` salvo especificación contraria.

3. **Una prueba dorada falla tras mi cambio y el nuevo valor es el correcto.**  
   No intentes bendecir el hash con `--bless`. Documenta en el PR la razón exacta del cambio numérico, añade la etiqueta `golden-change` y espera la validación de un revisor humano.

4. **Necesito una pequeña utilidad externa para serializar o transformar estructuras.**  
   No agregues la dependencia a `Cargo.toml`. Abre o actualiza la tarea indicando el nombre, licencia compatible, mantenimiento activo y por qué no es viable implementarlo con el código base actual. Etiqueta con `new-dependency`.

5. **La tarea asignada parece contradecir el Documento Maestro o un ADR previo.**  
   Detén el trabajo inmediatamente y plantea la consulta en la tarea. El Documento Maestro y los ADR aprobados prevalecen sobre el enunciado de cualquier tarea, salvo confirmación explícita del responsable.

6. **No encuentro fuentes fiables para un dato histórico específico.**  
   Asigna nivel de confianza C o D, expón las dudas en el diario de trabajo y en las notas del dato. Jamás inventes gobernantes, fechas o estadísticas.

7. **¿Puedo reorganizar módulos de un crate para hacerlo más elegante?**  
   Únicamente si la tarea lo solicita expresamente y dentro de los archivos autorizados. Las refactorizaciones estructurales requieren tareas y revisiones independientes.

8. **Mi solución exige modificar una interfaz pública en otro crate.**  
   Detente. No toques el otro crate. Registra la necesidad en el diario de trabajo y solicita al rol de Arquitectura la evaluación del cambio y la redacción del ADR pertinente.

9. **¿Cómo registro en el ledger un cambio indirecto generado por mi sistema?**  
   El registro debe emitirse en el sistema que materializa el delta, asociando el `Origin` más específico que corresponda. Si falta una variante semántica, solicita su creación.

10. **El benchmark muestra una regresión de rendimiento del 3 %. ¿Es admisible?**  
    Regresiones por debajo del 5 % son tolerables siempre que se justifiquen detalladamente en el cuerpo del PR. Cualquier regresión superior al 5 % exige la etiqueta `perf-regression` y requiere optimización o aprobación expresa.

11. **¿Puedo introducir cadenas de texto visibles en los archivos de datos `.ron` o `.csv`?**  
    *Nunca.* Los archivos de datos contienen únicamente claves semánticas y estructuras cuantitativas. Los textos visibles se alojan exclusivamente en `games/epoch/locale/`.

12. **¿Puedo realizar una petición de red en una prueba para validar datos reales?**  
    *Terminantemente prohibido.* Las pruebas unitarias, de integración o doradas no pueden acceder a la red externa bajo ninguna circunstancia. Toda prueba debe ser autónoma y utilizar mocks o datos locales del repositorio.
