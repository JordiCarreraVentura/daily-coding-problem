
# Problem #331

> This problem was asked by LinkedIn.
>
> You are given a string consisting of the letters *x* and *y*, such as *xyxxxyxyy*. In addition, you have an operation called flip, which changes a single *x* to *y* or vice versa.
>
> Determine how many times you would need to apply this operation to ensure that all *x*'s come before all *y*'s. In the preceding example, it suffices to flip the second and sixth characters, so you should return 2.


```python
import random
```


```python
def all_x_before_all_y(solution):
    xis = [i for i, char in enumerate(solution) if char == 'x']
    yis = [i for i, char in enumerate(solution) if char == 'y']
    if not xis or not yis:
        return True
    last_x = max(xis)
    first_y = min(yis)
    if last_x > first_y:
        return False
    return True


def flip(solution, change):
    # _from = one y
    # _to = one x
    _from, _to = change
    prev = solution[_to]
    solution[_to] = solution[_from]
    solution[_from] = prev
    return solution


def get_next_flip(solution):
    yis = dict([])
    for i, char in enumerate(solution):
        if char != 'y':
            continue
        yis[i] = [j for j, char in enumerate(solution) if j > i and char == 'x']
    yis_by_span = sorted(
        [item for item in yis.items() if item[1]],
        reverse=True,
        key=lambda x: max(x[1]) - x[0]
    )
    return (yis_by_span[0][0], max(yis_by_span[0][1]))


def f(test):
    changes = 0
    solution = [step for step in test]
    while True:
        if all_x_before_all_y(solution):
            print ''.join(solution)
            return changes
        next_flip = get_next_flip(solution)
        solution = flip(solution, next_flip)
        changes += 1
    print ''.join(solution)
    return -1
```


```python
tests = [
    ['x' if random.random() >= 0.5 else 'y' for _ in range(random.randrange(2, 12))]
    for _ in range(10)
]

for test in tests:
    print ''.join(test)
    print f(test)
    print
```

    yxxxyxyxyx
    xxxxxxyyyy
    2
    
    yyyyyyyx
    xyyyyyyy
    1
    
    yxyxyyxxy
    xxxxyyyyy
    2
    
    yyx
    xyy
    1
    
    yyyyyxxyx
    xxxyyyyyy
    3
    
    xyxxyyxx
    xxxxxyyy
    2
    
    yxyy
    xyyy
    1
    
    yyyyxy
    xyyyyy
    1
    
    xyyxyxxxxx
    xxxxxxxyyy
    3
    
    xxxyx
    xxxxy
    1
    

