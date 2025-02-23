from turtle import Turtle

# Constants for score display
ALIGNMENT = "center"
FONT = ("Courier", 24, "bold ")

class ScoreBoard(Turtle):
    """Handles score tracking and display"""
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 250)  # Position score at top center
        self.update_scoreboard()
        self.hideturtle()  # Hide turtle cursor
    
    def update_scoreboard(self):
        """Refresh the displayed score"""
        self.write(f"Score:{self.score}", align=ALIGNMENT, font=FONT)
    
    def game_over(self):
        """Display game over message"""
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increment score and update display"""
        self.score += 1
        self.clear()
        self.update_scoreboard()


class Boundaryline(Turtle):
    """Borderline below user score"""
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(-295, 250)
        self.pendown()
        self.width(3)
        self.forward(585)
        self.right(90)
        self.forward(540)
        self.right(90)
        self.forward(587)
        self.right(90)
        self.forward(540)
        self.hideturtle()