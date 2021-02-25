# PONG GAME
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time

# Screen Setup
screen = Screen()
screen.bgcolor("black")
screen.title("Pong by Brother's Co.")
screen.setup(height=600, width=800)
screen.tracer(0)

# Game Name
tim = Turtle()
tim.color("SpringGreen")
tim.write("PONG", align="center", font=("Engravers MT", 50, "normal"))
tim.hideturtle()
time.sleep(1.4)
tim.clear()

# Company Name
tim.color("RoyalBlue2")
tim.write("By Brother's Co.", align="center", font=("Algerian", 50, "normal"))
tim.hideturtle()
time.sleep(1.7)
tim.clear()

# Paddle Tuples
r_paddle = Paddle((370, 0))
l_paddle = Paddle((-380, 0))
ball = Ball()
scoreboard = Scoreboard()

# KEYPRESS
screen.listen()
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")


time.sleep(1)

game_is_on = False

def toggle_pause():
    global game_is_on
    if game_is_on == True:
        game_is_on = False
        tim.clear()
    else:
        game_is_on = True
        tim.write("Press SPACE to Resume!", align="center", font=("Unispace", 30, "normal"))


screen.listen()
screen.onkeypress(toggle_pause, "space")

while True:
    if not game_is_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()
    else:
        screen.update()

    # Detect Collision with Wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect Collision with Paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -350:
        ball.bounce_x()

    # Detect Right Paddle Misses
    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.l_point()

    # Detect Left Paddle Misses
    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
