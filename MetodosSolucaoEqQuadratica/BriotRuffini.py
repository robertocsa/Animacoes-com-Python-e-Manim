# manim -pqh -r 1296,2160 BriotRuffini.py BriotRuffini
# Totalmente compatível com Manim v0.18+ (2025)

from manim import *

class BriotRuffini(Scene):

    def construct(self):
        self.camera.background_color = "#0d0d0d"
        GREEN_RCS="#00FF0A"

        # ==================== 1. Título + equação ====================

        titulo = Tex(r"Resolvendo $x^2 - 5x + 6 = 0$", font_size=90)
        subtitulo = Tex(r"usando o método de", r" Briot-Ruffini", font_size=78)
        subtitulo[1].set_color(YELLOW)
        cabeçalho = VGroup(titulo, subtitulo).arrange(DOWN, buff=0.4)
        cabeçalho.move_to(UP*4).shift(DOWN*0.5)   # posição inicial (um pouco abaixo do topo)

        # Aparece no centro/topo inicial
        self.play(Write(titulo))
        self.wait(0.8)
        self.play(Write(subtitulo))
        self.wait(1.5)

        # Agora sobe bem para o topo (quase encostado na borda superior)
        self.play(
            cabeçalho.animate.move_to(UP*9).shift(DOWN*0.5),
            run_time=1.4,     
            rate_func=smooth            
        )
        self.wait(0.6)       
     
        # ==================== 2. Divisores possíveis ====================
        div_texto = Tex(r"Divisores possíveis de 6:", font_size=74)
        divisores = MathTex(r"\pm1,\ \pm2,\ \pm3,\ \pm6", font_size=94)
        grupo_div = VGroup(div_texto, divisores).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        grupo_div.next_to(cabeçalho, DOWN, buff=0.6)

        self.play(FadeIn(grupo_div, shift=RIGHT*0.2))
        self.wait(1)

        # Testes rápidos
        testes = VGroup()
        for v, res in zip([1,2,3,6], [2,0,-4,-6]):
            linha = MathTex(f"f({v})=", f"{v}^2 -5\\cdot{v}+6", "=", f"{res}", font_size=78)
            if res == 0: linha[3].set_color(GREEN_RCS)
            testes.add(linha)

        testes.arrange(DOWN, aligned_edge=LEFT, buff=0.52)
        testes.next_to(grupo_div, DOWN, buff=0.9).to_edge(LEFT, buff=1.2)

        for i, t in enumerate(testes):
            self.play(FadeIn(t, shift=UP*0.25), run_time=0.7)
            self.wait(0.8 if i != 1 else 2.2)

        caixa = SurroundingRectangle(testes[1], color=GREEN_RCS, buff=0.25, stroke_width=8)
        self.play(Create(caixa))
        self.wait(1)

        conclusao = Tex(r"$\Rightarrow (x-2)$ é fator!", font_size=80, color=GREEN_RCS)
        conclusao.next_to(testes, DOWN, buff=0.7)
        self.play(Write(conclusao))
        self.wait(2)

        # ==================== 4. BRIOT-RUFFINI LIMPO E ANIMADO ====================                
        self.play(FadeOut(grupo_div, testes, caixa, conclusao))
        self.wait(0.6)

        # Título
        titulo_br = Tex("Dispositivo Prático de Briot-Ruffini", font_size=88, color=YELLOW)
        titulo_br.move_to(UP*6)
        self.play(Write(titulo_br))
        self.wait(1.2)

        # Estrutura inicial
        coef = MathTex("1", r"\;-5", r"\;\;6", font_size=96)
        coef.arrange(RIGHT, buff=5.8).move_to(UP*2.8)

        linha = Line(start=LEFT*8.5, end=RIGHT*8.5).next_to(coef, DOWN, buff=0.3)
        
        # Linha de resultados (vai sendo preenchida)
        resultado = VGroup(
            MathTex("1", font_size=96),
            MathTex("?", font_size=96),
            MathTex("?", font_size=96)
        ).arrange(RIGHT, buff=5.8)
        resultado.next_to(linha, DOWN, buff=1.4)

        self.play(Write(coef), Create(linha), Write(resultado[0]))
        self.wait(1.5)

        # ==================== PASSO 1 ====================
        mult1 = MathTex(r"1 \times 2 = 2", font_size=86, color=YELLOW)
        mult1.next_to(resultado[0], UP, buff=0.4).shift(RIGHT*1.8)
        
        raiz = MathTex("2", font_size=96, color=BLUE)
        raiz.next_to(mult1, DOWN, buff=1.8)

        seta1 = Arrow(raiz.get_top(), mult1.get_bottom(), color=BLUE, stroke_width=8, buff=0.2)

        self.play(Create(seta1), Write(mult1), Write(raiz))
        self.wait(1.4)        

        # Baixa o 2 (temporário)
        dois_temp = MathTex("2", font_size=96, color=YELLOW)
        dois_temp.move_to(resultado[1].get_center() + UP*0.8)

        self.play(
            FadeOut(mult1), FadeOut(seta1), FadeOut(raiz),
            TransformFromCopy(mult1[-1], dois_temp)  # copia o "2"
        )
        self.wait(0.8)

        # Soma -5 + 2 = -3
        soma1 = MathTex(r"-5 + 2 = -3", font_size=86, color=GREEN)
        soma1.next_to(coef[1], DOWN, buff=1.8)

        self.play(Write(soma1))
        self.wait(1.4)

        # Resultado final do passo 1
        menos3 = MathTex("-3", font_size=96, color=WHITE)
        menos3.move_to(resultado[1])

        self.play(
            FadeOut(dois_temp), FadeOut(soma1),
            TransformFromCopy(soma1[-2:], menos3),
            resultado[1].animate.become(menos3)
        )
        self.wait(1)

        # ==================== PASSO 2 ====================
        mult2 = MathTex(r"-3 \times 2 = -6", font_size=86, color=YELLOW)
        mult2.next_to(resultado[1], UP, buff=0.4).shift(RIGHT*2)
        
        raiz.next_to(mult2, DOWN, buff=1.8) 

        seta2 = Arrow(raiz.get_top(), mult2.get_bottom(), color=BLUE, stroke_width=8, buff=0.2)

        self.play(Create(seta2), Write(mult2), Write(raiz))
        self.wait(1.4)

        # Baixa o -6 (temporário)
        menos6_temp = MathTex("-6", font_size=96, color=YELLOW)
        menos6_temp.move_to(resultado[2].get_center() + UP*0.8)

        self.play(
            FadeOut(mult2), FadeOut(seta2), FadeOut(raiz),
            TransformFromCopy(mult2[-2:], menos6_temp)
        )
        self.wait(0.8)

        # Soma final 6 + (-6) = 0
        soma_final = MathTex(r"6 + (-6) = 0", font_size=86, color=GREEN)
        soma_final.next_to(coef[2], DOWN, buff=1.8).shift(LEFT*2.2)

        self.play(Write(soma_final))
        self.wait(1.6)

        # ZERO FINAL COM DESTAQUE FORTE
        zero = MathTex("0", font_size=96, color=GREEN)
        zero.move_to(resultado[2])

        caixa_zero = SurroundingRectangle(zero, color=GREEN, buff=0.4, stroke_width=14, corner_radius=0.2)

        self.play(
            FadeOut(menos6_temp),
            FadeOut(soma_final),
            TransformFromCopy(soma_final[-1], zero),
            resultado[2].animate.become(zero),
            Create(caixa_zero),
            run_time=1.6
        )
        self.wait(2)

        # Conclusão
        conclusao = Tex(r"Resto = 0 $\Rightarrow$ $x=2$ é raiz da equação!", 
                        font_size=78, color=GREEN)
        conclusao.next_to(resultado, DOWN, buff=1.4)

        self.play(Write(conclusao))
        self.wait(3)
        self.play(FadeOut(conclusao))

        # ==================== CONCLUSÃO DO BRIOT-RUFFINI ====================
        
        # Depois que o zero já apareceu com a caixa verde...

        self.wait(0.5)

        # Destaca o quociente
        quociente = VGroup(resultado[0], resultado[1]).copy()
        caixa_quoc = SurroundingRectangle(quociente, color=TEAL, buff=0.4, stroke_width=10)

        quociente_texto = MathTex(r"x - 3", font_size=96, color=TEAL)
        quociente_texto.move_to(quociente.get_center())
        
        self.play(quociente_texto.animate.shift(DOWN*1.5))

        self.play(Create(caixa_quoc))
        self.wait(1.2)

        self.play(
            Transform(quociente, quociente_texto),
            run_time=1.2
        )
        self.wait(1)

        # Conclusão final poderosa
        fatoracao_final = MathTex(
            r"x^2 - 5x + 6 =",
            r"(x-2)",
            r"(x-3)",
            font_size=92
        )
        fatoracao_final[1].set_color(BLUE)
        fatoracao_final[2].set_color(TEAL)
        fatoracao_final.to_edge(DOWN, buff=1.2)
        
        fatoracao_final.next_to(quociente_texto, DOWN, buff=0.5).shift(RIGHT*2.5)
        
        self.play(FadeOut(quociente_texto))

        self.play(Write(fatoracao_final))
        self.wait(3)

        # Mensagem que todo aluno precisa ouvir
        mensagem = Tex(
            r"O Briot-Ruffini não só confirma a raiz,\\",
            r"como também informa o fator da outra raiz!",
            font_size=68, color=YELLOW
        )
        mensagem.next_to(fatoracao_final, DOWN, buff=0.6)

        self.play(Write(mensagem))
        self.wait(4)               
        
        # ==================== 5. Resultado final ====================
        self.play(FadeOut(*self.mobjects), run_time=1.5)
        final = MathTex(r"x^2 - 5x + 6", r"\;=\;", r"(x-2)(x-3)", font_size=90)
        final[2].set_color(GOLD)
        final.move_to(UP*8)

        self.play(Write(final))
        self.wait(2)

        raizes = MathTex(r"x=2", r"\quad ou \quad", r"x=3", font_size=95, color=GOLD)
        raizes.next_to(final, DOWN, buff=1.0)
        self.play(Write(raizes))
        self.wait(3.5)

        # ==================== 6. Tela final ====================
        self.play(FadeOut(*self.mobjects), run_time=1.5)

        fim = VGroup(
            Tex(r"Resolvido com sucesso!", font_size=96, color=TEAL),
            Tex(r"Usando teste de divisores + Briot-Ruffini", font_size=52, color=YELLOW)
        ).arrange(DOWN, buff=0.7)
        fim.center().shift(UP*0.6)

        self.play(Write(fim), run_time=2)
        self.wait(5)
        