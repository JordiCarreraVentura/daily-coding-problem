# This problem was asked by LinkedIn.
# 
# Given a set of characters C and an integer k, a De Bruijn sequence is a cyclic sequence in which every possible k-length string of characters in C occurs exactly once.
# 
# For example, suppose C = {0, 1} and k = 3. Then our sequence should contain the substrings {'000', '001', '010', '011', '100', '101', '110', '111'}, and one possible solution would be 00010111.
# 
# Create an algorithm that finds a De Bruijn sequence.


import random


def permutations(C, k):
    space = [[]]
    while True:
        new = []
        for h in space:
            for c in C:
                _h = [x for x in h]
                _h += [c]
                new.append(_h)
        space = new
        if len(space[0]) == k:
            break
    return [''.join(h) for h in space]


def f(C, k):

    def _add(p, series):
#         series += p
#         return series
        
        series_head = series[:2]
        series_tail = series[-2:]
        
        p_head = p[:2]
        p_tail = p[-2:]
        
        if series_head == p_tail:
            series = p[0] + series
        elif series_tail == p_head:
            series += p[-1]
        else:
            series += p

        return series

    pp = permutations(C, k)
    random.shuffle(pp)
    series = ''
    for p in pp:
        if p in series:
            continue
        series = _add(p, series)
    return series
    

if __name__ == '__main__':
    C = {'0', '1'}
    k = 3
    
    ll = []
    for xp in range(1000):
        print f(C, k)
        ll.append(len(f(C, k)))
#         print
    
    print sum(ll) / len(ll)
