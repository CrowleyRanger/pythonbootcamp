from turtle import Turtle
import time

ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")
MESSAGE_FONT = ("Courier", 8, "normal")

class Text(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0

        with open("save.txt", mode="r") as file:
            str_score = ""
            for char in file.read():
                if char.isdigit():
                    str_score += char
            self.highest_score = int(str_score)

        self.setposition(0, 260)
        self.color("white")
        self.update()
    
    def update(self):
        self.clear()
        self.write(arg=f"Score: {self.score} Highest Score = {self.highest_score}", align=ALIGNMENT, font=FONT)

    def update_highest_score(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            self.update()

    def game_over(self):
        self.color("red")
        self.setposition(0, 0)
        self.write(arg="YOU DIED", align=ALIGNMENT, font=FONT)

    def message_collision_with_tail(self):
        self.color("orange")
        self.setposition(0, -20)
        self.write(arg="Please, don't be a cannibal...", align=ALIGNMENT, font=MESSAGE_FONT)

    def message_collision_with_wall(self):
        self.color("orange")
        self.setposition(0, -20)
        self.write(arg="Well, now you're a snake with a face of a Pug dog.", align=ALIGNMENT, font=MESSAGE_FONT)

    def countdown(self):
        countdown = Turtle()
        countdown.hideturtle()
        for num in range(3, 0, -1):
            countdown.color("white")
            countdown.setposition(0, 0)
            countdown.write(arg=f"{num}", align=ALIGNMENT, font=FONT)
            time.sleep(1)
            countdown.clear()