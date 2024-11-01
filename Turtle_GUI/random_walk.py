import random
import turtle
from turtle import Turtle ,Screen

tini=Turtle()
turtle.colormode(255)
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)

    colour=(r,g,b)
    return colour

screen=Screen()
tini.pensize(30)
tini.speed("fastest")

direction=[0,90,180,270]
for i in range(300):
    tini.forward(30)
    tini.setheading(random.choice(direction))
    tini.color(random_color())




screen.exitonclick()