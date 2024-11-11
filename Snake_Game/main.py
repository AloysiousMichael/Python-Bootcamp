from turtle import Screen
from snake import Snake
from food import Food
import time
from scoreboard import Scoreboard


screen=Screen()
screen.tracer(0)
screen.setup(width=600,height=600)
screen.title("My Snake Game")
screen.bgcolor("black")

snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_on=True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


   #Collision with Food
    if snake.head.distance(food) <15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Collision with wall

    if snake.head.xcor() < -285 or snake.head.xcor() > 285 or snake.head.ycor() < -285 or snake.head.ycor() >285:
        scoreboard.reset()
        snake.reset()

    #Collision with tail
    for segment in snake.snake[1:]:
        if(snake.head.distance(segment) < 10):
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
