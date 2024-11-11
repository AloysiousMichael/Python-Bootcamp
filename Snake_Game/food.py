from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.speed("fastest")
        self.shapesize(0.5,0.5)


    def refresh(self):
        food_x=random.randint(-280,280)
        food_y=random.randint(-280,280)
        self.goto(food_x,food_y)







