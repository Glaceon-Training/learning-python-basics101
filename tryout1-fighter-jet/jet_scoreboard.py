from turtle import Turtle
FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(-380, 250)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score = {self.score}", align="left", font=FONT)

    def add_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.home()
        self.write(f"Game Over.", align="center", font=FONT)
