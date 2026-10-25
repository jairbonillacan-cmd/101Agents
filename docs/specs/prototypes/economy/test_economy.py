#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pruebas del prototipo económico T-008 (docs/specs/prototypes/economy).

Tres familias (encargo de la tarea T-008), solo biblioteca estándar:

  1. Conservación exacta de dinero y bienes (M5/M6) en escenario cerrado
     (sin_comercio=True) y con comercio, misma semilla. Las funciones
     comprobar_dinero/comprobar_bienes se ejecutan dentro de `ejecutar` y
     abortan con AssertionError si algo no cuadra, así que llegar al final de
     la simulación ya es evidencia; además se re-verifica la masa monetaria
     sobre el estado devuelto y en cada cierre mensual de la serie.
     Nota: met["m5"]/met["m6"] cuentan comprobaciones hechas, no violaciones
     (una violación no se registra: lanza AssertionError).
  2. Límites de precio: ±10 % semanal del grano por mercado (con tolerancia
     por redondeo entero) y cotas absolutas [0,2×, 10×] del precio base por
     bien, en el estado final y en cada semana de la serie del grano.
  3. Determinismo: misma semilla ⇒ series y CSV idénticos; semilla distinta
     ⇒ series distintas.

Ejecución:
    cd docs/specs/prototypes/economy && python -m unittest -v
    python -m unittest discover -s docs/specs/prototypes/economy -v  (raíz del repo)
"""

import contextlib
import io
import sys
import tempfile
import unittest
from pathlib import Path

# Shim: permite lanzar la suite desde esta carpeta o desde la raíz del repo.
_RUTA = Path(__file__).resolve().parent
if str(_RUTA) not in sys.path:
    sys.path.insert(0, str(_RUTA))

from economy import (  # noqa: E402
    BIENES,
    GRANO,
    NB,
    NM,
    NOMBRES_CSV,
    PMAX,
    PMIN,
    PRICE_MAX_DELTA,
    PRECIO_BASE,
    SEMANAS_POR_ANIO,
    SEMILLA_DEFAULT,
    calcular_metricas,
    escribir_csv,
    ejecutar,
    main,
)

SEMILLA = SEMILLA_DEFAULT
TOL_REDONDEO = 0.005   # margen por el redondeo entero de la regla 2.2.4


def _correr(anios, semilla=SEMILLA, shock=False, shock_anio=1, sin_comercio=False):
    """Ejecuta la simulación y devuelve (estado, series)."""
    return ejecutar(anios=anios, semilla=semilla, shock=shock,
                    shock_anio=shock_anio, sin_comercio=sin_comercio)


class TestConservacion(unittest.TestCase):
    """Familia 1: conservación exacta de dinero (M5) y bienes (M6)."""

    ANIOS = 6

    @classmethod
    def setUpClass(cls):
        # Misma semilla para el escenario cerrado y el de comercio.
        cls.est_cerrado, cls.ser_cerrado = _correr(cls.ANIOS, sin_comercio=True)
        cls.est_comercio, cls.ser_comercio = _correr(cls.ANIOS, sin_comercio=False)

    def _assert_masa_monetaria(self, est):
        # (c) masa monetaria total inicial == final, sobre el estado devuelto.
        self.assertEqual(sum(est["din_hog"]) + sum(est["din_merc"]), est["masa0"])

    def _assert_serie_dinero(self, series, est, anios):
        # En cada cierre mensual la suma entre mercados sigue siendo la masa.
        for t in range(anios * 12):
            total = sum(series["dinero_mes"][m][t] for m in range(NM))
            self.assertEqual(total, est["masa0"], f"cierre mensual {t + 1}")

    def _assert_contadores(self, met, anios):
        # (b) 0 violaciones de M5/M6: una violación lanza AssertionError dentro
        # de ejecutar, así que los contadores solo deben confirmar que las
        # comprobaciones se hicieron (≥ 1 por año en ambas familias).
        self.assertGreater(met["m5"], 0, "M5: no se hizo ninguna comprobación de dinero")
        self.assertGreaterEqual(met["m6"], anios,
                                "M6: menos identidades de bienes que años simulados")

    def test_conservacion_dinero_cerrado(self):
        met = calcular_metricas(self.est_cerrado, self.ser_cerrado,
                                self.ANIOS, False, 1)
        self._assert_contadores(met, self.ANIOS)
        self._assert_masa_monetaria(self.est_cerrado)
        self._assert_serie_dinero(self.ser_cerrado, self.est_cerrado, self.ANIOS)

    def test_conservacion_dinero_comercio(self):
        met = calcular_metricas(self.est_comercio, self.ser_comercio,
                                self.ANIOS, False, 1)
        self._assert_contadores(met, self.ANIOS)
        self._assert_masa_monetaria(self.est_comercio)
        self._assert_serie_dinero(self.ser_comercio, self.est_comercio, self.ANIOS)

    def test_conservacion_bienes_cerrado(self):
        met = calcular_metricas(self.est_cerrado, self.ser_cerrado,
                                self.ANIOS, False, 1)
        self._assert_contadores(met, self.ANIOS)

    def test_conservacion_bienes_comercio(self):
        met = calcular_metricas(self.est_comercio, self.ser_comercio,
                                self.ANIOS, False, 1)
        self._assert_contadores(met, self.ANIOS)


class TestLimitesPrecio(unittest.TestCase):
    """Familia 2: límite semanal ±10 % y cotas absolutas por bien."""

    ANIOS = 6

    @classmethod
    def setUpClass(cls):
        cls.est, cls.series = _correr(cls.ANIOS, sin_comercio=False)

    def test_limites_semanales_precio(self):
        lim = PRICE_MAX_DELTA / 10000.0            # ±10 % semanal (eco.price.max_change)
        lower = (1.0 - lim) * (1.0 - TOL_REDONDEO)
        upper = (1.0 + lim) * (1.0 + TOL_REDONDEO)
        for m in range(NM):
            pg = self.series["precios_grano"][m]
            self.assertEqual(len(pg), self.ANIOS * SEMANAS_POR_ANIO,
                             f"serie incompleta en mercado {m}")
            for s, (a, b) in enumerate(zip(pg, pg[1:]), start=2):
                ratio = b / a
                self.assertGreaterEqual(
                    ratio, lower, f"mercado {m}, semana {s}: caída {a}->{b} > 10 %")
                self.assertLessEqual(
                    ratio, upper, f"mercado {m}, semana {s}: subida {a}->{b} > 10 %")

    def test_cotas_absolutas_precios(self):
        # Las cotas importadas derivan del precio base por bien.
        for g in range(NB):
            self.assertLessEqual(PMIN[g], PRECIO_BASE[g])
            self.assertLessEqual(PRECIO_BASE[g], PMAX[g])
        # Estado final: todos los bienes en todos los mercados.
        for m in range(NM):
            for g in range(NB):
                p = self.est["precio"][m][g]
                self.assertGreaterEqual(
                    p, PMIN[g], f"{BIENES[g]} en mercado {m}: {p} < 0,2×base")
                self.assertLessEqual(
                    p, PMAX[g], f"{BIENES[g]} en mercado {m}: {p} > 10×base")
        # Serie semanal del grano: cada precio registrado dentro de cotas.
        for m in range(NM):
            for s, p in enumerate(self.series["precios_grano"][m], start=1):
                self.assertGreaterEqual(
                    p, PMIN[GRANO], f"mercado {m}, semana {s}: {p} < 0,2×base")
                self.assertLessEqual(
                    p, PMAX[GRANO], f"mercado {m}, semana {s}: {p} > 10×base")


class TestDeterminismo(unittest.TestCase):
    """Familia 3: misma semilla ⇒ resultado idéntico; distinta ⇒ cambia."""

    ANIOS = 3

    def test_determinismo_misma_semilla(self):
        e1, s1 = _correr(self.ANIOS)
        e2, s2 = _correr(self.ANIOS)
        self.assertEqual(s1, s2)
        self.assertEqual(e1["precio"], e2["precio"])
        self.assertEqual(e1["din_hog"], e2["din_hog"])
        self.assertEqual(e1["din_merc"], e2["din_merc"])
        # Redundancia: los CSV de ambas ejecuciones deben ser idénticos byte a byte.
        with tempfile.TemporaryDirectory() as tmp:
            r1 = Path(tmp) / "run1.csv"
            r2 = Path(tmp) / "run2.csv"
            escribir_csv(r1, s1)
            escribir_csv(r2, s2)
            self.assertEqual(r1.read_bytes(), r2.read_bytes())

    def test_no_determinismo_distinta_semilla(self):
        _, s1 = _correr(self.ANIOS, semilla=SEMILLA)
        _, s2 = _correr(self.ANIOS, semilla=SEMILLA + 1)
        self.assertNotEqual(s1, s2)


class TestEscenarios(unittest.TestCase):
    """El shock debe ejecutarse y dejar huella; el CLI debe escribir el CSV."""

    def test_shock_ejecuta(self):
        anios, shock_anio = 5, 3
        est, series = _correr(anios, shock=True, shock_anio=shock_anio)
        met = calcular_metricas(est, series, anios, True, shock_anio)
        self.assertIsNotNone(met["m3"], "el año del shock no quedó registrado en M3")
        self.assertGreater(met["m3_ref"], 0)
        self.assertGreater(met["m3_pico"], 0)
        # La sequía debe dejar huella frente a la misma ejecución sin shock.
        _, s_sin = _correr(anios, shock=False, shock_anio=shock_anio)
        self.assertNotEqual(series["precios_grano"], s_sin["precios_grano"])
        # Y la conservación de dinero sigue cuadrando con el shock activo.
        self.assertEqual(sum(est["din_hog"]) + sum(est["din_merc"]), est["masa0"])

    def test_main_cli_csv(self):
        with tempfile.TemporaryDirectory() as tmp:
            ruta = Path(tmp) / "cli.csv"
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                main(["--anos", "2", "--semilla", str(SEMILLA), "--csv", str(ruta)])
            lineas = ruta.read_text(encoding="utf-8").splitlines()
            self.assertEqual(lineas[0], "semana," + ",".join(NOMBRES_CSV))
            self.assertEqual(len(lineas), 1 + 2 * SEMANAS_POR_ANIO)


if __name__ == "__main__":
    unittest.main()
