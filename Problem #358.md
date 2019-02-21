
# Problem #358

> This problem was asked by Dropbox.
> 
> Create a data structure that performs all the following operations in *O(1)* time:
> 
> - **plus**: Add a key with value 1. If the key already exists, increment its value by one.
> - **minus**: Decrement the value of a key. If the key's value is currently 1, remove it.
> - **get_max**: Return a key with the highest value.
> - **get_min**: Return a key with the lowest value.


```python
import random
import time
import tqdm

from collections import defaultdict as deft
from tqdm import tqdm
```


```python
class Counter:
    
    def __init__(self):
        self.keys_by_f = dict([])
        self.F = dict([])
    
    def plus(self, key):
        if not self.F.has_key(key):
            self.F[key] = 1
            self.__fupdate(key, None, self.F[key])
        else:
            _n = self.F[key]
            n = _n + 1
            self.F[key] = n
            self.__fupdate(key, _n, n)
    
    def __fupdate(self, key, old, new):
        if old != None:
            self.keys_by_f[old] = self.keys_by_f[old] - set([key])
        if new != None and not self.keys_by_f.has_key(new):
            self.keys_by_f[new] = set([key])
        elif new != None:
            self.keys_by_f[new].update(set([key]))

    def minus(self, key):
        if not self.F.has_key(key):
            return
        else:
            _n = self.F[key]
            n = _n - 1
            if n:
                self.F[key] = n
                self.__fupdate(key, _n, n)
            else:
                del self.F[key]
                self.__fupdate(key, _n, None)
    
    def get_max(self):
        maxim = self.__get_max()
        if maxim != None and self.keys_by_f[maxim]:
            return random.choice(list(self.keys_by_f[maxim]))
        else:
            None
    
    def __get_max(self, minimize=False):
        val = None
        for _val in self.keys_by_f.keys():
            if val == None:
                val = _val
                continue
            if not minimize and _val > val:
                val = _val
            elif minimize and _val < val:
                val = _val
        return val
    
    def get_min(self):
        minim = self.__get_max(minimize=True)
        if minim != None and self.keys_by_f[minim]:
            return random.choice(list(self.keys_by_f[minim]))
        else:
            None
    
```

## Proof of concept test


```python
c = Counter()

test = [
    (True, [1, 2, 3, 4, 5]),
    (True, [1, 1, 1, 1, 2, 2, 2]),
    (True, [1, 1, 1, 1, 2, 2, 2]),
    (True, [1, 1, 1, 1]),
    (False, [2, 2, 2]),
    (False, [2, 2, 2])
]

for (add_or_subtract, items) in test:
    for item in items:
        if add_or_subtract:
            c.plus(item)
        else:
            c.minus(item)

print c.get_max()
print c.get_min()
print c.F
```

    1
    3
    {1: 13, 2: 1, 3: 1, 4: 1, 5: 1}


## *O(1)* complexity test


```python
# (plus, minus, get_max, get_min)
PROBS = [
    (0.25, 0.5, 0.75, 1.0),
    (0.3, 0.6, 0.8, 1.0),
    (0.4, 0.8, 0.9, 1.0),
    (0.2, 0.4, 0.7, 1.0),
    (0.1, 0.2, 0.6, 1.0),
]

times = deft(list)
for probs in PROBS:
    print probs
    for xp in tqdm(list(range(1000))):
        c = Counter()
        start = time.time()
        for _ in range(1000):
            n = random.randrange(1, 100)
            p = random.random()
            for i, prob in enumerate(probs):
                if p < prob:
                    if i == 0:
                        c.plus(i)
                    elif i == 1:
                        c.minus(i)
                    elif i == 2:
                        c.get_max()
                    else:
                        c.get_min()
                    break 
        runtime = time.time() - start
        times[probs].append(runtime)

        
for prob, runtimes in times.items():
    print prob, len(runtimes), sum(runtimes) / len(runtimes)
```

      1%|          | 8/1000 [00:00<00:13, 73.30it/s]

    (0.25, 0.5, 0.75, 1.0)


    100%|██████████| 1000/1000 [00:11<00:00, 84.08it/s]
      1%|          | 9/1000 [00:00<00:11, 88.45it/s]

    (0.3, 0.6, 0.8, 1.0)


    100%|██████████| 1000/1000 [00:14<00:00, 68.91it/s]
      1%|          | 12/1000 [00:00<00:08, 119.47it/s]

    (0.4, 0.8, 0.9, 1.0)


    100%|██████████| 1000/1000 [00:10<00:00, 96.85it/s]
      1%|          | 9/1000 [00:00<00:12, 79.90it/s]

    (0.2, 0.4, 0.7, 1.0)


    100%|██████████| 1000/1000 [00:12<00:00, 80.43it/s]
      1%|          | 12/1000 [00:00<00:08, 115.46it/s]

    (0.1, 0.2, 0.6, 1.0)


    100%|██████████| 1000/1000 [00:11<00:00, 86.57it/s]

    (0.4, 0.8, 0.9, 1.0) 1000 0.0101159570217
    (0.25, 0.5, 0.75, 1.0) 1000 0.0116818377972
    (0.2, 0.4, 0.7, 1.0) 1000 0.0122194430828
    (0.3, 0.6, 0.8, 1.0) 1000 0.0142225179672
    (0.1, 0.2, 0.6, 1.0) 1000 0.0112858295441


    

