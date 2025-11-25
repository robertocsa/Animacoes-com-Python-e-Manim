from manim import *

class ExemplosSegmentos(MovingCameraScene):
    def construct(self):
        # Configuração geral
        self.camera.background_color = "#0d1117"  # fundo escuro bonito

        # 1) Um segmento largo que começa no canto superior esquerdo e desce até o inferior direito
        seg1 = Line(
            start=np.array([-7.0, 3.99, 0]),   # canto superior esquerdo da tela
            end=np.array([-7.1, -3.99, 0]),     # canto inferior Esquerdo
            stroke_width=20,
            color=BLUE
        )
        seg1.set_stroke(opacity=0.9)

        # 2) Os outros três segmentos diagonais completando os cantos
        seg2 = Line(
            start=np.array([6.2, 4.05, 0]),    # superior direito
            end=np.array([6.2, -4.05, 0]),    # inferior direito
            stroke_width=20,
            color=RED
        )

        seg3 = Line(
            start=np.array([-6.2, 4.05, 0]),  # superior esquerdo
            end=np.array([6.2, 4.05, 0]),      # superior direito
            stroke_width=20,
            color=GREEN
        )

        seg4 = Line(
            start=np.array([6.2, -4.05, 0]),   # inferior direito
            end=np.array([-6.2, -4.05, 0]),     # inferior esquerdo
            stroke_width=20,
            color=YELLOW
        )

        # 3) Segmentos que saem do centro da tela até os quatro cantos
        centro = np.array([0, 0, 0])

        raio1 = Line(centro, [-7.2, 4.05, 0], stroke_width=12, color=TEAL)
        raio2 = Line(centro, [7.2, 4.05, 0], stroke_width=12, color=TEAL)
        raio3 = Line(centro, [-7.2, -4.05, 0], stroke_width=12, color=TEAL)
        raio4 = Line(centro, [7.2, -4.05, 0], stroke_width=12, color=TEAL)

        # Animações didáticas
        self.play(Create(seg1), run_time=2)
        self.wait(0.5)

        self.play(
            Create(seg2),
            Create(seg3),
            Create(seg4),
            run_time=2
        )
        self.wait(1)

        # Título opcional
        titulo = Tex(r"Diagonais completas da tela", font_size=64, color=WHITE).to_edge(UP)
        self.play(Write(titulo))
        self.wait(1)
        self.play(FadeOut(titulo))

        # Agora os raios saindo do centro
        self.play(
            Create(raio1),
            Create(raio2),
            Create(raio3),
            Create(raio4),
            run_time=3
        )
        self.wait(1)

        # Destaque final: todos juntos
        self.play(
            FadeOut(seg1, seg2, seg3, seg4),
            raio1.animate.set_stroke(width=20, color=PURPLE),
            raio2.animate.set_stroke(width=20, color=PURPLE),
            raio3.animate.set_stroke(width=20, color=PURPLE),
            raio4.animate.set_stroke(width=20, color=PURPLE),
            run_time=2
        )

        titulo2 = Tex(r"Raios partindo do centro $\to$ cantos", font_size=58, color=PURPLE)
        titulo2.to_edge(UP)
        self.play(Write(titulo2))
        self.wait(3)


# Se quiser rodar cada parte separadamente, pode criar cenas individuais:

class ApenasDiagonalPrincipal(Scene):
    def construct(self):
        linha = Line(
            start=[-7.2, 4.05, 0],
            end=[7.2, -4.05, 0],
            stroke_width=25,
            color=BLUE
        )
        self.play(Create(linha), run_time=2)
        self.wait(2)


class QuatroDiagonais(Scene):
    def construct(self):
        linhas = VGroup(
            Line([-7.2, 4.05, 0], [7.2, -4.05, 0], stroke_width=18, color=BLUE),
            Line([7.2, 4.05, 0], [-7.2, -4.05, 0], stroke_width=18, color=RED),
            Line([-7.2, -4.05, 0], [7.2, 4.05, 0], stroke_width=18, color=GREEN),
            Line([7.2, -4.05, 0], [-7.2, 4.05, 0], stroke_width=18, color=YELLOW),
        )
        self.play(Create(linhas), run_time=4)
        self.wait(2)


class RaiosDoCentro(Scene):
    def construct(self):
        centro = Dot(color=WHITE)
        raios = VGroup(
            Line(ORIGIN, [-7.2, 4.05, 0]),
            Line(ORIGIN, [7.2, 4.05, 0]),
            Line(ORIGIN, [-7.2, -4.05, 0]),
            Line(ORIGIN, [7.2, -4.05, 0]),
        ).set_stroke(width=14, color=TEAL)

        self.play(GrowFromCenter(centro))
        self.play(Create(raios), run_time=3)
        self.wait(2)