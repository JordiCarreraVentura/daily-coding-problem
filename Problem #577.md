# Problem #577

> This problem was asked by Dropbox.
>
> Given a list of words, determine whether the words can be chained to form a circle. A word X can be placed in front of another word Y in a circle if the last character of X is same as the first character of Y.
> 
> For example, the words 
> 
> _['chair', 'height', 'racket', touch', 'tunic']_
>
> can form the following circle: `chair --> racket --> touch --> height --> tunic --> chair`.


```python
def f(words):
    return search([], words)

def search(seq, space):

    if len(seq) == len(space):
        hypothesis = [(space[i][0], space[i][-1]) for i in seq]
        prev = hypothesis.pop(0)
        hypothesis.append(prev)
        z = [''.join(x) for x in hypothesis]
        q = seq
        a, b = len(hypothesis), len(space)
        while hypothesis:
            curr = hypothesis.pop(0)
            if prev[-1] != curr[0]:
                return False
            prev = curr
        return ' --> '.join([space[i] for i in seq])

    for i, pair in enumerate(space):
        _seq = [prev for prev in seq] + [i]
        if [i for i in _seq if _seq.count(i) > 1]:
            continue
        h = search(_seq, space)
        if h:
            return h

    return False
    
```


```python
tests = [
    ['chair', 'height', 'racket', 'touch', 'tunic'],
    ['height', 'racket', 'touch', 'tunic'],
]

for test in tests:
    print(test, f(test))
    
```

    ['chair', 'height', 'racket', 'touch', 'tunic'] chair --> racket --> touch --> height --> tunic
    ['height', 'racket', 'touch', 'tunic'] False



```python

```
