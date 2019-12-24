# Problem #396

> This problem was asked by Google.
> 
> Given a string, return the length of the longest palindromic subsequence in the string.
> 
> For example, given the following string:
> 
> `MAPTPTMTPA`
> 
> Return 7, since the longest palindromic subsequence in the string is `APTMTPA`. Recall that a subsequence of a string does not have to be contiguous!
> 
> Your algorithm should run in `O(n^2)` time and space.


```python

def make_vars(depth, ref, history, ii):
    while ii:
        i = ii.pop(0)
        if i in history:
            continue
        var = [_i  for _i in history] + [i]
        yield tuple(sorted(var))
        if depth < ref:
            for var in make_vars(depth + 1, ref, var, [_i for _i in ii]):
                yield var
    

def run(x):
    palindromes = []
    for i in range(len(x)):
        left = x[:i + 1]
        right = x[i:]
        shared = set(left).intersection(set(right))
        lefts, rights = [], []
        for j, ch in enumerate(x):
            if j < (i + 1) and ch in shared:
                lefts.append(j)
            elif ch in shared:
                rights.append(j)
        
        for fwd in make_vars(0, len(lefts), [], [l for l in lefts]):
            for bwd in make_vars(0, len(rights), [], [r for r in rights]):
                seq1 = ''.join([x[i] for i in fwd])
                seq2 = ''.join(list(reversed([x[i] for i in bwd])))
                if seq1 == seq2:
                    fwd_last = fwd[-1]
                    bwd_first = bwd[0]
                    if bwd_first - fwd_last == 2:
                        fwd = tuple(list(fwd) + [fwd_last + 1])
                        bwd = tuple([bwd_first - 1] + list(bwd))
                    palindromes.append(''.join([x[i] for i in sorted(set(fwd).union(bwd))]))
    
    if not palindromes:
        return None
    return sorted(palindromes, key=lambda x: len(x)).pop()


ii = [0, 1, 2, 3]
print(list(make_vars(0, len(ii), [], ii)))
```

    [(0,), (0, 1), (0, 1, 2), (0, 1, 2, 3), (0, 1, 3), (0, 2), (0, 2, 3), (0, 3), (1,), (1, 2), (1, 2, 3), (1, 3), (2,), (2, 3), (3,)]



```python
tests = [
    'aba',
    'aa',
    'foomemebar',
    'omeaembr',
    'asdfasdffdsafoobar',
    'f1o2o3o4o5fiiru',
    'f1o2o3o45f',
    'mefooembar',   # 0,1(,2,3,4),5,6   0-6, 1-5
    'MAPTPTMTPA',
]
```


```python
for test in tests:
    print(test, run(test))

```

    aba aba
    aa aa
    foomemebar eme
    omeaembr meaem
    asdfasdffdsafoobar afasdffdsafa
    f1o2o3o4o5fiiru foo3oof
    f1o2o3o45f fo3of
    mefooembar meooem
    MAPTPTMTPA APTMTPA



```python
import random
import time

ALPHABET = list('abcdefghijklmopqrstuvwxyz')

def word():
    return ''.join([random.choice(ALPHABET) for _ in range(random.randrange(3, 10))])


prev = None
for n in [10, 100, 1000, 10000, 100000]:
    tests = [word() for _ in range(n)]
    start = time.time()
    hits = 0
    for test in tests:
        palindromes = run(test)
        if palindromes:
            hits += 1
            #print(n, hits, test, palindromes)
    elapsed = time.time() - start
    avg_len = sum([len(w) for w in tests]) / n
    print(n, hits, avg_len, elapsed, (elapsed / prev) if prev else 1.0)
    prev = elapsed
```

    10 7 7.3 0.0011210441589355469 1.0
    100 42 5.79 0.0059430599212646484 5.301361122926414
    1000 455 5.981 0.06019711494445801 10.128976611706182
    10000 4743 6.0324 0.8556089401245117 14.213454264609778
    100000 46644 5.99674 6.381108999252319 7.457973730760357



```python

```
