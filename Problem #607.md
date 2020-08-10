# Problem #607

> This problem was asked by Walmart Labs.
> 
> There are M people sitting in a row of N seats, where M < N. Your task is to redistribute people such that there are no gaps between any of them, while keeping overall movement to a minimum.
> 
> For example, suppose you are faced with an input of `[0, 1, 1, 0, 1, 0, 0, 0, 1]`, where 0 represents an empty seat and 1 represents a person. In this case, one solution would be to place the person on the right in the fourth seat. We can consider the cost of a solution to be the sum of the absolute distance each person must move, so that the cost here would be five.
> 
> Given an input such as the one above, return the lowest possible cost of moving people to remove all gaps.


```python
import random
from copy import deepcopy as cp

arrangements = [
    [0, 1, 1, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 0, 1],
    [0, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0]
]

arrangements = [
    a for a in [
        [1 if random.random() > 0.66 else 0 for _ in range(random.randrange(12))]
        for _ in range(20)
    ]
    if sum(a) and sum(a) < len(a)
]


```


```python
def meets_adjacency_requirement(hypothesis):
    _a = cp(hypothesis[0])
    moves = hypothesis[-1]
    for person, seat in moves:
        _a[seat] = 1
        _a[person] = 0
    n_people = sum(hypothesis[0])
    for i in range(len(hypothesis[0]) - (n_people - 1)):
        if sum(_a[i:i + n_people]) == n_people:
            return True
    return False

def get_central_person(a, moves, people):
    for p, s in moves:
        a[s] = 1
        a[p] = 0
    people_indexes = [i for i, person in enumerate(a) if person]
    if len(people_indexes) > 2:
        avg_person_position = round(sum(people_indexes) / float(len(people_indexes)))
    else:
        return min(people_indexes)
    return avg_person_position

def get_furthest_person(a, moves, people):
    avg_person_position = get_central_person(a, moves, people)
    distances = []
    for person in people:
        dist = abs(person - avg_person_position)
        distances.append((person, dist))
    distances.sort(key=lambda x: x[1])
    return distances[-1][0]

def get_centermost_seat(a, moves, people, empty_seats):
    avg_person_position = get_central_person(a, moves, people)
    misplaced_position = max(people)
    distances = []
    for seat in empty_seats:
        dist = abs(seat - avg_person_position)
        distances.append((seat, dist, abs(seat - misplaced_position)))
    distances.sort(key=lambda x: (x[1], x[2]))
    return distances[0][0]

def recur(hypothesis):
    a, people, empty_seats, moves = hypothesis
    if meets_adjacency_requirement(hypothesis):
        return [hypothesis]
    if not people or not empty_seats:
        return []
    _people = cp(people)
    _empty_seats = cp(empty_seats)
    _moves = cp(moves)
    hypotheses = []
    for p in [get_furthest_person(cp(a), _moves, _people)]:
        for s in [get_centermost_seat(cp(a), _moves, _people, _empty_seats)]:
            move = (p, s)
            _moves.append(move)
            __people = set(_people) - set([p])
            __empty_seats = set(_empty_seats) - set([s])
            _hypothesis = (a, __people, __empty_seats, _moves)
            hypotheses += recur(_hypothesis)
    return hypotheses


def f(a):
    cost, moves = 0, []

    empty_seats = set([i for i, seat in enumerate(a) if not seat])
    people = set([i for i, seat in enumerate(a) if seat])
    hypothesis = (a, people, empty_seats, [])
    
    for h in recur(hypothesis):
        print(h)
    
    return cost, moves
```


```python
for a in arrangements:
    print(a)
    f(a)
    print()
```

    [1, 0, 1, 0, 0, 0, 0]
    ([1, 0, 1, 0, 0, 0, 0], {0}, {3, 4, 5, 6}, [(2, 1)])
    
    [1, 1, 0, 0, 1, 1]
    ([1, 1, 0, 0, 1, 1], {0, 1}, set(), [(5, 2), (4, 3)])
    
    [1, 0, 0, 0]
    ([1, 0, 0, 0], {0}, {1, 2, 3}, [])
    
    [0, 0, 0, 1, 0]
    ([0, 0, 0, 1, 0], {3}, {0, 1, 2, 4}, [])
    
    [0, 0, 1, 0, 0, 1]
    ([0, 0, 1, 0, 0, 1], {2}, {0, 1, 4}, [(5, 3)])
    
    [0, 1, 0, 0]
    ([0, 1, 0, 0], {1}, {0, 2, 3}, [])
    
    [0, 1, 0, 0, 1, 1, 0, 1]
    ([0, 1, 0, 0, 1, 1, 0, 1], {1, 4}, {0, 6}, [(7, 3), (5, 2)])
    
    [1, 0, 0, 1, 0, 0, 0]
    ([1, 0, 0, 1, 0, 0, 0], {0}, {2, 4, 5, 6}, [(3, 1)])
    
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0]
    ([0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0], {5}, {0, 2, 3, 7, 8, 10}, [(9, 6), (1, 4)])
    
    [1, 1, 1, 0, 1, 1, 0]
    ([1, 1, 1, 0, 1, 1, 0], {0, 1, 2, 4}, {6}, [(5, 3)])
    
    [1, 1, 0]
    ([1, 1, 0], {0, 1}, {2}, [])
    
    [0, 1, 1, 0, 0, 1, 0]
    ([0, 1, 1, 0, 0, 1, 0], {1, 2}, {0, 4, 6}, [(5, 3)])
    
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 1], {9}, {0, 1, 2, 3, 4, 5, 6, 7, 8}, [])
    
    [0, 0, 0, 1, 0, 0, 1]
    ([0, 0, 0, 1, 0, 0, 1], {3}, {0, 1, 2, 5}, [(6, 4)])
    
    [0, 0, 1, 1, 0, 1]
    ([0, 0, 1, 1, 0, 1], {2, 3}, {0, 1}, [(5, 4)])
    
    [0, 1, 0, 0]
    ([0, 1, 0, 0], {1}, {0, 2, 3}, [])
    



```python

```
