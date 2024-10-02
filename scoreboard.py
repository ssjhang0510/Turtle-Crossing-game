from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(-200, 250)
        self.Level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.Level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)

    def level_up(self):
        self.Level += 1
        self.update_scoreboard()

