from manim import *

class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency

        square = Square()  # create a square
        square.set_fill(BLUE, opacity=0.5)  # set the color and transparency

        square.next_to(circle, RIGHT, buff=0.5)  # set the position
        
        square2 = Square()  # create a square
        square2.set_fill(BLUE, opacity=0.5)  # set the color and transparency

        square2.next_to(circle, DOWN, buff=0.1)  # set the position
        
        
        self.play(Create(circle), Create(square), Create(square2))  # show the shapes on screen