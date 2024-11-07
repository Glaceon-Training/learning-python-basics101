from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.starting_move_distance = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle("square")
            car.penup()
            car.color(random.choice(COLORS))
            car.shapesize(stretch_wid=0.8, stretch_len=2)
            car.goto(300, random.randint(-250, 250))
            self.cars.append(car)

    def car_movement(self):
        for unit in range(len(self.cars)):
            x = self.cars[unit].xcor() - self.starting_move_distance
            self.cars[unit].goto(x, self.cars[unit].ycor())

    def car_speedup(self):
        self.starting_move_distance += MOVE_INCREMENT
