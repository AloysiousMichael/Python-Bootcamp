import turtle
from turtle import Turtle,Screen
import random
tini=Turtle()
screen=Screen()
turtle.colormode(255)
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    colour=(r,g,b)
    return colour
tini.speed("fastest")
def draw_circle(sizeofgap):
    for i in range(int(360/sizeofgap)):
        tini.color(random_color())
        tini.circle(100)
        currentheading=tini.heading()
        tini.setheading(currentheading+sizeofgap)

draw_circle(5)
screen.exitonclick()




