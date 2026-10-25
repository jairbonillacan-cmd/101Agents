# Especificación técnica: Fase de Aplicación (`apply`) y Catálogo de Invariantes (`e101-sim::apply`)

- **Estado:** Propuesto
- **Crates afectados:** `e101-sim` (módulos `apply`, `deltas`, `invariants`), en coordinación con `e101-store`, `e101-ledger`, `e101-commands` y `e101-save`
- **Tareas relacionadas:** `T-109` (`e101-sim`: esqueleto de bucle diario, `Deltas` y `apply` determinista, Anexo AM)
- **Referencias del documento maestro:** `§§ 09, 10, 11, 12, 13, 21, 22, 23, 25`; Anexos `B, P, T, W, X, AG, AH, AI, AM` (`docs/master/101_Agents_Games_Documento_Maestro_v0.7.md`, plantilla en línea 9077)
- **Decisiones de arquitectura:** [ADR 0001](../adr/0001-monorepo-and-crate-graph.md) (monorepo y grafo de crates), [ADR 0002](../adr/0002-determinism-rules.md) (reglas de determinismo y colecciones), [ADR 0003](../adr/0003-fixed-point-types.md) (aritmética en punto fijo), [ADR 0004](../adr/0004-tick-schedule-and-state-hash.md) (calendario de fases del tick diario y aplicación de deltas)

---

## 1. Objetivo

Definir la arquitectura, la semántica algebraica de fusión determinista y el verificador de invariantes de la **fase de aplicación (`e101-sim::apply`)** de **101 Engine**.

En **101 Engine**, ningún sistema de simulación muta `State` directamente durante su ejecución (`§ 21`, [ADR 0004](../adr/0004-tick-schedule-and-state-hash.md)). Todos los sistemas operan con acceso de solo lectura (`&State`) y emiten propuestas de cambio tipadas en contenedores `Deltas` locales a cada hilo de trabajo. Al cierre de cada fase del calendario del tick diario (`Fases 0 a 15`, [ADR 0004](../adr/0004-tick-schedule-and-state-hash.md)), la función `e101-sim::apply` recolecta el vector `Vec<Deltas>` producido por los hilos de Rayon, ordena todas las operaciones por su **clave canónica estable**, las fusiona mediante reglas algebraicas deterministas, muta `&mut State`, consolida las entradas causales en `e101-ledger` y verifica los **invariantes del motor** (`§§ 09–13`, `§ 21 Fase 17`, `§ 23`, `Anexo AI`).

Esta separación estricta cumple simultáneamente cuatro principios irrompibles del motor (`AGENTS.md § 2`):
1. **Determinismo multihilo bit a bit (`QA-CORE-02`, `T-109`):** el estado resultante al ejecutar con `1`, `4` o `16` hilos es idéntico bit a bit en todas las plataformas soportadas (`Anexo B`, [ADR 0002](../adr/0002-determinism-rules.md), [ADR 0004](../adr/0004-tick-schedule-and-state-hash.md)).
2. **Comandos y deltas, no mutaciones directas:** el estado solo cambia en los puntos de sincronización de `apply`.
3. **Contabilidad exacta (`§§ 09–13`):** ningún bien (`Qty`), unidad monetaria (`Money`), obligación de deuda ni persona aparece o desaparece sin un flujo explícito y balanceado.
4. **Registro causal obligatorio (`§ 22`, `Anexo T`):** toda mutación en una variable visible para el jugador queda vinculada a su `CauseKind` y entidad origen en `e101-ledger`.

---

## 2. Alcance y fuera de alcance

### Dentro de alcance
- Las estructuras públicas `Deltas`, los subcontenedores por dominio (`EconomyDeltas`, `PopulationDeltas`, `PoliticsDeltas`, `MilitaryDeltas`, `LedgerDeltas`, `TimeDeltas`, `MapDeltas`, `DiplomacyDeltas`, `CharacterDeltas`, `HistoryDeltas`), el rasgo `System` y la firma de `e101-sim::apply` (`Anexo X` líneas 8477–8494).
- La definición de la **clave canónica estable** `(TableTag, TargetId, FieldTag, OpKind, SourceId, SeqInSystem)` que independiza la aplicación del orden de planificación de los hilos de Rayon ([ADR 0004](../adr/0004-tick-schedule-and-state-hash.md), `T-109`).
- Las cuatro categorías algebraicas de deltas (transferencias conservativas, acumulaciones aditivas, asignaciones de estado y operaciones de ciclo de vida de entidades) y sus reglas exactas de reducción y acotación en punto fijo ([ADR 0002](../adr/0002-determinism-rules.md), [ADR 0003](../adr/0003-fixed-point-types.md)).
- El **catálogo exhaustivo de invariantes** del núcleo (`I-ECO-01` a `I-ECO-04`, `I-POP-01` a `I-POP-04`, `I-POL-01`, `I-POL-02`, `I-DIP-01`, `I-WAR-01`, `I-GEN-01`) con sus fórmulas exactas en `Money`, `Qty` y `Ratio` (`§§ 09–13`, `§ 23`, `Anexo AI`).
- La estructura de diagnóstico `InvariantViolation` y la política de ejecución diferenciada entre pruebas/CI/`101 Lab` (`Anexo AH`) y partidas del jugador (`§ 21 Fase 17`, `§ 25`, `e101-save`).

### Fuera de alcance
- Las fórmulas internas de negocio de cada sistema (p. ej. cómo `EconomySystem` calcula la demanda o cómo `CombatSystem` calcula las bajas por fase táctica), que pertenecen a las especificaciones de sus respectivos dominios (`§§ 09–19`).
- La validación previa de comandos de jugador e IA antes de entrar al `CommandLog`, que corresponde a `e101-commands` ([`docs/specs/commands.md`](./commands.md), `§ 21 Fase 0`).
- La disposición física de las tablas columnares y generacionales en memoria, que corresponde a `e101-store` ([`docs/specs/store.md`](./store.md), [ADR 0002](../adr/0002-determinism-rules.md)).
- La serialización binaria de instantáneas y registros de comandos en disco, que corresponde a `e101-save` (`§ 25`).

---

## 3. Modelo

### 3.1. Arquitectura de `Deltas`, rasgo `System` y función `apply`

Siguiendo el contrato público del `Anexo X` (líneas 8477–8494) y `ADR 0004`, los sistemas de simulación implementan el rasgo `System` y emiten todas sus salidas en `Deltas`:

```rust
pub struct Deltas {
    pub economy: EconomyDeltas,
    pub population: PopulationDeltas,
    pub politics: PoliticsDeltas,
    pub military: MilitaryDeltas,
    pub ledger: LedgerDeltas,
    // + time, map, diplomacy, characters, history
    pub time: TimeDeltas,
    pub map: MapDeltas,
    pub diplomacy: DiplomacyDeltas,
    pub characters: CharacterDeltas,
    pub history: HistoryDeltas,
}

pub trait System: Send + Sync {
    fn name(&self) -> &'static str;
    fn run(&self, state: &State, deltas: &mut Deltas);
}

/// Merge per-thread deltas in stable key order, then apply.
pub fn apply(state: &mut State, deltas: Vec<Deltas>) -> Result<(), InvariantViolation>;
```

### 3.2. Garantía de determinismo multihilo (`T-109` y `QA-CORE-02`)

El requisito `QA-CORE-02` (*"Resultado idéntico con 1, 4 y 16 hilos"*, `§ 23`, `Anexo B`) y la tarea `T-109` (`Anexo AM`) exigen que la paralelización con Rayon no introduzca ninguna dependencia del planificador del sistema operativo ni del número de hilos lógicos:

1. **Lectura inmutable en paralelo:** Dentro de cada una de las fases de sistemas del calendario del tick (`Fases 0 a 15`, `§ 21`, `ADR 0004`), `State` se comparte únicamente mediante referencia inmutable `&State`. Ningún trabajador de Rayon puede observar efectos parciales producidos por otro hilo durante la misma fase.
2. **Particionado por entidad de dominio y `Deltas` locales:** Cuando un sistema paraleliza el trabajo sobre un conjunto de entidades (p. ej. mercados en la Fase 6, provincias en la Fase 7 o ejércitos en la Fase 12), cada partición o tarea de Rayon construye e inicializa su propia instancia local de `Deltas`. Cada operación registrada dentro de una invocación determinista por entidad recibe un contador monótono local a esa entidad/sistema (`SeqInSystem: u32`).
3. **Recolección y canonización independiente del hilo:** Al finalizar la fase paralela, el recolector entrega `deltas: Vec<Deltas>` a `e101-sim::apply`. Aunque el orden de los elementos dentro de `Vec<Deltas>` dependa del robo de trabajo (*work-stealing*) de Rayon, `apply` aplana los subcontenedores de todos los elementos de `Vec<Deltas>` y los **ordena por su clave canónica estable** antes de ejecutar cualquier reducción o escritura sobre `&mut State`.

### 3.3. Clave canónica estable de ordenación

Toda operación elemental contenida en `Deltas` posee una clave de orden total de 6 componentes deterministas:

```rust
#[derive(Clone, Copy, Debug, PartialEq, Eq, PartialOrd, Ord)]
pub struct DeltaKey {
    /// Tabla destino en e101-store (EconomyMarkets, PopCohorts, PolStates, MilArmies, ...).
    pub table_tag: TableTag,
    /// Identificador determinista de la entidad destino (o entidad origen en transferencias).
    pub target_id: RawEntityId,
    /// Campo o propiedad dentro de la tabla destino.
    pub field_tag: FieldTag,
    /// Categoría algebraica (1 = Lifecycle, 2 = Transfer, 3 = Additive, 4 = SetState).
    pub op_kind: OpKind,
    /// Identificador determinista de la entidad o sistema emisor (p. ej. otra provincia, mercado o tratado).
    pub source_id: RawEntityId,
    /// Secuencia monótona emitida para el par (source_id, target_id) dentro del sistema.
    pub seq_in_system: u32,
}
```

Dado que `DeltaKey` implementa `Ord` únicamente sobre identificadores lógicos de `e101-store` ([ADR 0002](../adr/0002-determinism-rules.md)) y etiquetas estáticas del sistema —y nunca sobre punteros de memoria, identificadores de hilo (`ThreadId`) ni relojes del sistema—, el vector fusionado tras `sort_unstable_by_key(|d| d.key())` es **idéntico bit a bit** con `1`, `4` o `16` hilos.

### 3.4. Las cuatro categorías algebraicas de fusión de deltas

Para evitar condiciones de carrera lógicas y garantizar contabilidad exacta en punto fijo ([ADR 0003](../adr/0003-fixed-point-types.md)), todas las operaciones de `Deltas` se clasifican en cuatro categorías algebraicas que `apply` procesa en estricto orden de precedencia dentro de cada fase:

#### Categoría 1: Transferencias conservativas (`OpKind::Transfer`)
Incluye `TransferMoney`, `TransferQty`, `MigratePeople` y `TransferPrisoners`.
- **Estructura:** Contienen obligatoriamente la tupla completa `(from, to, amount, origin)`:
  ```rust
  pub struct TransferDelta<IdFrom, IdTo, Val> {
      pub from: IdFrom,
      pub to: IdTo,
      pub amount: Val, // Money o Qty (> 0)
      pub origin: LedgerCause,
      pub seq_in_system: u32,
  }
  ```
- **Prohibición de débitos/créditos sueltos:** Ningún sistema puede emitir un descuento en una entidad y un incremento separado en otra para representar un traslado de valor o población. Toda creación o destrucción neta debe usar primitivas explícitas de fuente/sumidero (`MintMoney`, `BurnMoney`, `HarvestQty`, `ConsumeQty`, `DecayQty`, `BirthQty`, `DeathQty`), que quedan contabilizadas en los acumuladores de auditoría del tick (`§§ 09, 10`).
- **Acotación determinista ante saldo insuficiente:** Las transferencias se agrupan por cuenta de origen `from` y se ordenan por `(from, to, origin, seq_in_system)`. Si la suma de transferencias salientes desde un mismo `from` en la misma fase supera el saldo disponible $S_{\text{disp}} \ge 0$, `apply` aplica una regla determinista sin permitir jamás saldos negativos (`I-GEN-01`):
  1. En sistemas con reserva previa o prorrateo proporcional (p. ej. liquidación de mercado en Fase 6 o pagos de tesorería en Fase 8), cada transferencia $i$ recibe $\lfloor S_{\text{disp}} \times \text{amount}_i / \sum_j \text{amount}_j \rfloor$ en aritmética entera de `i128`, y el residuo de redondeo se asigna de unidad en unidad siguiendo el orden canónico `(from, to, origin, seq_in_system)`.
  2. Tanto el emisor `from` como el receptor `to` y el `e101-ledger` registran exactamente el importe efectivamente transferido `effective_amount`.

#### Categoría 2: Acumulaciones aditivas (`OpKind::Additive`)
Incluye `AddMoney`, `AddQty` y `AddRatioDelta` (para creación/destrucción neta autorizada o ajustes diferenciales de atributos como `legitimacy`, `morale`, `organization`, `trust` o `war_exhaustion`).
- **Regla de reducción conmutativa exacta:** Todas las entradas aditivas dirigidas a la misma `(TableTag, TargetId, FieldTag)` se ordenan por `(SourceId, SeqInSystem)` y se acumulan primero en un entero ensanchado de **128 bits con signo (`i128`)** antes de tocar el campo en `State`:
  $$\Delta_{\text{total}} = \sum_{k=1}^{n} \text{ i128::from}(\delta_k)$$
- Una vez calculado $\Delta_{\text{total}}$, `apply` lo suma al valor actual del campo mediante `checked_add` (para `Money` y `Qty` de fuentes/sumideros verificados) o `saturating_add` acotado al rango válido del dominio (para `Ratio` en $[0, 10\,000]\text{ pb}$ o dimensiones diplomáticas en $[-100, +100]$). Al usar un acumulador exacto `i128` y un orden canónico para los recortes de frontera (*clamping*), el resultado final y el desglose del `Ledger` son independientes del orden en que terminaron los hilos.

#### Categoría 3: Asignaciones de estado (`OpKind::SetState`)
Incluye `SetPrice`, `SetPosition`, `SetLaw`, `SetControl`, `SetOwner` y cambios de estado discreto.
- **Orden y detección de conflictos:** Se ordenan por `(TargetId, FieldTag, SystemPhase, Priority, SourceId)`.
- **Regla de unicidad:** En una misma fase del calendario, un campo discreto solo puede recibir una asignación única o varias asignaciones con prioridades estrictamente distintas (`Priority`). Si dos deltas emitidos en la misma fase intentan fijar valores distintos (`v1 != v2`) para la misma `(TargetId, FieldTag)` con igual `(SystemPhase, Priority)`, `apply` **rechaza la aplicación** y devuelve `Err(InvariantViolation::conflicting_set_delta(...))`. Nunca depende de "quién escribió último".

#### Categoría 4: Ciclo de vida de entidades (`OpKind::Lifecycle`)
Incluye `SpawnCohort`, `MergeCohorts`, `DestroyCompany`, `DestroyArmy`, `CreateCharacter`, `KillCharacter` y `CreateTreaty`.
- **Determinismo de `Id<T>` en `e101-store` ([ADR 0002](../adr/0002-determinism-rules.md)):** La asignación o liberación de ranuras en `Table<T>` altera la lista libre y las generaciones de los identificadores. Por ello, `apply` ordena todas las operaciones de ciclo de vida por su **clave natural de dominio** antes de invocar `table.insert(...)` o `table.remove(...)`:
  - `SpawnCohort` y `MergeCohorts`: ordenadas por `(ProvinceId, OccupationId, CultureId, ReligionId, LegalStatus)` (`§ 09` líneas 2141, 2388).
  - `DestroyCompany` / `DestroyArmy`: ordenadas por `(ArmyId, CompanyId)`.
  - `CreateCharacter` / `KillCharacter`: ordenadas por `(HomePolityId, BirthProvinceId, RoleTag, DeterministicSeedSalt)`.
- De este modo, los `Id<T>` asignados son idénticos bit a bit independientemente del número de hilos de ejecución (`QA-CORE-02`).

---

## 4. Parámetros iniciales

Los umbrales y cotas empleados por `e101-sim::apply` y el verificador de invariantes provienen del `Anexo AI` y de las secciones de dominio (`§§ 09–13`, `§ 21`):

| Parámetro | Clave en `Anexo AI` / Ref. | Valor en punto fijo | Descripción |
| :--- | :--- | :--- | :--- |
| Suelo de precio de mercado | `eco.price.min_max` (`§ 10` l. 2488) | $2\,000\text{ pb}$ ($0{,}20 \times P_{\text{base}}$) | Cota mínima permitida para $P(m, g)$ tras la Fase 6. |
| Techo de precio de mercado | `eco.price.min_max` (`§ 10` l. 2488) | $100\,000\text{ pb}$ ($10{,}00 \times P_{\text{base}}$) | Cota máxima permitida para $P(m, g)$ tras la Fase 6. |
| Paso máximo semanal de precio | `eco.price.max_change` (`§ 10` l. 2487) | $\pm 1\,000\text{ pb}$ ($\pm 10\,\%$ de $P_t$) | Variación máxima por ajuste semanal de mercado (`I-ECO-04`). |
| Suma de franjas de edad | `§ 09` líneas 2127, 2387 | $10\,000\text{ pb}$ ($100{,}00\,\%$) | `age_share[0] + age_share[1] + age_share[2]` en toda cohorte. |
| Máximo de cohortes por provincia (S / M / L) | `pop.cohort.max_per_province` (`§ 09` l. 2141) | `70` (S) / `50` (M) / `40` (L) | Tope duro de cohortes activas por provincia (`I-POP-04`). |
| Umbral de creación de cohorte | `pop.cohort.create_threshold` (`Anexo AI`) | `50 personas` (`Qty::from_units(50)`) | Mínimo en `pending_flows` para crear un nuevo `CohortId` en Fase 8 (`§ 09`). |
| Umbral de fusión de cohorte menor | `pop.cohort.merge_threshold` (`Anexo AI`) | $\max(100\text{ personas};\; 30\text{ pb } [0{,}30\,\%\text{ pob. prov.]})$ | Por debajo de este umbral, la cohorte se fusiona en Fase 8 (`§ 09`). |
| Tope mensual de refugiados recibidos | `§ 09` línea 2392 | $5\,000\text{ pb}$ ($50{,}00\,\%$ pob. previa) | Máximo de refugiados admitidos por una provincia en un mes (`I-POP-04`). |
| Suma de poder político de grupos | `§ 11` líneas 2924, 3095 | $10\,000\text{ pb}$ ($100{,}00\,\%$) | Suma normalizada del poder de los grupos de interés de un Estado (`I-POL-01`). |
| Cota de legitimidad y control provincial | `§ 11` líneas 2989, 3095 | $[0, 10\,000]\text{ pb}$ ($0\text{–}100\,\%$) | Rango válido de `legitimacy` estatal y `control` provincial (`I-POL-01`). |
| Periodo de implantación de reformas | `§ 11` línea 3096 | $12\text{ a }60\text{ meses}$ | Ninguna reforma alcanza $10\,000\text{ pb}$ de efecto antes de su plazo (`I-POL-02`). |
| Rangos de vectores diplomáticos | `§ 12` líneas 3155–3162 | $[0, 100]$, $[-100, +100]$, $[-50, +50]$ | Cotas de `trust/grievance/threat/dependency`, `interest` y `affinity` (`I-DIP-01`). |
| Cotas de atributos militares | `§ 13` líneas 3462–3466 | $[0, 10\,000]\text{ pb}$ | Rango válido para `equipment`, `morale` y `organization` (`I-WAR-01`). |

---

## 5. Invariantes

### 5.1. Tabla maestra de invariantes del motor

Todos los invariantes de `§§ 09–13`, `§ 23` y `Anexo AI` se codifican en `e101-sim::invariants` utilizando exclusivamente tipos en punto fijo (`Money`, `Qty`, `Ratio`, [ADR 0003](../adr/0003-fixed-point-types.md)) y acumuladores `i128`:

| ID | Sistema | Fórmula exacta en punto fijo | Frecuencia | Referencia |
| :--- | :--- | :--- | :--- | :--- |
| **I-ECO-01** | Economía (Bienes) | $\forall g \in \text{StorableGoods}: \sum_{m} \text{stock}_{t+1}(m, g) + \text{in\_transit}_{t+1}(g) = \sum_{m} \text{stock}_t(m, g) + \text{in\_transit}_t(g) + \text{prod}_t(g) - \text{cons}_t(g) - \text{spoilage\_and\_destruction}_t(g)$ (exacto en `Qty`) | Por tick en test/CI/Lab; mensual (Fase 17) y pre-save en partida normal | `§ 10` l. 2526, `QA-ECO-01` |
| **I-ECO-02** | Economía (Dinero) | $\sum_{s} \text{treasury}_{t+1}(s) + \sum_{c} \text{wealth}_{t+1}(c) + \sum_{k} \text{escrow}_{t+1}(k) = \sum_{s} \text{treasury}_t(s) + \sum_{c} \text{wealth}_t(c) + \sum_{k} \text{escrow}_t(k) + \text{mint\_seigniorage}_t - \text{melt\_loss}_t - \text{default\_writeoff}_t$ (exacto en `Money`) | Por tick en test/CI/Lab; mensual (Fase 17) y pre-save en partida normal | `§ 10` l. 2527, `QA-ECO-02` |
| **I-ECO-03** | Economía (Deuda) | $\forall d \in \text{ActiveDebts}: \text{debtor\_liability}(d) = \sum_{a \in \text{creditors}(d)} \text{creditor\_asset}(d, a)$ y $\sum_{d} \text{debtor\_liability}(d) = \sum_{d, a} \text{creditor\_asset}(d, a)$ (exacto en `Money`; tras quita o impago ambos lados bajan en la misma cuantía exacta) | En cada `apply` que toque deuda y en Fase 17 | `§ 10` l. 2528, l. 2798 (`default_creditors`), `QA-ECO-06` |
| **I-ECO-04** | Economía (Precios) | $\forall (m, g)$ tras Fase 6: $P_{\text{base}}(g)\text{.scale}(2\,000\text{ pb}) \le P_{t+1}(m, g) \le P_{\text{base}}(g)\text{.scale}(100\,000\text{ pb})$ y $\|P_{t+1}(m, g) - P_t(m, g)\| \le P_t(m, g)\text{.scale}(1\,000\text{ pb})$ (salvo `clamp` inicial de banda) | Semanal (Fase 6) y en Fase 17 | `§ 10` l. 2487–2489, `Anexo AI`, `QA-ECO-03` |
| **I-POP-01** | Demografía (Población) | $\sum_{c} \text{size}_{t+1}(c) + \sum_{f} \text{pending\_flows}_{t+1}(f) = \sum_{c} \text{size}_t(c) + \sum_{f} \text{pending\_flows}_t(f) + \text{births}_t - \text{demo\_deaths}_t - \text{epidemic\_deaths}_t - \text{combat\_attrition\_deaths}_t$ (exacto en `Qty`) | Por tick en test/CI/Lab; mensual (Fase 17) y pre-save en partida normal | `§ 09`, `§ 10` l. 2529, `QA-POP-01` |
| **I-POP-02** | Demografía (Fusión) | En toda provincia $p$, antes y después de `MergeCohorts` (Fase 8): $\sum_{c \in p} \text{size}_{\text{post}}(c) = \sum_{c \in p} \text{size}_{\text{pre}}(c)$ (`Qty`) y $\sum_{c \in p} \text{wealth}_{\text{post}}(c) = \sum_{c \in p} \text{wealth}_{\text{pre}}(c)$ (`Money`) bit a bit | Inmediato en cada ejecución de `MergeCohorts` | `§ 09` l. 2386 |
| **I-POP-03** | Demografía (Edades y leva) | $\forall c \in \text{AliveCohorts}: \text{age\_share}_c[0] + \text{age\_share}_c[1] + \text{age\_share}_c[2] = \text{Ratio::from\_basis\_points}(10\,000)$ y $\text{mobilized}_c \le \text{size}_c\text{.scale}(\text{age\_share}_c[1])$ | En cada `apply` que modifique una cohorte y en Fase 17 | `§ 09` l. 2127, 2134, 2387 |
| **I-POP-04** | Demografía (Claves y topes) | Clave `(province, occupation, culture, religion, legal_status)` única por provincia; $\|\text{cohorts}(p)\| \le \text{max\_per\_province}$ (`70`/`50`/`40`); prohibido fusionar distinto `legal_status`; $\text{refugees\_in}_{\text{mes}}(p) \le \text{pop}_{\text{prev}}(p)\text{.scale}(5\,000\text{ pb})$ | En cada `SpawnCohort` / `MergeCohorts` / migración y en Fase 17 | `§ 09` l. 2141, 2156, 2168, 2388–2389, 2392, `Anexo AI` |
| **I-POL-01** | Política (Poder y soberanía) | $\forall s \in \text{ActivePolities}: \sum_{g \in s} \text{power}_g = 10\,000\text{ pb}$, $\text{legitimacy}_s \in [0, 10\,000]\text{ pb}$; $\forall p \in \text{HabitableLandProvinces}: \text{control}_p \in [0, 10\,000]\text{ pb}$ y existe exactamente un `owner` soberano válido y un `controller` de hecho válido | En cada `apply` de política/mapa y en Fase 17 | `§ 11` l. 2924, 2989, 3095, `QA-POL-01` |
| **I-POL-02** | Política (Reformas y rebeliones) | $\forall r \in \text{Reforms}: \text{elapsed\_months}(r) < \text{ rollout\_months}(r) \implies \text{effect\_ratio}(r) < 10\,000\text{ pb}$ ($\text{rollout\_months} \in [12, 60]$); toda rebelión activa tiene `interest_group_id`, `leader_id` y $\ge 1$ demanda resoluble | En Fase 10 (Política) y en Fase 17 | `§ 11` l. 3096, 3098 |
| **I-DIP-01** | Diplomacia (Tratados y vectores) | $\nexists (A, B, C)$ tal que $A$ esté obligado simultáneamente a atacar a $C$ y a defender a $C$ (`treaty_consistency`); $\text{trust}, \text{grievance}, \text{threat}, \text{dependency} \in [0, 100]$, $\text{interest} \in [-100, +100]$, $\text{affinity} \in [-50, +50]$ | En cada `apply` diplomático (Fase 11) y en Fase 17 | `§ 12` l. 3155–3162, 3358, `QA-DIP-01` |
| **I-WAR-01** | Militar (Compañías y hastío) | $\forall u \in \text{ActiveCompanies}: \text{troops}_u > \text{Qty::ZERO}$ (si $\text{troops}_u == 0$, `apply` elimina la compañía), $\text{equipment}_u, \text{morale}_u, \text{organization}_u \in [0, 10\,000]\text{ pb}$; $\forall s: \text{war\_exhaustion}_s = \text{clamp}_{[0, 10\,000]}\left(\sum_{e \in \text{ledger}(s)} \delta_{\text{we}}(e)\right)$ (`war_exhaustion_composed`) | En cada `apply` militar (Fases 2–4) y en Fase 17 | `§ 13` l. 3462–3466, 3690 |
| **I-GEN-01** | General (No negatividad) | $\forall (m, g): \text{stock}(m, g) \ge 0$; $\forall c: \text{size}_c \ge 0 \land \text{wealth}_c \ge 0$; $\forall \text{asedio } z: \text{food\_reserve}_z \ge 0$; $\forall u: \text{troops}_u > 0$ | En cada `apply` sobre las entidades tocadas y en Fase 17 | `§ 10` l. 2530 |

### 5.2. Política ante una violación de invariante (`InvariantViolation`)

De acuerdo con `§ 21` (Fase 17, línea 4728), `§ 23` y el `Anexo X`, toda infracción detectada por `apply` o por el verificador de cierre construye un valor estructurado `InvariantViolation`:

```rust
#[derive(Clone, Debug, PartialEq, Eq)]
pub struct InvariantViolation {
    pub day: Day,
    pub phase: u8,
    pub invariant_id: &'static str,
    pub subject: String,
    pub expected: String,
    pub actual: String,
    pub message: String,
}
```

La frecuencia y la respuesta ante `Err(InvariantViolation)` dependen del entorno de ejecución:

1. **En pruebas unitarias, pruebas de propiedad (`proptest`), escenarios dorados (`cargo xtask golden`), CI y `101 Lab`:**
   - Se ejecutan **todos** los invariantes locales y globales (`I-ECO-01..04`, `I-POP-01..04`, `I-POL-01..02`, `I-DIP-01`, `I-WAR-01`, `I-GEN-01`) tras cada llamada a `apply` y al cierre de cada tick diario (Fase 17).
   - Cualquier `Err(InvariantViolation)` aborta de inmediato la prueba o campaña con el volcado completo de `(day, phase, invariant_id, subject, expected, actual, message)` y la semilla reproducible (`QA-CORE-01`). Esto garantiza el criterio de salida del `Anexo AH`: *"0 violaciones de invariantes en 100 campañas de 300 años por modo"*.
2. **En partida normal del jugador (`Release` cliente):**
   - **Verificación incremental en cada `apply`:** Los invariantes locales de coste $O(k)$ sobre las $k$ entidades modificadas en la fase (`I-GEN-01` no negatividad, `I-POP-02` fusión exacta, `I-POP-03` suma de franjas de edad y leva, `I-POP-04` clave única y tope de cohortes, `I-ECO-03` paridad de deuda tocada, `I-ECO-04` bandas de precio, `I-POL-01` suma de poder y cotas, `I-WAR-01` efectivos $> 0$ y cotas) se comprueban en línea al aplicar los deltas.
   - **Auditoría global mensual y pre-guardado:** La auditoría de conservación global en todo el mapa ($O(N)$ sobre todos los mercados, cohortes, flujos en tránsito, tesoros y deudas: `I-ECO-01`, `I-ECO-02`, `I-ECO-03`, `I-POP-01`, `I-DIP-01`) se ejecuta en el cierre mensual (`§ 21 Fase 17`, día 30 de cada mes) y **obligatoriamente antes de escribir cualquier archivo en `e101-save`** (`§ 25`). Si la auditoría falla antes de guardar, `e101-save` aborta la escritura en el archivo temporal y **jamás sobrescribe un autoguardado sano con un estado corrupto**.

---

## 6. Interacción con otros sistemas

- **Calendario del tick diario (`e101-sim`, `§ 21`, [ADR 0004](../adr/0004-tick-schedule-and-state-hash.md)):** El bucle diario invoca `apply(state, deltas)` como barrera de sincronización al terminar cada una de las fases de sistemas (`Fases 0 a 15`) y ejecuta el verificador de invariantes en la `Fase 17`.
- **Almacén de estado (`e101-store`, [ADR 0002](../adr/0002-determinism-rules.md)):** `apply` es el único punto del motor autorizado para mutar las columnas de `State` y para invocar inserciones o bajas generacionales (`Id<T>`) en orden de clave canónica.
- **Cola de comandos (`e101-commands`, `§ 21 Fase 0`):** Los comandos validados de jugador, red e IA se traducen en la Fase 0 en deltas tipados que pasan por el mismo conducto `apply` y las mismas comprobaciones de invariantes que los sistemas autónomos.
- **Libro mayor causal (`e101-ledger`, `§ 22`, `Anexo T`):** Durante la ejecución de `apply`, cada transferencia o acumulación aplicada emite su entrada causal confirmada (con el importe real pos-acotación) hacia `e101-ledger`.
- **Persistencia (`e101-save`, `§ 25`):** Antes de serializar una instantánea (manual o autoguardado mensual), `e101-save` invoca `invariants::check_all(state)` para blindar la integridad de los archivos en disco.

---

## 7. Registro causal

Toda operación en `Deltas` que modifique una variable visible para el jugador (`stock`, `price`, `treasury`, `wealth`, `size`, `legitimacy`, `control`, `power`, `trust`, `war_exhaustion`, `morale`) incluye obligatoriamente un descriptor `LedgerCause` (`§ 22`, `Anexo T`).

- **Emisión atómica estado + ledger:** `apply` actualiza el campo en `State` y registra la contribución en `e101-ledger` dentro del mismo paso secuencial. No puede existir un cambio en `State` sin su asiento en `LedgerDeltas`, ni un asiento en `e101-ledger` por un delta que haya sido recortado o rechazado.
- **Consistencia comprobada por invariante (`I-WAR-01`, `§ 22`):** Para variables compuestas como `war_exhaustion` (`§ 13` línea 3690) o balances de tesorería, el verificador comprueba que el valor almacenado en `State` coincida exactamente con la suma acotada de las contribuciones vigentes en `e101-ledger`.

---

## 8. Interfaz de usuario

Aunque `e101-sim::apply` pertenece al núcleo sin dependencias gráficas (`AGENTS.md § 2.5`), alimenta dos superficies de interfaz del cliente y de las herramientas (`Anexo P`, `Anexo W`):

1. **Desgloses causales sin discrepancias (`§ 22`):** Como `apply` registra en `e101-ledger` el importe exacto tras el prorrateo o `clamp`, los *tooltips* de tesorería, precios, población y hastío bélico suman exactamente el cambio neto mostrado en la cabecera, sin residuos "inexplicables" por redondeo o concurrencia.
2. **Panel de diagnóstico e inspector de `101 Forge` / cliente:** Si se produce un `InvariantViolation` en modo desarrollo, mod o prueba, el motor expone los campos `day`, `phase`, `invariant_id`, `subject`, `expected` y `actual` en el panel de diagnóstico de `101 Forge` (`Anexo W`) y genera un informe reproducible con el `CommandLog` hasta el tick exacto del fallo.

---

## 9. Pruebas y escenarios

De acuerdo con `§ 23`, `Anexo B`, `Anexo AH` y `T-109` (`Anexo AM`), la validación de `apply` e invariantes requiere las siguientes pruebas obligatorias antes de cerrar el PR:

1. **Determinismo multihilo (`QA-CORE-02`, `T-109`):**
   - Ejecutar un escenario sintético y el escenario dorado de Tesalia 1300 durante 360 ticks con grupos de hilos de Rayon configurados explícitamente a `1`, `4` y `16` hilos (`rayon::ThreadPoolBuilder::new().num_threads(n)`).
   - Comprobar que el hash BLAKE3 de `State` y de `e101-ledger` al final de cada tick es **idéntico bit a bit** en las tres configuraciones.
2. **Conmutatividad de fusión por permutación (`proptest`):**
   - Generar mediante `proptest` vectores arbitrarios de `Deltas` con miles de `TransferMoney`, `TransferQty`, `AddMoney`, `AddRatioDelta` y `SpawnCohort`.
   - Barajar aleatoriamente el orden de los elementos de `Vec<Deltas>` (simulando llegadas en distinto orden desde hilos de Rayon) y verificar que `apply(state.clone(), shuffled_deltas)` produce siempre el mismo `State` final y el mismo `Ledger` bit a bit.
3. **Pruebas de conservación y acotación bajo estrés (`QA-ECO-01`, `QA-ECO-02`, `QA-ECO-06`, `QA-POP-01`):**
   - Forzar múltiples transferencias concurrentes desde un mismo tesoro o almacén cuya suma supere el saldo disponible y verificar que `I-GEN-01` ($\ge 0$), `I-ECO-01` e `I-ECO-02` se cumplen con error `0` en `Qty` y `Money`.
   - Ejecutar `default_creditors` (`§ 10` línea 2798) sobre una deuda con múltiples tramos de acreedores cuyos porcentajes requieran reparto de residuo y verificar `I-ECO-03` ($\sum \text{pasivo} == \sum \text{activo}$).
   - Ejecutar `MergeCohorts` en provincias que superen `pop.cohort.max_per_province` y verificar `I-POP-02`, `I-POP-03` e `I-POP-04`.
4. **Inyección de fallos (pruebas negativas del verificador):**
   - Construir pruebas unitarias que inyecten deliberadamente una discrepancia de `1` unidad interna en `Money`, `Qty` o `Ratio` para cada uno de los 13 invariantes (`I-ECO-01..04`, `I-POP-01..04`, `I-POL-01..02`, `I-DIP-01`, `I-WAR-01`, `I-GEN-01`) y un conflicto en `SetState`, comprobando que `apply` o `check_all` devuelven el `Err(InvariantViolation)` con el `invariant_id` esperado.

---

## 10. Preguntas abiertas

- **Abierto (`apply.recovery.client_policy`):** Definir la política de recuperación de experiencia de usuario en el cliente comercial (`1.0`) si el chequeo mensual de la Fase 17 detecta un `InvariantViolation` durante una partida normal (p. ej., causada por datos de un mod o un caso extremo no cubierto):
  - *Opción A:* Pausar inmediatamente la simulación, bloquear el sobreguardado, mostrar un diálogo de error con opción de exportar el paquete reproducible (`seed` + `CommandLog` + `InvariantViolation`) y ofrecer cargar el último autoguardado mensual sano.
  - *Opción B:* Revertir automáticamente en memoria al último estado mensual verificado al inicio del mes y reejecutar el mes en modo diagnóstico de 1 hilo para aislar si el fallo proviene de un comando inválido o de un sistema de simulación.
