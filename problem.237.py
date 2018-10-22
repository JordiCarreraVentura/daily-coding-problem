# A tree is symmetric if its data and shape remain unchanged when it is reflected about the root node. The following tree is an example:
# 
#         4
#       / | \
#     3   5   3
#   /           \
# 9              9
# Given a k-ary tree, determine whether it is symmetric.


def f(test):

    def recur(test, terminals, curr, i):
        
        def children(test, i):
            return [y for y, (parent, value) in enumerate(test) if parent == i]
        
        parent, value = test[i]
        if i in terminals:
            return [[x for x in curr] + [value]]
        else:
            paths = []
            for child in children(test, i):
                paths += recur(test, terminals, [x for x in curr] + [value], child)
            return paths
    
    def as_tuples(paths):
        return [tuple(path) for path in paths]
    
    node_ids = set(range(len(test)))
    roots = set(zip(*test)[0])
    terminals =  node_ids - roots
    paths = as_tuples(recur(test, terminals, [], 0))
    
#     print test
#     print 'node_ids', node_ids
#     print 'roots', roots
#     print 'terminals', terminals
#     print paths
    return paths == list(reversed(paths))



if __name__ == '__main__':
    
    tests = [

        #   positive
        [
            (None, 4), (0, 3), (0, 5), (0, 3), (1, 9), (3, 9)
        ],
        
        #   positive
        [
            (None, 4), (0, 3), (0, 5), (0, 3), (1, 9),
            (2, 12), (3, 9), (4, 15), (5, 12), (6, 15)
        ],
        
        #   positive
        [
            (None, 4), (0, 3), (0, 3)
        ],
        
        #   negative
        [
            (None, 4), (0, 3), (0, 5)
        ],
        
        #   negative
        [
            (None, 4), (0, 3), (0, 5), (0, 3), (1, 9),
            (2, 12), (3, 9), (4, 15), (5, 12), (6, 16)
        ]
    ]
    
    for test in tests:
        print test
        print f(test)
        print
