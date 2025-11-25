# FormulaQuadraticaBhaskara.py
# manim -pqh -r 648,1080 FormulaQuadraticaBhaskara-Introducao.py FormulaBhaskaraIntroducao para testes rápidos
# manim -pqh -r 1296,2160 FormulaQuadraticaBhaskara-Introducao.py FormulaBhaskaraIntroducao para versao producao

from manim import *

class FormulaBhaskaraIntroducao(Scene):
    def construct(self):
        self.camera.background_color = "#0d1117"  # fundo escuro bonito
        def to_exact_top(mobj):
            mobj.to_edge(UP)
            #print(mobj.get_top()[1])            
            mobj.shift(UP * (mobj.get_top()[1]+4))
            #print(UP * (mobj.get_top()[1]+4))

      
        # ==================== TÍTULO ====================

        titulo1 = Text("Fórmula Quadrática", font_size=64, color=TEAL, weight=BOLD)
        titulo2 = Text("(Fórmula de Bháskara)", font_size=58, color=TEAL, weight=BOLD)

        # Subtítulos
        subtitulo1 = Text(
            "Dedução por Completação do Quadrado",
            font_size=42,
            color=BLUE_B,
            weight=BOLD
        )
        subtitulo2 = Text(
            "e outros métodos de solução",
            font_size=42,
            color=BLUE_B,
            weight=BOLD
        )

        # Agrupando e posicionando
        titulo_group = VGroup(titulo1, titulo2).arrange(DOWN, buff=0.3).shift(UP * 3.5)

        subtitulo_group = VGroup(subtitulo1, subtitulo2).arrange(DOWN, buff=0.5)
        subtitulo_group.next_to(titulo_group, DOWN, buff=1.2)

        # Grupo completo (opcional, facilita fade out)
        intro_group = VGroup(titulo_group, subtitulo_group)

        # Animações
        self.play(Write(titulo_group), run_time=1.2)
        self.play(Write(subtitulo_group), run_time=1)
        self.wait(2)
        self.play(FadeOut(intro_group, shift=DOWN*0.5), run_time=0.8)
        self.wait(0.5)               

        # ==================== EQUAÇÃO GERAL ====================
        t1 = MathTex(r"\text{Equação do } 2^\circ \text{ grau}", font_size=68, color=YELLOW).shift(UP*6.5)
        eq_geral = MathTex(r"ax^2 + bx + c = 0", font_size=90).next_to(t1, DOWN, buff=0.8)        
        t2 = MathTex(r"a, b, c \in \mathbb{R} \quad ; \quad a \neq 0", font_size=46).next_to(eq_geral, DOWN, buff=0.4)

        self.play(Write(t1), Write(eq_geral), Write(t2))
        self.wait(3)
        self.play(FadeOut(t1, eq_geral, t2))        
       

        # ==================== MÉTODOS ====================
        tituloMetodos = Text("Métodos de solução da eq. 2º grau:", font_size=54, color=GOLD).shift(UP*6)
        apresentaremos = Text ("Neste vídeo, apresentaremos:", font_size=48, color=RED_E).next_to(tituloMetodos, DOWN, buff=1.2)        
        metodos = BulletedList(            
            "Completação do quadrado (exemplo)",
            "Fórmula de Bháskara (dedução)",
            "Soma e produto (exemplos)",
            "Fatoração (exemplos)",
            font_size=60, buff=0.5
        ).next_to(apresentaremos, DOWN, buff=0.4)
        self.play(FadeIn(tituloMetodos, apresentaremos, metodos))
        self.wait(2)
        
        for metodo in range (4):
            box = SurroundingRectangle(metodos[metodo], color=ORANGE, buff=0.25)
            self.play(Create(box))
            self.wait(2)
            self.play(FadeOut(box))    

        self.play(FadeOut(tituloMetodos, apresentaremos, metodos))            

        # ==================== COMPLETAÇÃO DO QUADRADO - TEORIA ====================
        titulo_comp = Text("Método de Completar o Quadrado", font_size=56, color=BLUE).shift(UP*6)
        self.play(Write(titulo_comp))
            
        leg = Tex("Binômio de Newton (n=2)", font_size=50).next_to(titulo_comp, DOWN, buff=0.8)
        binomio = MathTex(r"(a + b)^2 = a^2 + 2ab + b^2", font_size=72).next_to(leg, DOWN, buff=0.5)
        
        self.play(Write(leg), Write(binomio))
        self.wait(0.4)
                
        # ==================== ILUSTRAÇÃO GEOMÉTRICA ====================
        # Quadrado grande de lado (a + b) = 3.0 unidades (valor arbitrário, mas proporcional)
        lado = 4.0
        a = 2.5   # comprimento do lado "a"
        b = lado - a  # = 1.5 (lado "b")

        geo = VGroup()

        # 1) Quadrado grande a² (azul)
        quadrado_a = Square(side_length=a, color=BLUE_D, fill_opacity=0.8).move_to(LEFT*b/2 + DOWN*b/2)

        # 2) Retângulo horizontal a×b (amarelo)
        ret_h = Rectangle(width=a, height=b, color=YELLOW_E, fill_opacity=0.8)
        ret_h.next_to(quadrado_a, UP, buff=0).align_to(quadrado_a, LEFT)

        # 3) Retângulo vertical a×b (verde)
        ret_v = Rectangle(width=b, height=a, color=GREEN_E, fill_opacity=0.8)
        ret_v.next_to(quadrado_a, RIGHT, buff=0).align_to(quadrado_a, UP)

        # 4) Quadradinho b² (vermelho)
        quadrado_b = Square(side_length=b, color=RED_E, fill_opacity=0.9)
        quadrado_b.next_to(ret_h, RIGHT, buff=0)
        quadrado_b.next_to(ret_v, UP, buff=0)

        # 5) Rótulos "a" e "b"
        label_a = Tex("a", font_size=64, color=WHITE).move_to(quadrado_a.get_center() + LEFT*0.5)
        label_b = Tex("b", font_size=64, color=WHITE).move_to(quadrado_b.get_center() + RIGHT*0.3 + UP*0.3)
   
        geo.add(quadrado_a, ret_h, ret_v, quadrado_b, label_a, label_b)
        geo.next_to(binomio, DOWN, buff=0.8)  

        self.play(FadeIn(geo, scale=6.0), run_time=0.6)
        self.wait(3)
        self.play(FadeOut(titulo_comp, leg, binomio, geo))

