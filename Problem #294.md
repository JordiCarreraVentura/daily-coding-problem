
# Problem #294

> This problem was asked by Square.
> 
> A competitive runner would like to create a route that starts and ends at his house, with the condition that the route goes entirely uphill at first, and then entirely downhill.
> 
> Given a dictionary of places of the form {location: elevation}, and a dictionary mapping paths between some of these locations to their corresponding distances, find the length of the shortest route satisfying the condition above. Assume the runner's home is location 0.
> 
> For example, suppose you are given the following input:



```python
elevations = {0: 5, 1: 25, 2: 15, 3: 20, 4: 10}
paths = {
    (0, 1): 10,
    (0, 2): 8,
    (0, 3): 15,
    (1, 3): 12,
    (2, 4): 10,
    (3, 4): 5,
    (3, 0): 17,
    (4, 0): 10
}
```

> In this case, the shortest valid path would be 0 -> 2 -> 4 -> 0, with a distance of 28.


```python
HOME = 0


def next_points(route):
    last_end = route[-1][1]
    out = []
    for (start, end) in paths.keys():
        if start == last_end:
            out.append((start, end))
    return out


def flatten(route):
    steps = []
    for start, _ in route:
        steps.append(start)
    steps.append(route[-1][1])
    return steps


def upwards_then_downwards(routes):
    new = []
    for route in routes:
        steps = flatten(route)
        elevation_gains = [
            elevations[steps[i]] - elevations[steps[i - 1]]
            for i in range(1, len(steps))
        ]
        ups = [i for i, gain in enumerate(elevation_gains) if gain > 0]
        downs = [i for i, gain in enumerate(elevation_gains) if gain < 0]
        if downs[0] < ups[-1]:
            continue
        new.append(route)
    return new


def shortest(routes):
    return sorted(routes, key=lambda x: sum([paths[point] for point in x]))[0]


def f(routes):
    new = []
    for route in routes:
        if route and route[0][0] == HOME and route[-1][1] == HOME:
            new.append(route)
            continue
        for next_point in next_points(route):
            _route = [x for x in route] + [next_point]
            new += f([_route])
    new = upwards_then_downwards(new)   # all potential routes with those paths meet this condition
    return new

print f([[point] for point in paths.keys() if point[0] == HOME])
print shortest(f([[point] for point in paths.keys() if point[0] == HOME]))
```

    [[(0, 1), (1, 3), (3, 0)], [(0, 1), (1, 3), (3, 4), (4, 0)], [(0, 3), (3, 0)], [(0, 3), (3, 4), (4, 0)], [(0, 2), (2, 4), (4, 0)]]
    [(0, 2), (2, 4), (4, 0)]

