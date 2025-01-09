from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
WIDTH = 5
LENGTH = 1

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=WIDTH, stretch_len=LENGTH)
        self.penup()
        self.goto(position, 0)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)