# 
# Good morning! Here's your coding interview problem for today.
# 
# This problem was asked by Amazon.
# 
# Given a sorted array, find the smallest positive integer that is not the sum of a subset of the array.
# 
# For example, for the input [1, 2, 3, 10], you should return 7.
# 
# Do this in O(N) time.

import random
import time
import tqdm

from tqdm import tqdm

def f(test):

    def none_adds_up(hh, i):
        for h in hh:
            _sum = sum(h)
#             print i, '\t', _sum, h
            if _sum == i:
                return False
        return True

    maxim = test[-1]
    minim = test[0]
    space = set(test)
    if 1 not in test:
        return 1
    i = 1
    while True:
        i += 1
        # 1) for a number not in the original array ('space')
        if i in space:
            continue
        # 2) initialize all numbers smaller than that one ('operands')
        operands = [n for n in range(1, i) if n in space]
#         print i, operands
        if len(operands) < 1:
            continue
        # 3) and, if there is indeed any such number,
        _min, _max = operands[0], operands[-1]
        if _min + _max > i:
            continue
        hh = [[o] for o in operands]
        for o in operands[1:]:
            _hh = []
            for h in hh:
                if o in h:
                    _hh.append(h)
                    continue
                _h = [_o for _o in h] + [o]
                _hh += [h, _h]
            hh = _hh
        none_sums = none_adds_up(hh, i)
#         print 'none_sums', none_sums
#         raw_input()
        if none_sums:
            return i
    return -1



if __name__ == '__main__':

    tests = [
        [1, 2, 3, 10]
    ]
    
    first = None
    for l in [5, 10, 20, 40, 80, 160, 320, 640]:
        tests += [
            sorted(random.sample(list(range(1, 10)), random.randrange(2, 7)))
            for i in range(l - 1)
        ]
    
        start = time.time()
        for test in tqdm(tests):
            f(test)
#             print test
#             print f(test)
#             print '-----\n'
        diff = time.time() - start
        if not first:
            print l, diff
            first = diff
        else:
            print l, diff, first * (l / 5)
