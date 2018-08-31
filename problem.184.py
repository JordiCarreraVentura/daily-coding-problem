# Given n numbers, find the greatest common denominator between them.
# 
# For example, given the numbers [42, 56, 14], return 14.


import random


def f(nums):
    div = min(nums)
    while True:
        divided = True
        for n in nums:
            if n % float(div):
                divided = False
                break
        if divided:
            return div
        div -= 1
    return -1



if __name__ == '__main__':

    tests = [
        [42, 56, 14]
    ] + [
        [random.randrange(1, 100) for j in range(random.randrange(2, 8))]
        for i in range(200)
    ]
    
    for test in tests:
        print f(test), test
