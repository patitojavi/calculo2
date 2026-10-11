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
=============================================================================
"""

from manim import *

class AnimacionGrupo12(Scene):
    def construct(self):
        # =====================================================================
        # ESCENA 1: PORTADA Y PRESENTACIÓN (Voz 1)
        # =====================================================================
        titulo = Text("Sumas Inferiores y Superiores", font_size=38, color=BLUE)
        subtitulo = Text("Cálculo Intermedio • Grupo 12 • Proyecto Manim", font_size=22, color=GRAY_B)
        portada = VGroup(titulo, subtitulo).arrange(DOWN, buff=0.3)

        self.play(Write(titulo, run_time=1.5), FadeIn(subtitulo))
        self.wait(2)

        caja_pregunta = Rectangle(
            width=10.5, height=1.6, color=YELLOW, fill_opacity=0.1, stroke_width=2
        ).next_to(portada, DOWN, buff=0.6)

        texto_pregunta = Text(
            "Pregunta central:\n¿Cómo podemos encerrar el valor de una región\nentre dos aproximaciones?",
            font_size=24, color=YELLOW, line_spacing=1.2
        ).move_to(caja_pregunta.get_center())

        self.play(Create(caja_pregunta), Write(texto_pregunta, run_time=2))
        self.wait(3.5)

        # Limpieza total de la portada
        self.play(
            FadeOut(portada),
            FadeOut(caja_pregunta),
            FadeOut(texto_pregunta)
        )
        self.wait(0.5)

        # =====================================================================
        # ESCENA 2: EL PROBLEMA DEL ÁREA Y EJEMPLO PROPIO (Voz 1)
        # =====================================================================
        titulo_e2 = Text("1. El Problema del Área y Nuestro Ejemplo", font_size=26, color=BLUE_B).to_edge(UP, buff=0.4)
        self.play(Write(titulo_e2))

        # Ejes coordenados desplazados ligeramente a la derecha para dar espacio a los textos
        ejes = Axes(
            x_range=[0, 2.5, 0.5],
            y_range=[0, 5, 1],
            x_length=6.0,
            y_length=4.2,
            axis_config={"include_ticks": True}
        ).to_edge(DOWN, buff=0.7).shift(RIGHT * 1.8)

        etiqueta_x = Text("x", font_size=20).next_to(ejes.x_axis.get_end(), RIGHT)
        etiqueta_y = Text("y", font_size=20).next_to(ejes.y_axis.get_end(), UP)
        marca_0 = Text("0", font_size=16).next_to(ejes.c2p(0, 0), DL, buff=0.15)
        marca_1 = Text("1", font_size=16).next_to(ejes.c2p(1, 0), DOWN, buff=0.2)
        marca_2 = Text("2", font_size=16).next_to(ejes.c2p(2, 0), DOWN, buff=0.2)
        etiquetas_ejes = VGroup(etiqueta_x, etiqueta_y, marca_0, marca_1, marca_2)

        curva = ejes.plot(lambda x: x**2, x_range=[0, 2], color=BLUE_C, stroke_width=4)
        etiqueta_curva = Text("f(x) = x²", font_size=22, color=BLUE_C).next_to(ejes.c2p(2, 4), UR, buff=0.15)

        # Cuadro informativo lateral izquierdo para la teoría inicial
        info_ejemplo = VGroup(
            Text("Función continua y no negativa:", font_size=18, color=GRAY_A),
            Text("f(x) = x²  en  [0, 2]", font_size=20, color=WHITE, weight=BOLD),
            Text("Área bajo la curva:", font_size=18, color=GRAY_A),
            Text("∫₀² x² dx = 8/3 ≈ 2.67", font_size=20, color=YELLOW, weight=BOLD)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).to_edge(LEFT, buff=0.6).shift(UP * 0.5)

        area_sombreada = ejes.get_area(curva, x_range=[0, 2], color=BLUE_E, opacity=0.35)

        self.play(Create(ejes), FadeIn(etiquetas_ejes))
        self.play(Create(curva), Write(etiqueta_curva))
        self.play(FadeIn(info_ejemplo), FadeIn(area_sombreada))
        self.wait(3.5)

        # Limpiamos el área sombreada y los textos antes de pasar a las sumas
        self.play(
            FadeOut(area_sombreada),
            FadeOut(info_ejemplo),
            FadeOut(titulo_e2)
        )
        self.wait(0.5)

        # =====================================================================
        # ESCENA 3: SUMA INFERIOR L_4 (Voz 2)
        # =====================================================================
        titulo_e3 = Text("2. Partición Regular y Suma Inferior (L₄)", font_size=26, color=GREEN).to_edge(UP, buff=0.4)
        self.play(Write(titulo_e3))

        # Rectángulos inferiores con n = 4 (extremo izquierdo en función creciente)
        rects_inf_4 = ejes.get_riemann_rectangles(
            curva, x_range=[0, 2], dx=0.5,
            input_sample_type="left",
            fill_opacity=0.65, color=GREEN_C, stroke_color=WHITE, stroke_width=1.5
        )

        tarjeta_inf = VGroup(
            Text("Partición:", font_size=18, color=GRAY_A),
            Text("n = 4,  Δx = 0.5", font_size=19, color=WHITE),
            Text("Puntos: {0, 0.5, 1, 1.5, 2}", font_size=16, color=GRAY_B),
            Text("Suma Inferior (L₄):", font_size=18, color=GREEN, weight=BOLD),
            Text("L₄ = ∑ f(xᵢ₋₁) · Δx", font_size=17, color=WHITE),
            Text("L₄ = 1.75", font_size=22, color=GREEN_A, weight=BOLD),
            Text("(Aproximación por DEFECTO)", font_size=15, color=GREEN_B)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).to_edge(LEFT, buff=0.6).shift(UP * 0.3)

        self.play(Create(rects_inf_4, run_time=2), FadeIn(tarjeta_inf))
        self.wait(4)

        # =====================================================================
        # ESCENA 4: SUMA SUPERIOR U_4 Y ENCIERRO (Voz 2)
        # =====================================================================
        self.play(FadeOut(titulo_e3))
        titulo_e4 = Text("3. Suma Superior (U₄) y Encierro del Área", font_size=26, color=RED).to_edge(UP, buff=0.4)
        self.play(Write(titulo_e4))

        # Rectángulos superiores con n = 4 (extremo derecho)
        rects_sup_4 = ejes.get_riemann_rectangles(
            curva, x_range=[0, 2], dx=0.5,
            input_sample_type="right",
            fill_opacity=0.35, color=RED_C, stroke_color=WHITE, stroke_width=1.5
        )

        tarjeta_sup = VGroup(
            Text("Suma Superior (U₄):", font_size=18, color=RED, weight=BOLD),
            Text("U₄ = ∑ f(xᵢ) · Δx", font_size=17, color=WHITE),
            Text("U₄ = 3.75", font_size=22, color=RED_A, weight=BOLD),
            Text("(Aproximación por EXCESO)", font_size=15, color=RED_B),
            Text("El Área queda encerrada:", font_size=17, color=YELLOW, weight=BOLD),
            Text("1.75  ≤  2.67  ≤  3.75", font_size=19, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).to_edge(LEFT, buff=0.6).shift(UP * 0.3)

        # Reemplazamos la tarjeta izquierda limpiamente
        self.play(
            FadeOut(tarjeta_inf),
            FadeIn(tarjeta_sup),
            Create(rects_sup_4, run_time=2)
        )
        self.wait(4)

        # =====================================================================
        # ESCENA 5: PROCESO DE REFINAMIENTO (Voz 3)
        # =====================================================================
        # Limpieza de títulos y tarjetas anteriores
        self.play(
            FadeOut(titulo_e4),
            FadeOut(tarjeta_sup)
        )

        titulo_e5 = Text("4. Proceso de Refinamiento: n → ∞", font_size=26, color=ORANGE).to_edge(UP, buff=0.4)
        self.play(Write(titulo_e5))

        # Refinamiento a n = 16
        rects_inf_16 = ejes.get_riemann_rectangles(
            curva, x_range=[0, 2], dx=2/16,
            input_sample_type="left",
            fill_opacity=0.65, color=GREEN_C, stroke_color=WHITE, stroke_width=0.8
        )
        rects_sup_16 = ejes.get_riemann_rectangles(
            curva, x_range=[0, 2], dx=2/16,
            input_sample_type="right",
            fill_opacity=0.35, color=RED_C, stroke_color=WHITE, stroke_width=0.8
        )

        tarjeta_ref_16 = VGroup(
            Text("Refinando: n = 16 subintervalos", font_size=17, color=ORANGE, weight=BOLD),
            Text("• L₁₆ = 2.42  (Sube)", font_size=17, color=GREEN_A),
            Text("• Área Real = 2.67", font_size=17, color=WHITE),
            Text("• U₁₆ = 2.92  (Baja)", font_size=17, color=RED_A),
            Text("• Diferencia U - L = 0.50", font_size=17, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18).to_edge(LEFT, buff=0.6).shift(UP * 0.3)

        self.play(
            FadeIn(tarjeta_ref_16),
            Transform(rects_inf_4, rects_inf_16),
            Transform(rects_sup_4, rects_sup_16),
            run_time=2.5
        )
        self.wait(3.5)

        # Refinamiento a n = 40 (alta precisión visual)
        rects_inf_40 = ejes.get_riemann_rectangles(
            curva, x_range=[0, 2], dx=2/40,
            input_sample_type="left",
            fill_opacity=0.7, color=GREEN_C, stroke_color=None
        )
        rects_sup_40 = ejes.get_riemann_rectangles(
            curva, x_range=[0, 2], dx=2/40,
            input_sample_type="right",
            fill_opacity=0.35, color=RED_C, stroke_color=None
        )

        tarjeta_ref_40 = VGroup(
            Text("Refinando: n = 40 subintervalos", font_size=17, color=ORANGE, weight=BOLD),
            Text("• L₄₀ = 2.57", font_size=17, color=GREEN_A),
            Text("• Área Real = 2.67", font_size=17, color=WHITE),
            Text("• U₄₀ = 2.77", font_size=17, color=RED_A),
            Text("• Diferencia U - L = 0.20", font_size=17, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18).to_edge(LEFT, buff=0.6).shift(UP * 0.3)

        self.play(
            Transform(tarjeta_ref_16, tarjeta_ref_40),
            Transform(rects_inf_4, rects_inf_40),
            Transform(rects_sup_4, rects_sup_40),
            run_time=2.5
        )
        self.wait(4)

        # =====================================================================
        # ESCENA 6: CONCLUSIÓN Y RESPUESTA CENTRAL (Voz 3)
        # =====================================================================
        # Vaciado completo del escenario gráfico
        self.play(
            FadeOut(rects_inf_4),
            FadeOut(rects_sup_4),
            FadeOut(ejes),
            FadeOut(curva),
            FadeOut(etiqueta_curva),
            FadeOut(etiquetas_ejes),
            FadeOut(tarjeta_ref_16),
            FadeOut(titulo_e5)
        )
        self.wait(0.5)

        titulo_cierre = Text("Conclusión y Respuesta a la Pregunta Central", font_size=28, color=YELLOW).to_edge(UP, buff=0.6)
        self.play(Write(titulo_cierre))

        bloque_conclusion = VGroup(
            Text("1. Encierro riguroso: En toda función continua y no negativa,", font_size=20, color=WHITE),
            Text("   Ln ≤ Área Real ≤ Un para cualquier partición n.", font_size=20, color=GREEN_A),
            Text("2. Control del error: La diferencia entre cotas es:", font_size=20, color=WHITE),
            Text("   Un - Ln = [f(b) - f(a)] · Δx = (4 - 0) · (2/n) = 8/n", font_size=20, color=ORANGE),
            Text("3. Límite de Riemann: Al hacer la partición infinitamente fina (n → ∞):", font_size=20, color=WHITE),
            Text("   lim (Un - Ln) = 0  ⟹  lim Ln = lim Un = ∫₀² x² dx = 8/3", font_size=20, color=BLUE_B)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).shift(DOWN * 0.2)

        for linea in bloque_conclusion:
            self.play(FadeIn(linea, shift=RIGHT * 0.3), run_time=1.2)
            self.wait(1)

        self.wait(4)

        # =====================================================================
        # ESCENA 7: CRÉDITOS Y FUENTES (Cierre)
        # =====================================================================
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
