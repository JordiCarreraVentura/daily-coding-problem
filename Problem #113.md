
# Problem #113

> This problem was asked by Google.
> 
> Given a string of words delimited by spaces, reverse the words in string. For example, given "hello world here", return "here world hello"
>
> Follow-up: given a mutable string representation, can you perform this operation in-place?

[Definition](https://en.wikipedia.org/wiki/In-place_algorithm) of in-place operation.


```python
test = "hello world here"
test = "alpha beta gamma delta epsilon eta"

def f(test):
    out = ''
    word = ''
    for char in test:
        if char != ' ':
            word += char
        else:
            out = '%s %s' % (word, out)
            word = ''
    out = '%s %s' % (word, out)
    return out

print(test)
print(f(test))
```

    alpha beta gamma delta epsilon eta
    eta epsilon delta gamma beta alpha 



```python
def in_place(test):
    
    def insert(test, moved, i, w):
        spaces = 0
        if not moved:
            test = test[i + 1:] + ' ' + w
        else:
            for j in range(1, len(test)):
                if spaces >= moved:
                    break
                if test[-j] == ' ':
                    spaces += 1
            test = '%s %s %s' % (test[i + 1:-(j - 1)], w, test[-(j - 2):])
        return test
    
    moved = 0
    to_move = test.count(' ')
    while moved < to_move:
        i = test.index(' ')
        w = test[:i]
        test = insert(test, moved, i, w)
        moved += 1
    return test

print(test)
print(in_place(test))
```

    alpha beta gamma delta epsilon eta
    eta epsilon delta gamma beta alpha



```python

```
