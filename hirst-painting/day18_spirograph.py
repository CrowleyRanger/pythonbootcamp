from turtle import Turtle, Screen
import random

pen = Turtle()
pen.pensize(2)
pen.speed(5)

screen = Screen()
screen.colormode(255)
screen.bgcolor("black")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

directions = [0, 90, 180, 270]

for i in range(0, 365, 5):
    pen.pencolor(random_color())
    pen.circle(100)
    pen.setheading(i)

screen.exitonclick()