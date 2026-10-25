# Preguntas frecuentes para agentes

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
