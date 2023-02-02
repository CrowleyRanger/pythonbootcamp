import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE
    
    def spawn_car(self):
        new_car = CarManager()
        new_car.penup()
        new_car.setposition(320, random.randint(-3, 3)*40)
        new_car.shape("square")
        new_car.shapesize(1, 2)
        new_car.color(random.choice(COLORS))
        new_car.setheading(180)
        self.cars.append(new_car)

    def move_car(self, car):
        car.forward(self.move_distance)

    def reset_car_position(self):
        self.setposition(280, random.randint(-3, 3)*40)

    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT