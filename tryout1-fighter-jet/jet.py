from turtle import Turtle
MOVE_DISTANCE = 10


class Jet(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.goto(-300, 0)
