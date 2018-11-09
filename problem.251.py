# This problem was asked by Amazon.
# 
# Given an array of a million integers between zero and a billion, out of order, how can you efficiently sort it? Assume that you cannot store an array of a billion elements in memory.

import collections
import json
import math
import random

from collections import Counter


class IntStream:

    def __init__(self):

        def new_int():
            return random.randrange(0, 1000000000)

        self.ints = list([new_int() for _ in range(1000000)])

    def __iter__(self):
        for i in self.ints:
            yield i


class Bucket:

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
    
    
    n_buckets = 1000
    dispatcher = 1000000000 / n_buckets
    bucket = 0
    while bucket <= n_buckets:
        sortable = []
        for n, i in enumerate(int_stream):
            _bucket = i / dispatcher
            if _bucket == bucket:
                sortable.append(i)
        print bucket, len(sortable), '%s...' % str(sortable[:5]), '%s...' % (str(sorted(sortable)[:5]))
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