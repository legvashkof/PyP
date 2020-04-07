#Ghost game
from random import randint
print('Ghost game')
feeling_brave = True
score = 0
while feeling_brave:
    ghost_door = randint (1, 3)
    print('Three doors ahead...')
    print('A ghost is behind one.')
    print('Which door will you open?')
    door = input('1, 2, or 3?')
    door_num = int(door)
    if door_num == ghost_door:
        print('GHOST!')
        feeling_brave = False
    else:
        print('NO ghost! :((')
        print('You have to try next room.')
        score = score + 1
print('RUN away!!!')
print('Game over. You scored', score)
