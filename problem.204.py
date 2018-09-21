# This problem was asked by Amazon.
# 
# Given a complete binary tree, count the number of nodes in faster than O(n) time. Recall that a complete binary tree has every level filled except the last, and the nodes in the last level are filled starting from the left.

import random
import time


def On(tree):
    nodes = 0
    for parent, children in tree:
        nodes += sum([1 for child in children if child != None])
    return nodes + 1


def _On(tree, n=100):
    nodes = 0
    for i in range(len(tree) - 1, -1, -1):
        parent, children = tree[i]
        weight = sum([1 for child in children if child != None])
        if not weight:
            nodes += 1
        elif weight == 1:
            nodes += 2
        else:
            nodes += i
            break
    return nodes + 1


def generate_trees(n):
    trees = []
    for i in range(n):
        levels = random.randrange(3, 7)
        tree = [(True, 1, (2, 3))]
        curr = 3
        while max([a for _, a, b in tree]) < levels:
            _tree = []
            for node in tree:
                active, parent, (n1, n2) = node
                if not active:
                    _tree.append(node)
                else:
                    _tree.append((False, parent, (n1, n2)))
                    _tree.append((True, n1, (curr + 1, curr + 2)))
                    _tree.append((True, n2, (curr + 3, curr + 4)))
                    curr += 4
            tree = _tree
        
        branching = 1
        while branching > 0:
            _tree = []
            for node in tree:
                active, parent, (n1, n2) = node
                if not active:
                    _tree.append(node)
                else:
                    _tree.append((False, parent, (n1, n2)))
                    if branching == 1:
                        _tree.append((False, n1, (curr + 1, None)))
                        _tree.append((False, n2, (None, None)))
                        curr += 1
                        branching -= 1
                    else:
                        _tree.append((False, n1, (None, None)))
                        _tree.append((False, n2, (None, None)))
                d = random.random()
                if d < 0.5:
                    branching -= 1
            tree = _tree

        trees.append(sorted([(parent, children) for (_, parent, children) in tree]))
    return trees


def chron(f, test, slice_size=0):
    start = time.time()
    if slice_size and f == _On:
        f(test, n=slice)
    else:
        f(test)
    return time.time() - start


if __name__ == '__main__':

#     NN = [100, 1000, 10000, 100000, 1000000, 10000000]
    NN = [100, 1000, 10000, 100000, 1000000]
#     NN = [5]

    data = generate_trees(max(NN))
    
#     for tree in data:
#         for node in tree:
#             print node
#         print On(tree)
#         print _On(tree)
#         print
#     exit()
    
    dids = range(len(data))
    datasets = {
        n: [data[did] for did in random.sample(dids, n)]
        for n in NN
    }    

    for slice in [5, 10, 20, 50, 75, 100]:
        
        for n in NN:

            tests = datasets[n]

            On_times = []
            _On_times = []
            for test in tests:
                On_time = chron(On, test)
                _On_time = chron(_On, test, slice_size=slice)
                On_times.append(On_time)
                _On_times.append(_On_time)
            On_avg = sum(On_times) / len(On_times)
            _On_avg = sum(_On_times) / len(_On_times)
        
            print slice, n, sum(On_times), sum(_On_times)
