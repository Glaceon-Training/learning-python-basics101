import turtle as t
from racket import Racket
from ball import Ball
from pong_scoreboard import Scoreboard
import time

screen = t.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My First Ping Pong Game")
screen.tracer(0)

l_racket = Racket((-350, 0))
r_racket = Racket((350, 0))
ball = Ball()
l_scoreboard = Scoreboard((-250, 200))
r_scoreboard = Scoreboard((250, 200))

screen.listen()
screen.onkey(fun=l_racket.up, key="w")
screen.onkey(fun=l_racket.down, key="s")
screen.onkey(fun=r_racket.up, key="Up")
screen.onkey(fun=r_racket.down, key="Down")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(ball.ball_speed)
    ball.move()

    if (ball.distance(l_racket) < 50 and ball.xcor() == -330) or (ball.distance(r_racket) < 50 and ball.xcor() == 330):
        ball.bounce_horizontally()

    if ball.xcor() < -380:
        r_scoreboard.add_score()
        ball.reset_position()
    elif ball.xcor() > 380:
        l_scoreboard.add_score()
        ball.reset_position()

    if l_scoreboard.score == 5:
        print("Left Win!")
        is_game_on = False
    elif r_scoreboard.score == 5:
        print("Right Win!")
        is_game_on = False

screen.exitonclick()
