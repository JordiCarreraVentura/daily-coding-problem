# This problem was asked by Microsoft.
# 
# Given a string and a pattern, find the starting indices of all occurrences of the pattern in the string. For example, given the string "abracadabra" and the pattern "abr", you should return [0, 7].

import random

def f(w, pattern):
    space = list(w)
    query = list(pattern)
    focus = 0
    matches = []
    for i, l in enumerate(space):
        if l == pattern[focus]:
            focus += 1
            if (focus == len(pattern)):
                matches.append(i - (focus - 1))
                focus = 0
        else:
            focus = 0
    return matches


def sample_patterns(V):
    pp = []
    for w in V:
        if len(w) < 3:
            continue
        while True:
            start = random.randrange(0, len(w) - 1)
            end = random.randrange(start, len(w))
            if end < start:
                continue
            if start < end:
                pp.append(w[start:end])
                break
    return pp
            


if __name__ == '__main__':
    
    V = [w.lower() for w in 'Given a string and a pattern, find the starting indices of all occurrences of the pattern in the string. For example, given the string abracadabra and the pattern abr, you should return [0, 7].'.split() if w.isalpha()]
    
#     V = ['abracadabra']
    
    patterns = ['abr'] + sample_patterns(V)
    
    for pattern in patterns:
        for w in V:
            print pattern, w, f(w, pattern)
