from turtle import Screen
from food import Food
from scoreboard import ScoreBoard
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# TODO: Create Snake Body
snake = Snake()
food = Food()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake. left, "a")
screen.onkey(snake.right, "d")


game_is_on = True
while game_is_on:
    screen.update() # REFRESH THE SCREEN
    time.sleep(0.1) # DELAY THE REFRESH
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_the_score()

    # Detect collision with wall.
    if (snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or
            snake.head.ycor() < -290):
        scoreboard.reset_score()
        snake.reset_snake()


    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset_score()
            snake.reset_snake()


screen.exitonclick()