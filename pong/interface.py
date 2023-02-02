from turtle import Turtle

class Separator(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color(20, 20, 20)
        self.penup()
        self.setposition(0, -250)
        self.setheading(90)
        self.pensize(2)
        while self.ycor() < 250:
            self.pendown()
            self.forward(25)
            self.penup()
            self.forward(25)
            self.pendown()