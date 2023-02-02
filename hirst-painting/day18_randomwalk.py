from turtle import Turtle, Screen
import random

pen = Turtle()
pen.pensize(2)
pen.speed(0)

screen = Screen()
screen.colormode(255)
screen.bgcolor("black")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

directions = [0, 90, 180, 270]

while True:
    pen.pencolor(random_color())
    pen.setheading(random.choice(directions))
    pen.forward(10)

screen.exitonclick()