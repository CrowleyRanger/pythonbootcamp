from turtle import Turtle, Screen
import random

pen = Turtle()
pen.pensize(2)
pen.speed(0)

screen = Screen()
screen.colormode(255)
screen.bgcolor("black")

colours = colorgram.extract('example.py', 6)

# ========== FEATURES
paint_size = 100
dots_num = 10
dot_size = 5

# ========== STARTING POINT
pen.setposition(-paint_size/2, -paint_size/2)
dots_in_column = 0
dots_in_line = 0

while dots_in_column != dots_num or dots_in_line != dots_num:
    dots_in_line = 0

    # PAINTING A LINE
    while dots_in_line != dots_num:
        dots_in_line += 1

        pen.pencolor(random_color())

        pen.pendown()
        pen.dot(dot_size)
        pen.penup()

        pen.forward(paint_size/dots_num)

    dots_in_column += 1

    pen.setposition(-paint_size/2, -paint_size/2 + ((paint_size/dots_num)*dots_in_column))
    pen.pendown()

screen.exitonclick()