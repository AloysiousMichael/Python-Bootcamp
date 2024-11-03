from turtle import Turtle
ALIGNMENT="center"
FONT=("Courier",24,"normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        self.goto(0,250)
        self.penup()
        self.color("white")
        self.score_update()
        self.hideturtle()

    def score_update(self):
        self.write(f'Score : {self.score} ',align=ALIGNMENT,font=FONT)

    def increase_score(self):
        self.score+=1
        self.clear()
        self.score_update()


    def game_over(self):
        self.goto(0,0)
        self.write(f'Game Over',align=ALIGNMENT,font=FONT)

