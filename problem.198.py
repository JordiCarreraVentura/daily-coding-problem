# This problem was asked by Google.
# 
# Given a set of distinct positive integers, find the largest subset such that every pair of elements in the subset (i, j) satisfies either i % j = 0 or j % i = 0.
# 
# For example, given the set [3, 5, 10, 20, 21], you should return [5, 10, 20]. Given [1, 3, 6, 24], return [1, 3, 6, 24].

import json
import random


def f(test):

    def satisfies(n1, n2):
        if not n1 % float(n2) or not n2 % float(n1):
            return True
        return False
    
    def update(n1, n2, satisfied):
        if not satisfied.has_key(n1):
            satisfied[n1] = [n1]
        satisfied[n1].append(n2)

    satisfied = dict([])
    for i, n1 in enumerate(test):
        for j, n2 in enumerate(test):
            if i == j:
                continue
            if satisfies(n1, n2):
                update(n1, n2, satisfied)
    
#     print json.dumps(satisfied, indent=4)
    
    ranks = satisfied.items()
    if ranks:
        ranks.sort(key=lambda x: len(x[1]))
        return sorted(ranks[-1][1])
    return []



if __name__ == '__main__':
    
    tests = [
        [3, 5, 10, 20, 21],
        [1, 3, 6, 24]
    ] + [
        list(set([random.randrange(1, 101) for i in range(random.randrange(4, 10))]))
        for j in range(48)
    ]
    
    for test in tests:
        print test
        print f(test)
        print '--'
