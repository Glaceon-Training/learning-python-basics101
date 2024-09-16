from library import turn_right, turn_around, follow_right_wall


def mark_start_point():
    put()
    while not front_is_clear():
        turn_left()
    move()


found_start_point = object_here

mark_start_point()

while not found_start_point():
    follow_right_wall()
