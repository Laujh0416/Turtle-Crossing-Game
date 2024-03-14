from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-280, 270)
        self.color("black")
        self.score = 0
        self.update()
    
    def score_num(self):
        self.clear()
        self.score += 1
        self.update()

    def update(self):
        self.write(f"Level: {self.score}", align="left", font=("Arial", 10, "normal"))
    
    def game_over(self):
        self.goto(-5,0)
        self.color('white')
        self.write(f"GAME OVER", align="center", font=("Arial", 50, "normal"))

    def end_level_show(self):
        self.goto(-5, -30)
        self.color('white')
        self.write(f"End At Level: {self.score}", align="center", font=("Arial", 20, "normal"))
