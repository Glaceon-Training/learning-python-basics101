from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.goto(x=0, y=280)
        self.update_score()

    def update_score(self):
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.home()
        self.write("Game Over.", align=ALIGNMENT, font=FONT)
