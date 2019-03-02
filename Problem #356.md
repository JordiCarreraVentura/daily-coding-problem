
# Problem #356

> This problem was asked by Netflix.
> 
> Implement a queue using a set of fixed-length arrays.
> 
> The queue should support _enqueue, dequeue_, and _get_size_ operations.


```python
class Queue:
    def __init__(self, n):
        self.n = n
        self.data = [[]]
    
    def get_size(self):
        if len(self.data) == 1:
            return len(self.data[0])
        elif len(self.data) == 2:
            return len(self.data[0] + self.data[-1])
        else:
            out = sum([self.n for _ in range(len(self.data) - 2)])
            return out + len(self.data[0] + self.data[-1])
    
    def enqueue(self, item):
        self.data[-1].append(item)
        if len(self.data[-1]) == self.n:
            self.data.append([])
    
    def dequeue(self):
        if not self.data or not self.data[0]:
            return None
        item = self.data[0].pop(0)
        if not len(self.data[0]) and len(self.data) > 1:
            self.data = self.data[1:]
        return item
```


```python
import random

q = Queue(5)

numbers = range(10)
random.shuffle(numbers)

for n in numbers:
    if random.random() < 0.65:
        q.enqueue(n)
        print 'enqueue %d, new size: %d' % (n, q.get_size())
    else:
        m = q.dequeue()
        q.enqueue(n)
        print 'dequeue %s, enqueue %d, new size: %d' % (str(m), n, q.get_size())
```

    enqueue 4, new size: 1
    enqueue 7, new size: 2
    enqueue 2, new size: 3
    dequeue 4, enqueue 9, new size: 3
    dequeue 7, enqueue 1, new size: 3
    dequeue 2, enqueue 0, new size: 3
    enqueue 3, new size: 4
    enqueue 5, new size: 5
    enqueue 6, new size: 6
    dequeue 9, enqueue 8, new size: 6

