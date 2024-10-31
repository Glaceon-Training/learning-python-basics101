from turtle import Screen
from snake import Snake
import time

# Setting up screen of game
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My First Snake Game!")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

# The while loop of the game
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
