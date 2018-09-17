# This problem was asked by Google.
# 
# You are given an array of arrays of integers, where each array corresponds to a row in a triangle of numbers. For example, [[1], [2, 3], [1, 5, 1]] represents the triangle:
# 
#   1
#  2 3
# 1 5 1
# We define a path in the triangle to start at the top and go down one row at a time to an adjacent value, eventually ending with an entry on the bottom row. For example, 1 -> 3 -> 5. The weight of the path is the sum of the entries.
# 
# Write a program that returns the weight of the maximum weight path.

import random


def make_triangle():
    n_rows = random.randrange(1, 10)
    rows = []
    for i in range(n_rows):
        row = [random.randrange(1, 10) for j in range(i + 1)]
        rows.append(row)
    return rows


def cp(items):
    return [x for x in items]


def f(triangle):

    def get_adjacency_interval(row_number, position_in_row, triangle):
        left = position_in_row - 1
        right = position_in_row + 2
        if left < 0:
            left = 0
        if right > len(triangle[row_number]):
            right = len(triangle[row_number])
        return left, right

    def add(history, row_number, position_in_row, so_far, triangle):
        left, right = get_adjacency_interval(row_number, position_in_row, triangle)
        
        # when the bottom triangle row is reached, return the sum
        # of the accumulated value plus the largest value within
        # the adjacency interval:
        if row_number == len(triangle) - 1:
            last = max(triangle[row_number][left:right])
            return cp(history) + [last], so_far + last

        # until the bottom triangle row is reached, iterate over all
        # values within adjacency, call the function 'add'
        # recursively and keep the highest result:
        else:
            all = []
            for pos in range(left, right):
                num = triangle[row_number][pos]
                _history, added = add(
                    cp(history) + [num], row_number + 1, pos, so_far + num, triangle
                )
                all.append((added, pos, _history))
            all.sort()
            best_result, best_pos, best_history = all[-1]
            return best_history, best_result
    
    return add([], 0, 0, 0, triangle)



if __name__ == '__main__':

    triangles = [
        [[1]],
        [[1], [2, 3]],
        [[1], [2, 3], [1, 5, 1]],
        [[1], [2, 3], [1, 5, 1], [4, 1, 0, 4]],
        [[1], [2, 3], [1, 5, 1], [5, 7, 1, 2], [3, 8, 5, 4, 4]]
    ] + [
        make_triangle() for i in range(25)
    ]
    
    for triangle in triangles:
        for row in triangle:
            print row
        print f(triangle)
        print

