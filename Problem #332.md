
# Problem #332

> This problem was asked by Jane Street.
>
> Given integers M and N, write a program that counts how many positive integer pairs (a, b) satisfy the following conditions:
>
> 1. a + b = M
>
> 1. a XOR b = N


```python
# Set up the environment

import random
```


```python
# Create test dataset

def min_max(a, b):
    if a > b:
        return b, a
    else:
        return a, b

numbers = range(1, 100)

tests = [
    min_max(*tuple(random.sample(numbers, 2)))
    for _ in range(5)
]

for test in tests:
    print test
```

    (61, 89)
    (14, 60)
    (36, 78)
    (15, 70)
    (13, 43)



```python
def counter(test):
    
    def first_condition(i, j, m):
        return True if i + j == m else False
    
    def second_condition(i, j, n):
        return True if (
            i == n and j != n
        ) or (
            i != n and j == n
        ) else False
    
    c = 0
    m, n = test
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if first_condition(i, j, n) and second_condition(i, j, m):
                print 'pairs=%d M=%d N=%d i=%d j=%d' % (c, m, n, i, j)
                c += 1
    return c

```


```python
for test in tests:
    print
    print counter(test)
```

    
    pairs=0 M=61 N=89 i=28 j=61
    pairs=1 M=61 N=89 i=61 j=28
    2
    
    pairs=0 M=14 N=60 i=14 j=46
    pairs=1 M=14 N=60 i=46 j=14
    2
    
    pairs=0 M=36 N=78 i=36 j=42
    pairs=1 M=36 N=78 i=42 j=36
    2
    
    pairs=0 M=15 N=70 i=15 j=55
    pairs=1 M=15 N=70 i=55 j=15
    2
    
    pairs=0 M=13 N=43 i=13 j=30
    pairs=1 M=13 N=43 i=30 j=13
    2

