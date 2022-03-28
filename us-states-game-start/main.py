import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
states_to_learn = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's the another state's name?")
    answer_state = answer_state.title()
    print(answer_state)

    if answer_state == "Exit":
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())

# for state in all_states:
#     if state not in guessed_states:
#         states_to_learn.append(state)

states_to_learn = [state for state in all_states if state not in guessed_states]

states_to_learn_data = pandas.DataFrame(states_to_learn)
states_to_learn_data.to_csv("states_to_learn.csv")
