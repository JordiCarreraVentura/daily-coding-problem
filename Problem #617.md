# Problem #617

> This problem was asked by Facebook.
> 
> Given a number in Roman numeral format, convert it to decimal.
>
> The values of Roman numerals are as follows:
> 
> ```
> {
>     'M': 1000,
>     'D': 500,
>     'C': 100,
>     'L': 50,
>     'X': 10,
>     'V': 5,
>     'I': 1
> }
> ```
> 
> In addition, note that the Roman numeral system uses subtractive notation for numbers such as IV and XL.
> 
> For the input XIV, for instance, you should return 14.


```python
import math
    
    
TABLE = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}

RANGE = sorted(list(TABLE.items()), key=lambda x: x[1], reverse=True)


def decode(roman):
    space = list(roman)
    val = 0
    prev = None
    while space:
        letter = space.pop()
        if prev and TABLE[letter] < TABLE[prev]:
            val -= TABLE[letter]
        else:
            val += TABLE[letter]
        prev = letter
    return val


def encode_order(num):
    encoding = ''
    if not num:
        return encoding
    while num:
        _letter, _order = None, None
        for letter, order in reversed(RANGE):
            if _order and order > num:
                n = int(num / _order)
                encoding += _letter * n
                num %= _order
            _letter, _order = letter, order
        if not encoding:
            n = int(num / _order)
            encoding += _letter * n
            num %= _order
    return remove_four_consecutive(encoding)


def remove_four_consecutive(encoding):
    romans = [roman for roman, _ in reversed(RANGE)]
    consecutive = False
    for char in set(encoding):
        if encoding.count(char) > 3:
            consecutive = True
            break
    if not consecutive:
        return encoding
    value = decode(encoding)
    for letter, order in reversed(RANGE):
        if order > value:
            break
    delta = abs(TABLE[letter] - value)
    to_subtract = encode(delta)
    _encoding = to_subtract + letter
    return _encoding


def encode(decimal):
    thousands = 0
    hundreds = 0
    tens = 0
    units = 0
    while decimal:
        loga = int(math.log(decimal, 10))
        denom =  10 ** loga
        val = int(decimal / denom)
        decimal = decimal % denom

        if loga >= 3:
            thousands = val * (10 ** loga)
        elif loga >= 2:
            hundreds = val * (10 ** loga)
        elif loga >= 1:
            tens = val * (10 ** loga)
        else:
            units = val
    
    thousands = encode_order(thousands)
    hundreds = encode_order(hundreds)
    tens = encode_order(tens)
    units = encode_order(units)

    return thousands + hundreds + tens + units

```


```python
for test in [
    'XIV',         # 14
    'XXXIX',       # 39
    'CCXLVI',      # 246
    'DCCLXXXIX',   # 789
    'MMCDXXI'      # 2421
]:
    print(test, decode(test), encode(decode(test)))
```

    XIV 14 XIV
    XXXIX 39 XXXIX
    CCXLVI 246 CCXLVI
    DCCLXXXIX 789 DCCLXXXIX
    MMCDXXI 2421 MMCDXXI

