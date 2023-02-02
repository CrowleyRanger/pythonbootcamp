import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from interface import Interface

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.listen()
screen.colormode(255)

player = Player()
car_manager = CarManager()
interface = Interface()

interface.draw_lines()
cars_in_screen = 0
max_cars_in_screen = 15
interface.scoreboard()

game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()
    player.controls(screen)

    # SPAWNING CARS:
    spawn_attempt = random.randint(0, 6)
    if spawn_attempt == 1 and cars_in_screen < max_cars_in_screen:
        car_manager.spawn_car()
        cars_in_screen += 1
    
    # MOVING CARS
    for car in car_manager.cars:
        car_manager.move_car(car)

    # REMOVING CARS
    for car in car_manager.cars:
        if car.xcor() < -320:
            car.reset_car_position()

    # COLLISION WITH CARS
    for car in car_manager.cars:
        if player.distance(car) < 25:
            interface.game_over()
            game_is_on = False

    # REACHING THE OTHER SIDE
    if player.ycor() > 180:
        player.start_position()
        interface.level += 1
        car_manager.increase_speed()
        interface.scoreboard()

screen.exitonclick()