from library import turn_right, turn_around, follow_right_wall

def harvest():
    while front_is_clear() and is_facing_north():
        while object_here():
            take()
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear() and not is_facing_north():
         while object_here():
            take()
         move()
    turn_left()
    move()
    turn_left()

move()
move()
turn_left()
for go in range(3):
    harvest()
