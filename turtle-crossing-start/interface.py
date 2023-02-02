from turtle import Turtle

FONT = ("Courier", 16, "normal")

class Interface(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()

    def game_over(self):
        self.color("red")
        self.setposition(0, 0)
        self.write(arg="Game Over", align="center", font=FONT)

    def you_passed(self):
        self.color("white")
        self.setposition(0, 0)
        self.write(arg="Noice, you reached the other side!", align="center", font=FONT)

    def scoreboard(self):
        self.clear()
        self.penup()
        self.color("white")
        self.setposition(-225, 250)
        self.write(arg=f"Level: {self.level}", align="center", font=FONT)

    def draw_lines(self):
        lines = Turtle()
        lines.hideturtle()
        lines.setheading(180)
        lines.color(100, 100, 0)
        for num in range(8):
            lines.penup()
            lines.setposition(280, -140 + 40*num)
            while lines.xcor() > -285:
                lines.pendown()
                lines.forward(20)
                lines.penup()
                lines.forward(20)