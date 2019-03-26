
# Problem #293

> This problem was asked by Uber.
> 
> You have N stones in a row, and would like to create from them a pyramid. This pyramid should be constructed such that the height of each stone increases by one until reaching the tallest stone, after which the heights decrease by one. In addition, the start and end stones of the pyramid should each be one stone high.
> 
> You can change the height of any stone by paying a cost of 1 unit to lower its height by 1, as many times as necessary. Given this information, determine the lowest cost method to produce this pyramid.
> 
> For example, given the stones _[1, 1, 3, 3, 2, 1]_, the optimal solution is to pay 2 to create _[0, 1, 2, 3, 2, 1]_.


```python
import random
```


```python
tests = [
    [random.randrange(0, 4) for _ in range(random.randrange(3, 15))]
    for _ in range(20)
]
```


```python

def adjust(i, pyramid):
    pyramids = []

    vertex = pyramid[i]
    
    broke = False
    curr_left = i - 1
    curr_right = i + 1

    while curr_left >= 0 and curr_right < len(pyramid) and not broke:
        cost_adjustment = 0
        pyramid_area = list(range(curr_left, curr_right + 1))
        base = len(pyramid_area)
        height = (curr_right - i) + 1

        if [pyramid[j] for j in pyramid_area if not pyramid[j]]:
            return pyramids
        
        if vertex < height:
            return pyramids
        elif (vertex - i) > height:
            cost_adjustment += vertex - height
        
        ideal = list(range(1, height)) + [height] + list(reversed(list(range(1, height))))
        
        for j, adjusted_stones in enumerate(ideal):
            original_stones = pyramid[pyramid_area[j]]
            if original_stones < adjusted_stones:
                return pyramids
            cost_adjustment += original_stones - adjusted_stones

        cost_flat_left = sum([stones for stones in pyramid[:min(pyramid_area)]])
        cost_flat_right = sum([stones for stones in pyramid[max(pyramid_area) + 1:]])
        cost = cost_flat_left + cost_flat_right + cost_adjustment
        new_pyramid = [0 for _ in pyramid[:min(pyramid_area)]] + \
                      ideal + \
                      [0 for _ in pyramid[max(pyramid_area) + 1:]]
        pyramids.append((cost, new_pyramid))
        curr_left -= 1
        curr_right += 1

    return pyramids



def f(test):
    pyramids = []
    for i, stones in enumerate(test):
        if not i or i == len(test) - 1:
            continue
        pyramid = [x for x in test]
        pyramids += adjust(i, pyramid)
        print pyramids
    if pyramids:
        pyramids.sort()
        best_pyramid = pyramids[0]
    else:
        best_pyramid = None
    if best_pyramid:
        return best_pyramid
    else:
        return (0, None)
#     return cost, pyramid

# tests = [
#     [2, 3, 2, 2, 1, 3]
# ]

for test in tests:
    print test
    cost, pyramid = f(test)
    print '>>>>', cost, pyramid
    print
```

    [3, 3, 1, 3]
    [(6, [1, 2, 1, 0])]
    [(6, [1, 2, 1, 0])]
    >>>> 6 [1, 2, 1, 0]
    
    [2, 0, 0, 0, 3, 3, 3, 0, 1, 3, 3, 3, 1, 0]
    []
    []
    []
    []
    [(18, [0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0])]
    [(18, [0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0])]
    [(18, [0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0])]
    [(18, [0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0])]
    [(18, [0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0]), (18, [0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0])]
    [(18, [0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0]), (18, [0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0]), (18, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0]), (13, [0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 2, 1, 0])]
    [(18, [0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0]), (18, [0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0]), (18, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0]), (13, [0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 2, 1, 0]), (18, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 0])]
    [(18, [0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0]), (18, [0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0]), (18, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0]), (13, [0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 2, 1, 0]), (18, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 0])]
    >>>> 13 [0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 2, 1, 0]
    
    [1, 2, 2, 1, 1, 1, 0, 3, 1, 3, 0, 1, 0, 0]
    [(12, [1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])]
    [(12, [1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), (12, [0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])]
    [(12, [1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), (12, [0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])]
    [(12, [1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), (12, [0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])]
    [(12, [1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), (12, [0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])]
    [(12, [1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), (12, [0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])]
    [(12, [1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), (12, [0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])]
    [(12, [1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), (12, [0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])]
    [(12, [1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), (12, [0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])]
    [(12, [1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), (12, [0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])]
    [(12, [1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), (12, [0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])]
    [(12, [1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), (12, [0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])]
    >>>> 12 [0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    [3, 2, 1, 3, 1, 3, 2, 2, 1, 1, 0]
    [(15, [1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0])]
    [(15, [1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0])]
    [(15, [1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0]), (15, [0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0])]
    [(15, [1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0]), (15, [0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0])]
    [(15, [1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0]), (15, [0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0]), (15, [0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0])]
    [(15, [1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0]), (15, [0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0]), (15, [0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0]), (15, [0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0])]
    [(15, [1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0]), (15, [0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0]), (15, [0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0]), (15, [0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0]), (15, [0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0])]
    [(15, [1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0]), (15, [0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0]), (15, [0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0]), (15, [0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0]), (15, [0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0])]
    [(15, [1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0]), (15, [0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0]), (15, [0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0]), (15, [0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0]), (15, [0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0])]
    >>>> 15 [0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0]
    
    [2, 1, 1, 3, 3, 0, 3, 3, 1, 0, 1, 3]
    []
    []
    [(17, [0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0])]
    [(17, [0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0])]
    [(17, [0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0])]
    [(17, [0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0])]
    [(17, [0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0]), (17, [0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0])]
    [(17, [0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0]), (17, [0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0])]
    [(17, [0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0]), (17, [0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0])]
    [(17, [0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0]), (17, [0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0])]
    >>>> 17 [0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0]
    
    [0, 0, 3]
    []
    >>>> 0 None
    
    [3, 2, 2, 2, 1, 1, 0, 1, 3, 0, 1]
    [(12, [1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0])]
    [(12, [1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0]), (12, [0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0])]
    [(12, [1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0]), (12, [0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0]), (12, [0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0])]
    [(12, [1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0]), (12, [0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0]), (12, [0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0])]
    [(12, [1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0]), (12, [0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0]), (12, [0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0])]
    [(12, [1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0]), (12, [0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0]), (12, [0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0])]
    [(12, [1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0]), (12, [0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0]), (12, [0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0])]
    [(12, [1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0]), (12, [0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0]), (12, [0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0])]
    [(12, [1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0]), (12, [0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0]), (12, [0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0])]
    >>>> 12 [0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0]
    
    [0, 0, 2, 2, 1, 2, 1, 2, 2, 3]
    []
    []
    [(11, [0, 0, 1, 2, 1, 0, 0, 0, 0, 0])]
    [(11, [0, 0, 1, 2, 1, 0, 0, 0, 0, 0])]
    [(11, [0, 0, 1, 2, 1, 0, 0, 0, 0, 0]), (11, [0, 0, 0, 0, 1, 2, 1, 0, 0, 0])]
    [(11, [0, 0, 1, 2, 1, 0, 0, 0, 0, 0]), (11, [0, 0, 0, 0, 1, 2, 1, 0, 0, 0])]
    [(11, [0, 0, 1, 2, 1, 0, 0, 0, 0, 0]), (11, [0, 0, 0, 0, 1, 2, 1, 0, 0, 0]), (11, [0, 0, 0, 0, 0, 0, 1, 2, 1, 0])]
    [(11, [0, 0, 1, 2, 1, 0, 0, 0, 0, 0]), (11, [0, 0, 0, 0, 1, 2, 1, 0, 0, 0]), (11, [0, 0, 0, 0, 0, 0, 1, 2, 1, 0]), (11, [0, 0, 0, 0, 0, 0, 0, 1, 2, 1])]
    >>>> 11 [0, 0, 0, 0, 0, 0, 0, 1, 2, 1]
    
    [1, 1, 0, 2, 3]
    []
    []
    []
    >>>> 0 None
    
    [1, 3, 3, 2, 3, 2, 0, 0]
    [(10, [1, 2, 1, 0, 0, 0, 0, 0])]
    [(10, [1, 2, 1, 0, 0, 0, 0, 0]), (10, [0, 1, 2, 1, 0, 0, 0, 0]), (5, [1, 2, 3, 2, 1, 0, 0, 0])]
    [(10, [1, 2, 1, 0, 0, 0, 0, 0]), (10, [0, 1, 2, 1, 0, 0, 0, 0]), (5, [1, 2, 3, 2, 1, 0, 0, 0]), (10, [0, 0, 1, 2, 1, 0, 0, 0])]
    [(10, [1, 2, 1, 0, 0, 0, 0, 0]), (10, [0, 1, 2, 1, 0, 0, 0, 0]), (5, [1, 2, 3, 2, 1, 0, 0, 0]), (10, [0, 0, 1, 2, 1, 0, 0, 0]), (10, [0, 0, 0, 1, 2, 1, 0, 0])]
    [(10, [1, 2, 1, 0, 0, 0, 0, 0]), (10, [0, 1, 2, 1, 0, 0, 0, 0]), (5, [1, 2, 3, 2, 1, 0, 0, 0]), (10, [0, 0, 1, 2, 1, 0, 0, 0]), (10, [0, 0, 0, 1, 2, 1, 0, 0])]
    [(10, [1, 2, 1, 0, 0, 0, 0, 0]), (10, [0, 1, 2, 1, 0, 0, 0, 0]), (5, [1, 2, 3, 2, 1, 0, 0, 0]), (10, [0, 0, 1, 2, 1, 0, 0, 0]), (10, [0, 0, 0, 1, 2, 1, 0, 0])]
    >>>> 5 [1, 2, 3, 2, 1, 0, 0, 0]
    
    [2, 2, 3, 1, 2, 3, 0, 3, 2, 1]
    [(15, [1, 2, 1, 0, 0, 0, 0, 0, 0, 0])]
    [(15, [1, 2, 1, 0, 0, 0, 0, 0, 0, 0]), (15, [0, 1, 2, 1, 0, 0, 0, 0, 0, 0])]
    [(15, [1, 2, 1, 0, 0, 0, 0, 0, 0, 0]), (15, [0, 1, 2, 1, 0, 0, 0, 0, 0, 0])]
    [(15, [1, 2, 1, 0, 0, 0, 0, 0, 0, 0]), (15, [0, 1, 2, 1, 0, 0, 0, 0, 0, 0]), (15, [0, 0, 0, 1, 2, 1, 0, 0, 0, 0])]
    [(15, [1, 2, 1, 0, 0, 0, 0, 0, 0, 0]), (15, [0, 1, 2, 1, 0, 0, 0, 0, 0, 0]), (15, [0, 0, 0, 1, 2, 1, 0, 0, 0, 0])]
    [(15, [1, 2, 1, 0, 0, 0, 0, 0, 0, 0]), (15, [0, 1, 2, 1, 0, 0, 0, 0, 0, 0]), (15, [0, 0, 0, 1, 2, 1, 0, 0, 0, 0])]
    [(15, [1, 2, 1, 0, 0, 0, 0, 0, 0, 0]), (15, [0, 1, 2, 1, 0, 0, 0, 0, 0, 0]), (15, [0, 0, 0, 1, 2, 1, 0, 0, 0, 0])]
    [(15, [1, 2, 1, 0, 0, 0, 0, 0, 0, 0]), (15, [0, 1, 2, 1, 0, 0, 0, 0, 0, 0]), (15, [0, 0, 0, 1, 2, 1, 0, 0, 0, 0]), (15, [0, 0, 0, 0, 0, 0, 0, 1, 2, 1])]
    >>>> 15 [0, 0, 0, 0, 0, 0, 0, 1, 2, 1]
    
    [2, 1, 1, 3, 2, 1, 0]
    []
    []
    [(6, [0, 0, 1, 2, 1, 0, 0])]
    [(6, [0, 0, 1, 2, 1, 0, 0]), (6, [0, 0, 0, 1, 2, 1, 0])]
    [(6, [0, 0, 1, 2, 1, 0, 0]), (6, [0, 0, 0, 1, 2, 1, 0])]
    >>>> 6 [0, 0, 0, 1, 2, 1, 0]
    
    [3, 0, 2, 0, 1, 0, 3, 2, 0, 2, 2, 0, 3, 3]
    []
    []
    []
    []
    []
    []
    []
    []
    []
    []
    []
    []
    >>>> 0 None
    
    [3, 3, 3, 1, 2, 2, 1, 1, 1, 1, 0]
    [(14, [1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0])]
    [(14, [1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0]), (14, [0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0])]
    [(14, [1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0]), (14, [0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0])]
    [(14, [1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0]), (14, [0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0]), (14, [0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0])]
    [(14, [1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0]), (14, [0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0]), (14, [0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0]), (14, [0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0])]
    [(14, [1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0]), (14, [0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0]), (14, [0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0]), (14, [0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0])]
    [(14, [1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0]), (14, [0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0]), (14, [0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0]), (14, [0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0])]
    [(14, [1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0]), (14, [0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0]), (14, [0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0]), (14, [0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0])]
    [(14, [1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0]), (14, [0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0]), (14, [0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0]), (14, [0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0])]
    >>>> 14 [0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0]
    
    [0, 0, 2]
    []
    >>>> 0 None
    
    [3, 2, 1, 3, 1, 3, 3, 0, 3, 3, 3, 0, 1, 1]
    [(23, [1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])]
    [(23, [1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])]
    [(23, [1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), (23, [0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0])]
    [(23, [1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), (23, [0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0])]
    [(23, [1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), (23, [0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]), (23, [0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0])]
    [(23, [1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), (23, [0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]), (23, [0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0])]
    [(23, [1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), (23, [0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]), (23, [0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0])]
    [(23, [1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), (23, [0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]), (23, [0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0])]
    [(23, [1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), (23, [0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]), (23, [0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0]), (23, [0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0])]
    [(23, [1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), (23, [0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]), (23, [0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0]), (23, [0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0])]
    [(23, [1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), (23, [0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]), (23, [0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0]), (23, [0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0])]
    [(23, [1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), (23, [0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]), (23, [0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0]), (23, [0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0])]
    >>>> 23 [0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0]
    
    [3, 3, 1, 2, 2, 2, 3, 1, 3]
    [(16, [1, 2, 1, 0, 0, 0, 0, 0, 0])]
    [(16, [1, 2, 1, 0, 0, 0, 0, 0, 0])]
    [(16, [1, 2, 1, 0, 0, 0, 0, 0, 0]), (16, [0, 0, 1, 2, 1, 0, 0, 0, 0])]
    [(16, [1, 2, 1, 0, 0, 0, 0, 0, 0]), (16, [0, 0, 1, 2, 1, 0, 0, 0, 0]), (16, [0, 0, 0, 1, 2, 1, 0, 0, 0])]
    [(16, [1, 2, 1, 0, 0, 0, 0, 0, 0]), (16, [0, 0, 1, 2, 1, 0, 0, 0, 0]), (16, [0, 0, 0, 1, 2, 1, 0, 0, 0]), (16, [0, 0, 0, 0, 1, 2, 1, 0, 0])]
    [(16, [1, 2, 1, 0, 0, 0, 0, 0, 0]), (16, [0, 0, 1, 2, 1, 0, 0, 0, 0]), (16, [0, 0, 0, 1, 2, 1, 0, 0, 0]), (16, [0, 0, 0, 0, 1, 2, 1, 0, 0]), (16, [0, 0, 0, 0, 0, 1, 2, 1, 0])]
    [(16, [1, 2, 1, 0, 0, 0, 0, 0, 0]), (16, [0, 0, 1, 2, 1, 0, 0, 0, 0]), (16, [0, 0, 0, 1, 2, 1, 0, 0, 0]), (16, [0, 0, 0, 0, 1, 2, 1, 0, 0]), (16, [0, 0, 0, 0, 0, 1, 2, 1, 0])]
    >>>> 16 [0, 0, 0, 0, 0, 1, 2, 1, 0]
    
    [1, 2, 0, 1, 0, 2, 3, 3, 3, 0, 2, 1]
    []
    []
    []
    []
    []
    [(14, [0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0])]
    [(14, [0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0]), (14, [0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0])]
    [(14, [0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0]), (14, [0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0])]
    [(14, [0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0]), (14, [0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0])]
    [(14, [0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0]), (14, [0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0])]
    >>>> 14 [0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0]
    
    [2, 0, 1, 3, 1, 3, 0, 3, 2, 0, 1, 1, 0, 3]
    []
    []
    [(16, [0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0])]
    [(16, [0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0])]
    [(16, [0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0])]
    [(16, [0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0])]
    [(16, [0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0])]
    [(16, [0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0])]
    [(16, [0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0])]
    [(16, [0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0])]
    [(16, [0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0])]
    [(16, [0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0])]
    >>>> 16 [0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    [1, 1, 3, 2, 3, 3, 2]
    []
    [(11, [0, 1, 2, 1, 0, 0, 0])]
    [(11, [0, 1, 2, 1, 0, 0, 0]), (11, [0, 0, 1, 2, 1, 0, 0])]
    [(11, [0, 1, 2, 1, 0, 0, 0]), (11, [0, 0, 1, 2, 1, 0, 0]), (11, [0, 0, 0, 1, 2, 1, 0]), (6, [0, 0, 1, 2, 3, 2, 1])]
    [(11, [0, 1, 2, 1, 0, 0, 0]), (11, [0, 0, 1, 2, 1, 0, 0]), (11, [0, 0, 0, 1, 2, 1, 0]), (6, [0, 0, 1, 2, 3, 2, 1]), (11, [0, 0, 0, 0, 1, 2, 1])]
    >>>> 6 [0, 0, 1, 2, 3, 2, 1]
    
