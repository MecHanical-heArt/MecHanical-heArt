from turtle import Turtle, Screen

max = Turtle()
screen = Screen()

def  move_forwards():
    max.forward(10)
def move_backwards():
    max.backward(10)
def turn_left():
    new_heading = max.heading() + 10
    max.setheading(new_heading)
def turn_right():
    new_heading = max.heading() - 10
    max.setheading(new_heading)

def clear():
    max.clear()

def max_home():
    max.home()





screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="c", fun=clear)
screen.onkey(key="h", fun=max_home)


screen.exitonclick()