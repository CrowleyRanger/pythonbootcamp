from turtle import Turtle, Screen
from mob import Paddle, Ball
from text import Text
from interface import Separator
import time

screen = Screen()
text = Text()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()
screen.colormode(255)

# ==================== PADDLE 1
paddle1 = Paddle()
paddle1.position(350, 0)
paddle1.controls(screen, "Up", "Down")

# ==================== PADDLE 2
paddle2 = Paddle()
paddle2.position(-350, 0)
paddle2.controls(screen, "w", "s")

# ==================== BALL
ball = Ball()

# ==================== GAME
text.countdown()
text.scoreboard()
separator = Separator()

speed = 0.1
game_is_on = True
while game_is_on:
    
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # COLLISION WITH WALL
    if ball.ycor() > 275 or ball.ycor() < -270:
        ball.bounce("y")

    # COLLISION WITH PADDLE
    if ball.distance(paddle1) <= 60 and ball.xcor() == 330:
        ball.bounce("x")
    elif ball.distance(paddle2) <= 60 and ball.xcor() == -330:
        ball.bounce("x")

    # OUT OF THE BOUDARIES
    if ball.xcor() > 380:
        ball.reset_position()
        ball.bounce("x")
        text.clear()
        text.score2 += 1
    elif ball.xcor() < -380:
        ball.reset_position()
        ball.bounce("x")
        text.clear()
        text.score1 += 1

    text.update_scoreboard()
    

screen.exitonclick()