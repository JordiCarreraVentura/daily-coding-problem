# This problem was asked by Citrix.
# 
# You are given a circular lock with three wheels, each of which display the numbers 0 through 9 in order. Each of these wheels rotate clockwise and counterclockwise.
# 
# In addition, the lock has a certain number of "dead ends", meaning that if you turn the wheels to one of these combinations, the lock becomes stuck in that state and cannot be opened.
# 
# Let us consider a "move" to be a rotation of a single wheel by one digit, in either direction. Given a lock initially set to 000, a target combination, and a list of dead ends, write a function that returns the minimum number of moves required to reach the target state, or None if this is impossible.

import random
import time
import tqdm

from tqdm import tqdm


def new_target():
    return [
        random.randrange(0, 10),
        random.randrange(0, 10),
        random.randrange(0, 10)
    ]


def new_dead_ends():
    dead_ends = []
    for _ in range(random.randrange(1, 10)):
        dead_ends.append(new_target())
    return dead_ends


def moves(ascending):
    R = list(range(10))
    if not ascending:
        R.reverse()
    for i in R:
        for j in R:
            for k in R:
                yield [i, j, k]


def get_moves(target, ascending):
    for i, move in enumerate(moves(ascending)):
        if move == target:
            return i + 1
    return None


def f(target, dead_ends, count):

    dead_ends_increasing = sorted([[y for y in x] for x in dead_ends])
    dead_ends_decreasing = sorted([[y for y in x] for x in dead_ends], reverse=True)

    # dead end before target in increasing move order
    is_dead_end_increasing = False
    while dead_ends_increasing:
        dead_end = dead_ends_increasing.pop(0)
        space = [x for x in target]
        while space:
            _dead = dead_end.pop(0)
            _target = space.pop(0)        
            if _dead < _target:
                is_dead_end_increasing = True
                break
            elif _dead < _target:
                if not _dead:
                    is_dead_end_increasing = True
                    break
    
    # dead end after target in decreasing move order
    is_dead_end_decreasing = False
    while dead_ends_decreasing:
        dead_end = dead_ends_decreasing.pop(0)
        space = [x for x in target]
        while space:
            _dead = dead_end.pop(0)
            _target = space.pop(0)        
            if _dead > _target:
                is_dead_end_decreasing = True
                break
            elif _dead > _target:
                if not _dead:
                    is_dead_end_decreasing = True
                    break
    
    # n moves to target?
    if is_dead_end_increasing and is_dead_end_decreasing:
        return None
    elif not is_dead_end_increasing:
        if count:
            return get_moves(target, True)
        else:
            return 1 + sum([
                target[0] * 100,
                target[1] * 10,
                target[2]
            ])
    elif not is_dead_end_decreasing:
        if count:
            return get_moves(target, False)
        else:
            return 1000 - sum([
                target[0] * 100,
                target[1] * 10,
                target[2]
            ])


if __name__ == '__main__':
    
    tests = [
        # target, dead ends, count (True) or approximation (False)
        (new_target(), new_dead_ends(), True)
        for _ in range(100000)
    ] 
    
    tests += [
        # target, dead ends, count (True) or approximation (False)
        (a, b, False) for a, b, _ in tests
    ]
    
    
#     tests = [
#         ([4, 5, 5], [[1, 2, 3], [4, 5, 6]]),
#         ([1, 2, 1], [[1, 2, 3], [4, 5, 6]]),
#         ([1, 2, 4], [[1, 2, 3], [4, 5, 6]]),
#         ([1, 2, 4], [[1, 2, 3]]),
#     ]
    
    times_count = []
    times_approx = []
    for target, dead_ends, count in tqdm(tests):
        start = time.time()
        if target in dead_ends:
            continue
        f(target, dead_ends, count)
        duration = time.time() - start
        if count:
            times_count.append(duration)
        else:
            times_approx.append(duration)
    
    print 'count', sum(times_count) / len(times_count)
    print 'approx', sum(times_approx) / len(times_approx)
    #   19% faster to approximate than to count
        
