
# Problem #233

> This problem was asked by Apple.
>
> Implement the function fib(n), which returns the nth number in the Fibonacci sequence, using only O(1) space.


```python
import random
```


```python
def f(n):
    _n = 1
    if n < 1:
        return None
    elif n == 1:
        return 0
    before_last = 1
    last = 1
    curr = last
    while _n < (n - 2):
        print '[%d] %s%d + %d = %d' % (_n + 2, ' ' * _n, before_last, last, before_last + last)
        curr = before_last + last
        before_last = last
        last = curr
        _n += 1
    return curr
```


```python
for n in [random.randrange(1, 10) for _ in range(1, 3)]:
    print '\nx=%d' % n
    y = f(n)
    print 'y=%d' % y
```

    
    x=5
    [3]  1 + 1 = 2
    [4]   1 + 2 = 3
    y=3
    
    x=5
    [3]  1 + 1 = 2
    [4]   1 + 2 = 3
    y=3

