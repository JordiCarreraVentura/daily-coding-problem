# This problem was asked by Apple.
# 
# Given the root of a binary tree, find the most frequent subtree sum. The subtree sum of a node is the sum of all values under a node, including the node itself.
# 
# For example, given the following tree:
# 
#   5
#  / \
# 2  -5
# Return 2 as it occurs twice: once as the left leaf, and once as the sum of 2 + 5 - 5.

import random


def f(tree):
    
    def get_leaves():
        terminals = dict()
        for i, vertex in enumerate(tree):
            _id = vertex[1]
            children = [v for v in tree[i:] if v[2] == _id]
            if children:
                terminals[_id] = False
            else:
                terminals[_id] = True
        return terminals
    
    def add_all_children(_id, tree):
        ids = [_id]
        summed = 0
        while ids:
            _ids = []
            for vertex in tree:
                _, __id, parent, value = vertex
                if parent in ids:
                    _ids.append(__id)
                    summed += value
            ids = _ids
        return summed
    
    terminals = get_leaves()

    sums = dict([])
    for vertex in tree[::-1]:
        _, _id, parent, value = vertex
        if terminals[_id]:
            summed = value
        else:
            summed = value + add_all_children(_id, tree)

        if not sums.has_key(summed):
            sums[summed] = []
        sums[summed].append(vertex)
    
    ranks = sums.items()
    ranks.sort(reverse=True, key=lambda x: len(x[1]))
#     
#     for x in ranks:
#         print x
    
    return len(ranks[0][1])


def binary_tree(n, min_value=1, max_value=10):

    def randnode():
        return random.randrange(min_value, max_value + 1)
    
    def expand(curr, n):
        boost = (1 - (curr / float(n))) / 2
        if random.random() + boost >= 0.5:
            return True
        return False

    vertices = []
    while len(vertices) < n:
        if not vertices:
            vertices.append((True, len(vertices), None, randnode()))
            continue
        expanded = False
        for i, vertex in enumerate(vertices):
            active, _id, parent, value = vertex
            if len(vertices) >= n:
                break
            if not active:
                continue
            if not expand(len(vertices), n):
                vertices[i] = (False, _id, parent, value)
                continue
            child1 = (True, len(vertices), _id, randnode())
            child2 = (True, len(vertices) + 1, _id, randnode())
            vertices += [child1, child2]
            expanded = True
        if not expanded and len(vertices) < n:
            i = random.randrange(0, len(vertices))
            manually_expanded = vertices[i]
            _, b, c, d = manually_expanded
            vertices[i] = (True, b, c, d)

    return vertices
    


if __name__ == '__main__':
    
    tree = binary_tree(100, max_value=5)

    tree = [
        (False, 0, None, 5),
        (False, 1, 0, 2),
        (False, 2, 0, -5)
    ]
    
#     for i, vertex in enumerate(tree):
#         print '%d:' % i, vertex
    print f(tree)
