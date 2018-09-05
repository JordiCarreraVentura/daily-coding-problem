# This problem was asked by Facebook.
# 
# Given a circular array, compute its maximum subarray sum in O(n) time.
# 
# For example, given [8, -1, 3, 4], return 15 as we choose the numbers 3, 4, and 8 where the 8 is obtained from wrapping around.
# 
# Given [-4, 5, 1, 0], return 6 as we choose the numbers 5 and 1.

import random
import time


def f(test):
    
    if len(test) < 2:
        return test[0]

    l = len(test)    
    deduct = 1
    candidates = []
    while deduct < l:
        _l = len(test) - deduct
        for i in range(l):
            up_to = i + _l
            if up_to >= l:
                diff = up_to - l
                span = test[i:] + test[:diff]
            else:
                span = test[i:up_to]
            summ = sum(span)
            if summ:
                score = summ / float(len(span))
                candidates.append(span)
        deduct += 1
    if candidates:
        candidates.sort(reverse=True, key=lambda x: (sum(x), 1 / float(len(x))))
        return sum(candidates.pop(0))
    else:
        return 0


def f0(test):
    
    if len(test) < 2:
        return test[0]

    l = len(test)    
    _l = len(test) - 1
    candidates = []
    for i in range(l):
        up_to = i + _l
        if up_to >= l:
            diff = up_to - l
            span = test[i:] + test[:diff]
        else:
            span = test[i:up_to]
        summ = sum(span)
        if summ:
            score = summ / float(len(span))
            candidates.append(span)
    if candidates:
        candidates.sort(reverse=True, key=lambda x: (sum(x), 1 / float(len(x))))
        return sum(candidates.pop(0))
    else:
        return 0



if __name__ == '__main__':

    tests = [
        [8, -1, 3, 4],
        [-4, 5, 1, 0],
    ]
    
    for n in [100, 1000, 10000, 100000, 1000000]:
    
        tests += [
            [random.randrange(-10, 10) for i in range(random.randrange(3, 6))]
            for i in range(n)
        ]
    
        start = time.time()
        for test in tests:
#             print test, f(test)
            f(test)
        print n, 'f', time.time() - start

        start = time.time()        
        for test in tests:
#             print test, f(test)
            f0(test)
        print n, 'f0', time.time() - start
        
        sames = 0
        for test in random.sample(tests, 100):
            if f(test) == f0(test):
                sames += 1
        print n, sames
        print '---'
        
        

# 100 f 0.00244092941284
# 100 f0 0.00113081932068
# 100 48
# ---
# 1000 f 0.0254769325256
# 1000 f0 0.0101411342621
# 1000 35
# ---
# 10000 f 0.250658035278
# 10000 f0 0.0915789604187
# 10000 36
# ---
# 100000 f 2.52293300629
# 100000 f0 0.921736955643
# 100000 30
# ---
# 1000000 f 25.8486189842
# 1000000 f0 9.35112810135
# 1000000 34
# ---
