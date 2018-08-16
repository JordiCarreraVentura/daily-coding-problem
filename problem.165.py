# Given an array of integers, return a new array where each element in the new array is the number of smaller elements to the right of that element in the original input array.
# 
# For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0], since:
# 
# There is 1 smaller element to the right of 3
# There is 1 smaller element to the right of 4
# There are 2 smaller elements to the right of 9
# There is 1 smaller element to the right of 6
# There are no smaller elements to the right of 1

import random

def f(nums):
    out = []
    for i, n in enumerate(nums):
        count = 0
        for _n in nums[i:]:
            if _n < n:
                count += 1
        out.append(count)
    return out


if __name__ == '__main__':

    tests = [
        [3, 4, 9, 6, 1],
    ] + [
        [random.randint(0, 100) for i in range(5)]
        for j in range(4)
    ]

    for test in tests:
        print test
        print f(test)
        print
