# -*- encoding: utf-8 -*-

# This problem was asked by Amazon.
# 
# Given an array of a million integers between zero and a billion, out of order, how can you efficiently sort it? Assume that you cannot store an array of a billion elements in memory.

import collections
import json
import math
import random
import time

from collections import Counter


def new_int():
    return random.randrange(0, 1000000000)
        

class IntStream:            

    def __init__(self, n=1000000):

#         self.ints = list([new_int() for _ in range(1000000)])
        self.c = 0
        self.n = n

class Bucket:
    def __call__(self, bucket, dispatcher):
        for i in self:
            if i / dispatcher == bucket:
                yield i

    def __init__(self, maxref=1000000000, n_buckets=1000):
        self.buckets = dict([])
        self.k = maxref / n_buckets
    
    def __add__(self, i):
        bucket = self(i)
        self.buckets[bucket].append(i)
    
    def __call__(self, i):
        bucket = i / self.k
        if not self.buckets.has_key(bucket):
            self.buckets[bucket] = []
        return bucket
    
    def __iter__(self):
        for bucket, items in sorted(self.buckets.items()):
            yield {
                'bucket': bucket,
#                 'numbers': items,
                'n_numbers': len(items)
            }
    
    def __str__(self):
        data = [
            list(self)
        ]
        return json.dumps(data, indent=2)


class Hasher:

    def __init__(self, maxref=1000000000, loga=10):
        self.loga = loga
        self.steps = int(round(math.log(maxref, self.loga)))
    
    def __call__(self, i, verbose=False):
        step = self.steps - 1
        curr = i
        if verbose:
            print i
        hash = [0 for _ in range(1, self.steps + 1)]
        while step > -1:
            denom = 10 ** step
            divd = curr / denom
            remainder = curr % denom

#             if divd / 5.0 >= 5:
#                 hash[self.steps - (step + 1)] = 1

#             if divd:
#                 hash[self.steps - (step + 1)] = 1

            hash[self.steps - (step + 1)] = divd
            
            if verbose:
                print step, hash, '\t', curr, '\t', denom, '\t', '%d (%.1f)' % (divd, divd / 5.0), remainder
            
            curr = remainder
            step -= 1
        
#         if divd:
#             hash[-1] = 1
        while self.c < self.n:
            yield new_int()
            self.c += 1
        self.c = 0
#         for i in self.ints:
#             yield i

        if verbose:
            print tuple(hash)
            print
        return tuple(hash)
            

def f(gen, filter, prev):
    hr = Hasher(loga=10)
    buckets = defaultdict(list)
    for x in gen:
        h = hr(x)
        buckets[h].append(x)


if __name__ == '__main__':
    
    int_stream = IntStream()
    hr = Hasher(loga=3)
    hr = Hasher(loga=10)


    #   start of test cases
    tests_a = [
        1000000000, 500000000, 5000000,  # maxref
        1000, 100, 10, 5, 2, 0,          # base linear trend
    ]
    #   By not storing the whole list in memory but streaming its values instead
    #   and then sorting buckets thereof, memory usage is 10x lower.
    
    tests_b = [
        611894298, 112311810,            # all 1s
        58000, 51000, 50000, 47000,      # 50k case   
        550342022, 550342032, 550342059, # 5* case
        809624971,
        487932331,
        31140810,
    ]
    #   end of test cases

    #   start of tests 2
#     bucket = Bucket()
#     for test in tests_a + tests_b:
#         bucket + test
#     print bucket
#     exit()
    #   end of tests 2


    #   start of tests 1
#     for test in tests_a:
#     hashed = []
#     for test in tests_b:
#         h = hr(test, verbose=True)
#         hashed.append((h, test))
#     for h, test in sorted(hashed):
#         print h, '\t', test
#     exit()
    #   end of tests 1


    #   v2
#     bucket = Bucket()
#     for n, i in enumerate(int_stream):
#         bucket + i
#         if not n % 50000:
#             print n, bucket
#     print bucket
#     exit()
    #   Performance-wise, though, speed is significantly lower. Bucket-processing
    #   forces to perform several passess on the original list of items; although
    #   the memory usage in each pass is far smaller, the time spent on all those
    #   extra passes is far greater.
    
    #   Setting a higher bucket size helps; it dramatically decreases the number of
    #   passes, which is the most time-consuming step, while keeping the sorting
    #   time for each bucket constant and the memory usage to just 2x that of a
    #   bucket size 10**-2 smaller.
    
    int_stream = IntStream()
#     x = [i for i in int_stream]
#     print len(x)
#     raw_input()

    n_buckets = 100
    dispatcher = 1000000000 / n_buckets
    bucket = 0
    last = time.time()
    while bucket <= n_buckets:
        sortable = []
#         for n, i in enumerate(int_stream):
#             _bucket = i / dispatcher
#             if _bucket == bucket:
        for n, i in enumerate(int_stream(bucket, dispatcher)):
                sortable.append(i)
        print bucket, len(sortable), '%s...' % str(sortable[:5]), '%s...' % (str(sorted(sortable)[:5]))
        print time.time() - last, bucket, len(sortable), '%s...' % str(sortable[:5]), '%s...' % (str(sorted(sortable)[:5]))
        last = time.time()
        bucket += 1
    exit()
    
    
        
    #   v1
    hashes = Counter()
    for n, i in enumerate(int_stream):
        h = hr(i)
        hashes[h] += 1
        if not n % 10000:
            print n, i
            print h
            for x, f in hashes.most_common(10):
                print x, f
            print
#         if len([_h for _h in h]) == len(h):
#             exit()
    
    index = sorted(hashes.keys())

    while index:
        curr = index.pop(0)
        for x in int_stream:
            if hr(x) == curr:
                print len(index), h, x
        print '========='
