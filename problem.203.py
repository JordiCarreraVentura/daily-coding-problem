# This problem was asked by Uber.
# 
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand. Find the minimum element in O(log N) time. You may assume the array does not contain duplicates.
# 
# For example, given [5, 7, 10, 3, 4], return 3.
# 

import math
import random
import time
import tqdm

from tqdm import tqdm


def f(test):

    def halve(curr):
        l = len(curr)
        if l > 2:
            half = int(l / 2)
            return curr[:half], curr[half:]
        elif l == 2:
            return [curr[0]], [curr[1]]
        else:
            return [curr[0]], []

    curr = [x for x in test]
    while True:
        a, b = halve(curr)
#         print a, b
        if not b:
            return a[0]
        if a[-1] > b[-1]:
            curr = b
        else:
            curr = a
    return None


def new_rotated(n_digits):
    items = list(range(10000))
    base = list(random.sample(items, n_digits))
    k = random.randrange(0, len(base))
    return base[k:] + base[:k]


if __name__ == '__main__':

    # toy test
    tests = [
        [6, 7, 1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5, 6, 7],
        [2, 3, 4, 5, 6, 7, 1],
        [5, 7, 10, 3, 4]
    ]
    for test in tests:
        print f(test), test

    # performance test
    for n_samples in [10, 100, 500, 1000, 2000, 5000]:
        for n_digits in [5, 10, 20, 50, 100]:

            tests = [
                new_rotated(n_digits)
                for i in tqdm(list(range(n_samples)))
            ]

            start = time.time()
            search_times = []
            for test in tests:
                _start = time.time()
                f(test)
                search_times.append(time.time() - _start)
            avg_search_time = sum(search_times) / len(search_times)
            print n_samples, n_digits, math.log(n_digits / avg_search_time, 10)
