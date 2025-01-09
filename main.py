from turtle import Screen
from paddle import Paddle

WIDTH = 800
HEIGHT = 600

screen = Screen()
screen.setup(width= WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

paddle1 = Paddle(365)
paddle2 = Paddle(-370)

screen.listen()
screen.onkey(paddle1.move_up, "Up")
screen.onkey(paddle1.move_down, "Down")

screen.onkey(paddle2.move_up, "w")
screen.onkey(paddle2.move_down, "s")

game_is_on = True
while game_is_on:
    screen.update()


screen.exitonclick()
