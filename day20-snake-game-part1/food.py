from turtle import Turtle
import random

NEGATIVE_LIMIT = -260
POSITIVE_LIMIT = 260


class Food(Turtle):
    # Food is a subclass from Turtle class of turtle module.
    # The food is declared its shape and color in its attribute because the only function it has is random spawn
    # and has only one "segment".
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed(0)
        self.random_spawn()

    # The spawn area is specified between -270 to 270 of screen pixels. Not too close to wall.
    def random_spawn(self):
        random_x = random.randint(a=NEGATIVE_LIMIT, b=POSITIVE_LIMIT)
        random_y = random.randint(a=NEGATIVE_LIMIT, b=POSITIVE_LIMIT)
        self.goto(random_x, random_y)
