from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.penup()
        self.move_forward()
        self.setpos(STARTING_POSITION)


    def move_forward(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.sety(new_y)

    def move_original_location(self):
        self.setpos(STARTING_POSITION)
