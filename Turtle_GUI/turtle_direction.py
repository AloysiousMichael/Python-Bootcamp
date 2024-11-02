from turtle import Turtle,Screen

tini=Turtle()
screen=Screen()

def move_forward():
    tini.forward(20)
def move_backward():
    tini.backward(20)
def move_clockwise():
    tini.right(10)
def move_anticlockwise():
    tini.right(10)

def clear():
    tini.clear()
    tini.penup()
    tini.home()
    tini.pendown()

screen.listen()
screen.onkeypress(move_forward,'w')
screen.onkeypress(move_backward,'s')
screen.onkeypress(move_clockwise,'a')
screen.onkeypress(move_anticlockwise,'b')
screen.onkeypress(clear,'c')

screen.exitonclick()