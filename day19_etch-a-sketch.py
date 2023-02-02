from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(5)
def move_backwards():
    tim.back(5)
def turn_left():
    tim.left(5)
def turn_right():
    tim.right(5)

def reset():
    tim.clear()
    tim.reset()

screen.listen()

# ========== BUTTONS
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="a", fun=turn_left)
screen.onkeypress(key="d", fun=turn_right)

screen.onkey(key="c", fun=reset)

screen.exitonclick()