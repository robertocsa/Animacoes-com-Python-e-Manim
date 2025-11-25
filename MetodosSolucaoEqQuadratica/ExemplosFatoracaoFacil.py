# manim -pqh -r 1296,2160 ExemplosFatoracaoFacil.py ExemplosFatoracaoFacil

from manim import *

class ExemplosFatoracaoFacil(Scene):
    def construct(self):
        self.camera.background_color = "#0d1117"  # fundo escuro bonito
        def to_exact_top(mobj):
            mobj.to_edge(UP)        
            mobj.shift(UP * (mobj.get_top()[1]+4))       
        
        # ==================== RESUMO DOS CASOS FÁCEIS ====================
        resumo_facil = Text("Sinais de que a fatoração será fácil:", color=GOLD, font_size=40)      
        to_exact_top(resumo_facil)

        listaCasosFaceis=[
                "Coeficiente de x² = 1 e c pequeno",
                "Diferença de quadrados óbvia",
                "a = 2, 3 ou 4 e c tem poucos divisores",
                "Você enxerga os fatores em menos de 20–30 segundos!"                
            ]       

        self.play(Write(resumo_facil))
        self.wait(0.3)
                
        casosFaceis = VGroup()
        for texto in listaCasosFaceis:
            linha = VGroup(
                Dot(color=YELLOW, radius=0.08),
                Text(texto, font_size=36, color=WHITE)
            )
            linha.arrange(RIGHT, buff=0.35)
            casosFaceis.add(linha)
        casosFaceis.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        casosFaceis.next_to(resumo_facil, DOWN, buff=0.5)
        
        self.play(Write(casosFaceis))
        self.wait(6)
        self.play(FadeOut(resumo_facil), FadeOut(casosFaceis))

        # ----------------------------------------------------------------------
        # EXEMPLO 1 — a = 1 e c pequeno
        # ----------------------------------------------------------------------
        exemplo1 = VGroup(
            Text("Exemplo 1 — a = 1 e c pequeno", font_size=50, color=YELLOW),
            MathTex(
                r"\text{Equação: }", r"x^2 + 5x + 6",
                font_size=60,
                substrings_to_isolate=["x^2 + 5x + 6"]
            ),
            MathTex(
                r"\text{Fatoração: }", r"(x+2)(x+3)",
                font_size=60,
                substrings_to_isolate=["(x+2)(x+3)"]
            ),
            MathTex(
                r"\text{Raízes: }", r"x = -2,\;-3",
                font_size=60,
                substrings_to_isolate=["x = -2,\\;-3"]
            )
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).to_edge(LEFT).shift(DOWN*1)

        exemplo1[1][1].set_color(BLUE)    # equação
        exemplo1[2][1].set_color(GREEN)   # fatoração
        exemplo1[3][1].set_color(RED)     # raízes

        self.play(FadeIn(exemplo1, shift=RIGHT))
        self.wait(2)
        self.play(FadeOut(exemplo1))

        # ----------------------------------------------------------------------
        # EXEMPLO 2 — Diferença de quadrados
        # ----------------------------------------------------------------------
        exemplo2 = VGroup(
            Text("Exemplo 2 — Diferença de quadrados", font_size=50, color=YELLOW),
            MathTex(
                r"\text{Equação: }", r"x^2 - 49",
                font_size=60,
                substrings_to_isolate=["x^2 - 49"]
            ),
            MathTex(
                r"\text{Fatoração: }", r"(x-7)(x+7)",
                font_size=60,
                substrings_to_isolate=["(x-7)(x+7)"]
            ),
            MathTex(
                r"\text{Raízes: }", r"x = 7,\;-7",
                font_size=60,
                substrings_to_isolate=["x = 7,\\;-7"]
            )
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).to_edge(RIGHT).shift(DOWN*1)

        exemplo2[1][1].set_color(BLUE)
        exemplo2[2][1].set_color(GREEN)
        exemplo2[3][1].set_color(RED)

        self.play(FadeIn(exemplo2, shift=LEFT))
        self.wait(2)
        self.play(FadeOut(exemplo2))

        # ----------------------------------------------------------------------
        # EXEMPLO 3 — a pequeno e c com poucos divisores
        # ----------------------------------------------------------------------
        exemplo3 = VGroup(
            Text("Exemplo 3 — 'a' pequeno e \npoucos divisores de 'c'", font_size=50, color=YELLOW),
            MathTex(
                r"\text{Equação: }", r"2x^2 + 7x + 3",
                font_size=60,
                substrings_to_isolate=["2x^2 + 7x + 3"]
            ),
            MathTex(
                r"\text{Fatoração: }", r"(2x+1)(x+3)",
                font_size=60,
                substrings_to_isolate=["(2x+1)(x+3)"]
            ),
            MathTex(
                r"\text{Raízes: }", r"x = -\tfrac{1}{2},\;-3",
                font_size=60,
                substrings_to_isolate=[r"x = -\tfrac{1}{2},\\;-3"]
            )
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).to_edge(DOWN).shift(UP*1)

        exemplo3[1][1].set_color(BLUE)
        exemplo3[2][1].set_color(GREEN)
        exemplo3[3][1].set_color(RED)

        self.play(FadeIn(exemplo3, shift=UP))
        self.wait(3)
        self.play(FadeOut(exemplo3))
