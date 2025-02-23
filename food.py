from turtle import Turtle
import random

class Food(Turtle):
    """Handles food creation and movement"""
    
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Make food smaller
        self.color("blue")
        self.speed("fastest")  # Instant appearance
        self.refresh()
        
    def refresh(self):
        """Move food to random position on screen"""
        random_x = random.randint(-260, 260)
        random_y = random.randint(-260, 240)
        self.goto(random_x, random_y)