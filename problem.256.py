# This problem was asked by Fitbit.
# 
# Given a linked list, rearrange the node values such that they appear in alternating low -> high -> low -> high ... form. For example, given 1 -> 2 -> 3 -> 4 -> 5, you should return 1 -> 3 -> 2 -> 5 -> 4.


#   01 12 23 34
#   02 21 14 43

import random

def f(nodes, edges):
    space = [x for x in edges]
    out = []
    last = 0
    for i in range(0, len(edges) - 1, 2):
        first, second = edges[i], edges[i + 1]
        a, b = first
        b, c = second
        out += [(last, b + 1), (c, b)]
        last = b
    return out


if __name__ == '__main__':

    # Generate toy test dataset
    nodes = sorted([random.randint(0, 20) for _ in range(random.randint(5, 15))])
#     nodes = [1, 2, 3, 4, 5]
    
    indexes = list(range(len(nodes)))
    
    edges = []
    for i in range(len(indexes) - 1):
        edge = (i, i + 1)
        edges.append(edge)
    
    # 
    #for edge in sorted(edges, key=lambda x: (nodes[x[0]], nodes[x[1]])):
    print nodes
    print '---'
    print edges
    print '---'
    for edge in edges:
        a, b = edge
        if b != None:
            print edge, (nodes[a], nodes[b])
        else:
            print edge, (nodes[a], None)

    print '---'
    for edge in f(nodes, edges):
        a, b = edge
        if b != None:
            print edge, (nodes[a], nodes[b])
        else:
            print edge, (nodes[a], None)
