#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Prototipo económico T-008: simulación cerrada de 5 mercados y 10 bienes.

Implementa el contrato de docs/specs/prototypes/economy/MODEL.md (validación de
la sección 10 del documento maestro). Solo biblioteca estándar de Python 3.12;
matplotlib se importa únicamente dentro de la función de gráficas, de modo que
la simulación funciona sin él.

Unidades (MODEL.md §2):
  * dinero      en m  = milésimas de uc;
  * cantidades  en pb = milésimas de la unidad natural (1 t = 1000 pb);
  * precios     en m por unidad natural (m/u), nunca por pb.
Ningún float en el estado; los floats solo aparecen como variables locales en
la presión de precios y la igualación del comercio (§2, §6, §7).

Determinismo: un generador random.Random(semilla_entera) por mercado y año
(§9); iteración siempre sobre listas/tuplas con orden fijo; sin reloj del
sistema, sin variables de entorno, sin iterar dict/set en la lógica.

Rev. 2 (2026-10-24), sobre la rev. 1 (MODEL.md §16-§17):
  * S32 — ancla de nivel de precios por mercado (maestro §10 «Nivel de precios»
    + Anexo AI eco.price_level.adjust = 1/36 mensual): cada mercado lleva un
    escalar nivel (arranca 1,0); el precio real de transacción es el relativo ×
    nivel; todo lo que usa precios (hogares, comercio, granario, renta,
    métricas, CSV, PNG) usa el precio real. Objetivo:
    nivel_obj = (masa_monetaria × velocidad) / producción_real, con la
    producción real valorada a precios base (referencia fija) y la velocidad
    normalizada para que el objetivo arranque en 1,0; actualización mensual
    1/36, con el reescalado de precios repartido en las 4 semanas del mes y el
    cambio total semanal acotado al ±10 % de eco.price.max_change (concilia el
    ancla con el tope semanal de spec). La masa se acota a ≥ 0 (los fondos
    pueden ser negativos por S18). Hallazgo documentado: el ancla por masa
    polariza la distribución de dinero en un sistema cerrado (niveles
    observados 0,00–12,97) — ver MODEL.md §17.
  * S33 — Tesalónica exportador modesto de grano (340 ed → 8.840 t/año =
    1,15 × su consumo; el excedente retirado se reubica en Caffa +130 y
    Candía +130, el total de grano no cambia: 1.573 ed → 40.898 t/año). Sin
    esto el shock −40 % no mordía (la producción shockeada superaba el consumo
    local) y M3 era inalcanzable.
  * S31 rev. 2 — la cuota de la renta se escala con el nivel del pagador
    respecto al de la capital (carga real constante): sin el escalado, la renta
    reindexada polariza la masa y hunde a los pagadores hasta la cota inferior.
  * Tope del granario S29 rev. 2 = una reserva objetivo por mercado y bien
    (rev. 1 usaba una cosecha anual local: el granario bloqueaba tanto grano
    que el mercado se vaciaba y el precio encadenaba ratchets hasta el techo).
  * Knobs de §15: CAP_SEA_T = 400, CAP_CARRETERA_T = 400 (rev. 1);
    AJUSTE_COSECHA_GRANO_T = 0; MONEY_MONTHS 6/2.
  * Rev. 3 — M2 con dos lecturas impresas (sin tocar la simulación):
    M2a variación intra-anual (la literal del encargo y del Anexo F: cada
    precio semanal dentro de ±25 % de la media de SU año) y M2b nivel (la
    lectura estricta de las rev. 1-2: media anual dentro de ±25 % de 9.000).
    Ver MODEL.md §17 «Lecturas de M2».

Resultado de la validación rev. 2 (cifras completas en el informe de la tarea):
M1/M5/M6 PASS (conservación exacta: 0 violaciones en 12.000 comprobaciones de
dinero y 2.000 identidades anuales de bienes), M7 PASS por primera vez
(0,9564 conectado / 0,9565 shock), determinismo byte a byte, 200 años en
~2,4–4,0 s. M2/M3/M4 siguen FAIL por causas estructurales del diseño
(MODEL.md §17): el nivel de precios no tiene punto fijo estable en un
prototipo de cantidades rígidas — sin granero deriva a la baja, con granario
plaquea por encima del base y el ancla de masa polariza la distribución del
dinero entre mercados — y M3 exige una ventana/objeto de existencias
incompatibles con las 26 semanas del grano (Tesalónica shockeada tarda ~45-54
semanas en vaciar su stock, fuera de la ventana de 20 semanas). Escalar a
Arquitectura: demanda elástica, mercado externo o revisión del objetivo de
existencias del grano.

Notas de interpretación (puntos donde este código fija un matiz que MODEL.md
deja ambiguo; ninguno altera las métricas M1–M7 ni la conservación):
  * §5.3 dice "0,1 pb" de hierro por persona y mes, pero §4.2 exige que esa
    demanda "cuadre con la producción" (4.800 q/año). 0,1 kg/persona/mes son
    2 pb de quintal (1 pb de hierro = 50 g). Se implementa 0,1 kg = 2 pb.
  * §1.3 lista las rutas como pares no orientados, pero §7 necesita ambos
    sentidos (Caffa vende grano a Constantinopla, Bursa importa por
    Constantinopla). Cada ruta se recorre en sus dos sentidos con capacidad
    íntegra por sentido; en la ruta mixta la capacidad semanal es la del tramo
    más estrecho (carretera, 50 t), pues toda la carga pasa por ambos tramos
    (S13), y la piratería se aplica a la fracción marítima de los km (§1.3).
  * S21 excluye los insumos (lana) de la demanda semanal. Literalmente eso
    deja la lana sin demanda semanal y sin descubrimiento de precios. Se
    mantiene la letra en el cierre (consumo trimestral real) pero la lana
    entra en la demanda semanal suavizada (insumo medio mensual / 4, con
    carry como los demás bienes): sin picos, que es el objetivo declarado
    de S21, y con señal de escasez real.
  * §6: existencias_obj es constante y se calcula con la cesta de año normal
    (leña 25 pb); la estacionalidad invernal (40 pb) solo afecta a la demanda
    semanal y a la compra mensual.
  * §4.4: el pago neto del paño descuenta el valor del insumo de lana deseado
    del mes al precio vigente, acotado por debajo a 0, como ordena el texto.
  * §2.2.4 aplicado a la tarifa de almacenaje (S26): valor de la merma sumado
    bien a bien (podrido_g × precio_g // 1000); el pseudocódigo resume la
    merma en un total y eso mezclaría precios de bienes distintos.
  * CSV: el precio semanal registrado es el de cierre de semana (tras
    actualizar precios, §3 y §6).
  * La compra con presupuesto acota el término de dinero a ≥ 0 (defensivo:
    las carteras de hogares pueden ser negativas tras la renta o la tarifa;
    sin la acota, q saldría negativa y crearía bienes).
"""

import argparse
import os
import random

# ===========================================================================
# 1. Constantes del modelo (MODEL.md §14; origen citado en cada bloque)
# ===========================================================================

SCALE = 1000                       # m por uc; pb por unidad natural (§2)

# --- Calendario --------------------------------------------------------------
SEMANAS_POR_ANIO = 48              # 12 meses × 4 semanas (S2)
SEMANAS_POR_MES = 4
MESES_INVERNO_LENA = (12, 1, 2)            # leña ×1,6 (S11; maestro: dic–feb)
MESES_INVERNO_NAVEGACION = (11, 12, 1, 2)  # −50 % capacidad marítima, piratería ×2
MESES_VERANO_METEO = (4, 5, 6, 7, 8, 9)    # meteorológico 1 %; oct–mar 6 % (S15)
MESES_TRIMESTRE_LANA = (3, 6, 9, 12)       # consumo trimestral de insumos (S21)

# --- Bienes (tabla 1.1) ------------------------------------------------------
BIENES = ["grano", "pescado", "sal", "aceite", "vino",
          "lana", "pano", "hierro", "madera", "lena"]
(GRANO, PESCADO, SAL, ACEITE, VINO,
 LANA, PANO, HIERRO, MADERA, LENA) = range(10)
NB = len(BIENES)

PRECIO_BASE = [9000, 25000, 20000, 3000, 2000,
               4000, 6000, 2500, 1500, 1200]         # m/u (tabla 2.1)
PMIN = [p * 2 // 10 for p in PRECIO_BASE]             # 0,2× base (eco.price.min_max)
PMAX = [p * 10 for p in PRECIO_BASE]                  # 10×  base
PESO_MIL = [1000, 1000, 1000, 90, 100,
            50, 30, 50, 1000, 1000]                   # t × 1000 por unidad (tabla 1.1)
PCT_MERMA = [100, 200, 0, 50, 100,
             50, 20, 10, 50, 50]                      # centésimas de % mensual (§2.3)
ES_BIOLOGICO = [True, True, False, True, True,
                True, False, False, False, False]     # §4.5: grano, pescado, aceite, vino, lana

# --- Mercados (tabla 1.2; Anexo AK) -------------------------------------------
NOMBRES = ["Constantinopla", "Tesalónica", "Caffa", "Bursa", "Candía"]
NOMBRES_CSV = ["constantinopla", "tesalonica", "caffa", "bursa", "candia"]
(CON, TES, CAFFA, BURSA, CANDIA) = range(5)
NM = 5
POBLACION = [100000, 40000, 20000, 15000, 25000]
POB_MEDIO = [15000, 6000, 3000, 2250, 3750]           # S1: 15 %
POB_ALTO = [4500, 1800, 900, 675, 1125]               # S1: 4,5 %
POB_ELITE = [500, 200, 100, 75, 125]                  # S1: 0,5 %
GRANO_INICIAL = [10500, 8500, 6500, 9000, 8500]       # Anexo AK, en m/t

# --- Producción: edificios de referencia (tabla 4.2 rev. S33) -----------------
# S33: Tesalónica pasa a exportador modesto de grano (340 ed → 8.840 t/año =
# 1,15 × su consumo de 7.680 t) para que el shock −40 % del Anexo F muerda
# (con 600 ed su producción shockeada seguía superando su consumo). El
# excedente retirado se reubica en Caffa (+130 ed) y Candía (+130 ed),
# conservando el punto fijo global (1.573 ed → 40.898 t/año).
EDIFICIOS = [
    # grano pesc sal  ace vino lana pano hier made lena
    [400,  40,  2, 100,  40, 130, 175, 30, 20, 30],   # Constantinopla
    [340,  20,  0, 120,  60, 240,  72, 20, 40, 70],   # Tesalónica (S33: era 600)
    [390,  91,  7,  21,   8, 190,  33,  0, 20, 32],   # Caffa (S33: era 260)
    [ 90,   5,  0,  40,  25,  80,  36, 30, 60, 60],   # Bursa
    [353,  22,  1, 150, 100,  95,  48,  0, 22, 40],   # Candía (S33: era 223)
]
RENDIMIENTO_PB = [26000, 25000, 120000, 45000, 150000,
                  30000, 50000, 60000, 60000, 300000]   # pb/año por edificio (§4.1)
TOTAL_ED_GRANO = sum(fila[GRANO] for fila in EDIFICIOS)   # 1573 edificios (§4.2)

# --- Calendario de entrega (§4.3): (mes, numerador, denominador) ---------------
ENTREGA_GRANO = [
    [(6, 1, 2), (7, 1, 2)],    # Constantinopla: jun–jul 50/50 (mediterráneo costero)
    [(6, 1, 2), (7, 1, 2)],    # Tesalónica
    [(7, 1, 1)],               # Caffa: julio 100 % (costa del mar Negro)
    [(7, 1, 2), (8, 1, 2)],    # Bursa: jul–ago (meseta anatolia)
    [(6, 1, 2), (7, 1, 2)],    # Candía
]
ENTREGA_ACEITE = [(11, 1, 3), (12, 1, 3), (1, 1, 3)]          # olivar nov–ene
ENTREGA_VINO = [(9, 1, 2), (10, 1, 2)]                        # vid sep–oct
ENTREGA_PESCADO = [(mes, 1, 8) for mes in (4, 5, 6, 7, 8, 9, 10, 11)]  # abr–nov (S9)
ENTREGA_SAL = [(7, 1, 3), (8, 1, 3), (9, 1, 3)]               # salina jul–sep
ENTREGA_LANA = [(5, 1, 1)]                                    # esquila en mayo (S10)
ENTREGA_PANO = [(3, 1, 4), (6, 1, 4), (9, 1, 4), (12, 1, 4)]  # 12.500 pb/taller y trimestre
ENTREGA_CONTINUA = [(mes, 1, 12) for mes in range(1, 13)]     # hierro, madera, leña

# --- Rutas (tabla 1.3; S12) -----------------------------------------------------
# (a, b, km_mar, km_carretera). Costes en décimas de m por t·km (Anexo AI
# eco.transport.*): mar 0,0008 uc/t·km = 8; carretera 0,012 = 120; río 0,0032 = 32;
# animales 0,020 = 200 (definidos por si se añaden rutas).
RUTAS = [
    (CON, TES, 500, 0),
    (CON, CAFFA, 700, 0),
    (CON, CANDIA, 700, 0),
    (TES, CANDIA, 900, 0),
    (CON, BURSA, 200, 100),
]
COSTE_MAR_D = 8
COSTE_RIO_D = 32
COSTE_CARRETERA_D = 120
COSTE_ANIMALES_D = 200
CAP_SEA_T = 400                    # t/semana por ruta marítima (S13; knob de
                                   # calibración §15: las importaciones
                                   # estructurales de Constantinopla ≈ 800 t/sem
                                   # saturaban las 250 t/sem y el orden fijo de
                                   # bienes estrangulaba leña/madera → techos de
                                   # precio que reventaban los presupuestos)
CAP_CARRETERA_T = 400              # t/semana por carretera (S13; knob: la ruta
                                   # mixta Con–Bursa debe llevar el grano que
                                   # Bursa importa (≈105 t/sem) y el excedente de
                                   # leña bursés (≈250 t/sem); con 50 t/sem Bursa
                                   # no importaba grano ni exportaba leña y con
                                   # 250 la leña seguía en déficit)
CAPITAL_RUTA_M = 5000 * SCALE      # 5.000 uc por ruta y semana (S14)
RISK_PIRACY_PCT = 2                # % del valor por tramo marítimo (S15; ×2 nov–feb)
RISK_METEO_VERANO_PCT = 1          # abril–septiembre (S15)
RISK_METEO_INVIERNO_PCT = 6        # octubre–marzo (S15)

# --- Precios (§6, Anexo AI) ------------------------------------------------------
PRICE_K = 0.10                     # eco.price.k
STOCK_WEIGHT = 0.25                # eco.price.stock_weight
PRICE_MAX_DELTA = 1000             # ±10 % semanal en diezmilésimas (eco.price.max_change)
GRAIN_RESERVE_WEEKS = 26           # eco.stock.grain_weeks (grano, S30 lo mantiene)
PRESSURE_MIN_OFFER_PB = 1          # mínimo del denominador de la presión (S17)
TRADE_PARTIAL = 0.20               # eco.trade.partial_adjust

# --- Objetivos de existencias puente (S30; sustituye el valor plano de S3) -----
# semanas = máx(8, mayor hueco entre entregas del calendario §4.3 contando el
# mes de entrega itself, cuyo cierre llega al final del mes). El grano conserva
# las 26 de eco.stock.grain_weeks; hierro/madera/leña (entrega mensual) se
# quedan en las 8 de S3.
RESERVA_SEMANAS = [26, 20, 40, 40, 44, 48, 13, 8, 8, 8]
                   # grano 26; pescado abr–nov→20; sal jul–sep→40; aceite
                   # nov–ene→40; vino sep–oct→44; lana may→48; paño trim→13

# --- Granero público (S29; sección 10 del maestro vía parameters.md TABLA 2) ---
# Compra (consigna) si el precio queda bajo la media móvil de 52 semanas y
# libera si queda por encima, con límite del 10 % semanal del pool que toca
# (compra: existencias comerciales; liberación: stock del granero, sin pasar de
# cubrir el déficit bajo el objetivo). Tamaño máximo: una cosecha anual local.
GRANARIO_VENTANA_MA = 52           # media móvil de referencia (semanas)
GRANARIO_MIN_HISTORIAL = 8         # mín. semanas de historial antes de actuar
GRANARIO_LIM_NUM = 1000            # 10 % semanal, en diezmilésimas
GRANARIO_LIM_DEN = 10000

# --- Dinero (§8) -------------------------------------------------------------------
MONEY_MONTHS_HOGARES = 6           # S24
MONEY_MONTHS_MERCADO = 2           # S24

# --- Nivel de precios por mercado (S32; maestro §10 «Nivel de precios» +
#     Anexo AI eco.price_level.adjust = 1/36 mensual) ----------------------------
# nivel_objetivo = (masa_monetaria × velocidad) / producción_real, con
# producción_real valorada a precios base (referencia fija, evita
# autorreferencia) y velocidad = producción_real / masa inicial, de modo que el
# nivel objetivo arranca exactamente en 1. Actualización mensual 1/36; el nivel
# reescala los precios reales de su mercado (precio = relativo × nivel).
NIVEL_AJUSTE_DEN = 36              # eco.price_level.adjust = 1/36 mensual

# --- Aleatoriedad y escenarios (§9, §10) -----------------------------------------
HARVEST_NOISE = 1000               # ±10 % en diezmilésimas (S27)
SHOCK_FACTOR_NUM = 6000            # sequía: cosecha de grano ×0,6 (§10)
SHOCK_FACTOR_DEN = 10000
YEARS_DEFAULT = 200
SEMILLA_DEFAULT = 20261024         # la tarea fija esta semilla (MODEL.md §14 trae 42)
SHOCK_ANIO_DEFAULT = 100

# --- Criterios de aceptación (Anexo F, §11) --------------------------------------
CRIT_ANNUAL_BAND = 0.25            # M2
CRIT_SHOCK_MIN = 1.40              # M3
CRIT_SHOCK_MAX = 1.90
CRIT_RECOVERY_BAND = 0.15          # M4
CRIT_COBERTURA = 0.95              # M7 (indicador, sin umbral duro)

# --- Knob de calibración (§15): t/año extra de grano repartidos
#     proporcionalmente a los edificios de grano; 0 por defecto.
AJUSTE_COSECHA_GRANO_T = 0

# --- Orden de compra mensual (§5.2 y §5.3): prioridad fija -----------------------
ORDEN_COMPRA = (GRANO, SAL, ACEITE, LENA, PANO, PESCADO, VINO, HIERRO, MADERA)


# ===========================================================================
# 2. Tablas derivadas: cestas, entregas, dinero, renta (todo entero, con asserts)
# ===========================================================================

def cestas_mensuales():
    """Cestas mensuales por mercado en pb (§5.1, §5.3; S1, S4, S6, S7, S11, S28).

    Devuelve (hogar, semanal, lena_invierno):
      * hogar[m][g]      : demanda de compra mensual de los hogares; la lana no
                           se compra (la toman los talleres del stock, §4.4);
      * semanal[m][g]    : demanda deseada del mes para el algoritmo de precios
                           (§6): la de hogar más el insumo medio mensual de
                           lana (ver nota de interpretación sobre S21);
      * lena_invierno[m] : leña de diciembre–febrero (40 pb/persona, S11).
    """
    hogar = []
    semanal = []
    lena_invierno = []
    for m in range(NM):
        pob = POBLACION[m]
        assert pob % 2 == 0                    # sal 0,5 pb: entera por mercado (§1.2)
        grano = pob * 16                       # 16 GE = 16 kg/mes (§5.1; 192 kg/año)
        sal = pob // 2                         # 0,5 kg
        aceite = pob * 8                       # 0,8 l
        lena_n = pob * 25                      # 25 kg
        lena_i = pob * 40                      # ×1,6 en dic–feb (S11)
        pano = (pob * 5 + POB_MEDIO[m] * 10
                + POB_ALTO[m] * 20 + POB_ELITE[m] * 30)   # S4: 0,15 ud de tejido = 5 pb
        pescado = (POB_MEDIO[m] + POB_ALTO[m] + POB_ELITE[m]) * 89 // 10  # S7: 8,9 kg
        vino = POB_MEDIO[m] * 60 + POB_ALTO[m] * 100 + POB_ELITE[m] * 150
        hierro = pob * 2                       # S28: 0,1 kg = 2 pb de quintal
        madera = pob * 4                       # S28: 4 kg = 4 pb
        lana_insumo_mes = EDIFICIOS[m][PANO] * 60000 // 12   # 60 q/año por taller (§4.1)
        h = [grano, pescado, sal, aceite, vino, 0, pano, hierro, madera, lena_n]
        s = list(h)
        s[LANA] = lana_insumo_mes
        hogar.append(h)
        semanal.append(s)
        lena_invierno.append(lena_i)

    # Comprobación de calibración: cestas de la tabla §5.1, en pb.
    tabla_51 = [
        [1600000, 178000, 50000, 800000, 1425000, 2500000, 755000],
        [640000, 71200, 20000, 320000, 570000, 1000000, 302000],
        [320000, 35600, 10000, 160000, 285000, 500000, 151000],
        [240000, 26700, 7500, 120000, 213750, 375000, 113250],
        [400000, 44500, 12500, 200000, 356250, 625000, 188750],
    ]
    for m in range(NM):
        h = hogar[m]
        assert [h[GRANO], h[PESCADO], h[SAL], h[ACEITE], h[VINO], h[LENA], h[PANO]] \
            == tabla_51[m], "la cesta §5.1 no cuadra"
    # Consumo anual del sistema (§4.2), en pb; la leña con sus 3 meses de invierno.
    esperado_anual = {GRANO: 38400000, PESCADO: 4272000, SAL: 1200000,
                      ACEITE: 19200000, VINO: 34200000, PANO: 18120000,
                      HIERRO: 4800000, MADERA: 9600000, LENA: 69000000}
    for g, esperado in esperado_anual.items():
        if g == LENA:
            anual = sum(hogar[m][LENA] * 9 + lena_invierno[m] * 3 for m in range(NM))
        else:
            anual = sum(hogar[m][g] for m in range(NM)) * 12
        assert anual == esperado, f"consumo anual de {BIENES[g]} no cuadra con §4.2"
    insumo_lana_anual = sum(EDIFICIOS[m][PANO] for m in range(NM)) * 60000
    assert insumo_lana_anual == 21840000, "insumo de lana de los talleres no cuadra"
    return hogar, semanal, lena_invierno


def tabla_entregas():
    """entregas[m][g][mes] en pb (§4.3); todas las mensualidades enteras (assert)."""
    ent = [[[0] * 13 for _ in range(NB)] for _ in range(NM)]
    for m in range(NM):
        calendario = [ENTREGA_GRANO[m], ENTREGA_PESCADO, ENTREGA_SAL, ENTREGA_ACEITE,
                      ENTREGA_VINO, ENTREGA_LANA, ENTREGA_PANO, ENTREGA_CONTINUA,
                      ENTREGA_CONTINUA, ENTREGA_CONTINUA]
        for g in range(NB):
            base = EDIFICIOS[m][g] * RENDIMIENTO_PB[g]
            for (mes, num, den) in calendario[g]:
                assert (base * num) % den == 0, "mensualidad no entera en pb (§4.3)"
                ent[m][g][mes] += base * num // den
    # Producción anual del sistema (§4.2), comprobación bien a bien.
    esperado = [1573 * 26000, 178 * 25000, 10 * 120000, 431 * 45000, 233 * 150000,
                735 * 30000, 364 * 50000, 80 * 60000, 162 * 60000, 232 * 300000]
    for g in range(NB):
        anual = sum(EDIFICIOS[m][g] for m in range(NM)) * RENDIMIENTO_PB[g]
        assert anual == esperado[g], f"producción anual de {BIENES[g]} no cuadra con §4.2"
    # Knob de calibración (§15): grano extra repartido proporcionalmente,
    # añadido al primer mes de cosecha de cada mercado.
    if AJUSTE_COSECHA_GRANO_T:
        extra_total = AJUSTE_COSECHA_GRANO_T * SCALE
        for m in range(NM):
            extra = extra_total * EDIFICIOS[m][GRANO] // TOTAL_ED_GRANO
            ent[m][GRANO][ENTREGA_GRANO[m][0][0]] += extra
    return ent


def valor_cesta_money(hogar_m):
    """Valor a precios base de la cesta de consumo §5.1 (§8.1, S24):
    los 7 bienes de consumo; hierro y madera son demanda artesanal de S28 y la
    lana es insumo, ninguno entra en la cesta que dimensiona el dinero."""
    valor = 0
    for g in (GRANO, PESCADO, SAL, ACEITE, VINO, LENA, PANO):
        valor += hogar_m[g] * PRECIO_BASE[g] // 1000   # regla 2.2.1 por bien
    return valor


def calcular_renta(hogar, entregas, precios, nivel=None):
    """S25/S31: T = cesta anual de Constantinopla − producción neta anual,
    valorada con los precios dados (base en la inicialización, corrientes en la
    reindexación anual de S31), con el pago neto del paño de §4.4. La cuota se
    prorratea por población y, en la reindexación (S31 rev. 2), se escala con
    el nivel de precios del pagador respecto al de la capital: la carga real de
    cada pagador es constante, de modo que un pagador cuyo nivel cae no ve
    crecer su carga relativa (sin ese escalado, la renta polariza la masa
    monetaria y hunde a los pagadores hasta la cota inferior)."""
    cesta_anual_con = 0
    for g in (GRANO, PESCADO, SAL, ACEITE, VINO, LENA, PANO):
        cesta_anual_con += hogar[CON][g] * precios[CON][g] // 1000
    cesta_anual_con *= 12
    prod_neta = 0
    for g in range(NB):
        prod_anual = sum(entregas[CON][g][1:])
        valor = prod_anual * precios[CON][g] // 1000
        if g == PANO:
            insumo = EDIFICIOS[CON][PANO] * 60000
            valor = max(0, valor - insumo * precios[CON][LANA] // 1000)
        prod_neta += valor
    t_anual = max(0, cesta_anual_con - prod_neta)
    pob_resto = sum(POBLACION) - POBLACION[CON]
    nivel_con = 1.0 if nivel is None else max(nivel[CON], 0.05)
    cuotas = [0] * NM
    for m in range(NM):
        if m != CON:
            escalado = 1.0 if nivel is None else nivel[m] / nivel_con
            cuotas[m] = int(t_anual * POBLACION[m] * escalado // (pob_resto * 12))
    return cuotas


def iniciar_estado():
    """Estado inicial (§13, iniciar): listas planas con orden fijo, todo entero."""
    hogar, semanal, lena_invierno = cestas_mensuales()
    entregas = tabla_entregas()

    # Objetivos de existencias (§6 con S30): consumo mensual deseado × semanas
    # puente // 4; constante en toda la ejecución (leña: año normal, 25 pb).
    obj = []
    for m in range(NM):
        fila = []
        for g in range(NB):
            fila.append(semanal[m][g] * RESERVA_SEMANAS[g] // SEMANAS_POR_MES)
        obj.append(fila)
    for m in range(NM):
        for g in range(NB):
            assert obj[m][g] > 0, "existencias_obj nulas romperían §6 y §7.4"

    stock = [[obj[m][g] for g in range(NB)] for m in range(NM)]   # S19: 100 % del objetivo
    precio = [[PRECIO_BASE[g] for g in range(NB)] for m in range(NM)]
    for m in range(NM):
        precio[m][GRANO] = GRANO_INICIAL[m]                       # Anexo AK

    dinero_hog = []
    dinero_merc = []
    for m in range(NM):
        cesta_valor = valor_cesta_money(hogar[m])                 # §8.1 (S24)
        dinero_hog.append(MONEY_MONTHS_HOGARES * cesta_valor)
        dinero_merc.append(MONEY_MONTHS_MERCADO * cesta_valor)
    masa0 = sum(dinero_hog) + sum(dinero_merc)
    assert masa0 == 8 * 65260000, "masa monetaria inicial no cuadra con §8.1"
    # S32: producción real valorada a precios base (referencia fija) y
    # velocidad tal que el nivel objetivo arranca exactamente en 1,0.
    prod_real_m = [sum(EDIFICIOS[m][g] * RENDIMIENTO_PB[g] * PRECIO_BASE[g]
                       // 1000 for g in range(NB)) for m in range(NM)]
    velocidad_m = [prod_real_m[m] / (dinero_hog[m] + dinero_merc[m])
                   for m in range(NM)]

    renta_mensual = calcular_renta(hogar, entregas, precio)

    # Insumo de lana de los talleres, por mes (S21: trimestres de paño, §4.3).
    insumo_lana_mes = [[0] * 13 for _ in range(NM)]
    for m in range(NM):
        trimestral = EDIFICIOS[m][PANO] * 60000 // 4
        for mes in MESES_TRIMESTRE_LANA:
            insumo_lana_mes[m][mes] = trimestral

    # Rutas dirigidas: dos sentidos por ruta (ver nota de interpretación).
    rutas = []
    for (a, b, km_mar, km_car) in RUTAS:
        km_int = km_mar * COSTE_MAR_D + km_car * COSTE_CARRETERA_D
        km_tot = km_mar + km_car
        pura_mar = km_car == 0
        rutas.append((a, b, km_int, km_mar, km_tot, pura_mar))
        rutas.append((b, a, km_int, km_mar, km_tot, pura_mar))

    return {
        "stock": stock,
        "precio": precio,
        "carry": [[0] * NB for _ in range(NM)],
        "obj": obj,
        "cesta_hogar": hogar,
        "cesta_sem": semanal,
        "lena_normal": [hogar[m][LENA] for m in range(NM)],
        "lena_invierno": lena_invierno,
        "din_hog": dinero_hog,
        "din_merc": dinero_merc,
        "masa0": masa0,
        "renta_mensual": renta_mensual,
        "entregas": entregas,
        "insumo_lana_mes": insumo_lana_mes,
        "exportado_sem": [[0] * NB for _ in range(NM)],
        "importado_sem": [[0] * NB for _ in range(NM)],
        "rutas": rutas,
        # granero público (S29): consignación por mercado y bien, empieza vacío;
        # tamaño máximo: una reserva objetivo (S29 rev. 2 — el tope de cosecha
        # anual permitía al granario bloquear tanto grano que el mercado se
        # vaciaba y el precio encadenaba ratchets alcistas; un tope menor no
        # protegía la cobertura local frente a las exportaciones). Estado de la
        # media móvil por mercado-bien: [buffer circular, índice, nº semanas,
        # suma] para media O(1) de las últimas 52 semanas.
        "granero": [[0] * NB for _ in range(NM)],
        "cap_granero": [[obj[m][g] for g in range(NB)] for m in range(NM)],
        "ma_estado": [[[0] * GRANARIO_VENTANA_MA, 0, 0, 0] for _ in range(NM * NB)],
        # nivel de precios por mercado (S32): empieza en 1,0; ancla el nivel al
        # dinero (Hume) con actualización mensual 1/36; ratio semanal del
        # reescalado (raíz cuarta del ratio mensual, aplicado en paso_precios).
        "nivel": [1.0] * NM,
        "ratio_nivel_sem": [1.0] * NM,
        "prod_real_m": prod_real_m,
        "velocidad_m": velocidad_m,
        # acumuladores anuales para la identidad de bienes (§8.4)
        "prod_anio": [0] * NB,
        "cons_hogar_anio": [0] * NB,
        "cons_insumo_anio": [0] * NB,
        "podrido_anio": [0] * NB,
        "stock_anio_inicio": [sum(stock[m][g] + 0 for m in range(NM)) for g in range(NB)],
        # métricas
        "cob_comprado": [0] * NM,
        "cob_deseado": [0] * NM,
        "pagos_neto_neg": 0,
        "comprobaciones_dinero": 0,
        "identidades_bienes": 0,
    }


# ===========================================================================
# 3. Pasos semanales: comercio (§7) y precios (§6)
# ===========================================================================

def paso_comercio(est, mes):
    """Comercio semanal (§7): rutas en orden fijo (dos sentidos), bienes en
    orden fijo; capacidad compartida entre bienes dentro del sentido."""
    inv_navegacion = mes in MESES_INVERNO_NAVEGACION
    pir_pct = RISK_PIRACY_PCT * 2 if inv_navegacion else RISK_PIRACY_PCT
    met_pct = RISK_METEO_VERANO_PCT if mes in MESES_VERANO_METEO \
        else RISK_METEO_INVIERNO_PCT
    stock = est["stock"]
    precio = est["precio"]
    obj = est["obj"]
    din_hog = est["din_hog"]
    din_merc = est["din_merc"]
    exportado = est["exportado_sem"]
    importado = est["importado_sem"]

    for (a, b, km_int, km_mar, km_tot, pura_mar) in est["rutas"]:
        if pura_mar:
            cap_t = CAP_SEA_T // 2 if inv_navegacion else CAP_SEA_T
        else:
            cap_t = CAP_CARRETERA_T     # ruta mixta: manda el tramo de carretera
        for g in range(NB):
            stock_a = stock[a][g]
            if stock_a <= 0:
                continue
            pa = precio[a][g]
            coste = km_int * PESO_MIL[g] // 10000           # §7.1, m/u, entero
            prima = pa * (met_pct * km_tot + pir_pct * km_mar) // (100 * km_tot)  # §7.2
            margen = precio[b][g] - pa - coste - prima      # §7.3
            if margen <= 0:
                continue
            # §7.4 (S23): linealización del término de existencias; float local.
            denom = 0.025 * (pa / obj[a][g] + precio[b][g] / obj[b][g])
            q_ajuste = int(TRADE_PARTIAL * margen / denom)
            q = min(cap_t * 1000000 // PESO_MIL[g],          # capacidad, en pb
                    CAPITAL_RUTA_M * 1000 // pa,             # capital mercantil
                    q_ajuste,                                # ajuste parcial 20 %
                    stock_a)                                 # regla 2.2.7
            if q <= 0:
                continue
            valor = q * pa // 1000                           # regla 2.2.1
            flete = q * coste // 1000
            prim = q * prima // 1000
            stock[a][g] -= q
            stock[b][g] += q                                 # tránsito instantáneo (S16)
            din_merc[b] -= valor + flete + prim
            din_merc[a] += valor
            din_hog[a] += flete + prim                       # porteadores del origen (§7.6)
            exportado[a][g] += q
            importado[b][g] += q
            cap_t -= q * PESO_MIL[g] // 1000000              # capacidad compartida


def paso_nivel(est):
    """S32: ancla de nivel de precios por mercado (maestro §10 + Anexo AI
    eco.price_level.adjust). Mensual: nivel += (nivel_objetivo − nivel) × 1/36,
    con nivel_objetivo = (masa monetaria del mercado × velocidad) / producción
    real a precios base; masa acotada a ≥ 0 (los fondos pueden ser negativos
    por S18). El reescalado de los precios reales no se aplica de un golpe: se
    reparte en las 4 semanas del mes (raíz cuarta del ratio mensual) y
    paso_precios acota el cambio total de cada semana al ±10 % de
    eco.price.max_change, de modo que el ancla nunca añada un salto semanal
    por encima del tope de spec."""
    for m in range(NM):
        masa = est["din_hog"][m] + est["din_merc"][m]
        if masa < 0:
            masa = 0
        nivel_obj = masa * est["velocidad_m"][m] / est["prod_real_m"][m]
        nivel_viejo = est["nivel"][m]
        nivel_nuevo = nivel_viejo + (nivel_obj - nivel_viejo) / NIVEL_AJUSTE_DEN
        est["nivel"][m] = nivel_nuevo
        if nivel_viejo > 0 and nivel_nuevo > 0:
            est["ratio_nivel_sem"][m] = (nivel_nuevo / nivel_viejo) ** 0.25
        else:
            est["ratio_nivel_sem"][m] = 1.0


def _ma_apuntar(estado, precio):
    """Actualiza el estado de la media móvil [buffer, índice, nº semanas, suma]
    con una observación nueva: media O(1) de las últimas 52 semanas."""
    if estado[2] < GRANARIO_VENTANA_MA:
        estado[3] += precio
        estado[2] += 1
    else:
        estado[3] += precio - estado[0][estado[1]]
    estado[0][estado[1]] = precio
    estado[1] = (estado[1] + 1) % GRANARIO_VENTANA_MA


def paso_granario(est):
    """Granero público (S29, regla del maestro): si el precio queda bajo su
    media móvil de 52 semanas, el mercado consigna en el granero hasta el 10 %
    de sus existencias comerciales de la semana (pre-raza para las estaciones
    de escasez); si queda por encima, libera hasta el 10 % del stock del
    granero, sin pasar de cubrir el déficit bajo el objetivo. Tamaño máximo del
    granero: una cosecha anual local del bien. No mueve dinero: el granero es
    stock propio del mercado (la contraparte de una compra con efectivo sería
    el propio fondo, y una transferencia a hogares convertiría el granero en
    una bomba unidireccional que se apaga cuando el fondo toca 0, justo en los
    mercados exportadores cuyos fondos son estructuralmente negativos, S18).
    Los hogares pagan el precio vigente cuando compran el bien liberado en el
    cierre mensual."""
    stock = est["stock"]
    granero = est["granero"]
    precio = est["precio"]
    obj = est["obj"]
    ma_estado = est["ma_estado"]
    cap_granero = est["cap_granero"]
    for m in range(NM):
        for g in range(NB):
            estado = ma_estado[m * NB + g]
            if estado[2] < GRANARIO_MIN_HISTORIAL:
                continue
            media = estado[3] / estado[2]
            p = precio[m][g]
            if p < media:
                # compra/consigna: hasta el 10 % de las existencias comerciales,
                # sin rebasar el tamaño del granero (una cosecha anual local).
                q = stock[m][g] * GRANARIO_LIM_NUM // GRANARIO_LIM_DEN
                hueco = cap_granero[m][g] - granero[m][g]
                if hueco < q:
                    q = hueco
                if q > 0:
                    stock[m][g] -= q
                    granero[m][g] += q
            elif p > media and granero[m][g] > 0:
                # liberación: hasta el 10 % del stock del granero y solo hasta
                # cubrir el déficit bajo el objetivo de existencias.
                deficit = obj[m][g] - stock[m][g]
                if deficit <= 0:
                    continue
                q = granero[m][g] * GRANARIO_LIM_NUM // GRANARIO_LIM_DEN
                if deficit < q:
                    q = deficit
                granero[m][g] -= q
                stock[m][g] += q


def paso_precios(est, mes):
    """Actualización semanal de precios (§6), versión entera de la regla 2.2.4.
    Al inicio de cada mercado aplica la cuota semanal del reescalado de nivel
    (S32) y acota el cambio total de la semana (presión + reescalado) al ±10 %
    de eco.price.max_change sobre el precio de entrada de la semana."""
    stock = est["stock"]
    precio = est["precio"]
    obj = est["obj"]
    cesta_sem = est["cesta_sem"]
    carry = est["carry"]
    lena_normal = est["lena_normal"]
    lena_invierno = est["lena_invierno"]
    exportado = est["exportado_sem"]
    importado = est["importado_sem"]
    ratio_nivel_sem = est["ratio_nivel_sem"]
    invierno_lena = mes in MESES_INVERNO_LENA

    for m in range(NM):
        precio_m = precio[m]
        stock_m = stock[m]
        obj_m = obj[m]
        cesta_m = cesta_sem[m]
        carry_m = carry[m]
        exp_m = exportado[m]
        imp_m = importado[m]
        ratio_sem = ratio_nivel_sem[m]
        for g in range(NB):
            entrada = precio_m[g]
            if ratio_sem != 1.0:
                precio_m[g] = max(PMIN[g],
                                  min(PMAX[g], round(entrada * ratio_sem)))
            deseado = cesta_m[g]
            if g == LENA:
                deseado = lena_invierno[m] if invierno_lena else lena_normal[m]
            demanda = (deseado + carry_m[g]) // 4 + exp_m[g]     # regla 2.2.5
            carry_m[g] = (deseado + carry_m[g]) % 4
            # produccion_semana vale siempre 0: la entrega es mensual (nota §13).
            ventas_stock = min(max(0, demanda - imp_m[g]), stock_m[g])   # S20
            oferta = imp_m[g] + ventas_stock
            presion = (demanda - oferta) / max(oferta, PRESSURE_MIN_OFFER_PB) \
                + STOCK_WEIGHT * (obj_m[g] - stock_m[g]) / obj_m[g]      # float local
            delta = max(-PRICE_MAX_DELTA,
                        min(PRICE_MAX_DELTA, round(PRICE_K * presion * 10000)))
            nuevo = (precio_m[g] * (10000 + delta)) // 10000     # suelo (§2.2.4)
            # tope total semanal (presión + reescalado de nivel S32) sobre el
            # precio de entrada de la semana, y cotas 0,2× / 10× del base.
            techo = entrada * (10000 + PRICE_MAX_DELTA) // 10000
            suelo = entrada * (10000 - PRICE_MAX_DELTA) // 10000
            nuevo = max(suelo, min(techo, nuevo))
            precio_m[g] = max(PMIN[g], min(PMAX[g], nuevo))
            exp_m[g] = 0
            imp_m[g] = 0


# ===========================================================================
# 4. Cierre mensual (§8.3) y comprobaciones de conservación (§2.4)
# ===========================================================================

def cierre_mes(est, mes, anio, factores, shock, shock_anio):
    """Cierre mensual: producción y pago, insumos, consumo, deterioro, tarifa,
    renta de la capital y comprobación de la masa monetaria."""
    stock = est["stock"]
    precio = est["precio"]
    entregas = est["entregas"]
    din_hog = est["din_hog"]
    din_merc = est["din_merc"]

    # 1) Producción del mes y pago a los hogares (§4.3–§4.5, §9).
    for m in range(NM):
        factor = factores[m]
        for g in range(NB):
            q = entregas[m][g][mes]
            if q == 0:
                continue
            if ES_BIOLOGICO[g]:
                q = q * (10000 + factor) // 10000            # regla 2.2.2
            if shock and m == TES and g == GRANO and anio == shock_anio:
                q = q * SHOCK_FACTOR_NUM // SHOCK_FACTOR_DEN  # sequía fija, sin azar (§10)
            stock[m][g] += q
            est["prod_anio"][g] += q
            pago = q * precio[m][g] // 1000                  # regla 2.2.1
            if g == PANO:
                # Pago neto (§4.4): el taller consume lana del mercado; el valor
                # del insumo del mes se descuenta del pago, acotado por debajo a 0.
                insumo_pb = est["insumo_lana_mes"][m][mes]
                pago_neto = pago - insumo_pb * precio[m][LANA] // 1000
                if pago_neto < 0:
                    est["pagos_neto_neg"] += 1
                    pago_neto = 0
                pago = pago_neto
            din_merc[m] -= pago
            din_hog[m] += pago

    # 2) Insumos: los talleres toman lana del stock, sin dinero (S21).
    for m in range(NM):
        deseado = est["insumo_lana_mes"][m][mes]
        q = min(deseado, stock[m][LANA])
        stock[m][LANA] -= q
        est["cons_insumo_anio"][LANA] += q

    # 3) Consumo de los hogares con presupuesto y prioridad fija (§5.2, §5.3).
    for m in range(NM):
        restante = din_hog[m]
        stock_m = stock[m]
        precio_m = precio[m]
        cesta_m = est["cesta_hogar"][m]
        for g in ORDEN_COMPRA:
            deseado = cesta_m[g]
            if g == LENA and mes in MESES_INVERNO_LENA:
                deseado = est["lena_invierno"][m]
            presupuesto = restante * 1000 // precio_m[g]
            if presupuesto < 0:
                presupuesto = 0     # cartera negativa: no se compra (ver notas)
            q = min(deseado, stock_m[g], presupuesto)
            pago = q * precio_m[g] // 1000                       # regla 2.2.1
            stock_m[g] -= q
            est["cons_hogar_anio"][g] += q
            restante -= pago
            din_merc[m] += pago
            if g == GRANO:
                est["cob_comprado"][m] += q
                est["cob_deseado"][m] += deseado
        din_hog[m] = restante

    # 4) Deterioro en almacén (§2.3) y 5) tarifa de almacenaje (S26).
    #    El granero público (S29) se deteriora igual: sigue siendo grano/bien
    #    almacenado del mercado.
    for m in range(NM):
        valor_merma = 0
        for g in range(NB):
            podrido = stock[m][g] * PCT_MERMA[g] // 10000
            if podrido:
                stock[m][g] -= podrido
                est["podrido_anio"][g] += podrido
                valor_merma += podrido * precio[m][g] // 1000
            podrido_g = est["granero"][m][g] * PCT_MERMA[g] // 10000
            if podrido_g:
                est["granero"][m][g] -= podrido_g
                est["podrido_anio"][g] += podrido_g
                valor_merma += podrido_g * precio[m][g] // 1000
        din_hog[m] -= valor_merma
        din_merc[m] += valor_merma

    # 6) Renta de la capital (S25): transferencia entre carteras de hogares.
    for m in range(NM):
        if m != CON:
            cuota = est["renta_mensual"][m]
            din_hog[m] -= cuota
            din_hog[CON] += cuota

    # 7) Conservación de dinero (§2.4, M5).
    comprobar_dinero(est)


def comprobar_dinero(est):
    total = sum(est["din_hog"]) + sum(est["din_merc"])
    assert total == est["masa0"], \
        f"conservación de dinero rota: {total} != {est['masa0']}"
    est["comprobaciones_dinero"] += 1


def comprobar_bienes(est):
    """Identidad anual por bien (§8.4, M6):
    producido == consumido(hogares + insumos) + podrido + Δ(Σ stocks), tránsito 0.
    El granero público (S29) es stock del mercado: cuenta en el Δ."""
    for g in range(NB):
        stock_final = sum(est["stock"][m][g] + est["granero"][m][g] for m in range(NM))
        delta = stock_final - est["stock_anio_inicio"][g]
        consumido = est["cons_hogar_anio"][g] + est["cons_insumo_anio"][g]
        assert est["prod_anio"][g] == consumido + est["podrido_anio"][g] + delta, (
            f"conservación del bien {BIENES[g]}: "
            f"{est['prod_anio'][g]} != {consumido} + {est['podrido_anio'][g]} + {delta}")
        est["identidades_bienes"] += 1
        est["prod_anio"][g] = 0
        est["cons_hogar_anio"][g] = 0
        est["cons_insumo_anio"][g] = 0
        est["podrido_anio"][g] = 0
        est["stock_anio_inicio"][g] = stock_final


# ===========================================================================
# 5. Bucle principal (§13)
# ===========================================================================

def ejecutar(anios, semilla, shock, shock_anio, sin_comercio):
    est = iniciar_estado()
    precios_grano = [[] for _ in range(NM)]    # serie semanal (para CSV y métricas)
    stock_grano_mes = [[] for _ in range(NM)]  # instantánea mensual, tras el cierre
    dinero_mes = [[] for _ in range(NM)]       # din_hog + din_merc, mensual

    for anio in range(1, anios + 1):
        # S31: la renta de la capital se reindexa al inicio de cada año con los
        # precios corrientes (la misma fórmula de S25), de modo que el circuito
        # monetario no quiebra con derivas del nivel de precios.
        est["renta_mensual"] = calcular_renta(est["cesta_hogar"], est["entregas"],
                                              est["precio"], est["nivel"])
        # Un factor de cosecha por mercado y año, semilla entera (§9).
        factores = []
        for idx in range(NM):
            rnd = random.Random(semilla * 1000000 + anio * 10 + idx)
            factores.append(rnd.randint(-HARVEST_NOISE, HARVEST_NOISE))
        for mes in range(1, 13):
            paso_nivel(est)                # ancla de nivel de precios (S32)
            for sem in range(SEMANAS_POR_MES):
                if not sin_comercio:
                    paso_comercio(est, mes)
                paso_granario(est)             # granero público (S29)
                paso_precios(est, mes)
                # historial para la media móvil del granero (tras el ajuste)
                for m in range(NM):
                    precio_m = est["precio"][m]
                    for g in range(NB):
                        _ma_apuntar(est["ma_estado"][m * NB + g], precio_m[g])
                    precios_grano[m].append(precio_m[GRANO])
                comprobar_dinero(est)          # conservación en cada paso (§2.4)
                if sem == SEMANAS_POR_MES - 1:
                    cierre_mes(est, mes, anio, factores, shock, shock_anio)
                    for m in range(NM):
                        stock_grano_mes[m].append(est["stock"][m][GRANO])
                        dinero_mes[m].append(est["din_hog"][m] + est["din_merc"][m])
        comprobar_bienes(est)                  # identidad anual por bien (§8.4)

    series = {
        "precios_grano": precios_grano,
        "stock_grano_mes": stock_grano_mes,
        "dinero_mes": dinero_mes,
        "total_semanas": anios * SEMANAS_POR_ANIO,
    }
    return est, series


# ===========================================================================
# 6. Métricas M1–M7 (§11)
# ===========================================================================

def calcular_metricas(est, series, anios, shock, shock_anio):
    pg = series["precios_grano"]
    met = {}

    # M1: precio siempre dentro de las cotas [0,2×, 10×] del base.
    todos = [p for m in range(NM) for p in pg[m]]
    met["m1_min"] = min(todos)
    met["m1_max"] = max(todos)
    met["m1"] = PMIN[GRANO] <= met["m1_min"] and met["m1_max"] <= PMAX[GRANO]

    # M2, dos lecturas (MODEL.md §17 «Lecturas de M2»):
    #   m2_intra — lectura literal del encargo y del Anexo F: variación
    #     intra-anual, cada precio semanal dentro de ±25 % de la media de SU
    #     año, en años sin crisis.
    #   m2_nivel — lectura estricta: la media anual de cada mercado dentro de
    #     ±25 % del precio base (9.000 m/t).
    exentos = (shock_anio, shock_anio + 1) if shock else ()
    peor_intra = (0.0, 0, 0)
    peor_nivel = (0.0, 0, 0)
    for anio in range(1, anios + 1):
        if anio in exentos:
            continue
        i0 = (anio - 1) * SEMANAS_POR_ANIO
        for m in range(NM):
            semanas = pg[m][i0:i0 + SEMANAS_POR_ANIO]
            media = sum(semanas) / SEMANAS_POR_ANIO
            for p in semanas:
                d_intra = abs(p - media) / media
                if d_intra > peor_intra[0]:
                    peor_intra = (d_intra, m, anio)
            d_nivel = abs(media - PRECIO_BASE[GRANO]) / PRECIO_BASE[GRANO]
            if d_nivel > peor_nivel[0]:
                peor_nivel = (d_nivel, m, anio)
    met["m2_intra_peor"], met["m2_intra_mercado"], met["m2_intra_anio"] = peor_intra
    met["m2_intra"] = peor_intra[0] <= CRIT_ANNUAL_BAND
    met["m2_nivel_peor"], met["m2_nivel_mercado"], met["m2_nivel_anio"] = peor_nivel
    met["m2_nivel"] = peor_nivel[0] <= CRIT_ANNUAL_BAND

    # M3: pico tras el shock (solo con --shock y si el año del shock se simuló).
    met["m3"] = None
    if shock and anios >= shock_anio:
        base = (shock_anio - 1) * SEMANAS_POR_ANIO
        ref_semanas = pg[TES][base + 16:base + 20]           # 4 semanas previas (mayo)
        referencia = sum(ref_semanas) / len(ref_semanas)
        pico = max(pg[TES][base + 20:base + 40])             # 20 semanas desde el mes 6
        met["m3_ref"] = referencia
        met["m3_pico"] = pico
        met["m3"] = pico / referencia if referencia > 0 else None

    # M4: media móvil de 8 semanas al cierre del año shock_anio + 2.
    met["m4"] = None
    if shock and anios >= shock_anio + 2:
        base = (shock_anio + 1) * SEMANAS_POR_ANIO
        met["m4_media"] = sum(pg[TES][base + 40:base + 48]) / 8
        met["m4"] = met["m4_media"]

    # M5/M6: los asserts garantizan 0 violaciones (el programa aborta si no).
    met["m5"] = est["comprobaciones_dinero"]
    met["m6"] = est["identidades_bienes"]

    # M7: cobertura mensual de grano (agregada por cantidad comprada/deseada).
    total_comprado = sum(est["cob_comprado"])
    total_deseado = sum(est["cob_deseado"])
    met["m7"] = total_comprado / total_deseado if total_deseado else 1.0
    met["m7_por_mercado"] = [est["cob_comprado"][m] / est["cob_deseado"][m]
                             if est["cob_deseado"][m] else 1.0 for m in range(NM)]
    return met


def imprimir_resumen(args, est, series, met):
    precio_base = PRECIO_BASE[GRANO]
    print("== Prototipo económico T-008 — resumen (MODEL.md §11) ==")
    print(f"Escenario: anos={args.anos} semilla={args.semilla} "
          f"shock={'si' if args.shock else 'no'} "
          f"comercio={'no' if args.sin_comercio else 'si'}")
    print(f"Masa monetaria: {est['masa0']} m, comprobada "
          f"{est['comprobaciones_dinero']} veces (cada paso)")
    if est["pagos_neto_neg"]:
        print(f"Pagos netos de paño acotados a 0: {est['pagos_neto_neg']} veces")
    print("")

    estado = "PASS" if met["m1"] else "FAIL"
    print(f"M1  precio del grano en [{PMIN[GRANO]}, {PMAX[GRANO]}] m/t ......... "
          f"{estado}  (min {met['m1_min']}, max {met['m1_max']})")

    estado = "PASS" if met["m2_intra"] else "FAIL"
    print(f"M2a variación intra-anual ≤ ±{CRIT_ANNUAL_BAND:.0%} de la media del año "
          f"...... {estado}  (peor {met['m2_intra_peor'] * 100.0:.1f} % en "
          f"{NOMBRES[met['m2_intra_mercado']]}, año {met['m2_intra_anio']})")

    estado = "PASS" if met["m2_nivel"] else "FAIL"
    print(f"M2b media anual dentro de ±{CRIT_ANNUAL_BAND:.0%} de 9.000 (nivel) ....... "
          f"{estado}  (peor {met['m2_nivel_peor'] * 100.0:.1f} % en "
          f"{NOMBRES[met['m2_nivel_mercado']]}, año {met['m2_nivel_anio']})")

    if args.shock:
        if met["m3"] is None:
            print(f"M3  pico tras el shock .................................. "
                  f"N/A  (el año del shock {args.shock_anio} no se simuló)")
        else:
            ok = CRIT_SHOCK_MIN <= met["m3"] <= CRIT_SHOCK_MAX
            estado = "PASS" if ok else "FAIL"
            print(f"M3  pico/referencia en [{CRIT_SHOCK_MIN}, {CRIT_SHOCK_MAX}] ....... "
                  f"{estado}  (pico {met['m3_pico']:.0f} m/t / "
                  f"referencia {met['m3_ref']:.0f} m/t = {met['m3']:.2f})")
        if met["m4"] is None:
            print(f"M4  vuelta a ±{CRIT_RECOVERY_BAND:.0%} al cierre del año "
                  f"{args.shock_anio + 2} .......... N/A  (no se simuló)")
        else:
            desvio = abs(met["m4_media"] - precio_base) / precio_base
            estado = "PASS" if desvio <= CRIT_RECOVERY_BAND else "FAIL"
            print(f"M4  media 8 sem. cierre año {args.shock_anio + 2} ............... "
                  f"{estado}  ({met['m4_media']:.0f} m/t, desvío {desvio:.1%})")
    else:
        print("M3  pico tras el shock .................................. N/A  (sin --shock)")
        print("M4  vuelta tras dos cosechas ............................ N/A  (sin --shock)")

    print(f"M5  conservación de dinero .............................. PASS  "
          f"(0 violaciones en {met['m5']} comprobaciones)")
    print(f"M6  conservación de bienes (identidad anual) ............ PASS  "
          f"(0 violaciones en {met['m6']} identidades)")

    estado = "PASS" if met["m7"] > CRIT_COBERTURA else "FAIL"
    por_mercado = ", ".join(f"{NOMBRES[m]} {met['m7_por_mercado'][m]:.3f}"
                            for m in range(NM))
    print(f"M7  cobertura media de grano (> {CRIT_COBERTURA}, indicador) ....... "
          f"{estado}  ({met['m7']:.4f}; por mercado: {por_mercado})")


# ===========================================================================
# 7. Salidas: CSV (§10) y gráficas
# ===========================================================================

def escribir_csv(ruta, series):
    """CSV con el precio semanal del grano por mercado (48 × años filas)."""
    pg = series["precios_grano"]
    semanas = series["total_semanas"]
    lineas = ["semana," + ",".join(NOMBRES_CSV)]
    for s in range(semanas):
        lineas.append(f"{s + 1}," + ",".join(str(pg[m][s]) for m in range(NM)))
    with open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lineas) + "\n")


def graficar(dir_salida, series, anios, shock, shock_anio):
    """Cuatro PNG (etiquetas en español, dpi 120). matplotlib solo aquí."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    os.makedirs(dir_salida, exist_ok=True)
    semanas = series["total_semanas"]
    x_anios = [(i + 1) / SEMANAS_POR_ANIO for i in range(semanas)]
    precio_base = PRECIO_BASE[GRANO]

    # (1) Precio del grano por mercado, serie completa, con banda ±25 %.
    fig, ax = plt.subplots(figsize=(11, 5.5))
    for m in range(NM):
        ax.plot(x_anios, series["precios_grano"][m], linewidth=0.7, label=NOMBRES[m])
    ax.axhline(precio_base, color="black", linewidth=1.0, label="Precio base (9000 m/t)")
    ax.axhspan(precio_base * (1 - CRIT_ANNUAL_BAND), precio_base * (1 + CRIT_ANNUAL_BAND),
               color="gray", alpha=0.15, label="Banda ±25 %")
    ax.set_title("Precio semanal del grano por mercado")
    ax.set_xlabel("Año")
    ax.set_ylabel("Precio (m/t)")
    ax.set_xlim(1, anios)
    ax.legend(loc="upper left", fontsize=8, ncol=2)
    fig.tight_layout()
    fig.savefig(os.path.join(dir_salida, "precios_grano.png"), dpi=120)
    plt.close(fig)

    # (2) Zoom de los años alrededor del shock (solo con --shock).
    if shock:
        anio_ini = max(1, shock_anio - 1)
        anio_fin = min(anios, shock_anio + 3)
        i0 = (anio_ini - 1) * SEMANAS_POR_ANIO
        i1 = anio_fin * SEMANAS_POR_ANIO
        fig, ax = plt.subplots(figsize=(11, 5.5))
        for m in range(NM):
            ax.plot(x_anios[i0:i1], series["precios_grano"][m][i0:i1],
                    linewidth=1.8 if m == TES else 0.9, label=NOMBRES[m])
        ax.axhline(precio_base, color="black", linewidth=1.0, label="Precio base")
        ax.set_title(f"Precio del grano alrededor del shock de sequía "
                     f"(años {anio_ini}–{anio_fin}; Tesalónica en grueso)")
        ax.set_xlabel("Año")
        ax.set_ylabel("Precio (m/t)")
        ax.legend(loc="upper left", fontsize=8)
        fig.tight_layout()
        fig.savefig(os.path.join(dir_salida, "zoom_shock.png"), dpi=120)
        plt.close(fig)

    # (3) Existencias de grano por mercado (instantáneas mensuales, en t).
    n_meses = len(series["stock_grano_mes"][0])
    x_meses = [(i + 1) / 12 for i in range(n_meses)]
    fig, ax = plt.subplots(figsize=(11, 5.5))
    for m in range(NM):
        ax.plot(x_meses, [q / 1000 for q in series["stock_grano_mes"][m]],
                linewidth=0.8, label=NOMBRES[m])
    ax.set_title("Existencias de grano por mercado")
    ax.set_xlabel("Año")
    ax.set_ylabel("Existencias (t)")
    ax.set_xlim(1 / 12, anios)
    ax.legend(loc="upper left", fontsize=8, ncol=2)
    fig.tight_layout()
    fig.savefig(os.path.join(dir_salida, "existencias_grano.png"), dpi=120)
    plt.close(fig)

    # (4) Dinero total por mercado (hogares + fondo del mercado, en uc).
    fig, ax = plt.subplots(figsize=(11, 5.5))
    for m in range(NM):
        ax.plot(x_meses, [d / 1000 for d in series["dinero_mes"][m]],
                linewidth=0.8, label=NOMBRES[m])
    ax.set_title("Dinero total por mercado (hogares + fondo del mercado)")
    ax.set_xlabel("Año")
    ax.set_ylabel("Dinero (uc)")
    ax.set_xlim(1 / 12, anios)
    ax.legend(loc="upper left", fontsize=8, ncol=2)
    fig.tight_layout()
    fig.savefig(os.path.join(dir_salida, "dinero_mercados.png"), dpi=120)
    plt.close(fig)


# ===========================================================================
# 8. CLI (§10)
# ===========================================================================

def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Prototipo económico T-008 (MODEL.md): 5 mercados, 10 bienes, "
                    "simulación cerrada y determinista.")
    parser.add_argument("--anos", type=int, default=YEARS_DEFAULT,
                        help=f"años a simular (por defecto {YEARS_DEFAULT})")
    parser.add_argument("--semilla", type=int, default=SEMILLA_DEFAULT,
                        help=f"semilla entera (por defecto {SEMILLA_DEFAULT})")
    parser.add_argument("--shock", action="store_true",
                        help="sequía: cosecha de grano de Tesalónica −40 %% durante 1 año")
    parser.add_argument("--shock-anio", type=int, default=SHOCK_ANIO_DEFAULT,
                        dest="shock_anio",
                        help=f"año del shock (por defecto {SHOCK_ANIO_DEFAULT})")
    parser.add_argument("--csv", default=None, metavar="RUTA",
                        help="escribe un CSV con el precio semanal del grano por mercado")
    parser.add_argument("--plot", default=None, metavar="DIR",
                        help="directorio donde escribir las gráficas PNG (requiere matplotlib)")
    parser.add_argument("--sin-comercio", action="store_true", dest="sin_comercio",
                        help="desactiva el comercio entre mercados (diagnóstico)")
    args = parser.parse_args(argv)
    if args.anos < 1:
        parser.error("--anos debe ser >= 1")
    if args.shock_anio < 1:
        parser.error("--shock-anio debe ser >= 1")

    est, series = ejecutar(args.anos, args.semilla, args.shock,
                           args.shock_anio, args.sin_comercio)
    met = calcular_metricas(est, series, args.anos, args.shock, args.shock_anio)
    if args.csv:
        escribir_csv(args.csv, series)
    if args.plot:
        graficar(args.plot, series, args.anos, args.shock, args.shock_anio)
    imprimir_resumen(args, est, series, met)


if __name__ == "__main__":
    main()
