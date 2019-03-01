
# Problem #363

> This problem was asked by Squarespace.
> 
> Write a function, add_subtract, which alternately adds and subtracts curried arguments. Here are some sample operations:
> 
> *add_subtract(7) -> 7*
> 
> *add_subtract(1)(2)(3) -> 1 + 2 - 3 -> 0*
> 
> *add_subtract(-5)(10)(3)(9) -> -5 + 10 - 3 + 9 -> 11*


```python
import random

def f(items):
    if len(items) == 1:
        return items[0]
    elif len(items) == 2:
        a, b = items
        return a + b
    else:
        curr = items.pop(0)
        while items:
            if len(items) < 2:
                return curr + items[0]
            a = items.pop(0)
            b = items.pop(0)
            curr += a
            curr -= b
        return curr
```


```python
# Create some random tests
tests = [
    [ random.randrange(1, 10) if random.random() >= 0.2 else -random.randrange(1, 10)
        for _ in range(random.randrange(1, 7))
    ] for _ in range(20)
]

# Add exercise tests
tests += [
    [7],
    [1, 2, 3],
    [-5, 10, 3, 9]
]

# Run tests through function
for test in tests:
    print 'input:', test
    print 'output:', f(test)
    print
```

    input: [3, 1, 3, 3, 8, 5]
    output: 1
    
    input: [4, 4, 6]
    output: 2
    
    input: [9, -6, 8, 3]
    output: -2
    
    input: [9, 2]
    output: 11
    
    input: [1, 3, 1, -9, 4, 2]
    output: -8
    
    input: [7]
    output: 7
    
    input: [9]
    output: 9
    
    input: [2, 7, 1]
    output: 8
    
    input: [6]
    output: 6
    
    input: [8, 6, 6, 5, -1, 9]
    output: 23
    
    input: [2, -9]
    output: -7
    
    input: [6, 3]
    output: 9
    
    input: [5, -1, 6, 9]
    output: 7
    
    input: [9, 4, 9, 6]
    output: 10
    
    input: [-3, 3, -1, -9, 9]
    output: -17
    
    input: [9]
    output: 9
    
    input: [9, 8, -8]
    output: 25
    
    input: [8, 9, 8, 3, 9, -7]
    output: -4
    
    input: [-8]
    output: -8
    
    input: [-6, 5, 8, -6, 1, 3]
    output: -13
    
    input: [7]
    output: 7
    
    input: [1, 2, 3]
    output: 0
    
    input: [-5, 10, 3, 9]
    output: 11
    

