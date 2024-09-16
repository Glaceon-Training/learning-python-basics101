from library import turn_right, turn_around, follow_right_wall


def jump():
    turn_left()
    while wall_on_right():
        move()
    while not wall_on_right():
        turn_right()
        move()
    while front_is_clear():
        move()
    turn_left()


while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()


"""
from library import turn_right, turn_around, follow_right_wall

while not at_goal():
    follow_right_wall()

"""
