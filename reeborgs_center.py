from library import turn_right, turn_around, follow_right_wall


def cage():
    move()
    turn_around()
    build_wall()
    turn_right()


def bob_the_builder():
    while right_is_clear():
        turn_right()
        while front_is_clear():
            move()
        turn_around()
        cage()


def contractor():
    cage()
    bob_the_builder()


if front_is_clear():
    contractor()
    turn_around()
    contractor()
else:
    turn_left()
    contractor()
put()
