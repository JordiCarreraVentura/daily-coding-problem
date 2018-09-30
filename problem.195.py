# This problem was asked by Google.
# 
# Let M be an N by N matrix in which every row and every column is sorted. No two elements of M are equal.
# 
# Given i1, j1, i2, and j2, compute the number of elements of M smaller than M[i1, j1] and larger than M[i2, j2].

import math
import random



def make_matrix(m, values):
    rows = []
    row = []
    while values:
        val = values.pop(0)
        row.append(val)
        if len(row) == m:
            rows.append([x for x in row])
            row = []
    return rows


def f2(matrix, first, last):

    # v2
    m1, n1 = first
    m2, n2 = last
    n_d = len(matrix[0])
    
    if m1 == m2:
        return n2 - n1
    else:
        q = n_d - (n1 + 1)
        q += n2
        if m2 - m1 > 1:
            for r in range(1, m2 - m1):
                q += n_d
        return q


def f(matrix, first, last):

    # v1
    m1, n1 = first
    m2, n2 = last
    out = []
    m_d = len(matrix)
    n_d = len(matrix[0])
    
    out = []
    m, n = m1, n1
    while m <= m2:
        start, end = 0, n_d

        if not out:
            start = n1 + 1
        if m == m2:
            end = n2
        
        out += matrix[m][start:end]
        m += 1

    print 'range:', out
    return len(out)
    
    
    



if __name__ == '__main__':

    for i in range(5):

        d = random.randrange(4, 20)

        M = d
        N = d

        mn = M * N

        if mn < 10:
            space = list(range(int(mn * math.log(mn, 2))))
        elif mn < 35:
            space = list(range(int(mn * math.log(mn, 4))))
        else:
            space = list(range(int(mn * math.log(mn, 10))))

        values = sorted(random.sample(space, mn), reverse=True)

        matrix = make_matrix(M, values)

        for row in matrix:
            print row

        coordinates = sorted(random.sample(list(range(d)), 4))

        x = (coordinates[0], coordinates[1])
        y = (coordinates[2], coordinates[3])
#         x = (0, 1)
#         y = (0, 4)
        print f(matrix, x, y)
        print f2(matrix, x, y)
        print d
        print x, y
        print

