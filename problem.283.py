# This problem was asked by Google.
# 
# A regular number in mathematics is defined as one which evenly divides some power of 60. Equivalently, we can say that a regular number is one whose only prime divisors are 2, 3, and 5.
# 
# These numbers have had many applications, from helping ancient Babylonians keep time to tuning instruments according to the diatonic scale.
# 
# Given an integer N, write a program that returns, in order, the first N regular numbers.

import random


REGULAR_PRIME_DIVISORS = [1, 2, 3, 5]

def f(n):

    def prod(_nn):
        nn = [n for n in _nn]
        _prod = nn.pop(0)
        while nn:
            _prod *= nn.pop(0)
        return _prod
    
    def primes(curr):

        def is_prime(n):
            for x in range(2, n):
                if not n % x:
                    return False
            return True
    
        for n in range(2, curr):
            if is_prime(n):
                yield n

    def regular_prime_divisors(prev, curr):
    
        def dedup(out):
            prev = []
            for series in out:
                set1 = set(series)
                taken = False
                for _prev in prev:
                    set2 = set(_prev)
                    if set1.intersection(set2) == set1:
                        taken = True
                if taken:
                    continue
                prev.append(series)
            return prev
        
        if prev in REGULAR_PRIME_DIVISORS:
            return [prev]
    
        out = []
        for h in prev:
            new = []
            for prime in primes(curr):
                _h = [n for n in h] + [prime]
                if prod(_h) == curr:
                    out.append(_h)
                elif _h and prod(_h) < curr:
                    new.append(_h)
            if new:
                out += regular_prime_divisors(new, curr)
        out = dedup(out)
        return [
            h for h in out
            if not [x for x in h if x not in REGULAR_PRIME_DIVISORS]
        ]

    out = [x for x in REGULAR_PRIME_DIVISORS]
    curr = 1
    while True:
        if regular_prime_divisors([[]], curr):
            out.append(curr)
        if len(out) == n:
            return out
        curr += 1


if __name__ == '__main__':

    for n in [random.randrange(
        len(REGULAR_PRIME_DIVISORS),
        10 + len(REGULAR_PRIME_DIVISORS)
    ) for _ in range(10)]:
        print n, f(n)
