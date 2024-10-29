import colorgram
import turtle as t
import random

# Extracting colors from a picture using Colorgram python package
# color_palette = []
# colors = colorgram.extract("hirst-spot-image.jpg", 30)
#
# for color in colors:
#     rgb = color.rgb
#     red = rgb.r
#     green = rgb.g
#     blue = rgb.b
#     the_color = (red, green, blue)
#     color_palette.append(the_color)

final_color_palette = [
    (222, 232, 225), (207, 160, 83), (54, 89, 131), (145, 91, 40), (139, 27, 48), (222, 206, 108), (132, 177, 203),
    (157, 46, 83), (46, 55, 103), (168, 159, 40), (128, 188, 143), (83, 20, 44), (37, 43, 68), (186, 93, 106),
    (185, 139, 172), (84, 123, 181), (59, 39, 31), (79, 153, 165), (88, 156, 91), (194, 79, 72), (45, 74, 77),
    (161, 201, 220), (80, 73, 44), (62, 127, 120), (219, 175, 186), (168, 206, 169), (221, 181, 167)
]

timmy = t.Turtle()
t.colormode(255)
t.speed(0)


def draw_hirst(dots):
    dot_count = 0
    x = -230
    y = -225

    for _ in range(dots):
        t.teleport(x, y)
        t.pencolor(random.choice(final_color_palette))
        t.dot(20)
        dot_count += 1
        x += 50
        t.teleport(x, y)
        if dot_count % 10 == 0:
            x = -230
            y += 50


draw_hirst(100)
screen = t.Screen()
screen.exitonclick()
