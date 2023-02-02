import turtle
import pandas as pd

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("U.S. State Game")
map_image = "blank_states_img.gif"

screen.addshape(map_image)
turtle.shape(map_image)

data = pd.read_csv("50_states.csv")
state_names_list = data.state.tolist()


guessed_states = []
while len(guessed_states) < 50:
        guess = screen.textinput(title=f"{len(guessed_states)}/50 guessed states.", prompt="What's another state's name?").title()

        if guess == "Exit":
                # missing_states = []
                # for state in state_names_list:
                #         if state not in guessed_states:
                #                 missing_states.append(state)
                missing_states = [state for state in state_names_list if state not in guessed_states]
                new_data = pd.DataFrame(missing_states)
                print(new_data)
                new_data.to_csv("states_to_learn.csv")
                screen.bye()

        if guess in state_names_list and guess not in guessed_states:

                guessed_states.append(guess)

                x = int(data[data.state == guess].x)
                y = int(data[data.state == guess].y)

                state_name = turtle.Turtle()
                state_name.penup()
                state_name.hideturtle()
                state_name.color("blue")
                state_name.setposition(x, y)
                state_name.write(arg=guess, align="center", font=("Courier", 8, "normal"))      

screen.exitonclick()