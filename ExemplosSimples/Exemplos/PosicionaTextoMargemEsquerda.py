# blockchain_intro_manim.py
# Rode com: manim -pqh -r 1080,1082 PosicionaTextoMargemEsquerda.py BlockchainIntro

from manim import *
import os

class BlockchainIntro(Scene):
    def construct(self):
        # ==================== CONFIGURAÇÃO VERTICAL 1080x1082 ====================
        self.camera.background_color = "#0f172a"  # azul-escuro elegante
        self.camera.frame_width = 10.0
        self.camera.frame_height = 12.0  # Vertical quase quadrado
        
        metade_largura=self.camera.frame_width/2
        metade_altura=self.camera.frame_height/2
        
        # Cores personalizadas (você adicionou)
        CYAN = "#00FFFF"
        
        print(UL)
        print(DR)
        
        print("Largura em unidades Manim :", self.camera.frame_width)
        print("Altura em unidades Manim  :", self.camera.frame_height)
        print(f"Proporção → {self.camera.frame_width / self.camera.frame_height:.3f}:1")

        # Pixels finais (config é global, funciona em qualquer lugar)
        print(f"Pixels → {config.pixel_width} × {config.pixel_height}")
        print(f"Proporção pixels → {config.pixel_width / config.pixel_height:.3f}:1\n")

        # === TÍTULO GIGANTE E ANIMADO ===
        
        titulo = Text("Posiciona texto na margem esquerda", font_size=36, color="#58a6ff")
        tam_titulo=titulo.width
        titulo.move_to(UP*(metade_altura-0.6)+LEFT*(metade_largura-tam_titulo/2))
        self.add(titulo)

        print("Esq:",titulo.get_left(),", topo:", titulo.get_top(),", direita:",titulo.get_right(),", baixo:",titulo.get_bottom()) 
        self.play(titulo.animate.shift(DOWN*10)) 