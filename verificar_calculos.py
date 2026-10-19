"""
Verificación de los cálculos que aparecen en el video (f(x) = x^2 en [0, 2]).

Importa las funciones reales de animacion_grupo12.py y comprueba que los
valores mostrados en pantalla y leídos en la narración sean correctos.

Uso:
    python verificar_calculos.py
"""

# Reutilizamos las mismas funciones que usa la animación, así verificamos
# el código real del video y no una copia que podría diferir.
from animacion_grupo12 import AREA_EXACTA, suma_inferior, suma_superior

# n -> (L_n, U_n) tal como se muestran en la tabla del video (2 decimales)
TABLA_VIDEO = {
    4: (1.75, 3.75),
    8: (2.19, 3.19),
    16: (2.42, 2.92),
    40: (2.57, 2.77),
    100: (2.63, 2.71),
}


def verificar():
    # Aquí se acumulan los mensajes de las comprobaciones que fallen
    errores = []

    def comprobar(condicion, mensaje):
        """Imprime OK/ERR para una comprobación y registra si falló."""
        estado = "OK " if condicion else "ERR"
        print(f"[{estado}] {mensaje}")
        if not condicion:
            errores.append(mensaje)

    # Paso 1: el área exacta usada en el video es ∫ x² dx de 0 a 2 = 8/3.
    # Se compara con una tolerancia mínima porque son números decimales.
    comprobar(abs(AREA_EXACTA - 8 / 3) < 1e-12, "Área exacta = 8/3")

    # Paso 2: para cada n de la tabla, se calculan L_n y U_n con las
    # funciones de la animación y se revisan cuatro propiedades.
    for n, (L_video, U_video) in TABLA_VIDEO.items():
        L, U = suma_inferior(n), suma_superior(n)

        # 2a) El valor redondeado a 2 decimales coincide con el que se
        #     muestra en la tabla del video.
        comprobar(round(L, 2) == L_video, f"L_{n} = {L:.4f} (video: {L_video})")
        comprobar(round(U, 2) == U_video, f"U_{n} = {U:.4f} (video: {U_video})")

        # 2b) Encierro: la suma inferior y la superior dejan el área en medio.
        comprobar(L <= AREA_EXACTA <= U, f"L_{n} <= 8/3 <= U_{n}")

        # 2c) Control del error: para f creciente, U_n - L_n = (f(b) - f(a))·Δx
        #     = (4 - 0)·(2/n) = 8/n, la fórmula que aparece en el video.
        comprobar(abs((U - L) - 8 / n) < 1e-12, f"U_{n} - L_{n} = 8/{n} = {8 / n:.4f}")

    # Paso 3: propiedades del refinamiento. Se recorren los n en orden
    # creciente y se comparan pares consecutivos (4 vs 8, 8 vs 16, ...).
    ns = sorted(TABLA_VIDEO)

    # Las sumas inferiores suben al aumentar n ("L_n siempre sube").
    comprobar(
        all(suma_inferior(a) < suma_inferior(b) for a, b in zip(ns, ns[1:])),
        "L_n crece al refinar la partición",
    )
    # Las sumas superiores bajan al aumentar n ("U_n siempre baja").
    comprobar(
        all(suma_superior(a) > suma_superior(b) for a, b in zip(ns, ns[1:])),
        "U_n decrece al refinar la partición",
    )
    # Como el error es 8/n, duplicar n (4 -> 8) lo reduce a la mitad:
    # el error de n=8 multiplicado por 2 debe igualar al error de n=4.
    comprobar(
        abs((suma_superior(8) - suma_inferior(8)) * 2 - (suma_superior(4) - suma_inferior(4))) < 1e-12,
        "Al duplicar n el error se reduce a la mitad",
    )

    # Paso 4: resumen final.
    print()
    if errores:
        print(f"{len(errores)} verificación(es) fallaron.")
        raise SystemExit(1)
    print("Todas las verificaciones pasaron.")



if __name__ == "__main__":
    verificar()
