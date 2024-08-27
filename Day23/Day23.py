import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=player.up)

i = 0
game_is_on = True
while game_is_on:
    if(i % 10 == 0):
        car_manager.add_car()
    car_manager.move_cars()
    
    if car_manager.is_car_at(player.pos()):
        scoreboard.kill_player()
        game_is_on = False
    else:

        if player.is_finished():
            scoreboard.player_wins()
            player.next_level()
            car_manager.move_increment +=15
        

        scoreboard.display()
        time.sleep(0.1)
        screen.update()
        i+=1


screen.exitonclick()
