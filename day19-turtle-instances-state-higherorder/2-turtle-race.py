import turtle as t
import random

# Creating turtle race game in turtle module
screen = t.Screen()
screen.setup(width=500, height=400)

is_race_on = False
user_bet = screen.textinput(title="Make a bet!", prompt="Who will win the race? Enter your color: ")
color = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []


def spawn_turtles():
    y = [-80, -50, -20, 20, 50, 80]
    for turtle in range(len(color)):
        new_turtle = t.Turtle(shape="turtle")
        new_turtle.color(color[turtle])
        new_turtle.penup()
        new_turtle.goto(x=-240, y=y[turtle])
        turtles.append(new_turtle)


if user_bet:
    is_race_on = True
    spawn_turtles()

while is_race_on:
    for racer in turtles:
        if racer.xcor() > 220:
            is_race_on = False
            winner = racer.pencolor()
            if winner == user_bet:
                print(f"You've won! The winner is {winner}.")
            else:
                print(f"You've lost. The winner is {winner}.")
        random_distance = random.randint(0, 10)
        racer.forward(random_distance)

screen.exitonclick()
