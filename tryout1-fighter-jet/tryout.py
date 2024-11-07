from turtle import Screen, Turtle
import random
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

troops = []
missiles = []
troops_hit = []
score = 0


def r_spawn():
    enemies = Turtle("circle")
    enemies.penup()
    enemies.color("red")
    enemies.goto(300, random.randint(-100, 100))
    enemies.dx = -5
    troops.append(enemies)


def mis_spawn(x, y):
    missile = Turtle("square")
    missile.penup()
    missile.color("white")
    missile.shapesize(stretch_len=0.8, stretch_wid=0.2)
    missile.goto(-300, 0)
    missile.dx = 5
    missile.dy = 5
    missiles.append(missile)
    missile.goto(x, y)


def r_move():
    for a in range(len(troops)):
        x = troops[a].xcor() + troops[a].dx
        troops[a].goto(x, troops[a].ycor())


def l_move():
    for b in range(len(missiles)):
        x = missiles[b].xcor() + missiles[b].dx
        missiles[b].goto(x, missiles[b].ycor())


def mis_lastpos():
    x = -300
    y = missiles[-1].ycor()
    mis_spawn(x, y)


def l_moveup():
    y = missiles[-1].ycor() + missiles[-1].dy
    missiles[-1].goto(missiles[-1].xcor(), y)


def l_movedown():
    y = missiles[-1].ycor() - missiles[-1].dy
    missiles[-1].goto(missiles[-1].xcor(), y)


def calc_occur():
    for hit in range(len(troops)):
        for bullet in range(len(missiles)):
            if missiles[bullet].distance(troops[hit]) < 10:
                print("Hit!")
                new_hit = troops[hit]
                troops_hit.append(new_hit)
                global score
                score += 1
                print(f"Your current score: {score}")


def enemy_destroyed():
    for fallen in range(len(troops_hit)):
        troops_hit[fallen].hideturtle()
        troops_hit[fallen].goto(-300, -300)
        if troops_hit[fallen].xcor() < -300:
            troops_hit.pop()


screen.listen()
screen.onkey(fun=mis_lastpos, key="Right")
screen.onkeypress(fun=l_moveup, key="Up")
screen.onkeypress(fun=l_movedown, key="Down")

is_game_on = True
troops.clear()
missiles.clear()
troops_hit.clear()
r_spawn()
mis_spawn(-300, 0)
while is_game_on:
    screen.update()
    time.sleep(0.05)
    r_move()
    l_move()

    if troops[-1].xcor() < 200:
        r_spawn()

    calc_occur()
    enemy_destroyed()

screen.exitonclick()
