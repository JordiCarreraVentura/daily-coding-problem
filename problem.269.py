# This problem was asked by Microsoft.
# 
# You are given an string representing the initial conditions of some dominoes. Each element can take one of three values:
# 
# L, meaning the domino has just been pushed to the left,
# R, meaning the domino has just been pushed to the right, or
# ., meaning the domino is standing still.
# Determine the orientation of each tile when the dominoes stop falling. Note that if a domino receives a force from the left and right side simultaneously, it will remain upright.
# 
# For example, given the string .L.R....L, you should return LL.RRRLLL.
# 
# Given the string ..R...L.L, you should return ..RR.LLLL.

import random


SYMBOLS = ['.', 'R', 'L']

def new_game():
    l = random.randrange(5, 12)
    game = ['.' for _ in range(l)]
    for _ in range(random.randrange(2, 4)):
        game[random.sample(range(l), 1)[0]] = random.sample(SYMBOLS, 1)[0]
    return ''.join(game)


def f(test):
    space = list(test)
    moved = set([])
    while True:
        going_left = set(
            [i for i, ch in enumerate(space)
            if ch == 'L' and i not in moved]
        )
        going_right = set(
            [i for i, ch in enumerate(space)
            if ch == 'R' and i not in moved]
        )
        if not going_left and not going_right:
            break
        
        falling_left = set(
            [i for i, ch in enumerate(space)
            if ch == '.' and i + 1 in going_left
            and i not in moved and i + 1 not in moved]
        )
        
        falling_right = set(
            [i for i, ch in enumerate(space)
            if ch == '.' and i - 1 in going_right
            and i not in moved and i - 1 not in moved]
        )
        
        blocked = set(
            [i for i in falling_left if i in falling_right]
        )
        
        actually_falling_left = falling_left - blocked
        actually_falling_right = falling_right - blocked
        
        for i in actually_falling_left:
            space[i] = 'L'

        for i in actually_falling_right:
            space[i] = 'R'

    
        print 'going_left', going_left
        print 'going_right', going_right
        print 'actually_falling_left', actually_falling_left
        print 'actually_falling_right', actually_falling_right
        print 'blocked', blocked

        moved.update(going_left)
        moved.update(going_right)
        moved.update(blocked)
        print moved
        print '---'
    
    return ''.join(space)


if __name__ == '__main__':
    
    for game in [
        new_game() for _ in range(10)
    ]:
        print game
        print f(game)
        print
        
    for test in ['.L.R....L', '..R...L.L']:
        print test
        print f(test)
        print
