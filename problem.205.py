# This problem was asked by IBM.
# 
# Given an integer, find the next permutation of it in absolute order. For example, given 48975, the next permutation would be 49578.

import random

def f(test):
    space = list(str(test))
    jj, chars = zip(*list(enumerate(space)))
    chars = list(chars)
    for x in range(1, len(jj)):
        j = len(jj) - x
        i = j - 1
        n2 = int(chars[j])
        n1 = int(chars[i])
        if n2 > n1:
            left = chars[:i] + [chars[j]]
            right = [chars[i]] + chars[j + 1:]
            return int(''.join(left + right))
    return 0


if __name__ == '__main__':
    for test in [48975] + [random.randrange(1, 10000) for i in range(49)]:
        print test, f(test)
