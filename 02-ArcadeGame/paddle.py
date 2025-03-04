from turtle import Turtle

MOVE_DISTANCE = 20

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.penup()
        self.goto(position)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.sety(new_y)

    def down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.sety(new_y)
