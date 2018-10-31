# This problem was asked by Square.
# 
# The Sieve of Eratosthenes is an algorithm used to generate all prime numbers smaller than N. The method is to take increasingly larger prime numbers, and mark their multiples as composite.
# 
# For example, to find all primes less than 100, we would first mark [4, 6, 8, ...] (multiples of two), then [6, 9, 12, ...] (multiples of three), and so on. Once we have done this for all primes less than N, the unmarked numbers that remain will be prime.
# 
# Implement this algorithm.


import sys

def add_composites(n, curr):
    out = []
    for mult in range(2, n):
        prod = curr * mult
        if prod <= n:
            out.append(prod)
        else:
            break
    return out


if __name__ == '__main__':
    
    n = int(sys.argv[1])
    primes = []
    composites = set([])
    for curr in range(2, n + 1):
        composites.update(add_composites(n, curr))
    unmarked = set(range(2, n)) - composites
    print 'unmarked', sorted(unmarked)

        
