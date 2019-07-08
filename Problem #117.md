
# Problem #117

> This problem was asked by Facebook.
>
> Given a binary tree, return the level of the tree with minimum sum.


```python
import random

def create_binary_tree(branching_prob=0.75, decay=0.1):
    n_nodes = 12
    first_val = random.randrange(5, 10)
    values = set([first_val])
    tree = [(-1, 0, first_val, True)]
    while True:
        
        if not [active for parent, _id, value, active in tree]:
            break
        elif len(tree) >= n_nodes:
            break
        elif branching_prob <= 0.:
            break
            
        _tree = []
        added = len(tree)
        for node in tree:
            parent, _id, value, active = node
            if not active:
                _tree.append(node)
                continue
            _tree.append((parent, _id, value, False))
            if random.random() <= branching_prob:
                _parent1 = _id
                _parent2 = _id
                __id1 = added
                __id2 = added + 1
                added += 2
                _value1, _value2 = random.randrange(1, 10), random.randrange(1, 10)
                _tree.append((_parent1, __id1, _value1, True))
                _tree.append((_parent2, __id2, _value2, True))

        tree = _tree
        
        branching_prob -= decay
        
    return sorted(tree)
            
```


```python
    
def get_parents(tree, root_id, node):
    curr = node
    parent_id = node[0]
    parents = []
    while True:
        if parent_id != -1:
            parents.insert(0, parent_id)
        parent = [_node for _node in tree if _node[1] == parent_id][0]
        curr = parent
        parent_id = curr[0]
        if parent_id == -1:
            break
    return parents


def subtree_min_sum(tree, root_id, lvl):
    to_sum = []
    for node in tree:
        if node[1] == root_id:
            continue
        parents_to_root = get_parents(tree, root_id, node)
        if len(parents_to_root) == lvl:
            to_sum.append(node[2])
    return sum(to_sum)


def f(tree):
    root = [node for node in tree if node[0] == -1][0]
    root_id = root[1]
    min_sum = root[2]
    min_sum_arg = 0

    for lvl in range(1, len(tree)):
        _min_sum = subtree_min_sum(tree, root_id, lvl)
        if _min_sum and _min_sum < min_sum:
            min_sum = _min_sum
            min_sum_arg = lvl

    return (min_sum, min_sum_arg)
```


```python
for _ in range(10):

    while True:
        tree = create_binary_tree()
        if len(tree) > 1:
            break

    for node in tree:
        print(node)
    print(f(tree))
    print('----')
```

    (-1, 0, 8, False)
    (0, 1, 1, False)
    (0, 2, 5, False)
    (1, 3, 5, False)
    (1, 4, 4, False)
    (3, 5, 2, False)
    (3, 6, 9, False)
    (4, 7, 7, False)
    (4, 8, 1, False)
    (6, 1)
    ----
    (-1, 0, 5, False)
    (0, 1, 5, False)
    (0, 2, 5, False)
    (1, 3, 4, False)
    (1, 4, 2, False)
    (3, 5, 2, False)
    (3, 6, 5, False)
    (5, 7, 9, False)
    (5, 8, 3, False)
    (7, 9, 2, True)
    (7, 10, 2, True)
    (8, 11, 5, True)
    (8, 12, 6, True)
    (5, 0)
    ----
    (-1, 0, 5, False)
    (0, 1, 6, False)
    (0, 2, 7, False)
    (5, 0)
    ----
    (-1, 0, 7, False)
    (0, 1, 4, False)
    (0, 2, 5, False)
    (2, 3, 5, False)
    (2, 4, 2, False)
    (3, 5, 6, False)
    (3, 6, 9, False)
    (4, 7, 7, False)
    (4, 8, 5, False)
    (6, 9, 3, True)
    (6, 10, 4, True)
    (7, 11, 1, True)
    (7, 12, 6, True)
    (7, 0)
    ----
    (-1, 0, 6, False)
    (0, 1, 8, False)
    (0, 2, 6, False)
    (1, 3, 4, False)
    (1, 4, 5, False)
    (2, 5, 4, False)
    (2, 6, 7, False)
    (3, 7, 6, True)
    (3, 8, 6, True)
    (4, 9, 2, True)
    (4, 10, 4, True)
    (5, 11, 6, True)
    (5, 12, 6, True)
    (6, 13, 7, True)
    (6, 14, 7, True)
    (6, 0)
    ----
    (-1, 0, 5, False)
    (0, 1, 5, False)
    (0, 2, 3, False)
    (1, 3, 5, False)
    (1, 4, 3, False)
    (3, 5, 2, False)
    (3, 6, 4, False)
    (5, 7, 2, False)
    (5, 8, 3, False)
    (8, 9, 7, False)
    (8, 10, 7, False)
    (9, 11, 1, True)
    (9, 12, 9, True)
    (10, 13, 7, True)
    (10, 14, 1, True)
    (5, 0)
    ----
    (-1, 0, 7, False)
    (0, 1, 3, False)
    (0, 2, 7, False)
    (7, 0)
    ----
    (-1, 0, 8, False)
    (0, 1, 3, False)
    (0, 2, 2, False)
    (2, 3, 7, False)
    (2, 4, 9, False)
    (3, 5, 9, False)
    (3, 6, 8, False)
    (4, 7, 7, False)
    (4, 8, 9, False)
    (5, 9, 1, True)
    (5, 10, 1, True)
    (8, 11, 7, True)
    (8, 12, 1, True)
    (5, 1)
    ----
    (-1, 0, 8, False)
    (0, 1, 8, False)
    (0, 2, 8, False)
    (1, 3, 3, False)
    (1, 4, 3, False)
    (4, 5, 4, False)
    (4, 6, 3, False)
    (6, 2)
    ----
    (-1, 0, 8, False)
    (0, 1, 6, False)
    (0, 2, 2, False)
    (8, 0)
    ----

