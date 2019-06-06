
# Problem #271

> This problem was asked by Netflix.
> 
> Given a sorted list of integers of length N, determine if an element x is in the list without performing any multiplication, division, or bit-shift operations.
> 
> Do this in _O(log N)_ time.


```python
import time
import random


def avg(items):
    return sum(items) / len(items)


class Finder:
    
    def __init__(self, q):
        """param: int q: number searched for."""
        self.q = q
    
    def __call__(self, num):
        if num == self.q:
            return 1
        return 0


class Consumer:
    
    def __init__(self, q, slice_size=10, min_size=5):
        self.q = q
        self.slice_size = slice_size
        self.min_size = min_size
    
    def __call__(self, items):
        space = items
        slice_size = self.slice_size
        while True:
            slices = self.__slice(slice_size, space)
            if not slices:
                return False
            if len(slices) > 1:
                mapped = map(self.finder, slices)
                try:
                    some_true = mapped.index(True)
                except ValueError:
                    return False
                space = slices[some_true]
            else:
                if self.q in slices[0]:
                    return True
                return False
            slice_size = int(slice_size / 10)
            if slice_size < self.min_size:
                slice_size = self.min_size
    
    def finder(self, slice):
        if self.q < slice[0] \
        or self.q > slice[-1]:
            return False
        return True
    
    def __slice(self, slice_size, space):
        slices = []
        if len(space) < slice_size:
            return [space]
        _space = [item for item in space]
        while _space:
            slices.append(_space[:slice_size])
            _space = _space[slice_size:]
        return slices

    
def linear_finder(q, items):
    for item in items:
        if item == q:
            return True
        if item > q:
            return False
    return False


def binary_finder(q, items):
    space = items
    while True:
        middle = int(len(space) / 2)
        middle_item = space[middle]

        if q < middle_item:
            space = space[:middle]
        else:
            space = space[middle:]

        if len(space) == 2:
            if  (
                space[0] == q or
                space[1] == q
            ):
                return True
            else:
                return False
        elif len(space) == 1:
            if space[0] == q:
                return True
            return False

    
def skip_linear(q, items, skip=100):
    to_skip = skip if skip > 10 else 10
    to_retrieve = to_skip
    while True:
        to_retrieve = to_retrieve if to_retrieve < len(items) else len(items) - 1
        item = items[to_retrieve]
        if item >= q:
            start = to_retrieve - to_skip
            start = 0 if start < 0 else start
            end = to_retrieve + 1
            if q in items[start:end]:
                return True
            return False
        to_retrieve += to_skip
        if to_retrieve > len(items):
            return False


NN = [100, 1000, 10000, 100000, 1000000]  
Q = 50
N_max = 10000000

proto_space = range(N_max)
proto_queries = range(N_max, N_max * 2)

last_linear_time = None

for n in NN:

    space = sorted(random.sample(proto_space, n))

    queries = random.sample(space, Q) + random.sample(proto_queries, Q)

    runtimes = {
        'linear': [],
        'binary': [],
        'map_reduce': [],
        'consumer': [],
        'skip': []
    }

    for i, q in enumerate(queries):
        
        # Search in linear time (N)
        start = time.time()
        found_lin = linear_finder(q, space)
        linear = time.time() - start

        # Binary search in log N time
        start = time.time()
        found_bin = binary_finder(q, space)
        binary = time.time() - start

        # Search in skip-linear time (log N)
        start = time.time()
        found_skip = skip_linear(q, space, skip=n / 100)
        skip = time.time() - start

        # Parallel search with map-reduce
        f = Finder(q)
        _space = [x for x in space]
        start = time.time()
        out = map(f, _space)
        found_map = True if sum(out) else False
        map_reduce = time.time() - start

        # Slice-and-pop-search
        consumer = Consumer(q, slice_size=int(n / 10))
        start = time.time()
        found_consumer = consumer(space)
        consumed = time.time() - start

        # Keep track of runtimes
        runtimes['linear'].append(linear)
        runtimes['binary'].append(binary)
        runtimes['map_reduce'].append(map_reduce)
        runtimes['skip'].append(skip)
        runtimes['consumer'].append(consumed)
    
    
    # Display runtime benchmark
    for setting, times in runtimes.items():
        avg_time = avg(times)
        print '%d, ' % n, '%s, ' % setting, '%f, ' % avg_time, \
            'total runtime=%f, ' % sum(times), \
            'expected runtime=%f, ' % ((last_linear_time * 10) if last_linear_time else 0.0), \
            'ratio=%f' % ((sum(times) / (last_linear_time * 10)) if last_linear_time else 1.0)
    print '--'
    
    last_linear_time = sum(runtimes['linear'])
    
```

    100,  skip,  0.000006,  total runtime=0.000590,  expected runtime=0.000000,  ratio=1.000000
    100,  binary,  0.000014,  total runtime=0.001364,  expected runtime=0.000000,  ratio=1.000000
    100,  consumer,  0.000058,  total runtime=0.005821,  expected runtime=0.000000,  ratio=1.000000
    100,  linear,  0.000009,  total runtime=0.000910,  expected runtime=0.000000,  ratio=1.000000
    100,  map_reduce,  0.000072,  total runtime=0.007162,  expected runtime=0.000000,  ratio=1.000000
    --
    1000,  skip,  0.000041,  total runtime=0.004143,  expected runtime=0.009103,  ratio=0.455160
    1000,  binary,  0.000050,  total runtime=0.004961,  expected runtime=0.009103,  ratio=0.544997
    1000,  consumer,  0.000510,  total runtime=0.051010,  expected runtime=0.009103,  ratio=5.603745
    1000,  linear,  0.000109,  total runtime=0.010903,  expected runtime=0.009103,  ratio=1.197774
    1000,  map_reduce,  0.000806,  total runtime=0.080560,  expected runtime=0.009103,  ratio=8.850052
    --
    10000,  skip,  0.000032,  total runtime=0.003207,  expected runtime=0.109031,  ratio=0.029411
    10000,  binary,  0.000297,  total runtime=0.029675,  expected runtime=0.109031,  ratio=0.272168
    10000,  consumer,  0.002640,  total runtime=0.264012,  expected runtime=0.109031,  ratio=2.421434
    10000,  linear,  0.000734,  total runtime=0.073398,  expected runtime=0.109031,  ratio=0.673180
    10000,  map_reduce,  0.004247,  total runtime=0.424665,  expected runtime=0.109031,  ratio=3.894894
    --

