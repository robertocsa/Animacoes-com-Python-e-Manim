# manim -pqh -r 1296,2160 FactoringQuadratic.py FactoringQuadratic

from manim import *

class FactoringQuadratic(Scene):
    def construct(self):
        # Margem superior para vídeos 9:16
        TOP_Y = 3.2   # região alta da tela
        LINE_SPACING = 0.4

        # ---------- Título ----------
        title = Text(
            "Fatoração de Quadráticas",
            font_size=64
        ).move_to(UP*9).shift(DOWN * 0.3)

        self.play(Write(title))
        self.wait(1)

        # ---------- Expressão principal ----------
        expr = MathTex("x^2 + 26x + 168", font_size=80)
        expr.next_to(title, DOWN, buff=0.6)
        self.play(Write(expr))
        self.wait(2)

        # ---------- a, b, c ----------
        a_label = MathTex("a = 1", font_size=55)
        b_label = MathTex("b = 26", font_size=55)
        c_label = MathTex("c = 168", font_size=55)

        labels = VGroup(a_label, b_label, c_label).arrange(RIGHT, buff=1.2)
        labels.next_to(expr, DOWN, buff=0.5)

        self.play(FadeIn(labels, shift=UP))
        self.wait(2)

        # ---------- Produto e soma ----------
        prod_label = MathTex("a \\cdot c = 1 \\times 168 = 168", font_size=46)
        sum_label  = MathTex("b = 26", font_size=55)

        prod_label.next_to(labels, DOWN, buff=0.4)
        sum_label.next_to(prod_label, DOWN, buff=LINE_SPACING)

        self.play(Write(prod_label))
        self.play(Write(sum_label))
        self.wait(2)

        # ---------- Números 14 e 12 ----------
        nums = MathTex("14 \\times 12 = 168", font_size=55)
        nums2 = MathTex("14 + 12 = 26", font_size=55)

        nums.next_to(sum_label, DOWN, buff=0.5)
        nums2.next_to(nums, DOWN, buff=LINE_SPACING)

        self.play(Write(nums))
        self.play(Write(nums2))
        self.wait(2)

        # ---------- Reescrever 26x ----------
        rewrite = MathTex(
            "x^2 + 26x + 168 = x^2 + 14x + 12x + 168",
            font_size=64
        ).next_to(nums2, DOWN, buff=0.7)

        self.play(Write(rewrite))
        self.wait(2)

        # ---------- Agrupar ----------
        group1 = MathTex(
            "= (x^2 + 14x) + (12x + 168)",
            font_size=64
        ).next_to(rewrite, DOWN, buff=LINE_SPACING + 0.2)

        self.play(Transform(rewrite, group1))
        self.wait(2)

        # ---------- Fatorar ----------
        factor1 = MathTex(
            "= x(x + 14) + 12(x + 14)",
            font_size=64
        ).next_to(group1, DOWN, buff=LINE_SPACING + 0.2)

        self.play(Transform(rewrite, factor1))
        self.wait(2)

        # ---------- Resultado final ----------
        final = MathTex(
            "= (x + 14)(x + 12)",
            font_size=80
        ).next_to(factor1, DOWN, buff=0.7)

        self.play(Transform(rewrite, final))
        self.wait(2)

        # ---------- Conclusão ----------
        conclusion = Text(
            "Logo: x² + 26x + 168 = (x + 14)(x + 12)",
            font_size=50
        ).next_to(final, DOWN, buff=0.6)

        self.play(FadeIn(conclusion))
        self.wait(2)
