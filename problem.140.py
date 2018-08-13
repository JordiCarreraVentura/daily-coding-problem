# Given an array of integers in which two elements appear exactly once and all other elements appear exactly twice, find the two elements that appear only once.
# 
# For example, given the array [2, 4, 6, 8, 10, 2, 6, 10], return 4 and 8. The order does not matter.
# 
# Follow-up: Can you do this in linear time and constant space?

import random
import time


def f(numbers):
    unique = set([])
    for i in range(len(numbers)):
        ni = numbers[i]
        if ni in unique:
            continue
        dup = False
        for j in range(len(numbers)):
            if i == j:
                continue
            nj = numbers[j]
            if nj in unique:
                continue
            if ni == nj:
                dup = True
                break
        if not dup:
            unique.add(ni)
    return unique


if __name__ == '__main__':

    numbers = [2, 4, 6, 8, 10, 2, 6, 10]
    
    ref_global = None
    ref_local = None
    for n in [10, 50, 250, 1250, 6250, 31250]:
        numbers = range(n)
        random.shuffle(numbers)
        duplicates = n / 10
        while duplicates > 0:
            insertion = random.randint(0, n)
            duplicate_i = random.randint(0, n)
            if duplicate_i >= len(numbers):
                continue
            duplicate = numbers[duplicate_i]
            numbers[insertion] = duplicate
            duplicates -= 1
        start = time.time()
        r = f(numbers)
        end = time.time()
        diff = end - start
        if not ref_global:
            ref_global = diff
        if not ref_local:
            ref_local = diff
        print n, diff, diff / ref_local, diff / ref_global
        ref_local = diff

# MacBook-Pro:daily-coding-problem jordi$ python problem.140.py 
# 10 1.97887420654e-05 1.0 1.0
# 50 0.00029993057251 15.156626506 15.156626506
# 250 0.00562787055969 18.7639109698 284.397590361
# 1250 0.149276018143 26.5244227918 7543.48192771
# 6250 3.65718507767 24.4994817196 184811.39759
# 31250 99.061934948 27.0869351275 5005974.33735
