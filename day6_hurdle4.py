# REQUIRES REEBORG'S WEBSITE

# DEFINITIONS
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    height = 0
    turn_left()
    while wall_on_right():
        move()
        height += 1
    turn_right()
    move()
    turn_right()
    while height != 0:
        move()
        height -= 1
    turn_left()

# RUN
while not at_goal():
    if wall_in_front():
        jump()
    while front_is_clear() and not at_goal():
        move()        