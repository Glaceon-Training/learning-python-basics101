from turtle import Screen
from snake import Snake
from food import Food
from snake_scoreboard import Scoreboard
import time

# Setting up screen of game
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My First Snake Game!")
screen.tracer(0)

# Calling all classes to used in game.
snake = Snake()
food = Food()
score = Scoreboard()

# Setting up key to move snake
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
    # If snake eat food, the food refresh its random position, add score, extend snake's body segment.
    if snake.head.distance(food) < 15:
        food.random_spawn()
        score.add_score()
        snake.add_body()

    # Detect if snake hits the wall, and goes Game Over.
    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        is_game_on = False
        score.game_over()

    # Detect if snake's head hit its own body. Goes Game Over if it happens.
    for segment in snake.body[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            score.game_over()

screen.exitonclick()
