#Ex1 Reeborg's world Loop & Functions
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

def right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    move()
    turn_left()
    move()
    right()
    move()
    right()
    move()
    turn_left()
for step in range(6):
    jump()

#Ex2 Reeborg's world While Loop

def right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    move()
    right()
    move()
    right()
    move()
    turn_left()
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

#Ex3 Reeborg's world Jumping over Hurdles

def right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    while wall_on_right():
        move()
    right()
    move()
    right()
    while not wall_in_front():
        move()
    turn_left()
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

#Main Escaping the Maze
def right():
    turn_left()
    turn_left()
    turn_left()
while not at_goal(): 
    if not wall_on_right():
        right()
        move()
    elif wall_on_right():
        turn_left()
    else:
        turn_left()
        move()
