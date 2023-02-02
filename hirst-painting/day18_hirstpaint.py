from turtle import Turtle, Screen
import random

pen = Turtle()
pen.pensize(2)
pen.speed(0)
pen.hideturtle()

screen = Screen()
screen.colormode(255)
screen.bgcolor("black")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# ========== FEATURES
paint_size = 500
dots_num = 10
dot_size = 20

# ========== STARTING POINT
pen.setposition(-paint_size/2, -paint_size/2)
dots_in_column = 0
dots_in_line = 0

while dots_in_column != dots_num or dots_in_line != dots_num:
    dots_in_line = 0

    # PAINTING A LINE
    while dots_in_line != dots_num:
        dots_in_line += 1

        pen.pendown()
        pen.dot(dot_size, random_color())
        pen.penup()

        pen.forward(paint_size/dots_num)

    dots_in_column += 1

    pen.setposition(-paint_size/2, -paint_size/2 + ((paint_size/dots_num)*dots_in_column))
    pen.pendown()

screen.exitonclick()