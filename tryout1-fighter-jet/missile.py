from turtle import Turtle
from jet import Jet
MOVE_DISTANCE = 10


class Missile(Jet):
    def __init__(self):
        super().__init__()
        self.missiles = []
        self.dx = 5

    def spawn_missile(self):
        new_m = Turtle()
        new_m.penup()
        new_m.shape("square")
        new_m.color("white")
        new_m.shapesize(stretch_wid=0.2, stretch_len=0.8)
        new_m.goto(self.xcor()+10, self.ycor())
        self.missiles.append(new_m)

    def start_shoot(self):
        self.spawn_missile()

    def missile_move(self):
        for bullet in range(len(self.missiles)):
            x = self.missiles[bullet].xcor() + self.dx
            self.missiles[bullet].goto(x, self.missiles[bullet].ycor())

    def move_up(self):
        y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), y)

    def move_down(self):
        y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), y)
