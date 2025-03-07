from turtle import Turtle
import random

COLORS = ["red","orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE



    def create_car(self):
        chance = random.randint(1, 6)
        if chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.pencolor("black")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.goto(280, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.speed)

        self.all_cars = [car for car in self.all_cars  if car.xcor() > -320]


    def increase_speed(self):
        self.speed += MOVE_INCREMENT



