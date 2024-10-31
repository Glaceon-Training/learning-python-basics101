import turtle as t
STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        self.body = []
        self.spawn()
        self.head = self.body[0]

    """Creating snake body of 3 segments in starting point"""
    def spawn(self):
        for position in STARTING_POS:
            self.add_segment(position)

    def add_segment(self, position):
        new_body = t.Turtle("square")
        new_body.color("white")
        new_body.penup()
        new_body.goto(position)
        self.body.append(new_body)

    def add_body(self):
        self.add_segment(self.body[-1].position())

    """Making the snake moving from last to head body segment move"""
    def move(self):
        for bod_num in range(len(self.body) - 1, 0, -1):
            new_x = self.body[bod_num - 1].xcor()
            new_y = self.body[bod_num - 1].ycor()
            self.body[bod_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    """Controlling the snake movement with arrow pads"""
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
