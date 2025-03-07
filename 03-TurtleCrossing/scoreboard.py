from turtle import Turtle

FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.initial_level = 1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-210, 260)
        self.write(f"Level - {self.initial_level}", align="center", font=FONT)

    def increase_level(self):
        self.initial_level += 1
        self.update_score()

    def end_the_game(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)




