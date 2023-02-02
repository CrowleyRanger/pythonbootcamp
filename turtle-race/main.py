from turtle import Turtle, Screen
from players import turtles
import random

while True:

    screen = Screen()
    screen.bgcolor("black")

    timmy = Turtle()
    tommy = Turtle()
    jenny = Turtle()
    conny = Turtle()
    benny = Turtle()

    # Because turtle is a string, eval() is required to convert it back into an object.
    for turtle in turtles:
        eval(turtle).setposition(-400, turtles[turtle]["y_pos"])
        eval(turtle).color(turtles[turtle]["color"])
        eval(turtle).shape("turtle")

    guess = screen.textinput("Should the race begin?", "Start? [Press ENTER]")

    turtle_win = False
    while not turtle_win:
        for turtle in turtles:
            eval(turtle).forward(random.randint(1, 5))
            if eval(turtle).position() >= (400, turtles[turtle]["y_pos"]):
                turtle_win = True
                winner = turtles[turtle]["name"]
                break

    final_message = screen.textinput("Final result", f"WINNER: {winner}!\n\nWatch another race? [Y/n]").lower()
    if final_message == "y":
        screen.clear()
        continue
    else:
        screen.bye()

screen.exitonclick()