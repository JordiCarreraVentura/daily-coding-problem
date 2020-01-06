# Problem #411

> This problem was asked by Google.
>
> Given a string which we can delete at most _k_, return whether you can make a palindrome.
>
> For example, given `waterrfetawx` and a _k_ of 2, you could delete `f` and `x` to get `waterretaw`.


```python
def is_palindrome(string):
    if string == get_palindrome(string):
        return True
    return False

def get_palindrome(string):
    return ''.join(list(reversed(string)))

def f(string, k):
    if is_palindrome(string):
        return get_palindrome(string)
    if not k:
        return None
    for i, ch in enumerate(string):
        _string = string[:i] + string[i + 1:]
        __string = f(_string, k - 1)
        if __string:
            return __string
    return None
        
    
```


```python
for k in [1, 2, 3, 4]:

    for test in [
        'waterrfetawx',
        'waterretaw',
        'tiroliro',
        'tiroKPorit'
    ]:
        print(test, k, f(test, k))
    print()
```

    waterrfetawx 1 None
    waterretaw 1 waterretaw
    tiroliro 1 None
    tiroKPorit 1 tiroPorit
    
    waterrfetawx 2 waterretaw
    waterretaw 2 waterretaw
    tiroliro 2 None
    tiroKPorit 2 tiroPorit
    
    waterrfetawx 3 watefetaw
    waterretaw 3 waterretaw
    tiroliro 3 None
    tiroKPorit 3 iroPori
    
    waterrfetawx 4 aterreta
    waterretaw 4 waterretaw
    tiroliro 4 None
    tiroKPorit 4 iroori
    

