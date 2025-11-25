from manim import *

# manim -pqh -r 1296,2160 BhaskaraESomaProduto.py BhaskaraESomaProduto

class BhaskaraESomaProduto(Scene):
    CYAN_RCS="#00ffff"
    GREEN_RCS="#B1F6B1"
    YELLOW_RCS="#F1F108"
    
    def construct(self):
        self.camera.background_color = "#0d1117"  # fundo escuro bonito
        titulo = Text("Fórmula de Bháskara × Soma e Produto", font_size=48, color=BLUE)
        self.play(Write(titulo))
        self.play(titulo.animate.move_to(UP*8.2))
        self.wait(1)

        # Lista de equações que vamos usar (todas com raízes inteiras bonitas)
        equacoes = [
            {"a": 1, "b": -5, "c": 6,   "raizes": [2, 3]},   # x² - 5x + 6 = 0
            {"a": 2, "b": 4,  "c": -6,  "raizes": [-3, 1]},  # 2x² + 4x - 6 = 0
            {"a": 1, "b": 4,  "c": 4,   "raizes": [-2, -2]}  # x² + 4x + 4 = 0 (raiz dupla)
        ]

        for i, eq in enumerate(equacoes):
            self.play(FadeOut(titulo, shift=UP*12.5))
            self.resolver_com_bhaskara(eq, i+1)
            self.wait(1)
            self.resolver_com_soma_produto(eq, i+1)
            self.wait(2)
            self.clear()

        # Mensagem final
        final = Text("Os dois métodos sempre \n chegam às mesmas raízes!", font_size=48, color=GREEN)
        self.play(Write(final))
        self.wait(3)

    def resolver_com_bhaskara(self, eq, num):
        a, b, c = eq["a"], eq["b"], eq["c"]
        
        titulo = Text(f"Exemplo {num} – Fórmula de Bháskara", font_size=48, color=YELLOW).move_to(UP*8.2)
        self.play(Write(titulo))       

        # Equação
        equacao = MathTex(
            f"{a}x^2 + ({b})x + ({c}) = 0" if a != 1 else f"x^2 + ({b})x + ({c}) = 0"
        )                      
        if b >= 0:
            equacao = MathTex(f"{a}x^2 + {b}x + {c} = 0" if a != 1 else f"x^2 + {b}x + {c} = 0")
        
        equacao.set(font_size=50)
        equacao.next_to(titulo, DOWN, buff=0.5)  
        equacao.scale(1.5)
        
        coefsEquacao=MathTex(f"a={a}",",", f"b={b}",",", f"c={c}", font_size=52).next_to(equacao, DOWN, buff=0.5)
        coefsEquacao[0].set(color=self.CYAN_RCS)
        coefsEquacao[2].set(color=self.GREEN_RCS)
        coefsEquacao[4].set(color=self.YELLOW_RCS)
        coefsEquacao.scale(1.5)
        
        self.play(Write(equacao),Write(coefsEquacao))
        self.wait(1)

        # Fórmula de Bháskara
        bhaskara = MathTex(
            r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}"
        ).next_to(coefsEquacao, DOWN, buff=0.6)
        
        bhaskara.scale(1.5)
        
        self.play(Write(bhaskara))
        self.wait(1)


        # Delta
        discriminant = b**2 - 4*a*c

        delta = VGroup(
            MathTex(r"\Delta = b^2 - 4ac"),
            MathTex(rf"= ({b})^2 - 4 \cdot ({a}) \cdot ({c})")
        ).arrange(DOWN, aligned_edge=LEFT)

        delta.next_to(bhaskara, DOWN, buff=0.6)

        delta_val = MathTex(rf"\Delta = {discriminant}")

        delta_val.next_to(delta[1], DOWN, buff=0.5)

        # Uniform scaling
        for mob in (delta, delta_val):
            mob.font_size = 52
            mob.scale(1.5)

        self.play(Write(delta), run_time=2)
        self.play(Write(delta_val), run_time=1.5)
        self.wait(1)
       

        # Raízes
        raiz1 = eq["raizes"][0]
        raiz2 = eq["raizes"][1] if len(eq["raizes"]) > 1 else raiz1

        x1 = MathTex(
            r"x_1 = \frac{" + f"{-b}" + r" + \sqrt{" + f"{b**2-4*a*c}" + r"}" + "}{" + f"{2*a}" + r"}" + f" = {raiz1}"
        ).next_to(delta_val, DOWN, buff=0.8)
        
        if raiz1 != raiz2:
            x2 = MathTex(
                r"x_2 = \frac{" + f"{-b}" + r" - \sqrt{" + f"{b**2-4*a*c}" + r"}" + "}{" + f"{2*a}" + r"}" + f" = {raiz2}"
            ).next_to(x1, DOWN, buff=1.2)
        else:
            x2 = MathTex(r"(raiz dupla)").next_to(x1, DOWN, buff=0.8)
        
        x1.scale(1.5)
        x2.scale(1.5)

        self.play(Write(x1))
        self.play(Write(x2))
        self.wait(2)

        # Guarda os objetos para remover depois
        grupo_bhaskara = VGroup(titulo, equacao, coefsEquacao, bhaskara, delta, delta_val, x1, x2)
        self.play(FadeOut(grupo_bhaskara, shift=UP*10))

    def resolver_com_soma_produto(self, eq, num):
        a, b, c = eq["a"], eq["b"], eq["c"]
        r1, r2 = eq["raizes"][0], eq["raizes"][1] if len(eq["raizes"]) > 1 else eq["raizes"][0]

        titulo = Text(f"Exemplo {num} – Soma e Produto das raízes", font_size=48, color=GOLD).move_to(UP*8.2)
        self.play(Write(titulo))

        # Forma genérica
        gen = MathTex(r"ax^2 + bx + c = 0").scale(1.5)
        gen.next_to(titulo, DOWN, buff=0.8)
        self.play(Write(gen))
        self.wait(0.5)                
        
        # Equação
        equacao = MathTex(
            f"{a}x^2 + ({b})x + ({c}) = 0" if a != 1 else f"x^2 + ({b})x + ({c}) = 0"
        ).scale(1.8)
        equacao.next_to(gen, DOWN, buff=0.5) 
        self.play(Write(equacao))
        self.wait(0.5)
        
        # Coeficientes da Equacao
        coefsEquacao=MathTex(f"a={a}",",", f"b={b}",",", f"c={c}", font_size=52).next_to(equacao, DOWN, buff=0.5)
        coefsEquacao[0].set(color=self.CYAN_RCS)
        coefsEquacao[2].set(color=self.GREEN_RCS)
        coefsEquacao[4].set(color=self.YELLOW_RCS)
        coefsEquacao.scale(1.5)
        self.play(Write(coefsEquacao))

        # Soma e produto (teorema de Vieta)
        soma = MathTex(r"\text{Soma das raízes} = x_1 + x_2 = -\frac{b}{a}").next_to(coefsEquacao, DOWN, buff=0.6)
        produto = MathTex(r"\text{Produto das raízes} = x_1 \cdot x_2 = \frac{c}{a}").next_to(soma, DOWN, buff=0.8)
        soma.scale(1.5)
        produto.scale(1.5)

        self.play(Write(soma))
        self.play(Write(produto))
        self.wait(1)

        # Aplicando nos valores concretos
        soma_val = MathTex(
            r"x_1 + x_2 = -\frac{" + f"{b}" + "}{" + f"{a}" + "} = " + f"{r1 + r2}"
        ).next_to(produto, DOWN, buff=0.8)
        prod_val = MathTex(
            r"x_1 \cdot x_2 = \frac{" + f"{c}" + "}{" + f"{a}" + "} = " + f"{r1*r2}"
        ).next_to(soma_val, DOWN, buff=1.2)
        
        soma_val.scale(1.5)
        prod_val.scale(1.5)

        self.play(Write(soma_val))
        self.play(Write(prod_val))
        self.wait(1)
        
        sistema= MathTex("")

        # Resolvendo o sistema (só nos casos com raízes distintas)
        if r1 != r2:
            sistema = MathTex(
                r"\begin{cases} x + y = " + f"{r1+r2}" + r" \\ xy = " + f"{r1*r2}" + r" \end{cases}"
            ).next_to(prod_val, DOWN, buff=1)
            sistema.set(font_size=48)
            sistema.scale(1.5)
            self.play(Write(sistema))
            self.wait(0.5)

            sol = MathTex(
                r"x_1 = " + f"{r1}" + r", \quad x_2 = " + f"{r2}"
            ).next_to(sistema, DOWN, buff=0.8)
            sol.set(font_size=48)
            sol.scale(1.5)
            self.play(Write(sol))
        else:
            menosBdiv2a = -b / (2 * a)                  # valor numérico (ex: 3.0 ou -2.5)
            valor_formatado = f"{menosBdiv2a:.10g}".rstrip('.')  # tira zeros desnecessários e o ponto no final

            raiz_dupla = MathTex(
                r"\text{Raiz dupla} \quad \rightarrow \quad ",
                r"x",
                r"\;=\;",
                r"\dfrac{-b}{2a}",
                r"\;=\;",
                rf"{valor_formatado}",   # aqui aparece o número calculado (ex: 3 ou -1.5)
                font_size=48,
                color=ORANGE
            ).next_to(prod_val, DOWN, buff=1.0)
            raiz_dupla.next_to(prod_val, DOWN, buff=0.8)
            self.play(Write(raiz_dupla), run_time=2)
            self.wait(1)
                        
            sol = MathTex(r"x = \frac{" + f"{r1+r2}" + "}{2} = " + f"{r1}").next_to(raiz_dupla, DOWN)
            sol.set(font_size=48)
            sol.scale(1.5)
            self.play(Write(sol))

        conclusao = Text("Mesmas raízes do método anterior!", color=GREEN, font_size=45)
        conclusao.next_to(sol if 'sol' in locals() else raiz_dupla, DOWN, buff=0.8)
        self.play(Write(conclusao))
        self.wait(2)
        # Guarda os objetos para remover depois
        grupo_bhaskara = VGroup(titulo, gen, equacao, coefsEquacao, conclusao, sol, sistema, soma_val, prod_val, soma, produto)
        self.play(FadeOut(grupo_bhaskara, shift=UP*10))