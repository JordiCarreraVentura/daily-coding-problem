# This problem was asked by PagerDuty.
# 
# Given a positive integer N, find the smallest number
# of steps it will take to reach 1.
# 
# There are two kinds of permitted steps:
# 
# You may decrement N to N - 1.
# If a * b = N, you may decrement N to the larger of a 
# and b. For example, given 100, you can reach 1 in five 
# steps with the following route:
#
# 100 -> 10 -> 9 -> 3 -> 2 -> 1.

import random


def f(n):
    
    def multipliers(n, prev):
        out = []
        for a in range(n):
            for b in range(n):
                if a * b == n:
                    step = (max([a, b]), [x for x in prev] + [n])
                    out.append(step)
        return out
    
    def smallest(space):
        small = []
        for n, prev in space:
            if n < 1:
                continue
            elif n == 1:
                small.append((n, prev))
            else:
                _space = [
                    (n - 1, prev + [n])
                ] + multipliers(n, prev)
                small += smallest(_space)
        shortest = min([len(h) for n, h in small])
        return set([(n, tuple(h)) for n, h in small if len(h) == shortest])

    return smallest([(n, [])])
    


if __name__ == '__main__':
    
    for _ in range(10):
        n = random.randrange(3, 100)
        print n
        for x in f(n):
            print x
        print
        
    print 100
    for x in f(100):
        print x
