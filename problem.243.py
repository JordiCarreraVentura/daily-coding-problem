# This problem was asked by Etsy.
# 
# Given an array of numbers N and an integer k, your task is to split N into k partitions such that the maximum sum of any partition is minimized. Return this sum.
# 
# For example, given N = [5, 1, 2, 7, 3, 4] and k = 3, you should return 8, since the optimal partition is [5, 1, 2], [7], [3, 4].

import random


def avg(values):
    return sum(values) / len(values)


def f(test, k):

    def minsums(partition):
        ll = [sum(part) for part in partition]
        u = avg(ll)
        #print 'll', ll
        #print 'diff', [abs(l - u) for l in ll]
        return sum([abs(l - u) for l in ll])
    
    def partition(test, k):
        parts = []
        part = []
        space = [x for x in test]
        n = len(test) / k
        print '! k=%d len=%d n=%d' % (k, len(test), n)
        while space:
            part.append(space.pop(0))
            if len(part) == n:
                parts.append([x for x in part])
                part = []
        if part:
            parts.append(part)
        return parts
    
    def reorder(partition, k):
    
        def cp(h):
            return [[y for y in x] for x in h]
    
        def expand(k, i, partition, to_the_right):
            part = partition[i]
            h = cp(partition)
            if to_the_right and (len(h[i + 1]) > 1 or len(h) > k):
                h[i].append(h[i + 1].pop(0))
            elif to_the_right:
                return (i, minsums(partition), partition)
            elif not to_the_right and (len(h[i - 1]) > 1 or len(h) > k):
                h[i] = [h[i - 1].pop()] + h[i]
            elif not to_the_right:
                return (i, minsums(partition), partition)
            return (i, minsums(h), h)
    
        hh = []
        for i in range(len(partition)):
            # left-hand side partition
            if not i:
                hh.append(expand(k, i, partition, True))
            # two-fold partition
            elif i == len(partition) - 1:
                hh.append(expand(k, i, partition, False))
            # right-hand side partition
            else:
                hh.append(expand(k, i, partition, False))
                hh.append(expand(k, i, partition, True))
        hh.sort(key=lambda x: (x[1], x[0]))
        for h in hh:
           print '\t', h
        best = hh.pop(0)
        return (best[1], best[2])
        
    partition = partition(test, k)
    while True:
        minsum = minsums(partition)
        print '?', minsum, partition
        _minsum, _partition = reorder(partition, k)
        if _minsum < minsum:
            partition = [part for part in _partition if part]
        else:
            break
    return partition


if __name__ == '__main__':

    MAX_TEST_LENGTH = 20

    tests = [
        [5, 1, 2, 7, 3, 4]      # if using this, k should be = 3
    ] + [
        [
            random.randrange(1, 20)
            for _ in range(random.randrange(2, MAX_TEST_LENGTH))
        ] for _ in range(19)
    ]

    for test in tests:
        print test
        _k = int(len(test) * 0.34)
        k = random.randrange(2, _k if _k >= 3 else 3)
        print k
        print f(test, k)
        print
