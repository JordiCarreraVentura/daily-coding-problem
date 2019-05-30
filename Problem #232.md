
# Problem #232

> This problem was asked by Google.
>
> Implement a PrefixMapSum class with the following methods:
>
> - `insert(key: str, value: int):` Set a given key's value in the map. If the key already exists, overwrite the value.
> - `sum(prefix: str):` Return the sum of all values of keys that begin with a given prefix.
>
> For example, you should be able to run the following code:
> 
> ```
> mapsum.insert("columnar", 3)
> assert mapsum.sum("col") == 3
> ```
> ```
> mapsum.insert("column", 2)
> assert mapsum.sum("col") == 5
> ```


```python
class PrefixMapSum:
    
    def __init__(self):
        self.data = dict([])
    
    def insert(self, key, val):
        self.data[key] = val
    
    def __incr_lookup(self, prefix, key):
        for i, letter in enumerate(prefix):
            if i >= len(key) or key[i] != letter:
                return False
        return True
    
    def sum(self, prefix):
        out = 0
        for key, val in self.data.items():
            if self.__incr_lookup(prefix, key):
                out += val
        return out
```


```python
pms = PrefixMapSum()
pms.insert('columnar', 3)
print pms.sum('col')
pms.insert('column', 2)
print pms.sum('col')
```

    3
    5

