# This problem was asked by Dropbox.
# 
# Given an undirected graph G, check whether it is bipartite. Recall that a graph is bipartite if its vertices can be divided into two independent sets, U and V, such that no edge connects vertices of the same set.

import random

def new_graph():

    def num():
        return random.randrange(8, 15)

    n = num()
    vertices = list(range(n + 1))
    if random.random() > 0.25:
        addenda = list([num() for x in range(random.randrange(3, 10))])
        vertices += addenda
        
    random.shuffle(vertices)
    
    graph = []
    while len(vertices) > 1:
        a = vertices.pop(0)
        b = vertices.pop(0)
        if a != b:
            graph.append((a, b))
    return graph


def is_bipartite(graph):
    
    #   get all edges for all unique nodes, proto-set U and proto-set V

    #   get all edges with duplicate nodes;
    #   if any edge contains an element in U AND an element in V, break and false

    def count(graph):
    
        def add(counts, vertex):
            if not counts.has_key(vertex):
                counts[vertex] = 0
            counts[vertex] += 1        
    
        counts = dict([])
        for (a, b) in graph:
            add(counts, a)
            add(counts, b)
        return counts
    
    def find_unique(graph, counts):
        _U, _V, dups = set([]), set([]), set([])
        for (a, b) in graph:
            if not (counts[a] == 2 and counts[b] == 2):
                _U.add(a)
                _V.add(b)
            else:
                dups.add((a, b))
        return _U, _V, dups

    def same_set_dups(_U, _V, dups):
        for a, b in dups:
            if (a in _U and b in _U) or \
            (a in _V and b in _V):
                print '>>>>', (a, b)
                return True
        return False
    
    counts = count(graph)
    
    _U, _V, dups = find_unique(graph, counts)
    
    if not dups:
        return _U, _V
    
    if same_set_dups(_U, _V, dups):
        return None, None

    for a, b in dups:
        if a not in _U:
            _U.add(a)
        if b not in _V:
            _V.add(b)
    
    if _U.intersection(_V) == _V:
        return None, None
    return _U, _V



if __name__ == '__main__':
    
    tests = [
        [               # bipartite
            (1, 4),
            (2, 5),
            (3, 6)
        ],
        [               # bipartite
            (1, 4),
            (2, 5),
            (3, 6),
            (1, 5)
        ],
        [               # not bipartite
            (1, 4),
            (2, 5),
            (3, 6),
            (1, 2)
        ]
    ] + [
#         new_graph() for i in range(97)
#     ] + [
        [               # bipartite
            ('A', 'F'),
            ('A', 'J'),
            ('B', 'G'),
            ('B', 'H'),
            ('C', 'F'),
            ('C', 'I'),
            ('D', 'H'),
            ('D', 'I'),
            ('E', 'F'),
            ('E', 'I')
        ],
        [               # bipartite
            ('A', 'R'),
            ('A', 'S'),
            ('A', 'T'),
            ('A', 'U'),
            ('A', 'V'),
            ('B', 'U'),
            ('C', 'S'),
            ('D', 'T'),
            ('D', 'V'),
            ('E', None)
        ],
        [               # not bipartite
            (1, 2),
            (2, 3),
            (3, 4),
            (4, 5),
            (5, 6),
            (6, 7),
            (7, 8),
            (8, 1),
        ],
        [               # not bipartite
            (3, 1),
            (3, 5),
            (5, 4),
            (5, 2),
            (4, 6),
            (2, 6),
            (1, 7),
            (7, 2),
            (6, 8),
            (7, 8)
        ],
        [               # bipartite
            (1, 2),
            (2, 3),
            (2, 5),
            (3, 4),
        ],
        [               # not bipartite
            (1, 2),
            (2, 3),
            (3, 4),
            (4, 5),
            (5, 1),
        ],
        [               # not bipartite
            ('A', 'B'),
            ('B', 'C'),
            ('C', 'D'),
            ('D', 'A'),
        ],
#         [               # not bipartite
#             
#         ],
        [               # bipartite # ERROR
            ('A', 'B'),
            ('A', 'D'),
            ('B', 'C'),
            ('C', 'D')
        ],
        [               # bipartite
            ('A', 'B'),
            ('A', 'D'),
            ('A', 'F'),
            ('C', 'B'),
            ('C', 'D'),
            ('E', 'B'),
            ('E', 'D'),
            ('E', 'F'),
        ],
        [               # bipartite
            ('B', 'A'),
            ('A', 'D'),
            ('A', 'F'),
            ('C', 'B'),
            ('D', 'C'),
            ('E', 'B'),
            ('D', 'E'),
            ('F', 'E'),
        ]
    ]
    
    for test in tests:
        print
        for edge in test:
            print edge
        U, V = is_bipartite(test)
        if U:
            print 'U', U
            print 'V', V
            print 'is_bipartite'
        else:
            print 'U', U
            print 'V', V
            print 'not_bipartite'
