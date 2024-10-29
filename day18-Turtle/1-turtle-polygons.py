import turtle as t
import random

# Drawing  3 to 10 sided polygons with random pencolor

timmy = t.Turtle()
side = 3
colors = ["aquamarine3", "cadetblue", "bisque4", "brown", "darkviolet", "midnightblue"]

while side <= 10:
    t.pencolor(random.choice(colors))
    for _ in range(side):
        t.forward(100)
        t.right(360/side)
    side += 1

screen = t.Screen()
screen.exitonclick()
