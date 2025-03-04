from turtle import Screen
from paddle import Paddle
from ball import  Ball
from scoreboard import ScoreBoard
import time

WIDTH = 800
HEIGHT = 600
STARTING_POSITION_R = (350, 0)
STARTING_POSITION_L = (-350, 0)
BACKGROUND = 'black'

# Create the screen
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor(BACKGROUND)
screen.title("Pong")
screen.tracer(0) # controls the animation, to turn off; tracer(0)


# Create the paddle
r_paddle = Paddle(STARTING_POSITION_R)
l_paddle = Paddle(STARTING_POSITION_L)

# Create the ball
ball = Ball()

# Create the ScoreBoard
score = ScoreBoard()


# Listen the Screen
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")




game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect the collision with top and bottom wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # Detect the collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and
            ball.xcor() < -320) :
        ball.bounce_x()

    # Detect when  right paddle misses
    if ball.xcor() > 380 :
        ball.reset_position()
        score.l_point()


    # Detect when  right paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()