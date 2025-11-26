# DeltaTresCasosEq2Grau.py
# manim -pqh --fps 60 -r 1296,2160 DeltaTresCasosEq2Grau.py DeltaTresCasosEq2Grau

from manim import *

class DeltaTresCasosEq2Grau(Scene):
    def construct(self):
        self.camera.background_color = "#0d1117"

        # ==================== TÍTULO ====================
        titulo = Text("Os casos da função de 2º grau\nde acordo com o discriminante Δ",
                      color=GOLD, font_size=52, line_spacing=0.8)
        titulo.to_edge(UP, buff=0.35)
        self.play(Write(titulo), run_time=1.8)
        self.wait(1)
        # Título some subindo (o mais usado nos meus vídeos)
        self.play(FadeOut(titulo, shift=UP*3, run_time=1.0))

        # ==================== TAMANHOS PERFEITOS PARA 3:5 ====================
        larg = 3.7
        alt  = 4.8

        # ==================== CASO 1: Δ > 0 ====================
        ax1 = Axes(
            x_range=[-1, 7, 1], y_range=[-5, 10, 2],
            x_length=larg, y_length=alt,
            tips=False,
            axis_config={"color": WHITE, "stroke_opacity": 0.6},
            y_axis_config={"include_ticks": True}
        ).add_coordinates()

        parabola1 = ax1.plot(lambda x: x**2 - 5*x + 6, color=BLUE_E, stroke_width=6)
        raiz1 = Dot(ax1.c2p(2, 0), color=GREEN, radius=0.1)
        raiz2 = Dot(ax1.c2p(3, 0), color=GREEN, radius=0.1)
        l1 = MathTex("2", color=GREEN, font_size=42).next_to(raiz1, DOWN, buff=0.15)
        l2 = MathTex("3", color=GREEN, font_size=42).next_to(raiz2, DOWN, buff=0.15)

        texto1 = VGroup(
            MathTex(r"x^2-5x+6=0", font_size=44),
            MathTex(r"\Delta=1>0", color=GREEN, font_size=52),
            Text("2 raízes reais", color=GREEN, font_size=34)
        ).arrange(DOWN, buff=0.18).next_to(ax1, DOWN, buff=0.3)

        caso1 = VGroup(ax1, parabola1, raiz1, raiz2, l1, l2, texto1)

        # ==================== CASO 2: Δ = 0 ====================
        ax2 = Axes(
            x_range=[-7, 3, 1], y_range=[-1, 10, 2],
            x_length=larg, y_length=alt,
            tips=False,
            axis_config={"color": WHITE, "stroke_opacity": 0.6}
        ).add_coordinates()

        parabola2 = ax2.plot(lambda x: x**2 + 4*x + 4, color=BLUE_E, stroke_width=6)
        vertice = Dot(ax2.c2p(-2, 0), color=YELLOW, radius=0.12)
        lv = MathTex("-2", color=YELLOW, font_size=44).next_to(vertice, DOWN, buff=0.15)

        texto2 = VGroup(
            MathTex(r"x^2+4x+4=0", font_size=44),
            MathTex(r"\Delta=0", color=YELLOW, font_size=52),
            Text("Raiz dupla", color=YELLOW, font_size=34)
        ).arrange(DOWN, buff=0.18).next_to(ax2, DOWN, buff=0.3)

        caso2 = VGroup(ax2, parabola2, vertice, lv, texto2)

        # ==================== CASO 3: Δ < 0 – PLANO COMPLEXO 3D CORRETO ====================
        axes3d = ThreeDAxes(
            x_range=[-4, 4, 1],
            y_range=[-0.1, 0.1, 1],   # eixo y quase invisível
            z_range=[-4, 4, 1],
            x_length=larg,
            y_length=0.1,
            z_length=alt * 0.95,
            tips=False
        ).set_color(WHITE).set_opacity(0.6)

        # Rótulos corretos
        label_re = Text("Re", font_size=40, color=WHITE).next_to(axes3d.x_axis.get_end(), RIGHT)
        label_im = Text("Im", font_size=40, color=WHITE).rotate(90*DEGREES).next_to(axes3d.z_axis.get_end(), UP)

        # Raízes complexas: -1 ± 2i → x = -1, z = ±2
        r1 = Dot3D(axes3d.c2p(-1, 0, 2), color=RED, radius=0.11)
        r2 = Dot3D(axes3d.c2p(-1, 0, -2), color=RED, radius=0.11)
        l1 = MathTex("-1+2i", color=RED, font_size=44).next_to(r1, UR, buff=0.25)
        l2 = MathTex("-1-2i", color=RED, font_size=44).next_to(r2, DR, buff=0.25)

        texto3 = VGroup(
            MathTex(r"x^2+2x+5=0", font_size=44),
            MathTex(r"\Delta=-16<0", color=RED, font_size=52),
            Text("2 raízes complexas", color=RED, font_size=34)
        ).arrange(DOWN, buff=0.18).next_to(axes3d, DOWN, buff=0.3)

        caso3 = VGroup(axes3d, label_re, label_im, r1, r2, l1, l2, texto3)

        # ==================== MONTAGEM FINAL ====================
        tudo = VGroup(caso1, caso2, caso3).arrange(RIGHT, buff=0.75).scale(0.97)
        self.play(FadeIn(tudo), run_time=2.2)

        # ==================== CORTE DINÂMICO DO EIXO X ====================
        self.play(
            ShowPassingFlash(parabola1.copy().set_color(GREEN).set_stroke(width=14), time_width=0.9),
            ShowPassingFlash(parabola2.copy().set_color(YELLOW).set_stroke(width=14), time_width=0.9),
            run_time=2.8
        )

        # Flash nas raízes
        self.play(
            Flash(raiz1, flash_radius=0.35, color=GREEN),
            Flash(raiz2, flash_radius=0.35, color=GREEN),
            Flash(vertice, flash_radius=0.4, color=YELLOW),
            Flash(r1, flash_radius=0.35, color=RED),
            Flash(r2, flash_radius=0.35, color=RED),
            run_time=3
        )

        # Legenda
        legenda = VGroup(
            Text("Δ > 0", color=GREEN),
            Text("Δ = 0", color=YELLOW),
            Text("Δ < 0", color=RED)
        ).arrange(RIGHT, buff=1.5).to_edge(DOWN, buff=0.5)
        self.play(Write(legenda))
        self.wait(7)

        # FadeOut seguro
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1.5)
        self.wait(0.5)