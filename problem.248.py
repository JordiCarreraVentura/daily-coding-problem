# This problem was asked by Nvidia.
# 
# Find the maximum of two numbers without using any if-else statements, branching, or direct comparisons.

import random

def f(x, y):
    a, b = x, y
    while a and b:
        a -= 1
        b -= 1
    if a:
        return x
    else:
        return y

if __name__ == '__main__':
    
    tests = list([random.randrange(0, 1000) for _ in range(10)])
    random.shuffle(tests)
    
    for i in range(0, len(tests) - 1, 2):
        x = tests[i]
        y = tests[i + 1]
        print x, y, f(x, y)
