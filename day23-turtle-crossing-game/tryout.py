import time
from turtle import Screen, Turtle
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.title("My First Turtle Crossing Game")
screen.tracer(0)

PLAYER = []
CARS = []
SCORE = []
LEVEL = 1
STARTING_POS = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
CAR_COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
CAR_STARTING_MOVE_DISTANCE = 5
CAR_MOVE_INCREMENT = 10  # car move increase everytime level up
FONT = ("Courier", 24, "normal")


def create_player():  # player
    player = Turtle("turtle")
    player.penup()
    player.setheading(90)
    player.goto(STARTING_POS)
    PLAYER.append(player)


def player_forward():  # player
    PLAYER[-1].forward(MOVE_DISTANCE)


def create_cars():  # car manager
    car = Turtle("square")
    car.penup()
    car.color(random.choice(CAR_COLORS))
    car.shapesize(stretch_wid=0.8, stretch_len=2)
    car.goto(300, random.randint(-250, 250))
    CARS.append(car)


def car_movement():  # car manager
    for unit in range(len(CARS)):
        x = CARS[unit].xcor() - CAR_STARTING_MOVE_DISTANCE
        CARS[unit].goto(x, CARS[unit].ycor())


def scoreboard():  # scoreboard
    score = Turtle()
    score.penup()
    score.color("black")
    score.hideturtle()
    score.goto(-290, 260)
    SCORE.append(score)
    update_score()


def update_score():  # scoreboard
    SCORE[-1].write(f"Level: {LEVEL}", align="left", font=FONT)


def add_score():  # scoreboard
    global LEVEL
    global CAR_STARTING_MOVE_DISTANCE
    global CAR_MOVE_INCREMENT
    LEVEL += 1
    SCORE[-1].clear()
    update_score()
    CAR_STARTING_MOVE_DISTANCE += CAR_MOVE_INCREMENT
    # car increment in car manager


def game_over():  # scoreboard
    SCORE[-1].home()
    SCORE[-1].write(f"Game Over.", align="center", font=FONT)


def detect_crash():  # outside module
    for unit in range(len(CARS)):
        if PLAYER[-1].distance(CARS[unit]) < 20:
            game_over()
            global is_game_on
            is_game_on = False


def game_start():
    create_player()
    create_cars()
    scoreboard()


screen.listen()
screen.onkey(fun=player_forward, key="Up")

PLAYER.clear()
CARS.clear()
SCORE.clear()

game_start()
is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    car_movement()
    detect_crash()

    if CARS[-1].xcor() == 100:
        create_cars()

    if PLAYER[-1].ycor() == FINISH_LINE_Y:
        add_score()
        PLAYER[-1].goto(STARTING_POS)

    if LEVEL > 1:
        create_cars()

screen.exitonclick()