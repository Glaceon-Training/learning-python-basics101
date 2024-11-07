from turtle import Screen
# from jet import Jet
from missile import Missile
from enemies import Enemies
from jet_scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Space Impact")
screen.setup(width=800, height=600)
screen.tracer(0)

missile = Missile()
enemies = Enemies()
score = Scoreboard()

screen.listen()
screen.onkeypress(fun=missile.move_up, key="Up")
screen.onkeypress(fun=missile.move_down, key="Down")
screen.onkey(fun=missile.start_shoot, key="Right")

is_game_on = True
while is_game_on:
    time.sleep(0.05)
    screen.update()
    enemies.spawn_enemies()
    missile.missile_move()
    enemies.enemy_move()

    for enemy in enemies.troops:
        for bullet in missile.missiles:
            if bullet.distance(enemy) < 30:
                enemy.goto(-400, -300)
                enemy.hideturtle()
                score.add_score()

screen.exitonclick()
