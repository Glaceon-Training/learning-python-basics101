import turtle as t
import random

# Creating spirograph of random colors
timmy = t.Turtle()
t.colormode(255)
timmy.speed(0)
heading = 0


# Function to create random colors
def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return timmy.pencolor(r, g, b)


is_turtle_drawing = True
while is_turtle_drawing:
    random_colors()
    timmy.setheading(heading)
    timmy.circle(100)
    heading += 5
    if heading == 360:
        is_turtle_drawing = False


screen = t.Screen()
screen.exitonclick()
