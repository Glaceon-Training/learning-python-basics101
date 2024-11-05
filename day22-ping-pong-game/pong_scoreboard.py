from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 40, "bold")


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(position)
        self.update_score()

    def update_score(self):
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        if self.score == 5:
            self.write(f"Game Over", align=ALIGNMENT, font=FONT)
