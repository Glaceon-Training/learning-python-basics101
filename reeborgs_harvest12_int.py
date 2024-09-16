from library import turn_right, turn_around, follow_right_wall


def turn(int):
    i = 0
    while i < int:
        turn_left()
        i += 1


def harvest(int):
    while front_is_clear():
        move()
        while object_here():
            take()
    turn(int)
    move()
    turn(int)


move()
move()
turn(1)
for i in range(3):
    harvest(3)
    harvest(1)
