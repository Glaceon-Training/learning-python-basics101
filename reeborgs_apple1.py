from library import turn_right, turn_around, follow_right_wall

move()
while not at_goal():
    while not object_here():
        follow_right_wall()
        if at_goal:
            break
    take()
