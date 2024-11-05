import turtle as t

turtle = t.Turtle()
screen = t.Screen()
screen.tracer(10, 10)
dist = 2
for i in range(50):
    turtle.fd(dist)
    turtle.right(90)
    dist += 2

screen.exitonclick()