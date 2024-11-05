from turtle import Turtle
BALL_UPPER_BORDER = 280
BALL_BOTTOM_BORDER = -280
BALL_SPEED = ["slowest", "slow", "normal", "fast", "fastest"]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.dx = -5
        self.dy = -5
        self.ball_speed = 0.1

    def move(self):
        x = self.xcor() + self.dx
        y = self.ycor() + self.dy
        self.goto(x, y)
        if self.ycor() < BALL_BOTTOM_BORDER or self.ycor() > BALL_UPPER_BORDER:
            self.dy *= -1

    def bounce_horizontally(self):
        self.dx *= -1
        self.ball_speed *= 0.9

    def reset_position(self):
        self.home()
        self.ball_speed = 0.1
        self.dx *= -1
        self.dy *= -1
