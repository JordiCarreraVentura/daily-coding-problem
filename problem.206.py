# This problem was asked by Twitter.
# 
# A permutation can be specified by an array P, where P[i] represents the location of the element at i in the permutation. For example, [2, 1, 0] represents the permutation where elements at the index 0 and 2 are swapped.
# 
# Given an array and a permutation, apply the permutation to the array. For example, given the array [a, b, c] and the permutation [2, 1, 0], return [c, b, a].

import random

def f(test, permutations):
    out = []
    for p in permutations:
        out.append(test[p])
    return out


if __name__ == '__main__':
    
    items = [
        [random.randrange(0, 50) for j in range(random.randrange(2, 10))]
        for i in range(100)
    ]
    
    tests = []
    for item in items:
        _range = list(range(len(item)))
        random.shuffle(_range)
        tests.append((item, _range))
    
    for (test, permutations) in tests:
        print test, permutations
        print f(test, permutations)
        print
