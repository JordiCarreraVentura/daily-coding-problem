
# Problem #330

> This problem was asked by Dropbox.
> 
> A Boolean formula can be said to be satisfiable if there is a way to assign truth values to each variable such that the entire formula evaluates to true.
> 
> For example, suppose we have the following formula, where the symbol ¬ is used to denote negation:
> 
> `(¬c OR b) AND (b OR c) AND (¬b OR c) AND (¬c OR ¬a)`
> 
> One way to satisfy this formula would be to let a = False, b = True, and c = True.
> 
> This type of formula, with AND statements joining tuples containing exactly one OR, is known as 2-CNF.
> 
> Given a 2-CNF formula, find a way to assign truth values to satisfy it, or return False if this is impossible.

# Remarks

1. The solution must support a list of ORs that are joined by ANDs.
1. Each OR is a pair/tuple of items where each item has a polarity/sign.
1. Must get the vocabulary of items over all pairs, then assign a value to each item, and finally test it on the whole list of disjunctions.
1. I understand I must take a string as the input. Must parse the symbol and the letters.


```python
import re

OR = re.compile('(¬?)([a-z]+) OR (¬?)([a-z]+)')


class Term:
    def __init__(self, sign, value):
        self.sign = True if not sign.strip() else False
        self.value = value

        
class Disjunction:
    def __init__(self, sign1, term1, sign2, term2):
        self.first = Term(sign1, term1)
        self.second = Term(sign2, term2)
    
    def __str__(self):
        return """<OR terms=<
    1=<value=%s sign=%s>
    2=<value=%s sign=%s>
>>""" % (self.first.value, self.first.sign, self.second.value, self.second.sign)
    
    def __call__(self, vocab):
        val1 = vocab[self.first.value]
        val2 = vocab[self.second.value]
        bool1 = val1 if self.first.sign else not val1
        bool2 = val2 if self.second.sign else not val2
        return bool1 or bool2
    

def parse_c2nf_from_string(expression):
    ands = []
    for _and in expression.split(' AND '):
        _or_parts = OR.search(_and)
        sign1, term1, sign2, term2 = \
            _or_parts.group(1).strip(), \
            _or_parts.group(2).strip(), \
            _or_parts.group(3).strip(), \
            _or_parts.group(4).strip()
        ands.append(Disjunction(sign1, term1, sign2, term2))
    return ands


def get_vocab(ands):
    vocab = dict([])
    for _and in ands:
        vocab[_and.first.value] = False
        vocab[_and.second.value] = False
    return vocab


def try_resolve(switched, ands):
    states = []
    for _and in ands:
        states.append(_and(switched))
    if all(states):
        return True
    return False


def polarity_switch(history, vocab):
    switchable = [key for key in vocab.keys() if key not in history]
    if not switchable:
        return []
    switchs = []
    for to_switch in switchable:
        switched = dict(vocab.items())
        _history = [prev for prev in history]
        _history.append(to_switch)
        switched[to_switch] = True
        switchs.append((switched, _history))
    return switchs


def try_resolve_or_polarity_switch(history, vocab, ands):
    if try_resolve(vocab, ands):
        return vocab
    for switched, _history in polarity_switch(history, vocab):
        if try_resolve(switched, ands):
            return switched
        elif len(_history) < len(switched):
            return try_resolve_or_polarity_switch(_history, switched, ands)
    return None


def two_cnf(expression):
    ands = parse_c2nf_from_string(expression)
    vocab = get_vocab(ands)
    return try_resolve_or_polarity_switch([], vocab, ands)
```


```python
tests = [
    '(¬c OR b) AND (b OR c) AND (¬b OR c) AND (¬c OR ¬a)',
    '(a OR b)',
    '(a OR b) AND (¬a OR ¬b)',
    '(a OR b) AND (¬a OR b)'
]

for test in tests:
    print(two_cnf(test))
```

    {'c': True, 'b': True, 'a': False}
    {'a': True, 'b': False}
    {'a': True, 'b': False}
    {'a': True, 'b': True}



```python

```
