# Especificación técnica: Aritmética en punto fijo (`e101-store::fixed`)

- **Estado:** Aprobada (Fase 0 / M0 — Núcleo determinista)
- **Crate responsable:** `e101-store` (módulos `e101-store::fixed` y `e101-store::fixed::tables`)
- **Referencias del documento maestro:** `docs/master/101_Agents_Games_Documento_Maestro_v0.7.md` (§§ 09, 10, 11, 12, 13, 18, 22, 23, 46; Anexos B, P, T, W, X, AC, AG, AI)
- **Decisiones de arquitectura relacionadas:** `ADR 0002` (Determinismo estricto de simulación), `ADR 0003` (Aritmética en punto fijo para estado y contabilidad), decisiones cerradas `D-016` (unidad de cuenta metálica) y `D-019` (conversión de tasas anuales a mensuales)

---

## 1. Objetivo

Definir la representación binaria exacta, el álgebra dimensional, las reglas de redondeo determinista (*round half to even*), el reparto contable sin pérdidas de residuo y la evaluación de funciones no lineales tabuladas para las tres magnitudes numéricas fundamentales de **101 Engine**:

1. **`Money`**: valor monetario y precios expresados en unidades de cuenta (`uc`, equivalentes a $3{,}5\text{ g}$ de oro fino según `D-016` y § 11).
2. **`Qty`**: cantidades físicas de bienes materiales y efectivos demográficos (personas, soldados, toneladas equivalentes de grano, insumos; §§ 09, 10, 12).
3. **`Ratio`**: proporciones adimensionales, tasas demográficas, tipos impositivos, pesos de reparto y multiplicadores expresados en puntos básicos (`pb`; §§ 09–13).

El propósito de `e101-store::fixed` es garantizar el **Principio Innegociable 1 (Determinismo bit a bit)** y el **Principio Innegociable 3 (Contabilidad exacta)** en todas las arquitecturas soportadas (`x86_64` y `aarch64` en Windows, Linux y macOS), eliminando por construcción las divergencias de coma flotante IEEE 754 (`f32`/`f64`) en el estado persistente y en el libro mayor (`ADR 0002`, `ADR 0003`, § 22).

---

## 2. Alcance y fuera de alcance

### 2.1. Dentro del alcance

- Definición de los *newtypes* `Money(i64)`, `Qty(i64)` y `Ratio(i32)` en `e101-store::fixed` (Anexo X).
- Constantes de escala, constructores seguros, conversiones explícitas y serialización determinista (`serde::Serialize`, `serde::Deserialize`, `postcard`; § 23).
- Álgebra dimensional tipada: operaciones permitidas entre `Money`, `Qty`, `Ratio` y escalares enteros (`i64`), así como las operaciones prohibidas en tiempo de compilación.
- Aritmética intermedia en `i128` con redondeo al par más cercano (*banker's rounding* / *half-to-even*) mediante `div_round_half_to_even_i128`.
- Algoritmos de reparto contable exacto (`Money::allocate_exact`, `Qty::allocate_exact`) y normalización de cuotas (`Ratio::normalize_shares`), garantizando conservación estricta de masa y dinero (§§ 09, 10, 11).
- Modelo de errores tipado `FixedPointError` con `thiserror::Error` (§ 46).
- Submódulo `e101-store::fixed::tables` para funciones no lineales deterministas: conversión de tasas anuales a mensuales (`D-019`), decaimiento exponencial por semivida, raíz cuadrada entera escalada y tablas lineales por tramos (`PiecewiseLinearTable`; `ADR 0003`).
- Tabla de equivalencia exacta de los parámetros iniciales del Anexo AI a valores en punto fijo.

### 2.2. Fuera de alcance

- **Geometría de renderizado, cámara, audio e interpolación visual del cliente (`e101-client`, `e101-ui`):** pueden emplear `f32` o `f64` siempre que ningún valor de interfaz cruce la frontera hacia `e101-commands` o `e101-sim` (`ADR 0002`, `ADR 0003`, § 18).
- **Preprocesamiento offline en `data-build/`:** las herramientas de compilación geográfica pueden usar coma flotante durante la triangulación o proyección cartográfica, pero deben cuantizar todos los resultados a `Qty`, `Money`, `Ratio` o enteros antes de escribir los archivos `.ron`/`.bin` consumidos por el motor.
- **Lógica de negocio de mercados, demografía o combate:** esta especificación define las primitivas matemáticas en `e101-store::fixed`; las fórmulas de dominio viven en `e101-sim` y se rigen por sus respectivas especificaciones (§§ 09–13, Anexo W).

---

## 3. Modelo

### 3.1. Representación interna y escalas (`ADR 0003`, Anexo X)

Todos los tipos de punto fijo son envoltorios transparentes (`#[repr(transparent)]`) sobre enteros con signo en complemento a dos, ordenables (`Ord`, `PartialOrd`), comparables por igualdad exacta (`Eq`, `PartialEq`) y aptos para claves o valores deterministas sin el problema de `NaN` o `-0.0`.

| Tipo | Representación interna | Constante `SCALE` | Unidad base ($1{,}0$) | Resolución mínima ($1\text{ raw}$) | Rango representable aproximado | Uso principal en simulación |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **`Money`** | `i64` | $10\,000$ ($10^4$) | $1\text{ uc} = 10\,000\text{ raw}$ ($3{,}5\text{ g}$ oro fino, `D-016`) | $0{,}0001\text{ uc}$ ($10^{-4}\text{ uc}$) | $\pm 9{,}223 \times 10^{14}\text{ uc}$ | Tesoros, precios unitarios, salarios, impuestos, aranceles, costes de transporte y saldos del libro mayor (§ 10, § 11). |
| **`Qty`** | `i64` | $1\,000$ ($10^3$) | $1\text{ ud.} = 1\,000\text{ raw}$ ($1\text{ persona}$ o $1\text{ ud. bien}$) | $0{,}001\text{ ud.}$ ($10^{-3}\text{ ud.}$) | $\pm 9{,}223 \times 10^{15}\text{ ud.}$ | Población por cohorte, inventarios de bienes, producción, consumo, bajas y capacidad de transporte (§ 09, § 10, § 12). |
| **`Ratio`** | `i32` | $10\,000$ ($10^4$) | $1{,}0 = 10\,000\text{ pb}$ ($100\,\%$) | $1\text{ pb} = 0{,}01\,\% = 10^{-4}$ | $\pm 214\,748{,}3647$ ($\pm 21\,474\,836\,\%$) | Tasas de natalidad/mortalidad, impuestos, amortiguación de precios, modificadores de terreno, asimilación y cuotas (§§ 09–13). |

> [!IMPORTANT]
> **Invariante de serialización y memoria:** `Money`, `Qty` y `Ratio` llevan `#[repr(transparent)]`. En memoria y en capturas de `e101-save` (`postcard`, § 23), ocupan exactamente 8 bytes (`Money`, `Qty`) y 4 bytes (`Ratio`), permitiendo vectorización en las columnas SoA de `e101-store` (Anexo B, Anexo P).

### 3.2. Análisis dimensional y matriz de operaciones

El sistema de tipos de Rust impide sumar o multiplicar magnitudes incompatibles sin una conversión dimensional explícita (`ADR 0003`, Anexo X).

| Operando izquierdo | Operador / Método | Operando derecho | Tipo resultante | Fórmula intermedia y escala | Estado / Regla |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `Money` | `+`, `-` (`checked_*`, `saturating_*`) | `Money` | `Money` | `a.0 ± b.0` (escala $10^4$) | **Permitida.** Conserva dimensión monetaria. |
| `Money` | `Money::scale(self, r)` | `Ratio` | `Money` | $\text{round\_even}((m \cdot r) / 10\,000)$ en `i128` | **Permitida.** Escalado monetario por proporción. |
| `Money` | `checked_mul_i64` / `checked_div_i64` | `i64` | `Option<Money>` | `m.0 * k` / $\text{round\_even}(m / k)$ | **Permitida.** Multiplicación/división por escalar entero adimensional. |
| `Money` | `Ratio::from_money_quotient(num, den)` | `Money` | `Result<Ratio, FixedPointError>` | $\text{round\_even}((num \cdot 10\,000) / den)$ en `i128` | **Permitida.** Cociente de dos importes monetarios produce proporción adimensional. |
| `Qty` | `+`, `-` (`checked_*`, `saturating_*`) | `Qty` | `Qty` | `a.0 ± b.0` (escala $10^3$) | **Permitida.** Conserva dimensión física. |
| `Qty` | `Qty::scale(self, r)` | `Ratio` | `Qty` | $\text{round\_even}((q \cdot r) / 10\,000)$ en `i128` | **Permitida.** Aplicación de tasas a cantidades o poblaciones. |
| `Qty` | `Ratio::from_quotient(num, den)` | `Qty` | `Ratio` | $\text{round\_even}((num \cdot 10\,000) / den)$ en `i128` (saturante) | **Permitida.** Usada en exceso de demanda y ratios de inventario (Anexo W, Anexo X). |
| `Qty` | `Ratio::checked_from_quotient(num, den)` | `Qty` | `Result<Ratio, FixedPointError>` | $\text{round\_even}((num \cdot 10\,000) / den)$ en `i128` | **Permitida.** Variante estricta que devuelve error en división por cero o desbordamiento. |
| `Qty` | `Money::from_qty_price(qty, unit_price)` | `Money` | `Result<Money, FixedPointError>` | $\text{round\_even}((qty \cdot price) / 1\,000)$ en `i128` | **Permitida.** Producto de cantidad ($10^3$) por precio unitario ($10^4$) = importe total ($10^4$). |
| `Ratio` | `+`, `-`, `Neg` (`-r`), `checked_*` | `Ratio` | `Ratio` | `a.0 ± b.0` (escala $10^4$) | **Permitida.** Composición aditiva de tasas y modificadores (Anexo W). |
| `Ratio` | `*` (`Mul<Ratio>`), `Ratio::mul_ratio` | `Ratio` | `Ratio` | $\text{round\_even}((a \cdot b) / 10\,000)$ en `i128` | **Permitida.** Composición multiplicativa de factores (`imbalance * DAMPING`, Anexo W). |
| `Money` | `+`, `-` | `Qty` o `Ratio` | — | Error de compilación | **Prohibida.** Suma de dimensiones heterogéneas. |
| `Money` | `*` | `Money` | — | Error de compilación | **Prohibida.** $\text{uc}^2$ carece de significado económico. |
| `Qty` | `*` | `Qty` | — | Error de compilación | **Prohibida.** $\text{ud.}^2$ directo sin operador geométrico explícito. |

---

### 3.3. Algoritmo exacto de redondeo *half-to-even* (`div_round_half_to_even_i128`)

Toda división o reescalado en `e101-store::fixed` utiliza redondeo al entero más cercano y, en caso de empate exacto en la mitad ($\pm 0{,}5$), redondea hacia el entero **par** más cercano (*round half to even*, `ADR 0003`). Esto elimina el sesgo estadístico sistemático (deriva alcista o bajista) cuando se acumulan millones de transacciones semanales o tasas demográficas mensuales.

#### Implementación de referencia en Rust

```rust
/// Divide `num` entre `den` (donde `den > 0`) usando aritmética entera exacta en `i128`
/// y redondeo *half-to-even* (banker's rounding).
///
/// # Panics
/// Hace panic en modo debug si `den <= 0` (los llamadores internos garantizan `den > 0`
/// o validan previamente con `FixedPointError::DivisionByZero`).
#[inline]
pub const fn div_round_half_to_even_i128(num: i128, den: i128) -> i128 {
    debug_assert!(den > 0, "denominator must be strictly positive");
    let quot = num / den;
    let rem = num % den;
    let abs_rem = rem.abs();
    let twice_rem = abs_rem * 2;

    if twice_rem < den {
        quot
    } else if twice_rem > den {
        if num >= 0 {
            quot + 1
        } else {
            quot - 1
        }
    } else {
        // Empate exacto en .5: redondear hacia el cociente par más cercano.
        if quot % 2 == 0 {
            quot
        } else if num >= 0 {
            quot + 1
        } else {
            quot - 1
        }
    }
}
```

#### Demostración numérica de resolución de empates

| Operación racional | `num` (`i128`) | `den` (`i128`) | `quot` (`num / den`) | `rem` (`num % den`) | Comparación `2 * |rem|` vs `den` | Paridad de `quot` | Resultado *half-to-even* |
| :--- | ---: | ---: | ---: | ---: | :--- | :--- | ---: |
| $+2{,}4 = 24 / 10$ | $+24$ | $10$ | $+2$ | $+4$ | $8 < 10$ (menor que $0{,}5$) | — | **$+2$** |
| $+2{,}5 = 25 / 10$ | $+25$ | $10$ | $+2$ | $+5$ | $10 == 10$ (**empate `.5`**) | $+2$ es **par** | **$+2$** |
| $+3{,}5 = 35 / 10$ | $+35$ | $10$ | $+3$ | $+5$ | $10 == 10$ (**empate `.5`**) | $+3$ es **impar** ($\to +3 + 1$) | **$+4$** |
| $-2{,}5 = -25 / 10$ | $-25$ | $10$ | $-2$ | $-5$ | $10 == 10$ (**empate `.5`**) | $-2$ es **par** | **$-2$** |
| $-3{,}5 = -35 / 10$ | $-35$ | $10$ | $-3$ | $-5$ | $10 == 10$ (**empate `.5`**) | $-3$ es **impar** ($\to -3 - 1$) | **$-4$** |
| $+2{,}6 = 26 / 10$ | $+26$ | $10$ | $+2$ | $+6$ | $12 > 10$ (mayor que $0{,}5$) | — | **$+3$** |

---

### 3.4. Especificación completa de la API en Rust (`e101-store::fixed`)

El siguiente bloque define la interfaz pública normativa de `e101-store::fixed`, alineada al 100 % con el Anexo X (líneas 8262–8373) y el Anexo W (líneas 8196–8226) del documento maestro:

```rust
// crates/e101-store/src/fixed/mod.rs
#![forbid(unsafe_code)]

use core::ops::{Add, Mul, Neg, Sub};
use serde::{Deserialize, Serialize};
use thiserror::Error;

pub mod tables;

/// Error tipado para operaciones aritméticas y de tablas en punto fijo (§ 46).
#[derive(Copy, Clone, Debug, PartialEq, Eq, Error, Serialize, Deserialize)]
pub enum FixedPointError {
    #[error("fixed-point overflow during operation `{op}`")]
    Overflow { op: &'static str },

    #[error("division by zero during operation `{op}`")]
    DivisionByZero { op: &'static str },

    #[error("negative quantity not allowed in domain context: raw={raw}")]
    NegativeQuantityNotAllowed { raw: i64 },

    #[error("invalid piecewise linear table: {reason}")]
    InvalidPiecewiseTable { reason: &'static str },

    #[error("value {value} out of domain bounds [{min}, {max}]")]
    DomainOutOfBounds { value: i64, min: i64, max: i64 },
}

/// Importe monetario en diezmilésimas de unidad de cuenta (`1 uc = 10_000`).
/// 1 uc equivale a 3,5 g de oro fino (D-016).
#[repr(transparent)]
#[derive(
    Copy, Clone, Debug, Default, PartialEq, Eq, PartialOrd, Ord, Hash, Serialize, Deserialize,
)]
pub struct Money(pub i64);

/// Cantidad física de bienes o personas en milésimas de unidad (`1 unidad = 1_000`).
#[repr(transparent)]
#[derive(
    Copy, Clone, Debug, Default, PartialEq, Eq, PartialOrd, Ord, Hash, Serialize, Deserialize,
)]
pub struct Qty(pub i64);

/// Proporción o tasa en puntos básicos (`1.0 = 100 % = 10_000 pb`).
#[repr(transparent)]
#[derive(
    Copy, Clone, Debug, Default, PartialEq, Eq, PartialOrd, Ord, Hash, Serialize, Deserialize,
)]
pub struct Ratio(pub i32);

impl Money {
    pub const ZERO: Money = Money(0);
    pub const ONE_UC: Money = Money(10_000);
    pub const SCALE: i64 = 10_000;

    #[inline]
    pub const fn from_units(units: i64) -> Money {
        Money(units.saturating_mul(Self::SCALE))
    }

    #[inline]
    pub const fn from_raw(raw: i64) -> Money {
        Money(raw)
    }

    #[inline]
    pub const fn raw(self) -> i64 {
        self.0
    }

    /// Escala un importe monetario por un `Ratio` usando redondeo *half-to-even*.
    #[inline]
    pub fn scale(self, r: Ratio) -> Money {
        let prod = (self.0 as i128) * (r.0 as i128);
        let scaled = div_round_half_to_even_i128(prod, Ratio::SCALE as i128);
        Money(scaled.clamp(i64::MIN as i128, i64::MAX as i128) as i64)
    }

    #[inline]
    pub const fn checked_add(self, other: Money) -> Option<Money> {
        match self.0.checked_add(other.0) {
            Some(v) => Some(Money(v)),
            None => None,
        }
    }

    #[inline]
    pub const fn checked_sub(self, other: Money) -> Option<Money> {
        match self.0.checked_sub(other.0) {
            Some(v) => Some(Money(v)),
            None => None,
        }
    }

    #[inline]
    pub const fn checked_mul_i64(self, factor: i64) -> Option<Money> {
        match self.0.checked_mul(factor) {
            Some(v) => Some(Money(v)),
            None => None,
        }
    }

    #[inline]
    pub const fn checked_div_i64(self, divisor: i64) -> Option<Money> {
        if divisor == 0 {
            return None;
        }
        let num = self.0 as i128;
        let den = divisor as i128;
        let sign = if den < 0 { -1 } else { 1 };
        let res = div_round_half_to_even_i128(num * sign, den.abs());
        if res < (i64::MIN as i128) || res > (i64::MAX as i128) {
            None
        } else {
            Some(Money(res as i64))
        }
    }

    #[inline]
    pub const fn saturating_add(self, other: Money) -> Money {
        Money(self.0.saturating_add(other.0))
    }

    #[inline]
    pub const fn saturating_sub(self, other: Money) -> Money {
        Money(self.0.saturating_sub(other.0))
    }

    #[inline]
    pub fn clamp(self, min: Money, max: Money) -> Money {
        Money(self.0.clamp(min.0, max.0))
    }

    /// Calcula el importe monetario total `qty * unit_price` dividiendo entre `Qty::SCALE` (1_000)
    /// con redondeo *half-to-even*.
    #[inline]
    pub fn from_qty_price(qty: Qty, unit_price: Money) -> Result<Money, FixedPointError> {
        let prod = (qty.0 as i128) * (unit_price.0 as i128);
        let scaled = div_round_half_to_even_i128(prod, Qty::SCALE as i128);
        i64::try_from(scaled)
            .map(Money)
            .map_err(|_| FixedPointError::Overflow { op: "Money::from_qty_price" })
    }

    /// Reparte `total` proporcionalmente a `weights` garantizando que la suma de las partes
    /// sea exactamente igual a `total`. El residuo de redondeo se asigna a la partida con
    /// mayor peso (y menor índice en caso de empate).
    pub fn allocate_exact(total: Money, weights: &[Ratio]) -> Vec<Money> {
        if weights.is_empty() {
            return Vec::new();
        }
        let weight_sum: i128 = weights.iter().map(|w| i128::from(w.0.max(0))).sum();
        if weight_sum <= 0 {
            let mut out = vec![Money::ZERO; weights.len()];
            out[0] = total;
            return out;
        }
        let mut out = Vec::with_capacity(weights.len());
        let mut allocated_sum: i64 = 0;
        let mut max_idx: usize = 0;
        let mut max_weight: i32 = i32::MIN;

        for (i, w) in weights.iter().copied().enumerate() {
            let w_pos = w.0.max(0);
            if w_pos > max_weight {
                max_weight = w_pos;
                max_idx = i;
            }
            let raw_share =
                div_round_half_to_even_i128((total.0 as i128) * (w_pos as i128), weight_sum) as i64;
            allocated_sum = allocated_sum.saturating_add(raw_share);
            out.push(Money(raw_share));
        }

        let remainder = total.0.saturating_sub(allocated_sum);
        out[max_idx] = Money(out[max_idx].0.saturating_add(remainder));
        out
    }
}

impl Qty {
    pub const ZERO: Qty = Qty(0);
    pub const ONE: Qty = Qty(1_000);
    pub const SCALE: i64 = 1_000;

    #[inline]
    pub const fn from_units(units: i64) -> Qty {
        Qty(units.saturating_mul(Self::SCALE))
    }

    #[inline]
    pub const fn from_raw(raw: i64) -> Qty {
        Qty(raw)
    }

    #[inline]
    pub const fn raw(self) -> i64 {
        self.0
    }

    /// Escala una cantidad física por un `Ratio` usando redondeo *half-to-even*.
    #[inline]
    pub fn scale(self, r: Ratio) -> Qty {
        let prod = (self.0 as i128) * (r.0 as i128);
        let scaled = div_round_half_to_even_i128(prod, Ratio::SCALE as i128);
        Qty(scaled.clamp(i64::MIN as i128, i64::MAX as i128) as i64)
    }

    #[inline]
    pub const fn checked_add(self, other: Qty) -> Option<Qty> {
        match self.0.checked_add(other.0) {
            Some(v) => Some(Qty(v)),
            None => None,
        }
    }

    #[inline]
    pub const fn checked_sub(self, other: Qty) -> Option<Qty> {
        match self.0.checked_sub(other.0) {
            Some(v) => Some(Qty(v)),
            None => None,
        }
    }

    #[inline]
    pub const fn saturating_add(self, other: Qty) -> Qty {
        Qty(self.0.saturating_add(other.0))
    }

    #[inline]
    pub const fn saturating_sub(self, other: Qty) -> Qty {
        Qty(self.0.saturating_sub(other.0))
    }

    #[inline]
    pub fn clamp(self, min: Qty, max: Qty) -> Qty {
        Qty(self.0.clamp(min.0, max.0))
    }

    #[inline]
    pub fn max(self, other: Qty) -> Qty {
        Qty(self.0.max(other.0))
    }

    #[inline]
    pub fn min(self, other: Qty) -> Qty {
        Qty(self.0.min(other.0))
    }

    /// Reparte `total` proporcionalmente a `weights` garantizando conservación exacta de masa/población.
    pub fn allocate_exact(total: Qty, weights: &[Ratio]) -> Vec<Qty> {
        if weights.is_empty() {
            return Vec::new();
        }
        let weight_sum: i128 = weights.iter().map(|w| i128::from(w.0.max(0))).sum();
        if weight_sum <= 0 {
            let mut out = vec![Qty::ZERO; weights.len()];
            out[0] = total;
            return out;
        }
        let mut out = Vec::with_capacity(weights.len());
        let mut allocated_sum: i64 = 0;
        let mut max_idx: usize = 0;
        let mut max_weight: i32 = i32::MIN;

        for (i, w) in weights.iter().copied().enumerate() {
            let w_pos = w.0.max(0);
            if w_pos > max_weight {
                max_weight = w_pos;
                max_idx = i;
            }
            let raw_share =
                div_round_half_to_even_i128((total.0 as i128) * (w_pos as i128), weight_sum) as i64;
            allocated_sum = allocated_sum.saturating_add(raw_share);
            out.push(Qty(raw_share));
        }

        let remainder = total.0.saturating_sub(allocated_sum);
        out[max_idx] = Qty(out[max_idx].0.saturating_add(remainder));
        out
    }
}

impl Ratio {
    pub const ZERO: Ratio = Ratio(0);
    pub const ONE: Ratio = Ratio(10_000);
    pub const SCALE: i32 = 10_000;

    #[inline]
    pub const fn from_basis_points(bp: i32) -> Ratio {
        Ratio(bp)
    }

    #[inline]
    pub const fn basis_points(self) -> i32 {
        self.0
    }

    /// Calcula el cociente `num / den` como `Ratio` saturando a los límites de `i32` (Anexo W, Anexo X).
    #[inline]
    pub fn from_quotient(num: Qty, den: Qty) -> Ratio {
        if den.0 == 0 {
            return if num.0 >= 0 { Ratio(i32::MAX) } else { Ratio(i32::MIN) };
        }
        let n = (num.0 as i128) * (Self::SCALE as i128);
        let d = den.0 as i128;
        let sign = if d < 0 { -1 } else { 1 };
        let q = div_round_half_to_even_i128(n * sign, d.abs());
        Ratio(q.clamp(i32::MIN as i128, i32::MAX as i128) as i32)
    }

    /// Calcula el cociente `num / den` devolviendo error si `den == 0` o si desborda `i32`.
    #[inline]
    pub fn checked_from_quotient(num: Qty, den: Qty) -> Result<Ratio, FixedPointError> {
        if den.0 == 0 {
            return Err(FixedPointError::DivisionByZero { op: "Ratio::checked_from_quotient" });
        }
        let n = (num.0 as i128) * (Self::SCALE as i128);
        let d = den.0 as i128;
        let sign = if d < 0 { -1 } else { 1 };
        let q = div_round_half_to_even_i128(n * sign, d.abs());
        i32::try_from(q)
            .map(Ratio)
            .map_err(|_| FixedPointError::Overflow { op: "Ratio::checked_from_quotient" })
    }

    /// Calcula el cociente monetario `num / den` como `Ratio` verificando división por cero y overflow.
    #[inline]
    pub fn from_money_quotient(num: Money, den: Money) -> Result<Ratio, FixedPointError> {
        if den.0 == 0 {
            return Err(FixedPointError::DivisionByZero { op: "Ratio::from_money_quotient" });
        }
        let n = (num.0 as i128) * (Self::SCALE as i128);
        let d = den.0 as i128;
        let sign = if d < 0 { -1 } else { 1 };
        let q = div_round_half_to_even_i128(n * sign, d.abs());
        i32::try_from(q)
            .map(Ratio)
            .map_err(|_| FixedPointError::Overflow { op: "Ratio::from_money_quotient" })
    }

    #[inline]
    pub const fn checked_add(self, other: Ratio) -> Option<Ratio> {
        match self.0.checked_add(other.0) {
            Some(v) => Some(Ratio(v)),
            None => None,
        }
    }

    #[inline]
    pub const fn checked_sub(self, other: Ratio) -> Option<Ratio> {
        match self.0.checked_sub(other.0) {
            Some(v) => Some(Ratio(v)),
            None => None,
        }
    }

    /// Multiplica dos proporciones (`(self * other) / 10_000`) con redondeo *half-to-even*.
    #[inline]
    pub fn mul_ratio(self, other: Ratio) -> Ratio {
        let prod = (self.0 as i128) * (other.0 as i128);
        let scaled = div_round_half_to_even_i128(prod, Self::SCALE as i128);
        Ratio(scaled.clamp(i32::MIN as i128, i32::MAX as i128) as i32)
    }

    #[inline]
    pub fn clamp(self, min: Ratio, max: Ratio) -> Ratio {
        Ratio(self.0.clamp(min.0, max.0))
    }

    /// Normaliza `N` pesos no negativos para que la suma de los `Ratio` resultantes sea
    /// exactamente `Ratio::ONE` (`10_000 pb`), asignando el residuo al elemento de mayor peso
    /// (y menor índice en caso de empate; §§ 09, 11).
    pub fn normalize_shares<const N: usize>(weights: [i64; N]) -> [Ratio; N] {
        assert!(N > 0, "normalize_shares requires N > 0");
        let sum: i128 = weights.iter().map(|&w| i128::from(w.max(0))).sum();
        if sum <= 0 {
            let mut out = [Ratio::ZERO; N];
            out[0] = Ratio::ONE;
            return out;
        }
        let mut out = [Ratio::ZERO; N];
        let mut acc: i32 = 0;
        let mut max_idx: usize = 0;
        let mut max_weight: i64 = i64::MIN;

        for i in 0..N {
            let w = weights[i].max(0);
            if w > max_weight {
                max_weight = w;
                max_idx = i;
            }
            let bp = div_round_half_to_even_i128((w as i128) * (Self::SCALE as i128), sum) as i32;
            out[i] = Ratio(bp);
            acc = acc.saturating_add(bp);
        }

        let remainder = Self::SCALE.saturating_sub(acc);
        out[max_idx] = Ratio(out[max_idx].0.saturating_add(remainder));
        out
    }
}

// Traits estándar requeridos por Anexo W (p. ej. `Ratio::ONE + step`, `-MAX_STEP`, `imbalance * DAMPING`)
impl Add for Ratio {
    type Output = Ratio;
    #[inline]
    fn add(self, rhs: Ratio) -> Ratio {
        Ratio(self.0.saturating_add(rhs.0))
    }
}

impl Sub for Ratio {
    type Output = Ratio;
    #[inline]
    fn sub(self, rhs: Ratio) -> Ratio {
        Ratio(self.0.saturating_sub(rhs.0))
    }
}

impl Neg for Ratio {
    type Output = Ratio;
    #[inline]
    fn neg(self) -> Ratio {
        Ratio(self.0.saturating_neg())
    }
}

impl Mul<Ratio> for Ratio {
    type Output = Ratio;
    #[inline]
    fn mul(self, rhs: Ratio) -> Ratio {
        self.mul_ratio(rhs)
    }
}
```

---

### 3.5. Catálogo de errores (`FixedPointError`, § 46)

| Variante de `FixedPointError` | Cuándo se produce | Tratamiento en los sistemas de simulación (`e101-sim`) | Impacto en invariantes |
| :--- | :--- | :--- | :--- |
| `Overflow { op }` | El resultado de una operación verificada (`from_qty_price`, `checked_from_quotient`, `from_money_quotient`) excede el rango de `i64` o `i32`. | En validación de comandos se rechaza el comando; en un sistema de tick satura al límite de dominio (`clamp`) y emite diagnóstico de telemetría en modo debug/Lab. | Evita el *wrap-around* silencioso que violaría la no negatividad de tesoros o inventarios (Invariantes I-02, I-05). |
| `DivisionByZero { op }` | El denominador pasado a `checked_from_quotient` o `from_money_quotient` es `0`. | El sistema aplica la rama de guarda del dominio (p. ej. `target.max(Qty::ONE)` en precios, Anexo W, o cuota nula si la población total es `Qty::ZERO`). | Impide pánicos en ejecución dentro del bucle de ticks determinista (§ 46). |
| `NegativeQuantityNotAllowed { raw }` | Un constructor de dominio o función matemática (`sqrt_ratio`) recibe un valor negativo donde solo tienen sentido magnitudes $\ge 0$. | Se rechaza en la carga de datos (`cargo xtask data`) o se satura a `0` antes de calcular el delta. | Preserva la no negatividad estricta de poblaciones e inventarios (§§ 09, 10). |
| `InvalidPiecewiseTable { reason }` | Una tabla lineal por tramos cargada desde `.ron` tiene menos de 2 nodos, abscisas no estrictamente crecientes ($x_i \ge x_{i+1}$) o valores fuera de rango. | Fallo inmediato (*fail-fast*) al compilar o cargar el paquete de datos en `e101-content` / `cargo xtask data`. | Garantiza que toda evaluación de curva en tiempo de simulación sea total, continua y determinista. |
| `DomainOutOfBounds { value, min, max }` | Una entrada a una tabla precalculada (como `annual_to_monthly_rate`) cae fuera del dominio matemático válido ($r_{\text{año}} \notin [0, 10\,000]\text{ pb}$). | Fallo en validación de contenido o saturación explícita en los bordes del dominio según la especificación del sistema. | Garantiza tasas mensuales acotadas en $[0, 10\,000]\text{ pb}$ (`D-019`). |

---

### 3.6. Funciones no lineales por tablas (`e101-store::fixed::tables`, `ADR 0003`, `D-019`)

Dado que el motor prohíbe invocar `f64::powf`, `f64::exp`, `f64::ln` o `f64::sqrt` en la simulación (`ADR 0002`, `ADR 0003`), todas las relaciones no lineales de las §§ 09, 10, 11 y 12 se resuelven en `e101-store::fixed::tables` mediante cuatro primitivas deterministas:

#### 1. Conversión de tasa anual a tasa mensual compuesta (`annual_to_monthly_rate`, `D-019`)

En demografía (§ 09) y asimilación/conversión (§ 13), una tasa anual $r_{\text{año}} \in [0, 1]$ se convierte en su tasa mensual equivalente según la fórmula cerrada de `D-019`:

$$r_{\text{mes}} = 1 - (1 - r_{\text{año}})^{1/12}$$

- **Implementación:** Tabla estática `ANNUAL_TO_MONTHLY_BP: [i32; 10_001]` indexada directamente por los puntos básicos de `r_year` ($0 \le \text{bp} \le 10\,000$), generada en compilación/build con aritmética racional de alta precisión y redondeada *half-to-even* a puntos básicos, o para tasas pequeñas ($r_{\text{año}} \le 2\,000\text{ pb}$) serie de Taylor entera de orden 3 en `i128` verificada bit a bit contra la tabla.
- **Firma:** `pub fn annual_to_monthly_rate(r_year: Ratio) -> Ratio` (para entradas negativas devuelve `Ratio::ZERO`; para entradas $\ge 10\,000\text{ pb}$ devuelve `Ratio::ONE`).

#### 2. Decaimiento exponencial por semivida (`half_life_decay`)

Usado para el decaimiento de agravios diplomáticos, prestigio, devastación provincial y fatiga bélica (§§ 11, 12, 14):

$$v(t + \Delta t) = \text{round\_even}\!\left(v(t) \cdot 2^{-\Delta t / t_{1/2}}\right)$$

- **Implementación:** División euclídea $\Delta t = q \cdot t_{1/2} + r$ con $0 \le r < t_{1/2}$. El factor entero $2^{-q}$ se aplica como desplazamiento/división por $2^q$, y la fracción $2^{-r / t_{1/2}}$ se interpola linealmente en una tabla fija `EXP2_NEG_FRAC_TABLE: [i32; 1025]` de $1\,025$ nodos en escala $10^4$, finalizando con `div_round_half_to_even_i128`.
- **Firma:** `pub fn half_life_decay(value: i64, elapsed_days: u32, half_life_days: u32) -> i64`.

#### 3. Raíz cuadrada entera escalada (`sqrt_ratio`)

Usada en rendimientos decrecientes de infraestructura, alcance logístico y dispersión (§§ 10, 12):

$$\text{sqrt\_ratio}(x) = \text{round\_even}\!\left(\sqrt{\frac{x}{10\,000}} \times 10\,000\right) = \text{isqrt\_round}(x \times 10\,000)$$

- **Implementación:** Si `x.0 < 0`, devuelve `Err(FixedPointError::NegativeQuantityNotAllowed { raw: x.0 as i64 })`. Si `x.0 >= 0`, calcula $N = (x.0\text{ as i128}) \times 10\,000$, obtiene la raíz entera $s = \lfloor\sqrt{N}\rfloor$ por el método de Newton entero determinista y redondea a $s + 1$ si y solo si $N - s^2 > s$ (resolución exacta al entero más cercano).
- **Firma:** `pub fn sqrt_ratio(x: Ratio) -> Result<Ratio, FixedPointError>`.

#### 4. Tablas lineales por tramos (`PiecewiseLinearTable`, `ADR 0003`)

Evalúa las funciones de respuesta demográfica y económica definidas en `games/epoch/data/rules/*.ron` (§ 09):
- `f_vida` (modificador de mortalidad por nivel de vida),
- `g_alimentos` (modificador de natalidad/mortalidad por cobertura calórica),
- `f_paz` (modificador demográfico por paz/saqueo),
- `h_crianza` (supervivencia de la cohorte infantil $0\text{–}14$ años).

```rust
/// Punto de control `(x, y)` de una curva lineal por tramos en puntos básicos.
#[derive(Copy, Clone, Debug, PartialEq, Eq, Serialize, Deserialize)]
pub struct Knot {
    pub x: Ratio,
    pub y: Ratio,
}

/// Tabla lineal por tramos validada al cargar `games/epoch/data/rules/*.ron`.
#[derive(Clone, Debug, PartialEq, Eq, Serialize, Deserialize)]
pub struct PiecewiseLinearTable {
    knots: Vec<Knot>,
}

impl PiecewiseLinearTable {
    pub fn new(knots: Vec<Knot>) -> Result<Self, FixedPointError> {
        if knots.len() < 2 {
            return Err(FixedPointError::InvalidPiecewiseTable {
                reason: "at least 2 knots are required",
            });
        }
        for pair in knots.windows(2) {
            if pair[0].x >= pair[1].x {
                return Err(FixedPointError::InvalidPiecewiseTable {
                    reason: "knot x coordinates must be strictly increasing",
                });
            }
        }
        Ok(Self { knots })
    }

    /// Evalúa `y(x)` con saturación en los extremos e interpolación lineal exacta
    /// redondeada con *half-to-even* entre nodos adyacentes (`ADR 0003`).
    pub fn eval(&self, x: Ratio) -> Ratio {
        let first = self.knots[0];
        if x <= first.x {
            return first.y;
        }
        let last = self.knots[self.knots.len() - 1];
        if x >= last.x {
            return last.y;
        }
        // Búsqueda binaria determinista del tramo [k0, k1] tal que k0.x <= x <= k1.x
        let idx = self.knots.partition_point(|k| k.x <= x) - 1;
        let k0 = self.knots[idx];
        let k1 = self.knots[idx + 1];
        let dx = (k1.x.0 as i128) - (k0.x.0 as i128);
        let dy = (k1.y.0 as i128) - (k0.y.0 as i128);
        let num = ((x.0 as i128) - (k0.x.0 as i128)) * dy;
        let interp = (k0.y.0 as i128) + super::div_round_half_to_even_i128(num, dx);
        Ratio(interp as i32)
    }
}
```

---

## 4. Parámetros iniciales

Todos los parámetros numéricos cargados desde `games/epoch/data/rules/*.ron` se traducen a `Money`, `Qty` y `Ratio` siguiendo las cifras normativas del **Anexo AI** (*Tabla consolidada de parámetros iniciales*, líneas 9157–9205) y de las §§ 09, 10, 11 y 13:

| Clave de parámetro (Anexo AI) | Valor documental (Anexo AI) | Tipo en `e101-store::fixed` | Constructor / Valor crudo exacto | Equivalencia verificada |
| :--- | :--- | :--- | :--- | :--- |
| `pop.fertility.base` | $72{,}7\,\text{‰}$ anual por adulto ($15\text{–}54$) | `Ratio` | `Ratio::from_basis_points(727)` | $727\text{ pb} = 0{,}0727 = 72{,}7\,\text{‰}$ (§ 09, Anexo AI) |
| `pop.mortality.children` | $55\,\text{‰}$ anual ($0\text{–}14$) | `Ratio` | `Ratio::from_basis_points(550)` | $550\text{ pb} = 0{,}0550 = 55\,\text{‰}$ (§ 09, Anexo AI) |
| `pop.mortality.adults` | $16\,\text{‰}$ anual ($15\text{–}54$) | `Ratio` | `Ratio::from_basis_points(160)` | $160\text{ pb} = 0{,}0160 = 16\,\text{‰}$ (§ 09, Anexo AI) |
| `pop.mortality.elders` | $85\,\text{‰}$ anual ($55+$) | `Ratio` | `Ratio::from_basis_points(850)` | $850\text{ pb} = 0{,}0850 = 85\,\text{‰}$ (§ 09, Anexo AI) |
| `pop.migration.cap_free` | $1\,\%$ mensual de la cohorte origen | `Ratio` | `Ratio::from_basis_points(100)` | $100\text{ pb} = 0{,}0100 = 1\,\%$ (§ 09, Anexo AI) |
| `pop.mobility.cap` | $0{,}5\,\%$ mensual de la cohorte | `Ratio` | `Ratio::from_basis_points(50)` | $50\text{ pb} = 0{,}0050 = 0{,}5\,\%$ (§ 09, Anexo AI) |
| `eco.price.k` | $1\,000\text{ pb}$ ($0{,}10$) | `Ratio` | `Ratio::from_basis_points(1_000)` | $1\,000\text{ pb} = 10\,\%$ amortiguación semanal (§ 10, Anexo W, Anexo AI) |
| `eco.price.max_change` | $1\,000\text{ pb}$ ($\pm 10\,\%$ semanal) | `Ratio` | `Ratio::from_basis_points(1_000)` | $1\,000\text{ pb} = \pm 10\,\%$ cambio máximo por semana (§ 10, Anexo W, Anexo AI) |
| `eco.price.min_max` (mínimo) | $2\,000\text{ pb}$ ($0{,}20 \times P_{\text{base}}$) | `Ratio` | `Ratio::from_basis_points(2_000)` | Suelo de precio relativo $0{,}20 \times P_{\text{base}}$ (§ 10, Anexo W, Anexo AI) |
| `eco.price.min_max` (máximo) | $100\,000\text{ pb}$ ($10{,}0 \times P_{\text{base}}$) | `Ratio` | `Ratio::from_basis_points(100_000)` | Techo de precio relativo $10{,}0 \times P_{\text{base}}$ (§ 10, Anexo W, Anexo AI) |
| `eco.stock.grain_weeks` | $26\text{ semanas}$ | `Qty` (multiplicador) | `Qty::from_units(26)` (`26_000` raw) o escalar `26` | $26\text{ semanas}$ de consumo de grano objetivo (§ 10, Anexo AI) |
| `eco.transport.sea` | $0{,}0008\text{ uc} / (\text{ud.}\cdot\text{km})$ | `Money` | `Money::from_raw(8)` | $8 / 10\,000 = 0{,}0008\text{ uc}$ (§ 10, Anexo AI) |
| `eco.transport.river` | $0{,}0032\text{ uc} / (\text{ud.}\cdot\text{km})$ | `Money` | `Money::from_raw(32)` | $32 / 10\,000 = 0{,}0032\text{ uc}$ (§ 10, Anexo AI) |
| `eco.transport.road` | $0{,}0120\text{ uc} / (\text{ud.}\cdot\text{km})$ | `Money` | `Money::from_raw(120)` | $120 / 10\,000 = 0{,}0120\text{ uc}$ (§ 10, Anexo AI) |
| `eco.transport.pack` | $0{,}0200\text{ uc} / (\text{ud.}\cdot\text{km})$ | `Money` | `Money::from_raw(200)` | $200 / 10\,000 = 0{,}0200\text{ uc}$ (§ 10, Anexo AI) |
| `gov.corruption.base` | $1\,000\text{ pb}$ ($0{,}10$) | `Ratio` | `Ratio::from_basis_points(1_000)` | $1\,000\text{ pb} = 0{,}1000 = 10\,\%$ fuga base (§ 11, Anexo AI) |
| `gov.control.convergence` | $500\text{ pb}$ ($0{,}05$ mensual) | `Ratio` | `Ratio::from_basis_points(500)` | $500\text{ pb} = 0{,}0500 = 5\,\%$ mensual (§ 11, Anexo AI) |
| `war.attrition.base` | $200\text{ pb}$ ($2\,\%$ mensual) | `Ratio` | `Ratio::from_basis_points(200)` | $200\text{ pb} = 0{,}0200 = 2\,\%$ (§ 13, Anexo AI) |
| `war.attrition.cap` | $1\,500\text{ pb}$ ($15\,\%$ mensual) | `Ratio` | `Ratio::from_basis_points(1_500)` | $1\,500\text{ pb} = 0{,}1500 = 15\,\%$ (§ 13, Anexo AI) |
| `war.fire.coefficient` | $8\text{ pb}$ ($0{,}0008$ por fase) | `Ratio` | `Ratio::from_basis_points(8)` | $8 / 10\,000 = 0{,}0008$ (§ 13, Anexo AI) |
| `war.shock.coefficient` | $12\text{ pb}$ ($0{,}0012$ por fase) | `Ratio` | `Ratio::from_basis_points(12)` | $12 / 10\,000 = 0{,}0012$ (§ 13, Anexo AI) |
| `cul.assimilation.base` | $12\text{ pb}$ ($0{,}12\,\%$ mensual) | `Ratio` | `Ratio::from_basis_points(12)` | $12 / 10\,000 = 0{,}0012 = 0{,}12\,\%$ mensual (§ 09, Anexo AI) |
| `rel.conversion.base` | $3\text{ pb}$ ($0{,}03\,\%$ mensual) | `Ratio` | `Ratio::from_basis_points(3)` | $3 / 10\,000 = 0{,}0003 = 0{,}03\,\%$ mensual (§ 09, Anexo AI) |

---

## 5. Invariantes

Los tipos y operaciones de `e101-store::fixed` garantizan los siguientes invariantes formales, verificados en cada tick por los validadores de `e101-sim` (Anexo AC):

1. **Ausencia total de coma flotante (Invariante FP-01):** Ningún campo de `Money`, `Qty`, `Ratio` ni ninguna operación de `e101-store::fixed` instancia ni convierte a `f32` o `f64` (`ADR 0002`, `ADR 0003`). El lint estático de `cargo xtask check` rechaza cualquier aparición de `f32`/`f64` en los crates de simulación.
2. **Conservación exacta en repartos monetarios y físicos (Invariante FP-02, soporta I-01, I-02 e I-04 del Anexo AC):**
   Para todo `total: Money` y todo slice no vacío `weights: &[Ratio]`:
   $$\sum_{i} \text{Money::allocate\_exact}(\text{total}, \text{weights})[i] == \text{total}$$
   Idéntica propiedad se cumple para `Qty::allocate_exact(total, weights)`. Ninguna diezmilésima de `uc` ni milésima de bien o persona se crea ni se destruye por redondeo.
3. **Partición de la unidad en cuotas (Invariante FP-03, soporta I-07 del Anexo AC):**
   Para todo vector de pesos `weights: [i64; N]` con $N > 0$:
   $$\sum_{i=0}^{N-1} \text{Ratio::normalize\_shares}(weights)[i] == \text{Ratio::ONE} \quad (10\,000\text{ pb})$$
4. **Simetría de signo en redondeo *half-to-even* (Invariante FP-04):**
   Para todo `num: i128` y `den > 0`:
   $$\text{div\_round\_half\_to\_even\_i128}(-num, den) == -\text{div\_round\_half\_to\_even\_i128}(num, den)$$
   Esto asegura que cobrar un impuesto de $+X$ a una entidad y abonar $-X$ como gasto produce magnitudes idénticas bit a bit.
5. **Monotonía de escalado (Invariante FP-05):**
   Si $0 \le r_1 \le r_2$ (`Ratio`) y $q \ge 0$ (`Qty` o `Money`), entonces $q.\text{scale}(r_1) \le q.\text{scale}(r_2)$.
6. **Acotación de precios y tasas (Invariante FP-06, soporta I-03 e I-05 del Anexo AC):**
   `clamp(min, max)` con $min \le max$ garantiza siempre $min \le x.\text{clamp}(min, max) \le max$.

---

## 6. Interacción con otros sistemas

| Crate / Sistema | Cómo consume `e101-store::fixed` | Referencia |
| :--- | :--- | :--- |
| **`e101-store`** | Almacena columnas SoA de `Money`, `Qty` y `Ratio` en tablas indexadas por identificadores generacionales (`SettlementId`, `PolityId`, `GoodId`, `PopGroupId`). Define también el acumulador determinista `Deltas`. | § 18, Anexo B, Anexo P |
| **`e101-ledger`** | Registra cada apunte causal (`CauseEntry`) con su delta exacto en `Money`, `Qty` o `Ratio`. Verifica en modo debug que la suma de las contribuciones registradas coincide con el delta neto aplicado al estado. | § 18, § 22, Principio 4 |
| **`e101-commands`** | Los comandos de jugador e IA (`SetTaxRate`, `BuildFacility`, `RaiseLevy`, `CreateTradeRoute`) transportan únicamente `Money`, `Qty` y `Ratio`, impidiendo inyectar valores de coma flotante desde la red o la interfaz. | § 18, Principio 2 |
| **`e101-sim` (Demografía, § 09)** | Usa `Qty` para cohortes ($0\text{–}14$, $15\text{–}49$, $50+$), `tables::annual_to_monthly_rate` para convertir tasas anuales a mensuales (`D-019`), `PiecewiseLinearTable` para `f_vida`, `g_alimentos`, `f_paz` y `h_crianza`, y `Qty::allocate_exact` para distribuir nacimientos y migración sin perder fracciones de persona. | § 09, Anexo AI |
| **`e101-sim` (Economía, § 10)** | Usa `Money::from_qty_price` para facturar compraventas, `Ratio::from_quotient` y operadores de `Ratio` en el ajuste semanal de precios con amortiguación (`Anexo W`), y `Money::allocate_exact` para liquidar ingresos de mercado y tarifas de transporte. | § 10, Anexo W |
| **`e101-sim` (Política y Fiscalidad, § 11)** | Usa `Ratio::normalize_shares` para cuotas de poder de estamentos (`I-07`) y `Money::allocate_exact` para repartir la recaudación fiscal entre el tesoro estatal, la fuga por corrupción a las élites (`7_000 pb`) y la pérdida administrativa. | § 11, Anexo AC |
| **`e101-sim` (Militar, § 12)** | Usa `Qty` para efectivos y suministros, `Ratio` para moral, disciplina y desgaste (`mil.attrition.*`), y `tables::half_life_decay` para tradición militar y agotamiento. | § 12, Anexo AI |
| **`e101-save`** | Serializa `Money`, `Qty` y `Ratio` directamente como enteros `i64`/`i32` en `postcard` y los incorpora al hash de estado `BLAKE3` de cada tick/mes. | § 23, Anexo T |

---

## 7. Registro causal

El módulo `e101-store::fixed` es una biblioteca de primitivas matemáticas puras sin estado mutable propio; por tanto, **no invoca a `e101-ledger` directamente**. Sin embargo, está diseñado específicamente para hacer cumplir el **Principio Innegociable 4 (Registro causal)**:

1. **Trazabilidad sin residuos huérfanos:** Cuando un sistema de `e101-sim` desglosa un cambio agregado en varias causas visibles para el jugador (por ejemplo, el crecimiento demográfico mensual desglosado en *Nacimientos*, *Mortalidad base*, *Hambre* y *Migración*, o un cobro fiscal dividido entre *Tesoro real* y *Corrupción de las élites*), utiliza `Money::allocate_exact` o `Qty::allocate_exact`.
2. **Identidad contable en el Libro Mayor (`e101-ledger`):** Gracias a `allocate_exact`, la suma de los asientos individuales enviados a `ledger.record(entity, variable, cause_id, delta_i)` es **idéntica bit a bit** al cambio total aplicado en `State` durante la fase `apply_deltas`. Nunca aparece una línea fantasma de «ajuste por redondeo» en los *tooltips* del jugador (§ 22, § 26).

---

## 8. Interfaz de usuario

Aunque `e101-store::fixed` no depende de ninguna biblioteca gráfica (Principio 5), define el contrato de presentación que los formateadores de `e101-ui` y `Fluent` (`games/epoch/locale/`) deben seguir al mostrar valores al jugador (§ 26):

| Tipo | Regla de formateo en interfaz (`e101-ui`) | Ejemplo en pantallas generales | Ejemplo en *tooltip* de desglose causal (modo detallado) |
| :--- | :--- | :--- | :--- |
| **`Money`** | Divide `raw()` entre $10\,000$. Muestra 2 decimales por defecto y hasta 4 decimales en tarifas unitarias de transporte o precios pequeños. Añade el símbolo/unidad localizada `uc`. | `142,50 uc` (`Money(1_425_000)`) | `+0,0120 uc / (ud.·km)` (`Money(120)`, coste por calzada) |
| **`Qty` (Población)** | En resúmenes demográficos se redondea al entero más cercano (`div_round_half_to_even_i128(q.0, 1_000)`); en flujos mensuales pequeños se muestra con 1 o 3 decimales. | `12 450 hab.` (`Qty(12_450_000)`) | `+14,250 hab./mes` (`Qty(14_250)`) |
| **`Qty` (Bienes)** | Muestra 1 o 2 decimales de unidad física (`ud.`). | `320,5 ud. de grano` (`Qty(320_500)`) | `-12,375 ud./sem.` (`Qty(-12_375)`) |
| **`Ratio`** | $100\text{ pb} = 1{,}00\,\%$ (o $10\text{ pb} = 1{,}0\,\text{‰}$ en tasas demográficas anuales). | `15,00 %` (`Ratio(1_500)`) | `72,7 ‰ anual` (`Ratio(727)`) / `0,12 % mensual` (`Ratio(12)`) |

---

## 9. Pruebas y escenarios

Las pruebas de `e101-store::fixed` se ejecutan mediante `cargo xtask test e101-store` y forman parte obligatoria de `cargo xtask check` (Anexo T):

### 9.1. Pruebas unitarias deterministas
1. **Vectores canónicos de redondeo *half-to-even*:** verificación explícita de `div_round_half_to_even_i128` para $+2{,}5 \to +2$, $+3{,}5 \to +4$, $-2{,}5 \to -2$, $-3{,}5 \to -4$, valores nulos, divisores impares y valores extremos cercanos a `i64::MAX` / `i64::MIN`.
2. **Fórmula de ajuste de precios del Anexo W:** reproducción exacta del test `dampens_and_clamps_extreme_shortage` del Anexo W (líneas 8229–8242), comprobando que con `base = 10 uc`, `current = 10 uc`, `net_demand = 500 ud.` y `target_inventory = 100 ud.`, el nuevo precio es exactamente `Money::from_raw(110_000)` ($11{,}0000\text{ uc}$, límite del $+10\,\%$ semanal).
3. **Verificación de parámetros del Anexo AI:** prueba unitaria que instancia cada constante de la Sección 4 (`Money::from_raw(8)`, `Money::from_raw(32)`, `Money::from_raw(120)`, `Money::from_raw(200)`, `Ratio::from_basis_points(727)`, etc.) y comprueba sus conversiones inversas y operaciones de escala.
4. **Tablas no lineales (`e101-store::fixed::tables`):**
   - Comprobación de que `annual_to_monthly_rate(Ratio::ZERO) == Ratio::ZERO` y `annual_to_monthly_rate(Ratio::ONE) == Ratio::ONE`.
   - Comprobación de que aplicar $(1 - r_{\text{mes}})^{12}$ a partir de `annual_to_monthly_rate(Ratio::from_basis_points(727))` reproduce $1 - 0{,}0727$ dentro de $\le 1\text{ pb}$.
   - Comprobación de que `half_life_decay(10_000, t_half, t_half) == 5_000` y `half_life_decay(10_000, 2 * t_half, t_half) == 2_500`.
   - Comprobación de `sqrt_ratio(Ratio::ONE) == Ok(Ratio::ONE)` y `sqrt_ratio(Ratio::from_basis_points(2_500)) == Ok(Ratio::from_basis_points(5_000))` ($\sqrt{0{,}25} = 0{,}50$).

### 9.2. Pruebas de propiedades (`proptest`, Anexo T)
1. **Conservación exacta de `allocate_exact`:** para cualquier `total: i64` en `[-10^12, 10^12]` y cualquier vector de entre $1$ y $32$ pesos `Ratio` en `[0, 100_000]`, la suma de `Money::allocate_exact` es siempre igual a `Money(total)` y la suma de `Qty::allocate_exact` es siempre igual a `Qty(total)`.
2. **Suma constante de `normalize_shares`:** para cualquier array `[i64; N]` ($N \in \{2, 3, 5, 8\}$), la suma de los elementos devueltos por `Ratio::normalize_shares` es exactamente `Ratio::ONE` (`10_000 pb`).
3. **Simetría impar de división y escalado:** para todo `m: Money` y `r: Ratio`, `(-m).scale(r) == -(m.scale(r))` (salvo en `i64::MIN`).
4. **Idempotencia de serialización:** para cualquier `Money`, `Qty` y `Ratio`, `postcard::from_bytes(&postcard::to_allocvec(&v).unwrap()).unwrap() == v`.

### 9.3. Escenarios dorados (`cargo xtask golden`)
- El hash `BLAKE3` de un lote de $100\,000$ operaciones encadenadas de `scale`, `from_qty_price`, `allocate_exact`, `annual_to_monthly_rate` y `PiecewiseLinearTable::eval` debe coincidir bit a bit entre Windows (`x86_64`), Linux (`x86_64`) y macOS (`aarch64`).

---

## 10. Preguntas abiertas

Ninguna para el hito **M0 / M1**. Todas las decisiones fundacionales están cerradas en `ADR 0002`, `ADR 0003`, `D-016` y `D-019`.

Como nota de evolución controlada para hitos posteriores (M3+):
- Si en campañas de más de 400 años con hiperinflación inducida por mods un precio unitario superase $100\times$ su precio base, el límite actual de `Ratio` (`i32::MAX` $\approx 214\,748\times$) sigue ofreciendo un margen más de $2\,000$ veces superior al techo de diseño (`100_000 pb` = $10\times$). Cualquier cambio en el ancho de bits de `Money`, `Qty` o `Ratio` requeriría un nuevo ADR y la etiqueta `api-change` + `golden-change`.
