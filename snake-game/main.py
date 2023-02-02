from turtle import Screen, Turtle
from snake import Snake
from food import Food
from texts import Text
from pygame import mixer
import time
import movements

mixer.init()

def death_sound():
    mixer.Channel(0).play(mixer.Sound('sounds/death.wav'))

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()
screen.colormode(255)

snake = Snake()
food = Food()
text = Text()

text.update()
text.countdown()
     
speed_boost = 0
game_is_on = True
while game_is_on:

    # FRAMES
    screen.update()
    time.sleep(0.05 - speed_boost)    

    # SNAKE MOVEMENT
    snake.move()
    movements.enable_controls(snake)

    # COLLISION WITH FOOD
    if snake.head.distance(food) < 15:
        text.score += 1
        text.update()
        text.update_highest_score()
        food.eating_sound()
        food.refresh()
        snake.raise_segment()
        if speed_boost < 0.030:
            speed_boost += 0.001
        # print(f"SPEED BOOST: {speed_boost}")

    # COLLISION WITH WALL
    if snake.head.xcor() > 290 or snake.head.ycor() > 290 or snake.head.xcor() < -300 or snake.head.ycor() < -290:
        text.update_highest_score()
        text.game_over()
        text.message_collision_with_wall()
        death_sound()
        game_is_on = False

    # COLLISION WITH TAIL
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 1:
            text.message_collision_with_tail()
            text.game_over()
            text.update_highest_score()
            death_sound()
            game_is_on = False

with open("save.txt", mode="w") as file:
    file.write(f"highestScore = {text.highest_score}")

screen.exitonclick()