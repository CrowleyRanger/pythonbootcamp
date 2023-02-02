from turtle import Turtle, Screen, bgcolor
import heroes
import random

pen = Turtle()
bgcolor("black")
pen.color("blue")

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# MOVEMENT
i = 0
while True:
    for _ in range(3 + i):
        pen.forward(20)
        angle = 360/(3 + i)
        pen.right(angle)
    pen.pencolor(random.choice(colours))
    i += 1
    
print(heroes.gen())


screen = Screen()
screen.exitonclick() 