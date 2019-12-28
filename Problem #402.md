# Problem #402

> This problem was asked by Twitter.
>
> A strobogrammatic number is a positive number that appears the same after being rotated 180 degrees. For example, 16891 is strobogrammatic.
> 
> Create a program that finds all strobogrammatic numbers with `N` digits.


```python
import random
```


```python
EQUIVALENCES = {
    '0': '0',
    '1': '1',
    '2': '',
    '3': '',
    '4': '',
    '5': '',
    '6': '9',
    '7': '',
    '8': '8',
    '9': '6'
}


def rotate(curr):
    txt_curr = list(str(curr))
    out = []
    while txt_curr:
        char = txt_curr.pop()
        if not EQUIVALENCES[char]:
            return []
            out.append(char)
        else:
            out.append(EQUIVALENCES[char])
    return int(''.join([digit for digit in out]))


def f(n_digits):
    curr = 0
    out = []
    while len(str(curr)) < n_digits:
        rev_txt_curr = rotate(curr)
        if rev_txt_curr == curr:
            out.append(curr)
        curr += 1
    return out

```


```python
for test in range(7):
    print(test, f(test))
```

    0 []
    1 []
    2 [0, 1, 8]
    3 [0, 1, 8, 11, 69, 88, 96]
    4 [0, 1, 8, 11, 69, 88, 96, 101, 111, 181, 609, 619, 689, 808, 818, 888, 906, 916, 986]
    5 [0, 1, 8, 11, 69, 88, 96, 101, 111, 181, 609, 619, 689, 808, 818, 888, 906, 916, 986, 1001, 1111, 1691, 1881, 1961, 6009, 6119, 6699, 6889, 6969, 8008, 8118, 8698, 8888, 8968, 9006, 9116, 9696, 9886, 9966]
    6 [0, 1, 8, 11, 69, 88, 96, 101, 111, 181, 609, 619, 689, 808, 818, 888, 906, 916, 986, 1001, 1111, 1691, 1881, 1961, 6009, 6119, 6699, 6889, 6969, 8008, 8118, 8698, 8888, 8968, 9006, 9116, 9696, 9886, 9966, 10001, 10101, 10801, 11011, 11111, 11811, 16091, 16191, 16891, 18081, 18181, 18881, 19061, 19161, 19861, 60009, 60109, 60809, 61019, 61119, 61819, 66099, 66199, 66899, 68089, 68189, 68889, 69069, 69169, 69869, 80008, 80108, 80808, 81018, 81118, 81818, 86098, 86198, 86898, 88088, 88188, 88888, 89068, 89168, 89868, 90006, 90106, 90806, 91016, 91116, 91816, 96096, 96196, 96896, 98086, 98186, 98886, 99066, 99166, 99866]

