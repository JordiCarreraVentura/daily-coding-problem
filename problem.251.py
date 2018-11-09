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

    def __call__(self, bucket, dispatcher):
        for i in self:
            if i / dispatcher == bucket:
                yield i

    def __iter__(self):
        while self.c < self.n:
            yield new_int()
            self.c += 1
        self.c = 0
#         for i in self.ints:
#             yield i



if __name__ == '__main__':
    
    #   By not storing the whole list in memory but streaming its values instead
    #   and then sorting buckets thereof, memory usage is 10x lower.
    
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
        print time.time() - last, bucket, len(sortable), '%s...' % str(sortable[:5]), '%s...' % (str(sorted(sortable)[:5]))
        last = time.time()
        bucket += 1
