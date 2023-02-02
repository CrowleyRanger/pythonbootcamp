from turtle import Turtle
from pygame import mixer
from food_list import FOODS
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()

        
        self.speed(0)
        self.refresh()
    
    def refresh(self):
        self.random_food = random.choice(list(FOODS))
        self.shape(FOODS[self.random_food]["shape"])
        self.color(FOODS[self.random_food]["color"])
        self.shapesize(stretch_len=FOODS[self.random_food]["stretch_len"], stretch_wid=FOODS[self.random_food]["stretch_wid"])

        random_x = random.randint(-280, 260)
        random_y = random.randint(-280, 260)
        self.goto(random_x, random_y)

    def eating_sound(self):
        mixer.Channel(1).play(mixer.Sound(FOODS[self.random_food]["sound"]))

