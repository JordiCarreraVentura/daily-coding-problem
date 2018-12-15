# This problem was asked by Facebook.
# 
# On a mysterious island there are creatures known as Quxes which come in three colors: red, green, and blue. One power of the Qux is that if two of them are standing next to each other, they can transform into a single creature of the third color.
# 
# Given N Quxes standing in a line, determine the smallest number of them remaining after any possible sequence of such transformations.
# 
# For example, given the input ['R', 'G', 'B', 'G', 'B'], it is possible to end up with a single Qux through the following steps:
# 
#         Arrangement       |   Change
# ----------------------------------------
# ['R', 'G', 'B', 'G', 'B'] | (R, G) -> B
# ['B', 'B', 'G', 'B']      | (B, G) -> R
# ['B', 'R', 'B']           | (R, B) -> G
# ['B', 'G']                | (B, G) -> R
# ['R']                     |


import random


def color():
    x = random.randrange(0, 3)
    if x == 0:
        return 'R'
    elif x == 1:
        return 'G'
    else:
        return 'B'


COLORS = set(['R', 'G', 'B'])

def f(test):

    def any_adjacent(space):
        for i in range(len(space) - 1):
            curr = space[i]
            next = space[i + 1]
            if curr != next:
                return i
        return -1
    
    def switch(space, i):
        left = space[:i]
        right = space[i + 2:]
        a, b = space[i], space[i + 1]
        colors = set([a, b])
        new = list(COLORS - colors)
        all = left + new + right
        return all

    space = [x for x in test]
    while True:
        i = any_adjacent(space)
        print i, space
        if i == -1:
            break
        space = switch(space, i)
    return len(space)



if __name__ == '__main__':

    tests = [
        [color() for _ in range(random.randrange(3, 11))]
        for _ in range(10)
    ] + [
        ['R', 'G', 'B', 'G', 'B']
    ]

    for test in tests:
        print test
        print f(test)
