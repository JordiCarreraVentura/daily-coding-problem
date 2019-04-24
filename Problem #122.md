
# Problem #122

> This question was asked by Zillow.
>
> You are given a 2-d matrix where each cell represents number of coins in that cell. Assuming we start at matrix\[0\]\[0\], and can only move right or down, find the maximum number of coins you can collect by the bottom right corner.
>
> For example, in this matrix
>
`0 3 1 1
2 0 0 4
1 5 3 1`
>
> The most we can collect is 0 + 2 + 1 + 5 + 3 + 1 = 12 coins.


```python
import random
```


```python
def make_matrix(x, y, min_val=0, max_val=6):
    rows = []
    while len(rows) < y:
        row = [random.randrange(min_val, max_val) for _ in range(x)]
        rows.append(row)
    return rows

def f(xy, path, i, j, val):
    
    val += xy[i][j]
    val_under, val_right = -1, -1
    _path = [node for node in path]
    _path.append(('x=%d,y=%d,%d(+%d)' % (j, len(xy) - i, val, xy[i][j])))

#     print '%s%s' % (' ' * i, ''.join(['_' if _j != j else '*' for _j in range(len(xy[0]))])), i, j, val

    if i < len(xy) - 1:
        val_under, path_under = f(xy, _path, i + 1, j, val)
    if j < len(xy[i]) - 1:
        val_right, path_right = f(xy, _path, i, j + 1, val)
        
    if val_under > -1 and val_right > -1:
        if val_right < val_under:
            return val_under, path_under
        else:
            return val_right, path_right
    elif val_under > -1:
        return val_under, path_under
    elif val_right > -1:
        return val_right, path_right

    return val, _path
    
```


```python
# f([
#     [0, 3, 1, 1],
#     [2, 0, 0, 4],
#     [1, 5, 3, 1]
# ], [], 0, 0, 0)

for _ in range(3):
    x, y = random.randrange(3, 6), random.randrange(3, 6)
    xy = make_matrix(x, y)
    print '%d x %d' % (y, x)
    for row in xy:
        print row
    best, path = f(xy, [], 0, 0, 0)
    print best
    print path
    print
```

    5 x 4
    [1, 5, 3, 4]
    [5, 4, 2, 2]
    [1, 5, 2, 1]
    [4, 4, 1, 3]
    [0, 3, 2, 2]
    26
    ['x=0,y=5,1(+1)', 'x=1,y=5,6(+5)', 'x=1,y=4,10(+4)', 'x=1,y=3,15(+5)', 'x=1,y=2,19(+4)', 'x=1,y=1,22(+3)', 'x=2,y=1,24(+2)', 'x=3,y=1,26(+2)']
    
    3 x 3
    [2, 0, 1]
    [1, 1, 2]
    [3, 4, 3]
    13
    ['x=0,y=3,2(+2)', 'x=0,y=2,3(+1)', 'x=0,y=1,6(+3)', 'x=1,y=1,10(+4)', 'x=2,y=1,13(+3)']
    
    4 x 3
    [2, 1, 1]
    [0, 0, 3]
    [4, 0, 5]
    [5, 5, 3]
    19
    ['x=0,y=4,2(+2)', 'x=0,y=3,2(+0)', 'x=0,y=2,6(+4)', 'x=0,y=1,11(+5)', 'x=1,y=1,16(+5)', 'x=2,y=1,19(+3)']
    

