while at_goal() is False:
    while front_is_clear():
        move()
        while wall_in_front():
            if wall_on_right():
                turn_left()
                break
            else:
                turn_left()
                turn_left()
                turn_left()
                break
        if at_goal():
            break
