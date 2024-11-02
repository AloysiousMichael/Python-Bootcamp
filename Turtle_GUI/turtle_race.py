from turtle import Turtle,Screen
import random

screen=Screen()
screen.setup(width=500,height=400)
user_quess=screen.textinput(title="Make a bet !",prompt="Who will win the race , Enter a colour")
is_raceon=False
colour=["red","orange","green","blue","yellow","violet"]
turtles=[]
y_positions=[-70,-40,-10,20,50,80]
print(user_quess)



for i in range(6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colour[i])
    new_turtle.penup()
    new_turtle.goto(-230, y_positions[i])
    turtles.append(new_turtle)

if user_quess:
    is_raceon = True

while is_raceon:

    for turtle in turtles:
        if turtle.xcor() > 230 :
            is_raceon=False
            winning_color=turtle.pencolor()

            if winning_color==user_quess:
                print(f'You  Won !. The {winning_color} turtle is the winner')
            else:
                print(f'You Lost !. The {winning_color} turtle is the winner')

        distance = random.randint(0, 10)
        turtle.forward(distance)



screen.exitonclick()