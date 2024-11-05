from turtle import Turtle
MOVE_DISTANCE = 20


class Racket(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(position)

    def up(self):
        y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), y)

    def down(self):
        y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), y)
