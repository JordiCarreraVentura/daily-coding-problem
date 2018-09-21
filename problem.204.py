# This problem was asked by Amazon.
# 
# Given a complete binary tree, count the number of nodes in faster than O(n) time. Recall that a complete binary tree has every level filled except the last, and the nodes in the last level are filled starting from the left.

import random
import time


def On(tree):
    return len([x for x in tree])
#     return len(tree)


def _On(tree, n=100):
    q = 0
    while True:
        slice = tree[:n]
        if len(slice) == n:
            q += n
            tree = tree[n:]
        else:
            q += len(slice)
            break
    return q


def generate_trees(n):

    def populate_non_terminals(curr, levels):
        tree = [(True, None, 1)]
        while max([x[1] for x in tree]) < levels - 1:
            _tree = []
            extension = []
            for node in tree:
                active, parent, num = node
                if not active:
                    _tree.append(node)
                else:
                    a = (True, num, curr + 1)
                    b = (True, num, curr + 2)
                    curr += 2
                    _node = (False, parent, num)
                    _tree.append(_node)
                    extension += [a, b]
            tree = _tree + extension
        return curr, tree

    def populate_terminals(curr, tree):
        _tree = []
        extension = []
        for i, node in enumerate(tree):
            active, parent, num = node
            if not active:
                _tree.append((parent, num))
            else:
                branch = random.random() > 0.5
                if not branch:
                    _tree.append((parent, num))
                    if i < len(tree) - 1:
                        _tree += [(p, n) for _, p, n in tree[i + 1:]]
                    break
                else:
                    _tree.append((parent, num))
                    a = (num, curr + 1)
                    b = (num, curr + 2)
                    extension += [a, b]
                    curr += 2
        return _tree + extension

    curr = 1
    trees = []
    for i in range(n):
        levels = random.randrange(3, 25)
        curr, tree = populate_non_terminals(curr, levels)
        tree = populate_terminals(curr, tree)
        trees.append(tree)
    return trees


def chron(f, test, slice_size=slice):
    start = time.time()
    if slice_size and f == _On:
        f(test, n=slice)
    else:
        f(test)
    return time.time() - start


if __name__ == '__main__':

    NN = [100, 1000, 10000, 100000, 500000, 1000000, 10000000]

    data = generate_trees(1000000)
    dids = range(len(data))
    datasets = {
        n: [data[did] for did in random.sample(dids, n)]
        for n in NN
    }    

    for slice in [5, 10, 20, 50, 75, 100]:

        _first = None
        
        for n in NN:

            tests = datasets[n]

            On_times = []
            _On_times = []
            for test in tests:
                On_time = chron(On, test, slice_size=slice)
                _On_time = chron(_On, test)
                On_times.append(On_time)
                _On_times.append(_On_time)

            On_avg = sum(On_times) / len(On_times)
            _On_avg = sum(_On_times) / len(_On_times)
        
            if not _first:
                _first = On_avg / n
                print slice, n, '\tOn_avg', On_avg, '\t_On_avg', _On_avg
            else:
                r = (sum(On_times) / n) / _first
                _r = (sum(_On_times) / n) / _first
                print slice, n, '\tOn_avg', On_avg, r, '\t_On_avg', _On_avg, _r
