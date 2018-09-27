# This problem was asked by Apple.
# 
# A Collatz sequence in mathematics can be defined as follows. Starting with any positive integer:
# 
# if n is even, the next number in the sequence is n / 2
# if n is odd, the next number in the sequence is 3n + 1
# It is conjectured that every such sequence eventually reaches the number 1. Test this conjecture.
# 
# Bonus: what input n <= 1000000 gives the longest sequence?

import random
import tqdm

from tqdm import tqdm


def f(n):
    s = [n]
    while s[-1] != 1:
        last = s[-1]
        if not int(round(last % 2.0)):
            s.append(int(last / 2.0))
        else:
            s.append((3 * last) + 1)
        if len(s) > 2 and s[-1] == s[-2]:
            break
#         print s
    if s[-1] == 1:
        return True, ((n, len(s)))
    return False


if __name__ == '__main__':
    
    nn = list(range(10000000))
#     nn = list(range(10000))
    
    args = []
    f_args = []
    for n in tqdm(nn):
#     for i in range(10000000):
        n = random.randrange(1, 1000000000)
        is_collatz, arg = f(n)
        if not is_collatz:
            f_args.append(arg)
        else:
            args.append(arg)
    print 'collatz:', len(args)
    print 'number with the longest sequence:', sorted(args, key=lambda x: x[1])[-1][0]
    print 'highest number:', max(zip(*args)[0])
    print 'lowest number:', min(zip(*args)[0])
        
#         print n, f(n)
#         print f(n)
#         raw_input()
