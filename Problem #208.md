
# Problem 208

> This problem was asked by LinkedIn.
> 
> Given a linked list of numbers and a pivot k, partition the linked list so that all nodes less than k come before nodes greater than or equal to k.
> 
> For example, given the linked list 5 -> 1 -> 8 -> 0 -> 3 and k = 3, the solution could be 1 -> 0 -> 5 -> 8 -> 3.


```python
import random

from copy import deepcopy as cp

# Define a set of elements for the linked list to link
scope = list(range(100))
ELEMENTS = random.sample(scope, 10)

print ELEMENTS
```

    [89, 31, 3, 0, 67, 58, 92, 15, 65, 17]



```python
# Generate the linked list

space = cp(ELEMENTS)
random.shuffle(space)

links = []
while space:
    val = space.pop(0)
    link = ELEMENTS.index(space[0]) if space else None
    links.append((val, link))

print links
```

    [(89, 6), (92, 4), (67, 7), (15, 3), (0, 2), (3, 8), (65, 9), (17, 1), (31, 5), (58, None)]



```python
# Implement pivot function

def f(links, pivot):

    def get_vals(links, pivot):
        less_thans, greater_thans = [], []
        for val, _ in links:
            if val < pivot:
                less_thans.append(val)
            elif val > pivot:
                greater_thans.append(val)
        return less_thans, greater_thans

    less_thans, greater_thans = get_vals(links, pivot)
    arranged = less_thans + greater_thans + [pivot]
    out = []
    while arranged:
        val = arranged.pop(0)
        link = ELEMENTS.index(arranged[0]) if arranged else None
        out.append((val, link))
    return out
```


```python
# Pivot the list
pivot = random.choice(zip(*links)[0])

print links
print pivot
print f(links, pivot)
```

    [(89, 6), (92, 4), (67, 7), (15, 3), (0, 2), (3, 8), (65, 9), (17, 1), (31, 5), (58, None)]
    58
    [(15, 3), (0, 2), (3, 9), (17, 1), (31, 0), (89, 6), (92, 4), (67, 8), (65, 5), (58, None)]

