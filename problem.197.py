# This problem was asked by Amazon.
# 
# Given an array and a number k that's smaller than the length of the array, rotate the array to the right k elements in-place.

import numpy as np
import random


def rotate(a, k):
    slice = a[k:]
    rest = a[:k]
    return np.concatenate((slice, rest))


if __name__ == '__main__':

    for a in [
        np.array(
            [random.randrange(0, 100)
            for i in range(random.randrange(10, 20))
        ]) for i in range(10)
    ]:
        for k in [2, 3, 5]:
            print rotate(a, k)
