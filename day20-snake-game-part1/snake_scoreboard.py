from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")


class Scoreboard(Turtle):
    # Scoreboard is a subclass of Turtle class in turtle module.
    # Basically it is also a Turtle, so we hide the turtle, has it pen up, white colored text, go to the top screen.
    # It also has attribute of updating score. And has starting score at zero.
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("snake_highscore.txt") as file:
            self.highscore = int(file.read())
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.goto(x=0, y=280)
        self.update_score()

    # Using write function to update score.
    def update_score(self):
        self.clear()
        self.write(f"Score = {self.score} | High Score = {self.highscore}", align=ALIGNMENT, font=FONT)

    # Adding score by one everytime snake eats. Clear the current writing and update (rewrite) score.
    def add_score(self):
        self.score += 1
        self.update_score()

    # Get new high score from the current game score if it is a new highest score. Write new highscore
    # into "snake_highscore.txt".
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("snake_highscore.txt", mode='w') as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.update_score()

    # Printing "Game Over" and positioned at home when game is over.
    def game_over(self):
        self.home()
        self.write("Game Over.", align=ALIGNMENT, font=FONT)
