
# Problem #275

> This problem was asked by Epic.
> 
> The "look and say" sequence is defined as follows: beginning with the term 1, each subsequent term visually describes the digits appearing in the previous term. The first few terms are as follows:
> 
> 1
>
> 11
>
> 21
>
> 1211
>
> 111221
>
> As an example, the fourth term is 1211, since the third term consists of one 2 and one 1.
> 
> Given an integer N, print the Nth term of this sequence.


```python
import random
```


```python

# Using a 'while' loop to iterate over 
# the sequence of look-and-say digits.

def f(test):
    
    def get_digits(num):
        digits = []
        digit = []
        prev = None
        num = list(num)
        while num:
            curr = num.pop(0)
            if not prev:
                digit.append(curr)
            elif prev and prev == curr:
                digit.append(curr)
            elif prev and prev != curr:
                if digit:
                    digits.append(digit)
                    digit = [curr]
            prev = curr
        if digit:
            digits.append(digit)
        return digits
    
    if test == 1:
        return test
    num = '1'
    while test > 1:
        test -= 1
        digits = get_digits(num)
        num = ''.join(['%d%s' % (len(digit), digit[0]) for digit in digits])
    return num
```


```python

# Using a 'for' loop to iterate over 
# the sequence of look-and-say digits.

def _f(test):
    if test == 1:
        return test
    num = ['1']
    while test > 1:
        l = len(num)
        nums = []
        count = 1
        for i in range(l):
            if i == l - 1:
                nums.append((count, num[i]))
            else:
                x = num[i]
                y = num[i + 1]
                if x == y:
                    count += 1
                else:
                    nums.append((count, x))
                    count = 1
        num = ''.join(['%d%s' % (c, x) for c, x in nums])
        test -= 1
    return num
```


```python
# f(5)

for test in range(1, 10):
    print test, f(test), _f(test)
    print
```

    1 1 1
    
    2 11 11
    
    3 21 21
    
    4 1211 1211
    
    5 111221 111221
    
    6 312211 312211
    
    7 13112221 13112221
    
    8 1113213211 1113213211
    
    9 31131211131221 31131211131221
    

