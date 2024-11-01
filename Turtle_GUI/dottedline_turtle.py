from turtle import Turtle,Screen

tini=Turtle()
screen=Screen()

for j in range(25):
    tini.forward(5)
    tini.color("white")
    tini.forward(5)
    tini.color("black")

screen.exitonclick()
