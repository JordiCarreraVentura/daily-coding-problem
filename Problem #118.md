
# Problem #118

> This problem was asked by Google.
>
> Given a sorted list of integers, square the elements and give the output in sorted order.
>
> For example, given *\[-9, -2, 0, 2, 3\]*, return *\[0, 4, 4, 9, 81\]*.


```python
import random


tests = [
    [-9, -2, 0, 2, 3]
]

tests += [
    sorted([
        n if random.random() > 0.5 else -n
         for n in random.sample(range(10), random.randrange(3, 10))
    ]) for _ in range(9)
]

# tests = [
#     [-5, -4, -2, -1, 6, 7, 9]
# ]
```


```python
def f(test):
    negatives = [n for n in test if n < 0]
    squared = [n ** 2 for n in test if n >= 0]
    while negatives:
        n = abs(negatives.pop(0)) ** 2
        for insert_at, val in enumerate(squared):
            if val > n:
                squared.insert(insert_at, n)
                break
        else:
            squared.append(n)
    return squared

```


```python
for test in tests:
    print test
    print f(test)
    print
```

    [-9, -2, 0, 2, 3]
    [0, 4, 4, 9, 81]
    
    [-9, -5, -4, -3, 6]
    [9, 16, 25, 36, 81]
    
    [-9, 0, 1, 2, 3, 4]
    [0, 1, 4, 9, 16, 81]
    
    [-9, -8, -7, -5, -4, -3, -2, -1, 0]
    [0, 1, 4, 9, 16, 25, 49, 64, 81]
    
    [-9, -8, -6, -3, -2, 0, 7]
    [0, 4, 9, 36, 49, 64, 81]
    
    [-9, -8, -4, -2, -1, 0, 3, 5, 6]
    [0, 1, 4, 9, 16, 25, 36, 64, 81]
    
    [-6, 0, 4, 8]
    [0, 16, 36, 64]
    
    [-9, -7, -3, 4, 5, 6]
    [9, 16, 25, 36, 49, 81]
    
    [-9, -8, -7, -4, -2, 0, 3]
    [0, 4, 9, 16, 49, 64, 81]
    
    [-6, -3, 0, 1]
    [0, 1, 9, 36]
    

