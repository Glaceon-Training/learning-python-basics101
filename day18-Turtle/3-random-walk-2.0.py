import turtle as t
import random

# Drawing random-colored random walk

timmy = t.Turtle()
t.colormode(255)


# Creating a function to generate random color of RGB while in COLORMODE(255) and return it into pencolor for turtle
def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return t.pencolor(r, g, b)


t.width(6)
t.speed(9)
direction = [0, 90, 180, 270]

for _ in range(200):
    random_colors()
    t.forward(20)
    t.setheading(random.choice(direction))

screen = t.Screen()
screen.exitonclick()
