from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("white")
        self.setheading(90)
        self.start_position()
    
    def controls(self, screen):
        def move_up():
            if self.ycor() < 280:
                self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)
        def move_left():
            if self.xcor() > - 290:
                self.goto(self.xcor() - MOVE_DISTANCE, self.ycor())
        def move_down():
            if self.ycor() > - 280:
                self.goto(self.xcor(), self.ycor() - MOVE_DISTANCE)
        def move_right():
            if self.xcor() < 280:
                self.goto(self.xcor() + MOVE_DISTANCE, self.ycor())

        screen.onkeypress(move_up, "Up")
        screen.onkeypress(move_left, "Left")
        screen.onkeypress(move_down, "Down")
        screen.onkeypress(move_right, "Right")

    def start_position(self):
        self.setposition(STARTING_POSITION)