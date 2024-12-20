from turtle import Turtle
STARTING_POS = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.player_go_to_start()

    def player_forward(self):
        self.forward(MOVE_DISTANCE)

    def finish(self):
        return self.ycor() == FINISH_LINE_Y

    def player_go_to_start(self):
        self.goto(STARTING_POS)
