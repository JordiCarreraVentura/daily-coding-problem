# This problem was asked by Spotify.
# 
# Write a function, throw_dice(N, faces, total), that determines how many ways it is possible to throw N dice with some number of faces each to get a specific total.
# 
# For example, throw_dice(3, 6, 7) should equal 15.

import random


def f(history, n, faces, total):
    out = []
    for face in range(1, faces + 1):
        series = history + [face]
        outcome = sum(series)
        if len(series) == n:
            if outcome == total:
                out.append(tuple(series))
        else:
            out += [
                _series for _series in f(series, n, faces, total)
                if sum(_series) <= total
            ]
    return out


if __name__ == '__main__':

    tests = [
        (3, 6, 7)
    ]
    
    dice = [3, 6, 10, 12, 20]
    for _ in range(99):
        test = (
            random.randint(1, 5),
            random.sample(dice, 1)[0],
            random.randint(1, 50)
        )
        tests.append(test)
    
    
    for (n, faces, total) in tests:
        print n, faces, total
        ways = f([], n, faces, total)
        print len(ways)
        print
