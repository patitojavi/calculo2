"""
=============================================================================
PROYECTO: Evaluación Integrada de Desempeño (EID) - Cálculo Intermedio
GRUPO: 12
TEMA: Sumas inferiores y superiores (Aproximación y refinamiento)
PREGUNTA CENTRAL: ¿Cómo podemos encerrar el valor de una región entre dos aproximaciones?

ESTRUCTURA VISUAL LIMPIA:
- Zona superior (UP): Título de la escena activa (se borra antes del siguiente).
- Zona lateral izquierda (LEFT / UL): Cuadros informativos claros sin superposición.
- Zona central/inferior: Sistema de ejes y rectángulos de aproximación.
- Cada escena limpia totalmente los textos viejos antes de mostrar los nuevos.

SINCRONIZACIÓN CON EL GUION (duración total: 4:30):
- Voz 1 (0:00 - 0:45): Escena 1 (portada) y Escena 2 (problema del área).
- Voz 2 (0:45 - 2:00): Escena 3 (suma inferior) y Escena 4 (suma superior + encierro).
- Voz 3 (2:00 - 4:30): Escena 5 (refinamiento), Escena 6 (conclusión) y Escena 7 (créditos).
Cada escena usa marcas de tiempo ABSOLUTAS (esperar_hasta) para que el video
calce con la narración sin importar cuánto duren las animaciones individuales.
El texto de la narración está en guion_narracion.md.
=============================================================================
"""

from manim import *

# Fuente con buena cobertura de símbolos matemáticos en Windows.
# Si no existe en el sistema, Manim usa una fuente por defecto.
FUENTE = "Segoe UI"

# Datos matemáticos del proyecto: f(x) = x^2 en [0, 2]
A, B = 0, 2
AREA_EXACTA = 8 / 3


def f(x):
    return x ** 2


def suma_inferior(n):
    """Suma inferior L_n (f creciente: mínimo en el extremo izquierdo)."""
    dx = (B - A) / n
    return sum(f(A + i * dx) * dx for i in range(n))


def suma_superior(n):
    """Suma superior U_n (f creciente: máximo en el extremo derecho)."""
    dx = (B - A) / n
    return sum(f(A + i * dx) * dx for i in range(1, n + 1))


def t(texto, size=22, color=WHITE, bold=False):
    """Texto con markup Pango (permite <sub> y <sup> sin necesitar LaTeX)."""
    return MarkupText(
        texto, font=FUENTE, font_size=size, color=color,
        weight=BOLD if bold else NORMAL,
    )


class AnimacionGrupo12(Scene):
    # ------------------------------------------------------------------
    # Utilidades
    # ------------------------------------------------------------------
    def esperar_hasta(self, segundos):
        """Espera hasta el instante absoluto `segundos` del video."""
        restante = segundos - self.time
        if restante > 0.01:
            self.wait(restante)
        elif restante < -0.3:
            print(f"AVISO: la escena va {-restante:.1f} s atrasada respecto a {segundos} s")

    def tarjeta(self, items, buff=0.2):
        """Acomoda `items` en la esquina superior izquierda (sin mostrarlos)."""
        VGroup(*items).arrange(DOWN, aligned_edge=LEFT, buff=buff) \
            .to_corner(UL, buff=0.5).shift(DOWN * 1.0)
        return items

    def mostrar(self, *items, run_time=0.8):
        self.play(*[FadeIn(i, shift=RIGHT * 0.2) for i in items], run_time=run_time)

    def rectangulos(self, ejes, curva, n, tipo, stroke):
        dx = (B - A) / n
        rects = ejes.get_riemann_rectangles(
            curva, x_range=[A, B], dx=dx, input_sample_type=tipo,
            fill_opacity=0.65 if tipo == "left" else 0.35,
            color=GREEN_C if tipo == "left" else RED_C,
            stroke_color=WHITE, stroke_width=stroke,
        )
        if len(rects) != n:
            print(f"AVISO: se esperaban {n} rectángulos y hay {len(rects)}")
        return rects

    def etiquetas_alturas(self, ejes, tipo, color):
        """Altura de cada rectángulo (n = 4) sobre su borde superior."""
        dx = 0.5
        etiquetas = VGroup()
        for i in range(4):
            x_ref = i * dx if tipo == "izq" else (i + 1) * dx
            h = f(x_ref)
            etiquetas.add(
                t(f"{h:g}", 18, color).next_to(ejes.c2p(i * dx + dx / 2, h), UP, buff=0.1)
            )
        return etiquetas

    def marcadores(self, recta, n):
        """Barra [L_n, U_n] sobre la recta numérica con un punto en cada cota."""
        L, U = suma_inferior(n), suma_superior(n)
        barra = Line(recta.n2p(L), recta.n2p(U), color=YELLOW, stroke_width=10).set_z_index(3)
        punto_L = Dot(recta.n2p(L), color=GREEN, radius=0.09).set_z_index(4)
        punto_U = Dot(recta.n2p(U), color=RED, radius=0.09).set_z_index(4)
        return VGroup(barra, punto_L, punto_U)

    # ------------------------------------------------------------------
    # Escena principal
    # ------------------------------------------------------------------
    def construct(self):
        # =====================================================================
        # ESCENA 1: PORTADA Y PRESENTACIÓN (Voz 1)  |  0:00 - 0:20
        # =====================================================================
        titulo = t("Sumas Inferiores y Superiores", 46, BLUE, True)
        subtitulo = t("Cálculo Intermedio  •  Grupo 12  •  Proyecto Manim", 24, GRAY_B)
        portada = VGroup(titulo, subtitulo).arrange(DOWN, buff=0.3).shift(UP * 1.4)

        self.play(Write(titulo), run_time=2)
        self.play(FadeIn(subtitulo), run_time=1)
        self.esperar_hasta(9)

        pregunta = VGroup(
            t("Pregunta central", 22, YELLOW, True),
            t("¿Cómo podemos encerrar el valor de una región\nentre dos aproximaciones?", 30, WHITE),
        ).arrange(DOWN, buff=0.25).next_to(portada, DOWN, buff=0.9)
        caja = SurroundingRectangle(pregunta, color=YELLOW, buff=0.35, corner_radius=0.15)

        self.play(Create(caja), FadeIn(pregunta), run_time=2)
        self.esperar_hasta(19)

        # Limpieza total de la portada
        self.play(FadeOut(portada), FadeOut(caja), FadeOut(pregunta), run_time=1)

        # =====================================================================
        # ESCENA 2: EL PROBLEMA DEL ÁREA Y EJEMPLO PROPIO (Voz 1)  |  0:20 - 0:45
        # =====================================================================
        titulo_e2 = t("1. El Problema del Área y Nuestro Ejemplo", 28, BLUE_B, True).to_edge(UP, buff=0.4)
        self.play(Write(titulo_e2), run_time=1)

        # Ejes desplazados a la derecha para dejar espacio a los cuadros de texto
        ejes = Axes(
            x_range=[0, 2.5, 0.5],
            y_range=[0, 4.5, 1],
            x_length=7.0,
            y_length=4.6,
            axis_config={"include_ticks": True, "include_tip": False},
        ).to_edge(DOWN, buff=1.4).shift(RIGHT * 2.4)
        ejes.set_z_index(1)

        etiquetas_ejes = VGroup(
            t("x", 22).next_to(ejes.c2p(2.5, 0), RIGHT, buff=0.15),
            t("y", 22).next_to(ejes.c2p(0, 4.5), UP, buff=0.15),
        )
        for v in (0, 0.5, 1, 1.5, 2):
            etiquetas_ejes.add(t(f"{v:g}", 16, GRAY_B).next_to(ejes.c2p(v, 0), DOWN, buff=0.15))
        for v in (1, 2, 3, 4):
            etiquetas_ejes.add(t(f"{v:g}", 16, GRAY_B).next_to(ejes.c2p(0, v), LEFT, buff=0.15))

        curva = ejes.plot(f, x_range=[0, 2], color=BLUE_C, stroke_width=5).set_z_index(2)
        etiqueta_curva = t("f(x) = x²", 24, BLUE_C).next_to(ejes.c2p(2, 4), RIGHT, buff=0.2)

        info_ejemplo = VGroup(
            t("Función continua y no negativa", 20, GRAY_A),
            t("f(x) = x²   en   [0, 2]", 26, WHITE, True),
            t("Área bajo la curva", 20, GRAY_A),
            t("∫<sub>0</sub><sup>2</sup> x² dx = 8/3 ≈ 2.67", 26, YELLOW, True),
        )
        self.tarjeta(info_ejemplo, buff=0.25)

        area_sombreada = ejes.get_area(curva, x_range=[0, 2], color=BLUE_E, opacity=0.35)

        self.play(Create(ejes), FadeIn(etiquetas_ejes), run_time=2)
        self.play(Create(curva), Write(etiqueta_curva), run_time=2)
        self.esperar_hasta(28)
        self.play(FadeIn(info_ejemplo), run_time=1.5)
        self.esperar_hasta(34)
        self.play(FadeIn(area_sombreada), run_time=1.5)
        self.esperar_hasta(44)

        # Limpiamos el área sombreada y los textos antes de pasar a las sumas
        self.play(FadeOut(area_sombreada), FadeOut(info_ejemplo), FadeOut(titulo_e2), run_time=1)

        # =====================================================================
        # ESCENA 3: SUMA INFERIOR L_4 (Voz 2)  |  0:45 - 1:20
        # =====================================================================
        titulo_e3 = t("2. Partición Regular y Suma Inferior (L<sub>4</sub>)", 28, GREEN, True).to_edge(UP, buff=0.4)
        self.play(Write(titulo_e3), run_time=1)

        # Partición: puntos sobre el eje y ancho de cada subintervalo
        puntos = VGroup(*[Dot(ejes.c2p(i * 0.5, 0), color=YELLOW, radius=0.07) for i in range(5)])
        puntos.set_z_index(4)
        flecha_dx = DoubleArrow(
            ejes.c2p(0, 0) + DOWN * 0.75, ejes.c2p(0.5, 0) + DOWN * 0.75,
            buff=0, color=YELLOW, stroke_width=3, tip_length=0.12,
        )
        etiqueta_dx = t("Δx = 0.5", 18, YELLOW).next_to(flecha_dx, DOWN, buff=0.05)

        # Tarjeta izquierda (se revela línea por línea)
        c3 = self.tarjeta([
            t("Partición regular", 20, GRAY_A),
            t("n = 4,   Δx = (2 − 0)/4 = 0.5", 22, WHITE),
            t("x<sub>0</sub>=0,  x<sub>1</sub>=0.5,  x<sub>2</sub>=1,  x<sub>3</sub>=1.5,  x<sub>4</sub>=2", 18, GRAY_B),
            t("Suma inferior", 22, GREEN, True),
            t("L<sub>4</sub> = ∑ f(x<sub>i−1</sub>) · Δx", 22, WHITE),
            t("L<sub>4</sub> = 0.5 · (0 + 0.25 + 1 + 2.25)", 22, WHITE),
            t("L<sub>4</sub> = 1.75", 28, GREEN_A, True),
            t("(Aproximación por DEFECTO)", 20, GREEN_B),
        ])

        self.play(FadeIn(puntos), Create(flecha_dx), FadeIn(etiqueta_dx), run_time=2)
        self.mostrar(*c3[:3], run_time=1)
        self.esperar_hasta(52)
        self.mostrar(c3[3], c3[4], run_time=1)

        # Extremo izquierdo de cada subintervalo: mínimo (f es creciente)
        guias = VGroup()
        for i in range(4):
            x = i * 0.5
            guias.add(
                DashedLine(ejes.c2p(x, 0), ejes.i2gp(x, curva), color=GREEN_B, stroke_width=2),
                Dot(ejes.i2gp(x, curva), color=GREEN_B, radius=0.07),
            )
        guias.set_z_index(4)
        self.play(FadeIn(guias), run_time=1.5)
        self.esperar_hasta(60)

        rects_inf = self.rectangulos(ejes, curva, 4, "left", 1.5)
        self.play(Create(rects_inf, lag_ratio=0.3, run_time=3))
        etq_L4 = self.etiquetas_alturas(ejes, "izq", GREEN_A)
        self.play(FadeIn(etq_L4), run_time=1)
        self.esperar_hasta(66)

        self.mostrar(c3[5], run_time=1)
        self.esperar_hasta(71)
        self.mostrar(c3[6], run_time=1)

        # Recta numérica donde se irá "encerrando" el área
        recta = NumberLine(
            x_range=[1.5, 4, 0.5], length=5.0, include_ticks=True, include_numbers=False,
            include_tip=False, tick_size=0.1, color=GRAY_B, stroke_width=3,
        ).move_to([-4.1, -2.9, 0])
        marcas_recta = VGroup(*[
            t(f"{v}", 18, GRAY_B).next_to(recta.n2p(v), DOWN, buff=0.15) for v in (2, 3, 4)
        ])
        marc_L4 = self.marcadores(recta, 4)
        punto_L4 = marc_L4[1]
        texto_L4 = t("1.75", 20, GREEN).next_to(punto_L4, UP, buff=0.15)

        self.play(Create(recta), FadeIn(marcas_recta), run_time=1.5)
        self.play(FadeIn(punto_L4, scale=2), FadeIn(texto_L4), run_time=1)
        self.mostrar(c3[7], run_time=0.8)
        self.esperar_hasta(80)

        # =====================================================================
        # ESCENA 4: SUMA SUPERIOR U_4 Y ENCIERRO (Voz 2)  |  1:20 - 2:00
        # =====================================================================
        titulo_e4 = t("3. Suma Superior (U<sub>4</sub>) y Encierro del Área", 28, RED, True).to_edge(UP, buff=0.4)
        self.play(
            FadeOut(titulo_e3), FadeOut(*c3), FadeOut(etq_L4), FadeOut(guias),
            FadeOut(puntos), FadeOut(flecha_dx), FadeOut(etiqueta_dx),
            run_time=1,
        )
        self.play(Write(titulo_e4), run_time=1)

        c4 = self.tarjeta([
            t("Suma superior", 22, RED, True),
            t("f creciente: máximo en x<sub>i</sub> (extremo derecho)", 18, GRAY_B),
            t("U<sub>4</sub> = ∑ f(x<sub>i</sub>) · Δx", 22, WHITE),
            t("U<sub>4</sub> = 0.5 · (0.25 + 1 + 2.25 + 4)", 22, WHITE),
            t("U<sub>4</sub> = 3.75", 28, RED_A, True),
            t("(Aproximación por EXCESO)", 20, RED_B),
            t("El área queda encerrada:", 22, YELLOW, True),
            t("1.75  ≤  8/3 ≈ 2.67  ≤  3.75", 22, YELLOW),
        ])

        self.esperar_hasta(82)
        rects_sup = self.rectangulos(ejes, curva, 4, "right", 1.5)
        self.play(Create(rects_sup, lag_ratio=0.3, run_time=3))
        etq_U4 = self.etiquetas_alturas(ejes, "der", RED_A)
        self.play(FadeIn(etq_U4), run_time=1)

        self.esperar_hasta(90)
        self.mostrar(c4[0], c4[1], run_time=1)
        self.esperar_hasta(92)
        self.mostrar(c4[2], run_time=1)
        self.esperar_hasta(95)
        self.mostrar(c4[3], run_time=1)
        self.esperar_hasta(98)
        self.mostrar(c4[4], run_time=1)
        self.mostrar(c4[5], run_time=0.8)

        # Cota superior y valor exacto sobre la recta numérica
        punto_U4, barra4 = marc_L4[2], marc_L4[0]
        texto_U4 = t("3.75", 20, RED).next_to(punto_U4, UP, buff=0.15)
        marca_area = Line(
            recta.n2p(AREA_EXACTA) + DOWN * 0.22, recta.n2p(AREA_EXACTA) + UP * 0.22,
            color=WHITE, stroke_width=4,
        ).set_z_index(4)
        texto_area = t("8/3 ≈ 2.67", 20, WHITE).next_to(marca_area, UP, buff=0.12)

        self.esperar_hasta(102)
        self.play(Create(barra4), FadeIn(punto_U4, scale=2), FadeIn(texto_U4), run_time=1.5)
        self.play(Create(marca_area), FadeIn(texto_area), run_time=1)
        self.esperar_hasta(108)
        self.mostrar(c4[6], c4[7], run_time=1)

        # El intervalo todavía es amplio: ¿podemos achicarlo?
        self.esperar_hasta(114)
        self.play(Indicate(barra4, color=YELLOW, scale_factor=1.3), run_time=1.5)
        self.esperar_hasta(120)

        # =====================================================================
        # ESCENA 5: PROCESO DE REFINAMIENTO (Voz 3)  |  2:00 - 3:35
        # =====================================================================
        titulo_e5 = t("4. Proceso de Refinamiento: n → ∞", 28, ORANGE, True).to_edge(UP, buff=0.4)
        self.play(
            FadeOut(titulo_e4), FadeOut(*c4), FadeOut(etq_U4),
            FadeOut(texto_L4), FadeOut(texto_U4),
            run_time=1,
        )
        self.play(Write(titulo_e5), run_time=1)

        # Cambiamos los marcadores sueltos por un grupo único (para poder transformarlo)
        self.remove(barra4, punto_L4, punto_U4)
        marc = self.marcadores(recta, 4)
        self.add(marc)

        # Tabla de valores (n, L_n, U_n, U_n − L_n)
        columnas_x = [-6.2, -4.95, -3.55, -2.15]

        def fila(y, valores, colores, size=20, bold=False):
            return VGroup(*[
                t(v, size, c, bold).move_to([x, y, 0])
                for x, v, c in zip(columnas_x, valores, colores)
            ])

        def fila_n(k, n):
            L, U = suma_inferior(n), suma_superior(n)
            return fila(
                1.8 - 0.4 * k,
                [str(n), f"{L:.2f}", f"{U:.2f}", f"{U - L:.2f}"],
                [WHITE, GREEN_A, RED_A, YELLOW],
            )

        encabezado = fila(
            2.3,
            ["n", "L<sub>n</sub>", "U<sub>n</sub>", "U<sub>n</sub> − L<sub>n</sub>"],
            [GRAY_A, GREEN, RED, YELLOW], size=22, bold=True,
        )
        regla = Line([-6.6, 2.05, 0], [-1.7, 2.05, 0], color=GRAY, stroke_width=1.5)

        fila_inicial = fila_n(0, 4)
        todas_filas = VGroup(fila_inicial)
        self.play(FadeIn(encabezado), Create(regla), FadeIn(fila_inicial), run_time=1.5)

        # Refinamiento: n = 4 -> 8 -> 16 -> 40 -> 100
        rects_L, rects_U = rects_inf, rects_sup

        def refinar(n, k, stroke, rects_L, rects_U, marc):
            nuevos_L = self.rectangulos(ejes, curva, n, "left", stroke)
            nuevos_U = self.rectangulos(ejes, curva, n, "right", stroke)
            nuevo_marc = self.marcadores(recta, n)
            nueva_fila = fila_n(k, n)
            self.play(
                ReplacementTransform(rects_L, nuevos_L),
                ReplacementTransform(rects_U, nuevos_U),
                ReplacementTransform(marc, nuevo_marc),
                FadeIn(nueva_fila),
                run_time=3,
            )
            todas_filas.add(nueva_fila)
            return nuevos_L, nuevos_U, nuevo_marc

        self.esperar_hasta(130)
        rects_L, rects_U, marc = refinar(8, 1, 1.2, rects_L, rects_U, marc)
        self.esperar_hasta(143)
        rects_L, rects_U, marc = refinar(16, 2, 0.8, rects_L, rects_U, marc)
        self.esperar_hasta(156)
        rects_L, rects_U, marc = refinar(40, 3, 0.3, rects_L, rects_U, marc)

        # Observación: las cotas se acercan al área por ambos lados
        self.esperar_hasta(168)
        observacion = t(
            "L<sub>n</sub> siempre sube   •   U<sub>n</sub> siempre baja\n8/3 siempre queda en medio",
            19, WHITE,
        ).move_to([-4.15, -0.55, 0])
        self.play(FadeIn(observacion), run_time=1)

        # Control del error: U_n − L_n = 8/n
        self.esperar_hasta(180)
        formula_error = t(
            "U<sub>n</sub> − L<sub>n</sub> = (f(b) − f(a)) · Δx\n= (4 − 0) · 2/n = 8/n",
            20, ORANGE, True,
        ).move_to([-4.15, -1.5, 0])
        self.play(FadeIn(formula_error), run_time=1)

        self.esperar_hasta(195)
        rects_L, rects_U, marc = refinar(100, 4, 0, rects_L, rects_U, marc)
        self.esperar_hasta(206)
        self.play(Indicate(todas_filas[-1][3], color=YELLOW, scale_factor=1.5), run_time=1.5)
        self.esperar_hasta(214)

        # =====================================================================
        # ESCENA 6: CONCLUSIÓN Y RESPUESTA CENTRAL (Voz 3)  |  3:35 - 4:15
        # =====================================================================
        # Vaciado completo del escenario gráfico
        self.play(
            FadeOut(rects_L), FadeOut(rects_U), FadeOut(marc),
            FadeOut(ejes), FadeOut(curva), FadeOut(etiqueta_curva), FadeOut(etiquetas_ejes),
            FadeOut(recta), FadeOut(marcas_recta), FadeOut(marca_area), FadeOut(texto_area),
            FadeOut(encabezado), FadeOut(regla), FadeOut(todas_filas),
            FadeOut(observacion), FadeOut(formula_error), FadeOut(titulo_e5),
            run_time=1,
        )

        titulo_cierre = t("Conclusión y Respuesta a la Pregunta Central", 30, YELLOW, True).to_edge(UP, buff=0.6)
        self.play(Write(titulo_cierre), run_time=1)

        bloques = VGroup(
            VGroup(
                t("1.  Encierro riguroso", 24, YELLOW, True),
                t("L<sub>n</sub>  ≤  ∫<sub>0</sub><sup>2</sup> x² dx  ≤  U<sub>n</sub>    para toda partición regular", 22, GREEN_A),
            ),
            VGroup(
                t("2.  Control del error", 24, ORANGE, True),
                t("U<sub>n</sub> − L<sub>n</sub> = (f(b) − f(a)) · Δx = (4 − 0) · (2/n) = 8/n", 22, WHITE),
            ),
            VGroup(
                t("3.  Paso al límite", 24, BLUE_B, True),
                t("Si n → ∞,  entonces  8/n → 0  y  L<sub>n</sub>, U<sub>n</sub> → ∫<sub>0</sub><sup>2</sup> x² dx = 8/3", 22, WHITE),
            ),
        )
        for bloque in bloques:
            bloque.arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        bloques.arrange(DOWN, aligned_edge=LEFT, buff=0.45).shift(UP * 0.4)

        respuesta_texto = t(
            "El área queda encerrada entre dos aproximaciones\nque se juntan al refinar la partición.",
            26, WHITE, True,
        )
        caja_respuesta = SurroundingRectangle(respuesta_texto, color=YELLOW, buff=0.3, corner_radius=0.15)
        respuesta = VGroup(caja_respuesta, respuesta_texto).next_to(bloques, DOWN, buff=0.6)

        self.esperar_hasta(217)
        self.play(FadeIn(bloques[0], shift=RIGHT * 0.3), run_time=1.2)
        self.esperar_hasta(229)
        self.play(FadeIn(bloques[1], shift=RIGHT * 0.3), run_time=1.2)
        self.esperar_hasta(240)
        self.play(FadeIn(bloques[2], shift=RIGHT * 0.3), run_time=1.2)
        self.esperar_hasta(251)
        self.play(Create(caja_respuesta), FadeIn(respuesta_texto), run_time=1.5)
        self.esperar_hasta(254)

        # =====================================================================
        # ESCENA 7: CRÉDITOS Y FUENTES (Cierre)  |  4:15 - 4:30
        # =====================================================================
        self.play(FadeOut(titulo_cierre), FadeOut(bloques), FadeOut(respuesta), run_time=1)

        creditos = VGroup(
            t("Cálculo Intermedio  •  Proyecto Manim Community", 26, GRAY_A),
            t("Grupo 12: Sumas Inferiores y Superiores", 24, BLUE, True),
            t("Herramientas: Python 3.13  •  Manim Community v0.22.0", 20, WHITE),
            t("Fuentes: apunte «Introducción a la integral»  y  Stewart, Cálculo de una variable", 18, GRAY_B),
            t("Declaración de uso de IA: ver README.md", 18, GRAY_B),
        ).arrange(DOWN, buff=0.35)

        self.play(FadeIn(creditos), run_time=1)
        self.esperar_hasta(269)
        self.play(FadeOut(creditos), run_time=1)
        print(f"Duración total del video: {self.time:.1f} s")
