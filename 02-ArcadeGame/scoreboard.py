from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update_score()

    def update_score(self):
        self.clear()  # to prevent overwriting previous score
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Arial", 60, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Arial", 60, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()


