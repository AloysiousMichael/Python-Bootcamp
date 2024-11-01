from turtle import Turtle,Screen
import random

tini=Turtle()
screen=Screen()


col = ['yellow', 'green', 'blue', 'red','grey','orange']
def draw_shape(num_side):
    angle = 360 / num_side
    for i in range(num_side):
        tini.forward(75)
        tini.right(angle)


for shape_of_side in range(3,11):
    draw_shape(shape_of_side)
    tini.color(random.choice(col))

screen.exitonclick()
