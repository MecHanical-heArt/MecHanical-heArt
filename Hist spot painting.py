#import colorgram
#rgb_colors = []
#colors = colorgram.extract('image.jpg',30)
#for color in colors:
    #r = color.rgb.r
    #g = color.rgb.g
    #b = color.rgb.b
    #new_color = (r, g, b)

    #rgb_colors.append(new_color)
import turtle as turtle_module
import random
max = turtle_module.Turtle()
max.speed("fastest")
turtle_module.colormode(255)
color_list = [(249, 248, 248), (238, 246, 244), (237, 242, 246), (246, 240, 244), (2, 13, 31), (52, 25, 17),
              (218, 128, 106), (11, 105, 159), (241, 213, 70), (149, 84, 40), (214, 87, 64), (156, 7, 24),
              (164, 162, 32)
    , (156, 63, 102), (11, 62, 31), (206, 74, 104), (12, 96, 57), (93, 6, 21), (174, 135, 162), (1, 63, 145),
              (9, 173, 215), (157, 32, 22), (5, 212, 206), (10, 139, 86), (146, 226, 215), (121, 193, 149),
              (101, 219, 229), (222, 177, 213), (123, 171, 191), (80, 135, 179)]

max.penup()
max.hideturtle()  # turtle imlecini gizliyor
y_position = -200
#10*10 luk renk ızgarası oluşturma
for _ in range(10):
    max.dot(20, random.choice(color_list))
    max.forward(50)
    max.setx(-200)
    max.sety(y_position)
    for _ in range(10):
        max.dot(20,random.choice(color_list))
        max.forward(50)
    y_position +=50
















screen = turtle_module.Screen()
screen.exitonclick()







