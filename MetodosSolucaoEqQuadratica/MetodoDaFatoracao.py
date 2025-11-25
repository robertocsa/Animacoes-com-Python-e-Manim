# manim -pqh -r 1296,2160 MetodoDaFatoracao.py MetodoDaFatoracao
'''
Animação completa e bem explicada: 
"Quando o método da fatoração é realmente fácil e rápido?"
'''

from manim import *

class MetodoDaFatoracao(Scene):
    def construct(self):
        def to_exact_top(mobj):
            mobj.to_edge(UP)
            mobj.shift(UP * (mobj.get_top()[1]+4))

        # ==================== TÍTULO E RESPOSTA INICIAL ====================
        GREEN_SCREEN = "#00FF0A"   
        
        titulo = Text("O método da fatoração é sempre viável \n para equações quadráticas?",
                      font="Verdana", font_size=50, color=BLUE)
        to_exact_top(titulo)
        self.play(Write(titulo))
        self.wait(2)

        resposta = Text("NÃO! Nem sempre é viável ou prático", font="Verdana",
                        color=RED, font_size=48)
        resposta.next_to(titulo, DOWN, buff=0.8)
        self.play(FadeIn(resposta, shift=UP))
        self.wait(2)
        self.play(FadeOut(titulo),FadeOut(resposta))
        # =========================Explicacao inicial ===========================
        titulo2 = Text("Funcionamento do método da fatoração",
                      font="Verdana", font_size=50, color=BLUE)
        to_exact_top(titulo2)
        self.play(Write(titulo2))
        self.wait(2)
        explic = Text("Primeiro e mais difícil passo é encontrar uma \n forma fatorada da equação, por exemplo:",
                      font="Verdana", font_size=44, color=BLUE)        
        self.play(Write(explic))
        self.wait(2)
        # Equação já fatorada
        eq_fatorada = MathTex(
            r"\text{Equação } x^{2}-5x+6 \text{ fatorada:} \quad (x-2)(x-3)=0",            
            font_size=56
        )        
        eq_fatorada.next_to(explic,DOWN, 0.5)
        self.play(Write(eq_fatorada))
        self.wait(1.5)
        self.play(FadeOut(titulo2, explic, eq_fatorada))                

        # Título do conceito
        titulo = Text("Propriedade do produto nulo", color=YELLOW, font_size=50)
        to_exact_top(titulo)
        self.play(Write(titulo))
        self.wait(1)

        # Explicação formal
        explicacao = Tex(
            r"Se o produto de dois fatores é zero,",
            r"\\[0.3em]pelo menos um dos fatores deve ser zero:",
            r"\\[0.5em]Se (x-2)(x-3)=0, então:",
            font_size=56
        )

        explicacao.next_to(titulo, DOWN, buff=1)
        self.play(Write(explicacao))
        self.wait(2)

        # Casos separados com setas
        caso1 = MathTex(r"x - 2 = 0", r"\quad \Rightarrow \quad", r"x_1 = 2", font_size=60)
        caso2 = MathTex(r"x - 3 = 0", r"\quad \Rightarrow \quad", r"x_2 = 3", font_size=60)

        grupo_casos = VGroup(caso1, caso2).arrange(DOWN, buff=0.8)
        grupo_casos.next_to(explicacao, DOWN, buff=1)

        # Animação aparecendo um de cada vez
        self.play(Write(caso1[0]), Write(caso1[1]), Write(caso1[2]))
        self.wait(1.5)
        self.play(Write(caso2[0]), Write(caso2[1]), Write(caso2[2]))
        self.wait(2)

        # Destaque das raízes
        raiz1 = caso1[2].copy().set_color(GREEN)
        raiz2 = caso2[2].copy().set_color(GREEN)
        raizes = VGroup(raiz1, raiz2).arrange(RIGHT, buff=1)
        raizes.next_to(grupo_casos, DOWN, buff=0.8)

        texto_raizes = Text("As raízes (ou soluções) são:", color=WHITE, font_size=42)
        texto_raizes.next_to(raizes, DOWN, buff=0.5)
        self.play(FadeOut(raizes))

        self.play(
            Write(texto_raizes),
            Transform(caso1[2].copy(), raiz1),
            Transform(caso2[2].copy(), raiz2)
        )
        self.wait(1)
        
        # Resumo final com destaque
        solucao_final = MathTex(r"x_1 = 2 \quad ;\quad x_2 = 3", font_size=72, color=GREEN)
        solucao_final.move_to(DOWN*-1)
        texto_raizes.next_to(solucao_final, UP, 0.5)
        caixa = SurroundingRectangle(solucao_final, color=GREEN, buff=0.4, corner_radius=0.2)

        self.play(
            FadeOut(VGroup(titulo, explicacao, grupo_casos, raizes)),
            GrowFromCenter(caixa),
            Write(solucao_final)
        )
        self.wait(3)

        # Mensagem final opcional
        final = Text("Pronto! Usamos apenas a propriedade do produto nulo.", 
                     color=TEAL, font_size=36)
        final.to_edge(DOWN)
        self.play(Write(final))
        self.wait(3)
        
        # Fade out de tudo
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.5)
        self.wait(0.5)                

        # ==================== CASOS FÁCEIS (EXPLICADOS UM A UM) ====================
               
        facil = Text("✓ Casos em que a fatoração pode ser fácil e rápida", 
                     color=GREEN_SCREEN, font_size=36)
        #self.play(facil.animate.scale(0.8).move_to(UP*7.5 + LEFT*5))
        self.play(facil.animate.scale(1.1).move_to(UP*9.5))
        
        #self.play(Write(facil))
        self.wait(0.5)        

        # ---------- Exemplo 1: x² + 12x + 32 = 0 ----------
        eq1 = MathTex(r"x^2 + 12x + 32 = 0", font_size=52)
        #eq1.shift(UP*1.5 + LEFT*2)
        eq1.next_to(facil, DOWN, 0.5)

        exp1 = Text("a = 1 → precisamos de dois números que:", font_size=32, color=YELLOW)
        exp1a = Text("• somados deem 12", font_size=32, color=YELLOW)
        exp1b = Text("• multiplicados deem 32", font_size=32, color=YELLOW)
        explicacao1 = VGroup(exp1, exp1a, exp1b).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        explicacao1.next_to(eq1, DOWN, buff=0.5)

        pares = MathTex(r"(4)\;e\;(8)", r"\;\to\; 4+8=12", r"\;\to\; (4)\cdot(8)=32", 
                        color=WHITE, font_size=52)
        pares.next_to(explicacao1, DOWN, buff=0.5)

        fatorada1 = MathTex(r"\to (x+4)(x+8)=0", r"\quad \Rightarrow \quad x_1=-4\;,\;x_2=-8", 
                            color=WHITE, font_size=52)
        fatorada1.next_to(pares, DOWN, buff=0.4)

        self.play(Write(eq1))
        self.wait(1)
        self.play(Write(explicacao1))
        self.wait(2)
        self.play(Write(pares))
        self.wait(2)
        self.play(Write(fatorada1))
        self.wait(4)
        self.play(FadeOut(VGroup(eq1, explicacao1, pares, fatorada1)))

        # ---------- Exemplo 2: diferença de quadrados ----------
        eq2 = MathTex(r"x^2 - 9 = 0", font_size=58)        
        eq2.next_to(facil, DOWN, 0.6)

        exp2 = Text("Reconhecemos diferença de quadrados:", font_size=42)
        identidade = MathTex(r"A^2 - B^2 = (A-B)(A+B)", font_size=46)
        aplicacao = MathTex(r"x^2 - 3^2 \to (x-3)(x+3)=0", font_size=54)
        raizes2 = MathTex(r"x_1=3\;,\;x_2=-3", font_size=54)

        grupo2 = VGroup(exp2, identidade, aplicacao, raizes2).arrange(DOWN, buff=0.4)
        grupo2.next_to(eq2, DOWN, buff=0.6)

        self.play(Write(eq2))
        self.wait(1)
        self.play(Write(grupo2, run_time=4))
        self.wait(5)
        self.play(FadeOut(VGroup(eq2, grupo2)))
                
        # ---------- Exemplo 3: 2x² + 7x + 3 = 0 ----------
        eq3 = MathTex(r"2x^2 + 7x + 3 = 0", font_size=48)
        eq3.next_to(facil, DOWN, 0.6)

        dica3 = Text("a ≠ 1, mas os números são pequenos → tentativa rápida", 
                     color=ORANGE, font_size=36)
        dica3.next_to(eq3, DOWN, buff=0.5)

        tentativa = MathTex(r"(2x \,+\,?)\,(x \,+\,?)", font_size=54)
        tentativa.next_to(dica3, DOWN, buff=0.5)

        self.play(Write(eq3))
        self.wait(1)
        self.play(Write(dica3))
        self.play(Write(tentativa))
        self.wait(2)

        # Animação da descoberta
        certo = MathTex(r"(2x+1)(x+3)", color=GREEN_SCREEN, font_size=54)
        certo.move_to(tentativa)
        self.play(Transform(tentativa, certo))
        self.wait(2)

        verificacao = MathTex(r"2x^2 + 6x + x + 3 = 2x^2 + 7x + 3 \;\checkmark", 
                              color=GREEN_SCREEN, font_size=54)
        verificacao.next_to(certo, DOWN, buff=0.5)
        self.play(Write(verificacao))
        self.wait(2)

        raizes3 = MathTex(r"x_1 = -\dfrac{1}{2}\;,\;x_2 = -3", color=GREEN_SCREEN, font_size=54)
        raizes3.next_to(verificacao, DOWN)
        self.play(Write(raizes3))
        self.wait(3)
        self.play(FadeOut(VGroup(eq3, dica3, tentativa, verificacao, raizes3)))
        
        self.play(FadeOut(facil))
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

        # ==================== CASOS DIFÍCEIS (seu código original mantido) ====================
        dificil = Text("✗ Casos em que é difícil ou impraticável", color=RED_B, font_size=40)
        to_exact_top(dificil)
        self.play(Write(dificil))

        itens = [
            "Raízes não inteiras: 3x² + 5x − 2 = 0",
            "Raízes irracionais: 4x² − 7x + 1 = 0",
            "Raízes complexas: x² + 2x + 5 = 0",
            "Coeficientes decimais ou grandes",
        ]
        casos = VGroup()
        for texto in itens:
            linha = VGroup(
                Dot(color=YELLOW, radius=0.08),
                Text(texto, font_size=36, color=WHITE)
            )
            linha.arrange(RIGHT, buff=0.35)
            casos.add(linha)
        casos.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        casos.next_to(dificil, DOWN, buff=0.5).to_edge(LEFT)
        self.play(Write(casos))
        self.wait(6)

        exemplo1 = MathTex(r"3x^2 + 5x - 2 = 0 \quad \to \quad x = -2,\; x = \frac{1}{3}")
        exemplo2 = MathTex(r"4x^2 - 7x + 1 = 0 \quad \to \quad x = \dfrac{7 \pm \sqrt{33}}{8}")
        exemplo3 = MathTex(r"x^2 + 2x + 5 = 0 \quad \Delta = -16 \quad (\text{complexas})")
        exemplos = VGroup(exemplo1, exemplo2, exemplo3).arrange(DOWN, buff=0.6)
        exemplos.next_to(casos, DOWN, buff=0.6).shift(RIGHT*1.2)

        self.play(Write(exemplo1))
        self.wait(2)
        self.play(Write(exemplo2))
        self.wait(2)
        self.play(Write(exemplo3))
        self.wait(3)

        # ==================== Metodos que sempre funcionam ====================
        self.play(FadeOut(VGroup(casos, exemplo1, exemplo2, exemplo3, dificil)))
        sempre = Text("Métodos que SEMPRE funcionam", color=GREEN, font_size=44)
        to_exact_top(sempre)
        self.play(Write(sempre))
        metodos = VGroup(
            Text("• Fórmula de Bhaskara", color=TEAL),
            Text("• Completar o quadrado", color=TEAL)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.6)
        metodos.next_to(sempre, DOWN, buff=0.6)
        self.play(Write(metodos))
        self.wait(2)

        dica = Text("Dica de prova:\nTente fatorar 20–30 s → não saiu? Use Bhaskara!",
                    color=ORANGE, font_size=40)
        dica.to_edge(DOWN)
        caixa = SurroundingRectangle(dica, color=ORANGE, buff=0.4)
        self.play(Create(caixa), Write(dica))
        self.wait(4)

        conclusao = Text("Conclusão", color=GOLD, font_size=48)
        to_exact_top(conclusao)
        texto_final = Text(
            "A fatoração é ótima quando funciona rápido,\n"
            "mas NÃO é sempre viável.\n\n"
            "Bhaskara, sim!",
            font_size=42
        )
        texto_final.next_to(conclusao, DOWN, buff=0.8)
        self.play(
            FadeOut(VGroup(sempre, metodos, dica, caixa)),
            FadeIn(conclusao)
        )
        self.play(Write(texto_final))
        self.wait(8)
        self.play(FadeOut(VGroup(conclusao, texto_final)))
        