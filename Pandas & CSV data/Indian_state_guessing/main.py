from turtle import Turtle,Screen
import pandas

screen=Screen()
turtle=Turtle()
screen.title("Indian States Game")
image="indian_map.gif"
screen.addshape(image)
turtle.shape(image)

data=pandas.read_csv("indian_states.csv")
guessed_state=[]
all_states=data.state.to_list()
while len(guessed_state) < 30 :
    answer_state=screen.textinput(title=f'{len(guessed_state)}/ 29 States Correct' ,prompt="Whats the states name ?").title()
    print(answer_state)

    if answer_state=="Exit":
        missing_states=[]
        for states in all_states:
            if states not in guessed_state:
                missing_states.append(states)
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
            name_print=Turtle()
            state_details=data[data.state==answer_state]
            name_print.hideturtle()
            name_print.penup()
            name_print.goto(state_details.x.item(),state_details.y.item())
            name_print.write(answer_state)
            guessed_state.append(answer_state)