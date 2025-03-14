from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("./externalfiles/data.txt") as data:
            self.highscore = int(data.read())
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 275)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > int(self.highscore):
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_score()


    def increase_the_score(self):
        self.score += 1
        self.update_score()