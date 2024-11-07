from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.color("black")
        self.hideturtle()
        self.goto(-290, 260)
        self.update_score()

    def update_score(self):
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def add_score(self):
        self.level += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.home()
        self.write(f"Game Over.", align="center", font=FONT)
