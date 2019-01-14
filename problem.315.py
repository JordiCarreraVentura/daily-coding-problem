# This problem was asked by Google.
# 
# In linear algebra, a Toeplitz matrix is one in which the elements on any given diagonal from top left to bottom right are identical.
# 
# Here is an example:
# 
# 1 2 3 4 8
# 5 1 2 3 4
# 4 5 1 2 3
# 7 4 5 1 2
# Write a program to determine whether a given input is a Toeplitz matrix.

import random


def f(matrix):
    n_rows = len(matrix)
    n_columns = len(matrix[0])
    are_toeplitz = True
    for row in range(n_rows):
        for column in range(n_columns):
            cursor = (row, column)
            is_toeplitz = True
            while cursor[0] < n_rows and cursor[1] < n_columns:
                a, b = cursor
                if matrix[a][b] != matrix[row][column]:
                    is_toeplitz = False
                    break
                cursor = (a + 1, b + 1)
            if not is_toeplitz:
                are_toeplitz = False
                break
        if not are_toeplitz:
            break
    if are_toeplitz:
        return True
    return False


def new_matrix():
    rows, columns = random.randrange(3, 6), random.randrange(3, 6)
    return [
        [random.randrange(1, 10) for _ in range(columns)]
        for _ in range(rows)
    ]
    



if __name__ == '__main__':
    
    #   correct test
    test = [
        [1, 2, 3, 4, 8],
        [5, 1, 2, 3, 4],
        [4, 5, 1, 2, 3],
        [7, 4, 5, 1, 2]
    ]

    #   incorrect (7 blocks 1s)
    test = [
        [1, 2, 3, 4, 8],
        [5, 1, 2, 3, 4],
        [4, 5, 7, 2, 3],
        [7, 4, 5, 1, 2]
    ]

    #   incorrect (6 blocks 1s)
    test = [
        [1, 2, 3, 4, 8],
        [5, 1, 2, 3, 4],
        [4, 5, 1, 2, 3],
        [7, 4, 5, 6, 2]
    ]

    #   incorrect (7 blocks 4s)
    test = [
        [1, 2, 3, 4, 8],
        [5, 1, 2, 3, 7],
        [4, 5, 1, 2, 3],
        [7, 4, 5, 1, 2]
    ]
    
    f(test)
    
    toeplitz = 0
    for i in range(1000000):
        if not i % 100000:
            print i, toeplitz, round(toeplitz / 1000000.0, 2)

        matrix = new_matrix()
        if f(matrix):
            for row in matrix:
                print row
            print
            toeplitz += 1
        
        
