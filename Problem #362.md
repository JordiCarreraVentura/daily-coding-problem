
# Problem #362

> This problem was asked by Twitter.
>
> A strobogrammatic number is a positive number that appears the same after being rotated 180 degrees. For example, 16891 is strobogrammatic.
>
> Create a program that finds all strobogrammatic numbers with N digits.


```python
ROTATIONS = {
    0: 0,
    1: 1,
    9: 6,
    6: 9,
    8: 8
}


def rotates(num):
    digits = list(str(num))
    for i, digit in enumerate(digits):
        if not ROTATIONS.has_key(int(digits[-(i + 1)])) \
        or not ROTATIONS.has_key(int(digit)):
            return False
        elif ROTATIONS[int(digits[-(i + 1)])] != int(digit):
            return False
    return True

    
def f(n):
    
    out = []
    curr = 1
    while True:
        if curr / (10 ** n) >= 1:
            break
        if rotates(curr):
            out.append(curr)
        curr += 1
    return out


print 16891, rotates(16891)
print 16890, rotates(16890)
```

    16891 True
    16890 False



```python
for x in range(1, 6):
    print x, f(x)
```

    1 [1, 8]
    2 [1, 8, 11, 69, 88, 96]
    3 [1, 8, 11, 69, 88, 96, 101, 111, 181, 609, 619, 689, 808, 818, 888, 906, 916, 986]
    4 [1, 8, 11, 69, 88, 96, 101, 111, 181, 609, 619, 689, 808, 818, 888, 906, 916, 986, 1001, 1111, 1691, 1881, 1961, 6009, 6119, 6699, 6889, 6969, 8008, 8118, 8698, 8888, 8968, 9006, 9116, 9696, 9886, 9966]
    5 [1, 8, 11, 69, 88, 96, 101, 111, 181, 609, 619, 689, 808, 818, 888, 906, 916, 986, 1001, 1111, 1691, 1881, 1961, 6009, 6119, 6699, 6889, 6969, 8008, 8118, 8698, 8888, 8968, 9006, 9116, 9696, 9886, 9966, 10001, 10101, 10801, 11011, 11111, 11811, 16091, 16191, 16891, 18081, 18181, 18881, 19061, 19161, 19861, 60009, 60109, 60809, 61019, 61119, 61819, 66099, 66199, 66899, 68089, 68189, 68889, 69069, 69169, 69869, 80008, 80108, 80808, 81018, 81118, 81818, 86098, 86198, 86898, 88088, 88188, 88888, 89068, 89168, 89868, 90006, 90106, 90806, 91016, 91116, 91816, 96096, 96196, 96896, 98086, 98186, 98886, 99066, 99166, 99866]

