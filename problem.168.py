
# This problem was asked by Facebook.
# 
# Given an N by N matrix, rotate it by 90 degrees clockwise.
# 
# For example, given the following matrix:
# 
# [[1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]]
# you should return:
# 
# [[7, 4, 1],
#  [8, 5, 2],
#  [9, 6, 3]]
#
# Follow-up: What if you couldn't use any extra space?

def f(matrix):
    nX = len(matrix)
    nY = len(matrix[0]) - 1
    reversed = [
        [None for column in vector]
        for vector in matrix
    ]
    
    # 0,0 -> 0,2    1,0 -> 0,1    2,0 -> 0,0
    # 0,1 -> 1,2    1,1 -> 1,1    2,1 -> 1,0
    # 0,2 -> 2,2    1,2 -> 2,1    2,2 -> 2,0
    for i, row in enumerate(matrix):
        for j, column in enumerate(row):
            reversed[j][nY - i] = column
    
    return reversed


if __name__ == '__main__':

    test = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    for row in f(test):
        print row
