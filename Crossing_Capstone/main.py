from turtle import Turtle ,Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time
screen=Screen()
player=Player()
car_manager=CarManager()
scoreboard=Scoreboard()
screen.setup(width=600,height=600)
screen.tracer(0)

game_is_on=True
screen.listen()
while game_is_on:

    time.sleep(0.1)
    screen.onkey(player.move_up,"Up")
    screen.update()
    car_manager.create_car()
    car_manager.move_car()

    for car in car_manager.all_cars:
        if car.distance(player) <20 :
            game_is_on= False
            scoreboard.game_over()

    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()


screen.exitonclick()



