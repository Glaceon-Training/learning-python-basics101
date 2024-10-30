import turtle as t
import random

# Drawing full-colored random walk

timmy = t.Turtle()
colors = ["light slate gray", "navy", "pale turquoise", "teal", "light green", "khaki", "wheat", "orange", "tomato",
          "pink", "plum", "medium purple"]
timmy.width(6)
timmy.speed(9)
direction = [0, 90, 180, 270]

for _ in range(200):
    timmy.pencolor(random.choice(colors))
    timmy.forward(20)
    timmy.setheading(random.choice(direction))

screen = t.Screen()
screen.exitonclick()
