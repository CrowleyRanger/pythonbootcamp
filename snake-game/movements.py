from turtle import Screen
screen = Screen()

# ==================== MOVEMENTS
def enable_controls(snake_object):
    def move_up():
        snake_object.segments[0].setheading(90)

    def move_down():
        snake_object.segments[0].setheading(270)

    def move_right():
        snake_object.segments[0].setheading(0)

    def move_left():
        snake_object.segments[0].setheading(180)

    screen.onkeypress(key="w", fun=move_up)
    screen.onkeypress(key="a", fun=move_left)
    screen.onkeypress(key="s", fun=move_down)
    screen.onkeypress(key="d", fun=move_right)