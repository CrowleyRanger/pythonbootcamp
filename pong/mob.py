from turtle import Turtle

# By setting Paddle as Turtle, Paddle receives the same attributes of a turtle object.
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.setheading(90)
        self.shapesize(1, 5)
        self.color("white")

    def position(self, x, y):
        self.setposition(x, y)

    def controls(self, screen, up, down):

        def move_up():
            if self.ycor() > 240:
                pass
            else:
                self.forward(20)
        def move_down():
            if self.ycor() < -240:
                pass
            else:
                self.back(20)

        screen.onkeypress(key=up, fun=move_up)
        screen.onkeypress(key=down, fun=move_down)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.setheading(45)
        self.setposition(0, 0)
        self.color("white")
        self.move_speed = 0.1

        self.x_dist = 10
        self.y_dist = 10

    def move(self):
        self.setposition(self.xcor() + self.x_dist, self.ycor() + self.y_dist)

    def bounce(self, axis):
        if axis == "x":
            self.x_dist *= -1
            self.move_speed *= 0.9
        elif axis == "y":
            self.y_dist *= -1

    def reset_position(self):
        self.setposition(0, 0)
        self.move_speed = 0.1