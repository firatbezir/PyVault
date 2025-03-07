import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


# Create the turtle
turtle = Player()

# Create Scoreboard
score = Scoreboard()

# Create a car
car_manager = CarManager()

# Listen the screen
screen.listen()
screen.onkey(turtle.move_forward, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Create random cars:
    car_manager.create_car()
    car_manager.move()

    # Move turtle to original position, increase the level and speed of cars
    if turtle.ycor() > FINISH_LINE_Y:
        turtle.move_original_location()
        score.increase_level()
        car_manager.increase_speed()

    # Manage the collision with cars
    for car in car_manager.all_cars:
        if turtle.distance(car) < 20:
            score.end_the_game()
            game_is_on = False

screen.exitonclick()