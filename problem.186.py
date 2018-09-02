# This problem was asked by Microsoft.
# 
# Given an array of positive integers, divide the array into two subsets such that the difference between the sum of the subsets is as small as possible.
# 
# For example, given [5, 10, 15, 20, 25], return the sets {10, 25} and {5, 15, 20}, which has a difference of 5, which is the smallest possible difference.

import random


def f(test):
    nums = [x for x in test]
    nums.sort(reverse=True)
    a = [nums.pop(0)]
    
    last_diff = 0
    while True:
        diffs = []
            
        if abs(sum(nums) - sum(a)) <= min(nums):
            b = nums
            break
        
        for i, num in enumerate(nums):
            l, r = nums[:i], nums[i + 1:]
            sum_rest = sum(l + r)
            sum_a = sum(a + [num])
            diffs.append((i, abs(sum_a - sum_rest)))
        
        if diffs:
            _diffs = zip(*diffs)[1]
            min_diff = min(_diffs)
            diff_i, diff = [(x, y) for x, y in diffs if y == min_diff][0]
            if sum(nums) - sum(a) < nums[diff_i]:
                b = nums
                break
            if last_diff and diff > last_diff:
                b = nums
                break
            new_num = nums.pop(diff_i)
            a.append(new_num)
            last_diff = diff
        else:
            break

    return a, b



if __name__ == '__main__':

    tests = [
        [5, 10, 15, 20, 25],
        [5, 15, 20, 25],
        [10, 15, 20, 25]
    ] + [
        [random.randrange(1, 100) for j in range(random.randrange(2, 15))]
        for i in range(97)
    ]
    
#     tests = [[8, 14, 34, 42, 45]]
#     tests = [[78, 33, 24, 10]]
    
    for test in tests:
        a, b = f(test)
        print '\ninput array:', test
        print 'subset 1 (sum=%d):' % sum(a), a
        print 'subset 2 (sum=%d):' % sum(b), b
