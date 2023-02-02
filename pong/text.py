from turtle import Turtle
import time

ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")
SCORE_FONT = ("Courier", 32, "normal")

class Text(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score1 = 0
        self.score2 = 0

    def scoreboard(self):
        self.color("blue")
        self.setposition(150, 250)
        self.write(arg=self.score1, align=ALIGNMENT, font=SCORE_FONT)
        self.color("orange")
        self.setposition(-150, 250)
        self.write(arg=self.score2, align=ALIGNMENT, font=SCORE_FONT)

    def update_scoreboard(self):
        self.clear()
        self.scoreboard()

    def game_over(self):
        self.color("red")
        self.setposition(0, 0)
        self.write(arg="Game Over", align=ALIGNMENT, font=FONT)

    def countdown(self):
        self.color("white")
        self.setposition(0, 0)
        for number in range(3, 0, -1):
            self.write(arg=number, align=ALIGNMENT, font=FONT)
            time.sleep(1)
            self.clear()