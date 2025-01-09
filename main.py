from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

WIDTH = 800
HEIGHT = 600

screen = Screen()
screen.setup(width= WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
move = 10

paddle_r = Paddle(365)
paddle_l = Paddle(-365)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_r.move_up, "Up")
screen.onkey(paddle_r.move_down, "Down")

screen.onkey(paddle_l.move_up, "w")
screen.onkey(paddle_l.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with paddles
    if ball.distance(paddle_r) < 50 and ball.xcor() > 330 or ball.distance(paddle_l) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    #Detect collision with walls behind paddles
    if ball.xcor() > 340:
        ball.reset_ball()
        scoreboard.l_point()

    if ball.xcor() < -340:
        ball.reset_ball()
        scoreboard.r_point()


screen.exitonclick()
