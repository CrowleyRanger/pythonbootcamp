# REQUIRES REEBORG'S WEBSITE

# DEFINITIONS
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# START: FACE NORTH
while not is_facing_north():
    turn_left()
    
# START: GO AT THE MAX TOP
while front_is_clear():
    move()
    
# START: GO AT THE MAX RIGHT POSITION
if right_is_clear():
    turn_right()
    while front_is_clear():
        move()
    turn_left()

# ALWAYS KEEP A WALL ON RIGHT
while not at_goal(): 
    while wall_in_front() and wall_on_right():
        turn_left()

    while front_is_clear() and wall_on_right():
        move()

    while right_is_clear() and not at_goal():
        turn_right()
        move()