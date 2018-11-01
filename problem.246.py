# This problem was asked by Dropbox.
# 
# Given a list of words, determine whether the words can be chained to form a circle. A word X can be placed in front of another word Y in a circle if the last character of X is same as the first character of Y.
# 
# For example, the words ['chair', 'height', 'racket', touch', 'tunic'] can form the following circle: chair --> racket --> touch --> height --> tunic --> chair.

import random


def word(V):
    ll = []
    for _ in range(random.randrange(2, 6)):
        ll.append(V[random.randrange(0, len(V))])
    return ''.join(ll)


def f(test):

    def is_chained(_prev, test):
        for i in range(len(test) - 1):
            w1 = test[_prev[i]]
            w2 = test[_prev[i + 1]]
            if w2[0] != w1[-1]:
                return False
        if test[_prev[-1]][-1] != test[_prev[0]][0]:
            return False
        return True
    
    def chain(prev, i, test):
        if len(test) == 2 and len(prev) == 2:
            j, k = prev
            a = test[j]
            b = test[k]
            if a[-1] == b[0] and b[-1] == a[0]:
                return prev
            return []
        _prev = [x for x in prev]
        _prev.append(i)
        left = [j for j in range(len(test)) if j not in _prev]
        if left:
            chained = []
            for j in left:
                chained += chain(_prev, j, test)
            return chained
        elif is_chained(_prev, test):
            return _prev
        else:
            return []

    for i in range(len(test)):
        chained = chain([], i, test)
        if chained:
            return [test[j] for j in chained]
    return []


if __name__ == '__main__':

    VOCABULARY = 'a b c d e f g h'.split()

    tests = [
        [word(VOCABULARY) for w in range(random.randrange(2, 6))]
        for _ in range(99)
    ]
    
#     tests = [
#         ['chair', 'height', 'racket', 'touch', 'tunic']
#     ]

    for test in tests:
        print f(test), test
