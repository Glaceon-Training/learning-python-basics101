from library import turn_right, turn_around, follow_right_wall


def harvest():
    while front_is_clear() and is_facing_north():
        while object_here():
            take()
        while front_is_clear() and not object_here():
            move()
    turn_right()
    move()
    turn_right()
    while front_is_clear() and not is_facing_north():
        while object_here():
            take()
        while front_is_clear() and not object_here():
            move()
    turn_left()
    move()
    turn_left()


def sow():
    while is_facing_north():
        move()
        move()
        for z in range(6):
            put()
            move()
        for x in range(2):
            move()
            turn_right()
    while not is_facing_north():
        move()
        move()
        for zz in range(6):
            put()
            move()
        for y in range(2):
            move()
            turn_left()


def back_to_start():
    turn_left()
    for back in range(6):
        move()
    turn_right()


for start in range(2):
    move()
turn_left()
for go in range(3):
    harvest()
back_to_start()
for asu in range(3):
    sow()
