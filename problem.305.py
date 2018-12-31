# This problem was asked by Amazon.
# 
# Given a linked list, remove all consecutive nodes that sum to zero. Print out the remaining nodes.
# 
# For example, suppose you are given the input 3 -> 4 -> -7 -> 5 -> -6 -> 6. In this case, you should first remove 3 -> 4 -> -7, then -6 -> 6, leaving only 5.

import random

def f(test):

    def remove(covered, test):
        return [x for i, x in enumerate(test) if i not in covered]

    stacks = []
    covered = set([])
    for i in range(len(test) - 1):
#         print i, stacks, covered
        if i in covered:
            continue
        stack = []
        for j in range(i, len(test)):
            if j in covered:
                continue
            curr = test[j]
            stack.append((j, curr))
            if len(stack) > 1 and sum(zip(*stack)[1]) == 0:
                stacks.append(stack)
                stack = []
                covered.update(range(i, j + 1))
                break
    print i, stacks, covered
    return remove(covered, test)


if __name__ == '__main__':
    
    tests = [
        [3, 4, -7, 5, -6, 6],
    ] + [
        [random.randrange(-10, 10) for _ in range(5, 15)] for _ in range(99)
    ]
    
    for test in tests:
        print test
        print f(test)
        print
