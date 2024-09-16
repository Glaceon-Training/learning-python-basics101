from library import turn_right, turn_around


def climb_one_floor():
    turn_left()
    move()
    turn_right()
    move()
    move()


def climb_to_f3():
    for i in range(3):
        climb_one_floor()


def down_one_floor():
    move()
    move()
    turn_left()
    move()
    turn_right()


def down_to_f1():
    for i in range(3):
        down_one_floor()


take()
climb_to_f3()
put()
turn_around()
down_to_f1()
done()
