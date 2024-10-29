import turtle as t
import random

# Drawing full-colored random walk

timmy = t.Turtle()
colors = ["light slate gray", "navy", "pale turquoise", "teal", "light green", "khaki", "wheat", "orange", "tomato",
          "pink", "plum", "medium purple"]
t.width(6)
t.speed(9)
direction = [0, 90, 180, 270]

for _ in range(200):
    t.pencolor(random.choice(colors))
    t.forward(20)
    t.setheading(random.choice(direction))

screen = t.Screen()
screen.exitonclick()
