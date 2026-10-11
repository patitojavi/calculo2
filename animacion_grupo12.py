"""
=============================================================================
PROYECTO: Evaluación Integrada de Desempeño (EID) - Cálculo Intermedio
GRUPO: 12
TEMA: Sumas inferiores y superiores (Aproximación y refinamiento)
PREGUNTA CENTRAL: ¿Cómo podemos encerrar el valor de una región entre dos aproximaciones?

ESTRUCTURA DEL GUION / ANIMACIÓN (Duración sincronizada con pausas explicativas):
- PARTE 1 (Voz 1): Presentación, problema del área y pregunta central.
- PARTE 2 (Voz 2): Definición de partición, suma inferior (L_n) y suma superior (U_n).
- PARTE 3 (Voz 3): La cota L_n <= Área <= U_n, proceso de refinamiento (n -> infinito)
                   y conclusión matemática formal.
=============================================================================
"""

from manim import *

class AnimacionGrupo12(Scene):
    def construct(self):
        # =====================================================================
        # SECCIÓN 1: INTRODUCCIÓN Y PREGUNTA CENTRAL (Voz Integrante 1)
        # =====================================================================
        # Título principal del proyecto y datos del grupo
        titulo = Text("Sumas Inferiores y Superiores", font_size=38, color=BLUE)
        subtitulo = Text("Cálculo Intermedio • Grupo 12 • Proyecto Manim", font_size=22, color=GRAY_B)
        encabezado_grupo = VGroup(titulo, subtitulo).arrange(DOWN, buff=0.25)

        self.play(Write(titulo, run_time=1.5), FadeIn(subtitulo))
        self.wait(2)

        # Pregunta central asignada
        caja_pregunta = Rectangle(
            width=11, height=1.6, color=YELLOW, fill_opacity=0.1, stroke_width=2
        ).next_to(encabezado_grupo, DOWN, buff=0.6)

        texto_pregunta = Text(
            "Pregunta central:\n¿Cómo podemos encerrar el valor de una región\nentre dos aproximaciones?",
            font_size=24, color=YELLOW, line_spacing=1.2
        ).move_to(caja_pregunta.get_center())

        self.play(Create(caja_pregunta), Write(texto_pregunta, run_time=2))
        self.wait(3.5)

        # Transición hacia el problema geométrico
        self.play(
            FadeOut(encabezado_grupo),
            FadeOut(caja_pregunta),
            FadeOut(texto_pregunta)
        )

        # =====================================================================
        # SECCIÓN 2: PLANTEAMIENTO DEL PROBLEMA Y EJEMPLO PROPIO (Voz Integrante 1)
        # =====================================================================
        titulo_seccion2 = Text("1. El Problema del Área y Nuestro Ejemplo", font_size=26, color=BLUE).to_edge(UP)
        self.play(Write(titulo_seccion2))

        # Configuración de los ejes coordenados
        # Intervalo [0, 2] en el eje X, y valores [0, 4.5] en el eje Y
        ejes = Axes(
            x_range=[0, 2.5, 0.5],
            y_range=[0, 5, 1],
            x_length=6.5,
            y_length=4.2,
            axis_config={"include_ticks": True}
        ).to_edge(DOWN, buff=0.8)

        # Etiquetas manuales de los ejes para total compatibilidad sin dependencias externas
        etiqueta_x = Text("x", font_size=20).next_to(ejes.x_axis.get_end(), RIGHT)
        etiqueta_y = Text("y", font_size=20).next_to(ejes.y_axis.get_end(), UP)
        marca_0 = Text("0", font_size=16).next_to(ejes.c2p(0, 0), DL, buff=0.15)
        marca_1 = Text("1", font_size=16).next_to(ejes.c2p(1, 0), DOWN, buff=0.2)
        marca_2 = Text("2", font_size=16).next_to(ejes.c2p(2, 0), DOWN, buff=0.2)
        etiquetas_ejes = VGroup(etiqueta_x, etiqueta_y, marca_0, marca_1, marca_2)

        # Función seleccionada: f(x) = x^2, no negativa y creciente en [0, 2]
        curva = ejes.plot(lambda x: x**2, x_range=[0, 2], color=BLUE_C, stroke_width=4)
        etiqueta_funcion = Text("f(x) = x²", font_size=24, color=BLUE_C).next_to(ejes.c2p(2, 4), UR, buff=0.15)

        # Sombreado del área bajo la curva que deseamos calcular
        area_sombreada = ejes.get_area(curva, x_range=[0, 2], color=BLUE_E, opacity=0.35)
        texto_area_exacta = Text("Área Exacta = ∫₀² x² dx = 8/3 ≈ 2.67", font_size=20, color=BLUE_B).to_corner(UL)

        self.play(Create(ejes), FadeIn(etiquetas_ejes))
        self.play(Create(curva), Write(etiqueta_funcion))
        self.play(FadeIn(area_sombreada), Write(texto_area_exacta))
        self.wait(3.5)

        # Limpiamos el área sombreada para comenzar con los rectángulos
        self.play(FadeOut(area_sombreada), FadeOut(titulo_seccion2))

        # =====================================================================
        # SECCIÓN 3: PARTICIÓN Y SUMA INFERIOR L_n (Voz Integrante 2)
        # =====================================================================
        titulo_seccion3 = Text("2. Partición Regular y Suma Inferior (L₄)", font_size=26, color=GREEN).to_edge(UP)
        self.play(Write(titulo_seccion3))

        # Detalle de la partición: n = 4 subintervalos, dx = (2 - 0) / 4 = 0.5
        detalle_particion = Text("Partición: n = 4,  Δx = 0.5\nPuntos: {0,  0.5,  1.0,  1.5,  2.0}", font_size=18, color=GRAY_A).next_to(titulo_seccion3, DOWN, buff=0.2)
        self.play(FadeIn(detalle_particion))
        self.wait(2)

        # Como f(x)=x^2 es creciente, el mínimo en cada subintervalo [x_{i-1}, x_i]
        # ocurre en el extremo izquierdo (input_sample_type='left').
        rects_inferiores_4 = ejes.get_riemann_rectangles(
            curva, x_range=[0, 2], dx=0.5,
            input_sample_type="left",
            fill_opacity=0.6, color=GREEN_C, stroke_color=WHITE, stroke_width=1.5
        )

        tarjeta_inferior = VGroup(
            Text("Suma Inferior (L₄):", font_size=20, color=GREEN, weight=BOLD),
            Text("L₄ = [0² + 0.5² + 1² + 1.5²] · 0.5", font_size=17, color=WHITE),
            Text("L₄ = 1.75  (Aproximación por DEFECTO)", font_size=17, color=GREEN_A)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).to_corner(UL)

        self.play(Create(rects_inferiores_4, run_time=2), FadeIn(tarjeta_inferior))
        self.wait(4)

        # =====================================================================
        # SECCIÓN 4: SUMA SUPERIOR U_n Y EL ENCIERRO (Voz Integrante 2)
        # =====================================================================
        self.play(FadeOut(titulo_seccion3), FadeOut(detalle_particion))
        titulo_seccion4 = Text("3. Suma Superior (U₄) y Encierro del Área", font_size=26, color=RED).to_edge(UP)
        self.play(Write(titulo_seccion4))

        # El máximo en cada subintervalo ocurre en el extremo derecho (input_sample_type='right').
        rects_superiores_4 = ejes.get_riemann_rectangles(
            curva, x_range=[0, 2], dx=0.5,
            input_sample_type="right",
            fill_opacity=0.35, color=RED_C, stroke_color=WHITE, stroke_width=1.5
        )

        tarjeta_superior = VGroup(
            Text("Suma Superior (U₄):", font_size=20, color=RED, weight=BOLD),
            Text("U₄ = [0.5² + 1² + 1.5² + 2²] · 0.5", font_size=17, color=WHITE),
            Text("U₄ = 3.75  (Aproximación por EXCESO)", font_size=17, color=RED_A)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).next_to(tarjeta_inferior, DOWN, aligned_edge=LEFT, buff=0.25)

        self.play(Create(rects_superiores_4, run_time=2), FadeIn(tarjeta_superior))
        self.wait(3)

        # Conclusión de la cota doble
        caja_desigualdad = Rectangle(width=7, height=0.9, color=YELLOW, fill_opacity=0.2).to_edge(UP, buff=0.1)
        texto_desigualdad = Text(
            "L₄ ≤ Área Real ≤ U₄   ⟺   1.75 ≤ 2.67 ≤ 3.75",
            font_size=20, color=YELLOW
        ).move_to(caja_desigualdad.get_center())

        self.play(FadeOut(titulo_seccion4), Create(caja_desigualdad), Write(texto_desigualdad))
        self.wait(4)

        # =====================================================================
        # SECCIÓN 5: REFINAMIENTO Y RESPUESTA CENTRAL (Voz Integrante 3)
        # =====================================================================
        self.play(
            FadeOut(tarjeta_inferior),
            FadeOut(tarjeta_superior),
            FadeOut(caja_desigualdad),
            FadeOut(texto_desigualdad)
        )

        titulo_seccion5 = Text("4. Proceso de Refinamiento: n → ∞", font_size=26, color=ORANGE).to_edge(UP)
        self.play(Write(titulo_seccion5))

        # Subimos la partición a n = 16 subintervalos (dx = 2/16 = 0.125)
        rects_inferiores_16 = ejes.get_riemann_rectangles(
            curva, x_range=[0, 2], dx=2/16,
            input_sample_type="left",
            fill_opacity=0.6, color=GREEN_C, stroke_color=WHITE, stroke_width=0.8
        )
        rects_superiores_16 = ejes.get_riemann_rectangles(
            curva, x_range=[0, 2], dx=2/16,
            input_sample_type="right",
            fill_opacity=0.35, color=RED_C, stroke_color=WHITE, stroke_width=0.8
        )

        info_refinamiento = VGroup(
            Text("Refinando con n = 16 subintervalos:", font_size=19, color=WHITE),
            Text("• Suma Inferior:   L₁₆ = 2.42", font_size=18, color=GREEN_A),
            Text("• Área Real:       A   = 2.67", font_size=18, color=BLUE_B),
            Text("• Suma Superior:   U₁₆ = 2.92", font_size=18, color=RED_A),
            Text("• Diferencia U - L = 0.50", font_size=18, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).to_corner(UL)

        self.play(
            FadeIn(info_refinamiento),
            Transform(rects_inferiores_4, rects_inferiores_16),
            Transform(rects_superiores_4, rects_superiores_16),
            run_time=2.5
        )
        self.wait(4)

        # Ahora mostramos n = 40 (casi continuo)
        rects_inferiores_40 = ejes.get_riemann_rectangles(
            curva, x_range=[0, 2], dx=2/40,
            input_sample_type="left",
            fill_opacity=0.65, color=GREEN_C, stroke_color=None
        )
        rects_superiores_40 = ejes.get_riemann_rectangles(
            curva, x_range=[0, 2], dx=2/40,
            input_sample_type="right",
            fill_opacity=0.4, color=RED_C, stroke_color=None
        )

        info_refinamiento_40 = VGroup(
            Text("Refinando con n = 40 subintervalos:", font_size=19, color=WHITE),
            Text("• Suma Inferior:   L₄₀ = 2.57", font_size=18, color=GREEN_A),
            Text("• Área Real:       A   = 2.67", font_size=18, color=BLUE_B),
            Text("• Suma Superior:   U₄₀ = 2.77", font_size=18, color=RED_A),
            Text("• Diferencia U - L = 0.20", font_size=18, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).to_corner(UL)

        self.play(
            Transform(info_refinamiento, info_refinamiento_40),
            Transform(rects_inferiores_4, rects_inferiores_40),
            Transform(rects_superiores_4, rects_superiores_40),
            run_time=2.5
        )
        self.wait(4)

        # =====================================================================
        # SECCIÓN 6: CONCLUSIÓN Y RESPUESTA CENTRAL (Voz Integrante 3)
        # =====================================================================
        self.play(
            FadeOut(rects_inferiores_4),
            FadeOut(rects_superiores_4),
            FadeOut(ejes),
            FadeOut(curva),
            FadeOut(etiqueta_funcion),
            FadeOut(etiquetas_ejes),
            FadeOut(info_refinamiento),
            FadeOut(texto_area_exacta),
            FadeOut(titulo_seccion5)
        )

        titulo_cierre = Text("Conclusión y Respuesta a la Pregunta Central", font_size=28, color=YELLOW).to_edge(UP)
        self.play(Write(titulo_cierre))

        bloque_conclusion = VGroup(
            Text("1. Encierro riguroso: En toda función continua y no negativa,", font_size=20, color=WHITE),
            Text("   Ln ≤ Área Real ≤ Un para cualquier cantidad n de rectángulos.", font_size=20, color=GREEN_A),
            Text("2. Control del error: La diferencia entre las cotas es exactamente:", font_size=20, color=WHITE),
            Text("   Un - Ln = [f(b) - f(a)] · Δx = (4 - 0) · (2/n) = 8/n", font_size=20, color=ORANGE),
            Text("3. Límite de Riemann: Al hacer la partición infinitamente fina (n → ∞),", font_size=20, color=WHITE),
            Text("   lim (Un - Ln) = 0  ⟹  lim Ln = lim Un = ∫₀² x² dx = 8/3", font_size=20, color=BLUE_B)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).shift(DOWN * 0.2)

        for linea in bloque_conclusion:
            self.play(FadeIn(linea, shift=RIGHT * 0.3), run_time=1.2)
            self.wait(1)

        self.wait(4)

        # Créditos finales
        self.play(FadeOut(titulo_cierre), FadeOut(bloque_conclusion))
        creditos = VGroup(
            Text("Cálculo Intermedio • Proyecto Manim Community", font_size=24, color=GRAY_A),
            Text("Grupo 12: Sumas Inferiores y Superiores", font_size=22, color=BLUE),
            Text("Herramientas: Python 3.13, Manim Community v0.22.0, Matplotlib", font_size=18, color=WHITE),
            Text("Fuentes: Apunte 'Introducción a la Integral' & Stewart (Cálculo Multivariable)", font_size=16, color=GRAY_B)
        ).arrange(DOWN, buff=0.3)

        self.play(FadeIn(creditos))
        self.wait(4)
        self.play(FadeOut(creditos))
