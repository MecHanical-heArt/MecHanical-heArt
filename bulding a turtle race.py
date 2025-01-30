
from turtle import Turtle , Screen
import random
is_race_on = False
screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt="which turtle will win the race ? enter a color: ")
print(user_bet)
colors = ["red","orange","yellow","green","blue","purple"]


turtles = []
location_y = [-70 , -40 , -10 , 20 , 50 ,80]
for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x= -230,y= location_y[turtle_index])
    turtles.append(new_turtle)
if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on=False
            win_turtle = (turtle.pencolor())
            if win_turtle == user_bet:
                print(f"You've won! the {win_turtle}")
            else:
                print(f"You've lost! the {win_turtle}")

        ran_distance= random.randint(0,10)
        turtle.forward(ran_distance)



screen.exitonclick()