import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, 'Up')

loop = 0
game_is_on = True
while game_is_on:
    loop += 1
    time.sleep(0.1)
    screen.update()
    # generate car only each 6 loops
    if loop == 6:
        loop = 1
        car_manager.generate_new_car()

    car_manager.move_cars()

    # detect collision with a car
    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
    # detect if the player reached the top of the screen
    if player.has_reached_end():
        player.go_to_start()
        car_manager.increment_speed()
        scoreboard.increase_level()


screen.exitonclick()
