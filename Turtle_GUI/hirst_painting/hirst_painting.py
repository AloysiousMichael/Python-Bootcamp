import turtle

import colorgram
from turtle import Turtle ,Screen
import random

turtle.colormode(255)
tini=Turtle()
screen=Screen()

colors=colorgram.extract('image.jpg',50)
new_rgb=[]
tini.speed("fastest")
tini.penup()
tini.hideturtle()
tini.setheading(225)
tini.forward(300)
tini.setheading(0)
number_of_dot=100

for color in colors:
    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.b
    new_color=(r,g,b)
    new_rgb.append((new_color))

for dot_count in range(1,number_of_dot+1):
    tini.dot(20,random.choice(new_rgb))
    tini.penup()
    tini.forward(50)

    if dot_count%10==0:
        tini.setheading(90)
        tini.forward(50)
        tini.setheading(180)
        tini.forward(500)
        tini.setheading(0)



screen.exitonclick()

