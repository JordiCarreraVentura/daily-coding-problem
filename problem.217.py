# This problem was asked by Oracle.
# 
# We say a number is sparse if there are no adjacent ones in its binary representation. For example, 21 (10101) is sparse, but 22 (10110) is not. For a given input N, find the smallest sparse number greater than or equal to N.
# 
# Do this in faster than O(N log N) time.

import math
import random
import time
import tqdm

from tqdm import tqdm


class BinaryNumber:
    
    def __init__(self):
        return

    def __set_exp(self, rest):
        exp = 1
        while True:
            m = 2 ** exp
            if m > rest:
                exp -= 1
                break
            elif m == rest:
                break
            exp += 1
        return exp
        
    def __update(self, rest, exp, slots):
        m = 2 ** exp
        rest -= m
        if not slots:
            slots = 10 ** exp
        else:
            slots += 10 ** exp
        return slots, rest

    def __call__(self, n):
        slots = []
        rest = n
        if not rest:
            return str(0)
        while rest:
            exp = self.__set_exp(rest)
            slots, rest = self.__update(rest, exp, slots)
        return str(slots)


def is_sparse(out):
    for i, char in enumerate(out):
        if i == len(out) - 1 or len(out) < 2:
            break
        if char != '1':
            continue
        if out[i + 1] == '1':
            return False
    return True


if __name__ == '__main__':

    bn = BinaryNumber()
    for test, expected in [
        (0, 0),
        (1, 1),
        (2, 10),
        (3, 11),
        (4, 100),
        (5, 101),
        (6, 110),
        (8, 1000),
        (10, 1010),
        (14, 1110),
        (16, 10000),
        (21, 10101),
        (22, 10110),
        (365, 101101101),
        (6775, 1101001110111),
        (77474, 10010111010100010),
    ]:
        out = bn(test)
        print test, out, '/%d' % expected, '\t', is_sparse(out)
    
    last = 0
    first = 0
    nn = [10, 100, 1000, 5000, 10000, 100000, 500000, 1000000]
    for n in nn:
        nums = [
            bn(random.randrange(0, 100000))
            for i in range(n)
        ]
        start = time.time()
        for num in tqdm(nums):
            is_sparse(num)
        elapsed = time.time() - start
        if not first:
            first = elapsed
        if last:
            expected = (last * (n / float(nn[(nn.index(n) - 1)])))
            actual_ratio = elapsed / expected
#             print n, elapsed, '/%f' % expected, '(%f)' % actual_ratio

            factor = n / nn[0]
            expected = first * factor
            print n, elapsed, expected, expected / elapsed
        else:    
            print n, elapsed
        last = elapsed
