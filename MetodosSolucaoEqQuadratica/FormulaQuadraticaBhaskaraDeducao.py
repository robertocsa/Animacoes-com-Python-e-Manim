# FormulaQuadraticaBhaskara.py
# manim -pqh -r 648,1080 FormulaQuadraticaBhaskaraDeducao.py FormulaBhaskaraDeducao para testes rápidos
# manim -pqh -r 1296,2160 FormulaQuadraticaBhaskaraDeducao.py FormulaBhaskaraDeducao para versao producao

from manim import *

class FormulaBhaskaraDeducao(Scene):
    def construct(self):
        self.camera.background_color = "#0d1117"  # fundo escuro bonito
        def to_exact_top(mobj):
            mobj.to_edge(UP)
            #print(mobj.get_top()[1])            
            mobj.shift(UP * (mobj.get_top()[1]+4))
            #print(UP * (mobj.get_top()[1]+4))
        
        # ==================== DEDUÇÃO GERAL ====================
        titulo_ded = Text("Dedução Geral da Fórmula", font_size=64, color=BLUE_C)
        to_exact_top(titulo_ded)
        self.play(Write(titulo_ded))
        
        # Frase inicial ---------------------------------------------
        msg1 = Text("A fórmula quadrática (Bháskara)", font="DejaVu Sans", font_size=50, color=TEAL)
        msg1.to_edge(UP)

        msg2 = Text("generaliza o método de", font="DejaVu Sans", font_size=50, color=TEAL)
        msg2.next_to(msg1, DOWN, buff=0.5)

        msg3 = Text("completar quadrado", font="DejaVu Sans", font_size=50, color=TEAL)
        msg3.next_to(msg2, DOWN, buff=0.5)  # <-- correção

        self.play(
            Write(msg1),
            Write(msg2),
            Write(msg3)
        )

        self.wait(2)
        self.play(FadeOut(msg1, msg2, msg3))
        #-----------------------------------------------
        
        bloco = VGroup()

        equacoes = [
            r"ax^2 + bx + c = 0",
            r"ax^2 + bx + c -c = 0 - c",
            r"ax^2 + bx = -c",
            r"\frac{ax^2}{a} + \frac{b}{a}x = -\frac{c}{a}",
            r"x^2 + \frac{b}{a}x + \left(\frac{b}{2a}\right)^2 = -\frac{c}{a} + \left(\frac{b}{2a}\right)^2",
            r"\left(x + \frac{b}{2a}\right)^2 = \frac{b^2 - 4ac}{4a^2}",
            r"x + \frac{b}{2a} = \pm \frac{\sqrt{b^2 - 4ac}}{2a}",
            r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}",
        ]

        explicacoes = [
            "Inicia-se pela equação típica acima",
            "Subtraímos 'c' dos dois lados, para levá-lo para a direita",            
            "Somente os termos que têm 'x' ficam à esquerda",
            r"Dividimos todos os termos da equação por 'a' \\ para tornar o coeficiente de $x^{2}$ igual a 1",                   
            r"Para completar o quadrado, precisamos \\ adicionar ${\left( \dfrac{\text{coeficiente de x}}{2} \right)^{2}}$ nos dois lados",
            "Obtivemos assim um quadrado perfeito no lado esquerdo",
            "Raiz de 2 nos dois lados, para remover a potência de 2",
            "Isolamos o 'x' e ... Fórmula pronta!"
        ]

        eq_atual = MathTex(equacoes[0], font_size=76).next_to(titulo_ded,DOWN, buff=0.25)
        bloco.add(eq_atual)
        self.play(Write(eq_atual))
        self.wait(1)               

        bloco = VGroup(eq_atual)
        
        #==========================================
        
        for i in range(8):
            nova_eq = MathTex(equacoes[i], font_size=70 if i <= 7 else 74)
            nova_eq.next_to(eq_atual, DOWN, buff=0.6 if i  <= 7 else 1.2)
            
            exp=Text("")
            exp = Tex(explicacoes[i], font_size=50, color=YELLOW).next_to(nova_eq, DOWN, buff=0.5)

            if (i<7):
                self.play(Transform(eq_atual, nova_eq), run_time=1.4)
            else:
                self.play(Write(nova_eq), run_time=1.4)
            self.play(Write(exp), run_time=0.8)
            self.wait(2.2)
            #if i < 8:
            self.play(FadeOut(exp))
            eq_atual = nova_eq
            bloco.add(eq_atual)
        
        # Animação de descida suave: exatamente 2.2 vezes a própria altura
        self.play(
            eq_atual.animate.shift(DOWN * eq_atual.height * 1.2),
            run_time=1.8,
            rate_func=smooth  # opcional: deixa mais fluido
        )

        # Agora cria a caixa e o título com espaço perfeito
        box = SurroundingRectangle(eq_atual, color=YELLOW, buff=0.45, corner_radius=0.3)
        titulo_final = Text("Fórmula de Bháskara", font_size=62, color=YELLOW, weight=BOLD)
        titulo_final.next_to(box, UP, buff=0.4)

        self.play(
            Create(box),
            Write(titulo_final),
            run_time=1.5
        )

        self.wait(2)

        # Fade out de tudo
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.5)
        self.wait(0.5)
                
        # ================================================================
        # Discriminante
        titulo_delta = Text("Resultados possíveis, de acordo com o discriminante:", font_size=38, color=RED_C)
        to_exact_top(titulo_delta)
        self.play(Write(titulo_delta))
        
        delta = MathTex(r"\Delta = b^2 - 4ac", font_size=74, color=ORANGE).next_to(titulo_delta, DOWN, buff=0.4)
        self.play(Write(delta))
        self.wait(1)

        infos = VGroup(
            Tex(r"$\Delta > 0 \;\to$ 2 raízes reais distintas", color=WHITE),
            Tex(r"$\Delta = 0 \;\to$ 1 raiz real (dupla)", color=WHITE),
            Tex(r"$\Delta < 0 \;\to$ raízes complexas", color=WHITE)
        ).arrange(DOWN, buff=0.5).next_to(delta, DOWN, buff=0.7)

        for linha in infos:
            self.play(Write(linha), run_time=1)
            self.wait(1.5)

        self.play(FadeOut(Group(*self.mobjects)))      
        
        