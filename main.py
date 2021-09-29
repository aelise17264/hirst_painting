# extracted colors from image to create color list
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('dots.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle
import random
color_list = [(238, 250, 244), (187, 18, 44), (243, 231, 66), (252, 235, 239), (210, 236, 242), (196, 75, 32), (218, 66, 107), (17, 124, 173), (196, 175, 17), (108, 181, 209), (12, 142, 88), (12, 166, 214), (210, 152, 96), (187, 41, 61), (241, 231, 2), (23, 39, 76), (77, 174, 94), (36, 44, 112), (215, 69, 50), (218, 130, 155), (124, 185, 119), (235, 165, 183), (5, 58, 39), (146, 209, 220), (8, 95, 55), (4, 86, 111), (162, 29, 27), (234, 171, 164), (162, 212, 176)]

new_turtle = turtle.Turtle()
turtle.colormode(255)
new_turtle.shape("turtle")
new_turtle.penup()
new_turtle.setheading(225)
new_turtle.forward(315)
new_turtle.setheading(0)


def draw_dots(num):
    for _ in range(num):
        ran_color = random.choice(color_list)
        new_turtle.dot(20, ran_color)
        new_turtle.forward(50)


def new_line():
    for _ in range(10):
        draw_dots(10)
        new_turtle.setheading(90)
        new_turtle.forward(50)
        new_turtle.setheading(180)
        new_turtle.forward(500)
        new_turtle.setheading(0)
new_line()

my_screen = turtle.Screen()
my_screen.exitonclick()