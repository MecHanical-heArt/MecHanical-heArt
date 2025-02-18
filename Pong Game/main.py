import random
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()






screen.listen()
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
game_is_on = True

def move_l_paddle():
    if random.random() > 0.1:
        if ball.ycor() > l_paddle.ycor():
            l_paddle.go_up()
        elif ball.ycor() < l_paddle.ycor():
            l_paddle.go_down()




while game_is_on:
    time.sleep(0.07)
    screen.update()
    ball.move()
    move_l_paddle()


    #delect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        #needs to bounce

        #detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() > -340:
        ball.bounce_x()
    #Detect r paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    #detect l paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()





screen.exitonclick()