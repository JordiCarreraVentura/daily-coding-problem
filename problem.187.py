# This problem was asked by Google.
# 
# You are given given a list of rectangles represented by min and max x- and y-coordinates. Compute whether or not a pair of rectangles overlap each other. If one rectangle completely covers another, it is considered overlapping.
# 
# For example, given the following rectangles:
# 
# {
#     "top_left": (1, 4),
#     "dimensions": (3, 3) # width, height
# },
# {
#     "top_left": (-1, 3),
#     "dimensions": (2, 1)
# },
# {
#     "top_left": (0, 5),
#     "dimensions": (4, 3)
# }
# return true as the first and third rectangle overlap each other.


import numpy as np

import random


def get_rectangles(test):

    def base_matrix(buffer_x, buffer_y, min_x, min_y, max_x, max_y):
        matrix = []
        for row in range(max_y + buffer_y + 1):
            matrix.append(np.array([0 for i in range(max_x + buffer_x + 1)]))
        return np.array(matrix)

    def fill(buffer_x, buffer_y, rect, matrix):
        start_x, start_y = rect['top_left']
        run_x, run_y = rect['dimensions']
        from_x, to_x = start_x, start_x + run_x
        from_y, to_y = start_y, start_y - run_y
        for width in range(from_x, to_x):
            for height in range(from_y, to_y, -1):
                matrix[height + buffer_y][width + buffer_x] = 1

    rects = []
    buffer_x, buffer_y = 0, 0
    
    lowest = min(
        [rect['top_left'][1] - rect['dimensions'][1] for rect in test]
    )

    leftmost = min(
        [rect['top_left'][0] for rect in test]
    )
    
    buffer_y = -lowest
    buffer_x = -leftmost

    highest = max([rect['top_left'][1] for rect in test])

    rightmost = max(
        [rect['top_left'][0] + rect['dimensions'][0] for rect in test]
    )

    for rect in test:
        matrix = base_matrix(buffer_x, buffer_y, leftmost, lowest, rightmost, highest)
        fill(buffer_x, buffer_y, rect, matrix)
        rects.append(matrix)

    return rects
    

def overlap(matrices):
    
    def display(m1, m2):
        print m1
        print '-'
        print m2
        
    l = len(matrices)
    overlapped = False
    for i in range(l - 1):
        m1 = matrices[i]
        for j in range(i + 1, l):
            m2 = matrices[j]
            m12 = m1 * m2
            o = sum([sum(x) for x in m12])
            display(m1, m2)
            if o:
                overlapped = True
                print True
            else:
                print False
            raw_input('----')
    return overlapped
            
    



if __name__ == '__main__':

    tests = [[
        {
            "top_left": (1, 4),
            "dimensions": (3, 3) # width, height
        },
        {
            "top_left": (-1, 3),
            "dimensions": (2, 1)
        },
        {
            "top_left": (0, 5),
            "dimensions": (4, 3)
        }
    ]] + [
        [
            {
                'top_left': (random.randrange(-5, 5), random.randrange(-5, 5)),
                'dimensions': (random.randrange(1, 10), random.randrange(1, 10)),
            },
            {
                'top_left': (random.randrange(-5, 5), random.randrange(-5, 5)),
                'dimensions': (random.randrange(1, 10), random.randrange(1, 10)),
            }
        ],
        [
            {
                'top_left': (random.randrange(-5, 5), random.randrange(-5, 5)),
                'dimensions': (random.randrange(1, 10), random.randrange(1, 10)),
            },
            {
                'top_left': (random.randrange(-5, 5), random.randrange(-5, 5)),
                'dimensions': (random.randrange(1, 10), random.randrange(1, 10)),
            }
        ]
    ]
    
    for test in tests:
        matrices = get_rectangles(test)
        overlapped = overlap(matrices)
