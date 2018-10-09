# This problem was asked by Palantir.
# 
# Typically, an implementation of in-order traversal of a binary tree has O(h) space complexity, where h is the height of the tree. Write a program to compute the in-order traversal of a binary tree using O(1) space.

import random
import time

from tqdm import tqdm


def generate_tree(l):
    tree = []
    vertices = list(range(l))
    roots = [vertices.pop(0)]
    while vertices:
        _roots = []
        for root in roots:
            _l = len(vertices)
            if _l < 1:
                break
            elif _l < 2:
                tree.append([root, vertices.pop(0)])
                break
            else:
                a = vertices.pop(0)
                b = vertices.pop(0)
                tree.append([root, a])
                tree.append([root, b])
                r = random.random()
                if r > 0.75:
                    _roots += [a, b]
                elif r > 0.50:
                    _roots.append(a)
                elif r > 0.25 or not _roots:
                    _roots.append(b)
                    
        roots = _roots
    return tree


def f(test):
    q = 0
    start = time.time()
    for node in test:
        q += 1
    return time.time() - start
    

def f(test):

    def unroll(parent, children):
        out = []
        try:
            a, b = children[parent]
            out += unroll(a, children)
            out.append(parent)
            out += unroll(b, children)
        except KeyError:
            out = [parent]
        except ValueError:
            a = children[parent][0]
            out.append(parent)
            out += unroll(a, children)
        return out

    start = time.time()
    parents = []
    children = dict([])
    for parent, child in test:
        if not children.has_key(parent):
            children[parent] = []
            parents.append(parent)
        children[parent].append(child)
    
    out = unroll(parents[0], children)
    return time.time() - start


if __name__ == '__main__':

#     test = [
#         (1, 2),
#         (1, 3),
#         (2, 4),
#         (2, 5)
#     ]
#     f(test)
#     exit()
    
    n_tests = 10000
    first = None
    so_far = []
    for l in [5, 10, 20, 40, 80, 160, 320, 640, 1280]:
        tests = []
        tt = []
        for i in tqdm(range(n_tests)):
            tt.append(f(generate_tree(l)))
        avg_time = sum(tt) / len(tt)

        if not first:
            first = avg_time
            so_far.append(first)
            print l, avg_time
        elif so_far:
            estim_first = first * (l / 5)
            proj_time = sum(so_far) / len(so_far)
            estim_time = (l / 5) * proj_time
            print 'n=%d avg_t=%.12f projected_from_first=%.12f projected_from_average=%.12f ratio_first_to_average=%.12f' % (
                l, avg_time, estim_first, estim_time, estim_first / estim_time
            )
            so_far.append(avg_time / (l / 5))

