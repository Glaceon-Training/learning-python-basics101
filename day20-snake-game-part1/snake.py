import turtle as t
STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    # Snake has attribute body as a list, spawn at start, and has a head.
    # Why the color and shape attribute is not at __init__ is because it is also used to extend body when
    # the snake eats the food.
    def __init__(self):
        self.body = []
        self.spawn()
        self.head = self.body[0]

    """Creating snake body of 3 segments in starting point"""
    def spawn(self):
        for position in STARTING_POS:
            self.add_segment(position)

    # Snake can add their body segment. Derivatively to spawn at start (spawn()) and
    # add segment when eating food (add_body())
    def add_segment(self, position):
        new_body = t.Turtle("square")
        new_body.color("white")
        new_body.penup()
        new_body.goto(position)
        self.body.append(new_body)

    def add_body(self):
        self.add_segment(self.body[-1].position())

    """Making the snake moving from last to head body segment move"""
    # Range(Start, Stop, Step): Moving from last index toward head as first index.
    # New X of index 2 go to index 1 (of length of 3 body part at start, thus 2-1), so is New Y.
    # So then body at index 2 move to body at index 1.
    # The head will move forward at distance 20 so that the rest of the body will follow.
    def move(self):
        for bod_num in range(len(self.body) - 1, 0, -1):
            new_x = self.body[bod_num - 1].xcor()
            new_y = self.body[bod_num - 1].ycor()
            self.body[bod_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    """Controlling the snake movement with arrow pads"""
    # Snake can go up, left, down, or right. With direction as global variable above.
    # A constraint is created: if the heading is going left, snake can not turn right.
    # Instead, it can turn up or down.
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
