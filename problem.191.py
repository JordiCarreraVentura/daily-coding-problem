# This problem was asked by Stripe.
# 
# Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
# 
# Intervals can "touch", such as [0, 1] and [1, 2], but they won't be considered overlapping.
# 
# For example, given the intervals (7, 9), (2, 4), (5, 8), return 1 as the last interval can be removed and the first two won't overlap.
# 
# The intervals are not necessarily sorted in any order.

import random

def f(test):
    
    if len(test) < 2:
        return [], 0
    
    def count_intervals(intervals_by_position):
        dist = dict([])
        for intervals in intervals_by_position.values():
            if len(intervals) < 2:
                continue
            for interval in intervals:
                if not dist.has_key(interval):
                    dist[interval] = 0
                dist[interval] += 1
        return dist
    
    def maxfreq_interval(interval_dist):
        hist = [
            (interval, freq) for interval, freq in interval_dist.items()
            if freq > 1
        ]
        if not hist:
            return None
        hist.sort(key=lambda x: x[1])
        return hist[-1][0]
    
    def subtract(intervals_by_position, to_remove):
        for position, intervals in intervals_by_position.items():
            intervals_by_position[position] = [
                interval for interval in intervals
                if interval != to_remove
            ]

    #   area by interval
    area_by_interval = dict([])
    for i, (start, end) in enumerate(test):
        area_by_interval[i] = set(range(start, end + 1))

    #   intervals by position
    intervals_by_position = dict([])
    for i, area in area_by_interval.items():
        for position in area:
            if not intervals_by_position.has_key(position):
                intervals_by_position[position] = []
            intervals_by_position[position].append(i)
    
    #   repeat until none of the positions 
    #   is mapped to more than one interval:
    removed = []
    while [
        position for position, intervals in intervals_by_position.items()
        if len(intervals) > 1
    ] and len(removed) < len(test) - 1:
        interval_dist = count_intervals(intervals_by_position)
        to_remove = maxfreq_interval(interval_dist)
        if to_remove == None:
            break
        subtract(intervals_by_position, to_remove)
        removed.append(to_remove)
    
    return [test[i] for i in removed], len(removed)



if __name__ == '__main__':

    base_tests = [
        [
            random.randrange(1, 25) for j in range(random.randrange(1, 10))
        ]
        for i in range(48)
    ]

    tests = [
        [(7, 9), (2, 4), (5, 8)],
        [(0, 1), (1, 2)]
    ] + [
        [(minim, minim + random.randrange(1, 15)) for minim in base_test]
        for base_test in base_tests
    ]
    
    for test in tests:
        edits, n_edits = f(test)
        print test
        print n_edits, edits
        print [interval for interval in test if interval not in edits]
        print
    

