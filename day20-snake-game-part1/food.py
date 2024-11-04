from turtle import Turtle
import random


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
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)
