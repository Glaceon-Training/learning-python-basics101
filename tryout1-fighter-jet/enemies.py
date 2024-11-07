from turtle import Turtle
import random
SPAWN_CHANCE = 25
MOVE_INCREMENT = 1


class Enemies:
    def __init__(self):
        self.troops = []
        self.steps = 5
        self.spawn_chance = SPAWN_CHANCE

    def spawn_enemies(self):
        random_chance = random.randint(1, self.spawn_chance)
        if random_chance == 1:
            new_troop = Turtle("circle")
            new_troop.color("yellow")
            new_troop.penup()
            new_troop.goto(350, random.randint(-200, 200))
            self.troops.append(new_troop)

    def enemy_move(self):
        for troop in self.troops:
            troop.backward(self.steps)

    def chance_increase(self):
        self.steps += MOVE_INCREMENT
