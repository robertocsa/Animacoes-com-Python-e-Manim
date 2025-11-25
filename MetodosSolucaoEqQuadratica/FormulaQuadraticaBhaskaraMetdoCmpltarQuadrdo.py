# FormulaQuadraticaBhaskara.py
# manim -pqh -r 648,1080 FormulaQuadraticaBhaskaraMetdoCmpltar.py FormulaBhaskaraCompletarQuadrado para testes rápidos
# manim -pqh -r 1296,2160 FormulaQuadraticaBhaskaraMetdoCmpltar.py FormulaBhaskaraCompletarQuadrado para versao producao

from manim import *

class FormulaBhaskaraCompletarQuadrado(Scene):
    def construct(self):
        self.camera.background_color = "#0d1117"  # fundo escuro bonito
        def to_exact_top(mobj):
            mobj.to_edge(UP)
            #print(mobj.get_top()[1])            
            mobj.shift(UP * (mobj.get_top()[1]+4))
            #print(UP * (mobj.get_top()[1]+4))

        # ==================== TÍTULO ====================
        titulo = Text("Método de completar o quadrado", font_size=56, color=ORANGE)
        subtitulo = Text("(exemplo com explicações passo a passo)", font_size=42, color=YELLOW)
        VGroup(titulo, subtitulo).arrange(DOWN, buff=0.4).shift(UP*8.4)       
        self.play(Write(titulo), Write(subtitulo))

        # ==================== PASSOS MATEMÁTICOS ====================
        passos_math = VGroup(
            MathTex(r"x^{2} + 6x + 7 = 0", font_size=72, color=WHITE),
            
            # 1ª linha – caixinhas amarelas
            MathTex(
            r"x^{2} + 6x + {\boxed{\phantom{9}}} = -7 + {\boxed{\phantom{9}}}",
            substrings_to_isolate=[r"{\boxed{\phantom{9}}}"],
            font_size=72,
            color=WHITE ).set_color_by_tex(r"{\boxed{\phantom{9}}}", YELLOW),           

            # 2ª linha – (b/2)² em amarelo
            MathTex(r"x^{2} + 6x + {\left(\frac{b}{2}\right)^{2}} = -7 + {\left(\frac{b}{2}\right)^{2}}", 
            substrings_to_isolate=[r"{\left(\frac{b}{2}\right)^{2}}"], 
            font_size=72, color=WHITE).set_color_by_tex(r"{\left(\frac{b}{2}\right)^{2}}", YELLOW),

            # 3ª linha – (6/2)² = 9 em azul
            MathTex(r"x^{2} + 6x + {\left(\frac{6}{2}\right)^{2}} = -7 + {\left(\frac{6}{2}\right)^{2}}", 
            substrings_to_isolate=[r"{\left(\frac{6}{2}\right)^{2}}"], 
            font_size=72, color=WHITE).set_color_by_tex(r"{\left(\frac{6}{2}\right)^{2}}", BLUE),
            
            # 4ª linha
            MathTex(r"x^{2} + 6x + 9 = -7 + 9 ", substrings_to_isolate="9", font_size=72, color=WHITE).set_color_by_tex("9", BLUE),
            
            # 5ª linha
            MathTex(r"(x+3)^{2} = 2", font_size=72, color=GREEN),
            
            # 6ª linha
            MathTex(r"x+3 = \pm \sqrt{2}", font_size=72, color=TEAL),
            
            # 7ª linha
            MathTex(r"x = -3 \pm \sqrt{2}", font_size=72, color=TEAL)
        ).arrange(DOWN, buff=0.5).next_to(subtitulo, DOWN, 0.6)

        # ==================== EXPLICAÇÕES (texto) ====================
        explicacoes_texto = [
            Text("1. Partimos da equação x² + 6x + 7 = 0 (exemplo).\nPrecisamos encontrar um quadrado perfeito (x + ?)² \n"+
                 "equivalente à equação a resolver.", font_size=36, color=YELLOW, line_spacing=0.8 ),
            Text("2. Condição necessária para este método funcionar \n"+
                 "é que o coeficiente de x², o 'a' de ax², seja = 1.\n"+
                 "O 'a'=1 pode ser obtido dividindo-se todos os \n"+
                 "termos pelo valor de 'a'.", font_size=36, color=YELLOW, line_spacing=0.8),
            Text("3. Para completar o quadrado, precisamos \n"+
                 "adicionar (b/2)² nos dois lados", font_size=36, color=YELLOW, line_spacing=0.8),
            Text("4. Aqui b = 6, logo: (6/2)² = 3² = 9. \n"+
                 "Adicionamos, então, 9 dos dois lados", font_size=36, color=YELLOW, line_spacing=0.8),
            Text("5. Do produto notável (x+k)²=x²+2kx+k², temos que:\n"+
                 "x² + 6x + 9 = x² + 6x + 3² = (x+3)²", font_size=36, color=YELLOW, line_spacing=0.8),
            Text("6. Agora o lado esquerdo é um quadrado perfeito:\n"+
                 "(x+3)²!", font_size=36, color=YELLOW, line_spacing=0.8),
            Text("7. Tiramos a raiz quadrada dos dois lados\n"+
                 "para remover a potência de 2 à esquerda.\n"+
                 "Lembrando que as raízes quadradas resultam em\n"+
                 "valores positivos ou negativos (±)", font_size=36, color=YELLOW, line_spacing=0.8),
            Text("8. Chegamos à solução desta equação!", font_size=36, color=YELLOW, line_spacing=0.8)
        ]        
        
        # Alinha perfeitamente a primeira linha de cada explicação
        #explicacoes.align_to(explicacoes[0][0], UP)
        
        # antes do loop
        explicacao_atual = explicacoes_texto[0].next_to(passos_math, DOWN, buff=0.6)
        self.play(Write(passos_math[0]), FadeIn(explicacao_atual))
        self.wait(2)

        # dentro do loop
        for i in range(1, 8):
            nova_explicacao = explicacoes_texto[i].next_to(passos_math, DOWN, buff=0.6)
            if i<7:
                self.play(
                    TransformMatchingTex(passos_math[i-1].copy(), passos_math[i]),
                    ReplacementTransform(explicacao_atual, nova_explicacao),  # <-- troca limpa
                    #FadeIn(nova_explicacao),
                    #FadeOut(explicacao_atual),
                    run_time=2.0
                )
            else:
                self.play(
                Write(passos_math[i]), 
                ReplacementTransform(explicacao_atual, nova_explicacao), 
                run_time=2.0
                #Write(nova_explicacao), run_time=2.0)                
                #FadeOut(explicacao_atual),
                )
                
            explicacao_atual = nova_explicacao        

            # Tempos diferentes de espera para leitura
            if i == 1:  # quando aparece o 9                                
                self.wait(2)
            elif i == 7:  # solução final
                self.wait(3.5)
            else:
                self.wait(1.5)        
                
            #FadeOut(nova_explicacao)
        
        # Animação de descida suave: exatamente 1.2 vezes a própria altura
        self.play(
            passos_math[7].animate.shift(DOWN * passos_math[7].height * 1.2),
            FadeOut(explicacoes_texto[7]),
            #explicacao_atual.animate.shift(DOWN * passos_math[7].height * 1.2), 
            run_time=1.8,
            rate_func=smooth  # opcional: deixa mais fluido
        )

        # ==================== DESTAQUE FINAL ====================
        caixa = SurroundingRectangle(passos_math[7], color=YELLOW, buff=0.35, corner_radius=0.25)
        #passos_math[7].next_to(caixa, DOWN, 0.2)
        seta = Arrow(start=RIGHT*0.8, end=LEFT, color=YELLOW, max_tip_length_to_length_ratio=0.2)
        seta.next_to(caixa, RIGHT, buff=0.5)
        texto_final = Text("Solução!", color=YELLOW, font_size=38).next_to(seta, RIGHT)

        self.play(Create(caixa), GrowArrow(seta), Write(texto_final))
        self.wait(4)

        # ==================== FADE OUT ====================
        #self.play( FadeOut(VGroup(titulo, subtitulo, passos_math, explicacoes_texto, caixa, seta, texto_final)), run_time=0.25)
        # Limpeza final        
        self.play(FadeOut(*self.mobjects))
        
      