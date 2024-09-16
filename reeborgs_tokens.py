from library import turn_right, turn_around, follow_right_wall


def move_until_goal():
    i = 0
    while not at_goal():
        if object_here():
            take()
            i += 1
        elif not object_here() and i > 0:
            for x in range(i):
                put()
                i -= 1
        move()


move_until_goal()
