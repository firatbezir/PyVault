import turtle
import pandas
from turtle import Turtle

screen = turtle.Screen()
screen.title("Name the State")
screen.setup(width=800, height=600)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

text = Turtle()
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
correct_guess_list = []
game_is_on = True

while game_is_on:

    # 1. Convert the guess to Title case
    answer_state = screen.textinput(title=f"{len(correct_guess_list)}/50 States Correct", prompt="What's "
                                                                                    "another "
                                                                            "state's "
                                                                    "name?").title()

    if answer_state == "Exit":
        states_to_learn = [state for state in all_states if state not in correct_guess_list]
        df = pandas.DataFrame(data={"State Name": states_to_learn})
        df.to_csv("states_to_learn.csv")
        break

    # 2. Check if the guess is among the 50 states
    state_specific_data = data[data["state"] == answer_state]
    if answer_state in all_states and answer_state not in correct_guess_list:
        text.penup()
        text.hideturtle()
        text.goto((state_specific_data.iloc[0]["x"]), state_specific_data.iloc[0]["y"])
        text.write(state_specific_data.iloc[0]["state"])
        correct_guess_list.append(state_specific_data.iloc[0]["state"])

screen.exitonclick()