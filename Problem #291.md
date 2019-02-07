
# Problem #291

> This problem was asked by Glassdoor.
>
> An imminent hurricane threatens the coastal town of Codeville. If at most two people can fit in a rescue boat, and the maximum weight limit for a given boat is k, determine how many boats will be needed to save everyone.
> 
> For example, given a population with weights \[100, 200, 150, 80\] and a boat limit of 200, the smallest number of boats required will be three.


```python
import random

K = [100, 200, 350, 500]
W = range(50, 251, 5)
PEOPLE_PER_BOAT = [1, 2, 3, 4]


def sort_(rescuable, max=False):
    out = []
    while rescuable:
        arg, val = None, None
        for i, w in enumerate(rescuable):
            if arg == None \
            or (
                (not max and w <= val) or
                (max and w >= val)
            ):
                val = w
                arg = i
        out.append(rescuable.pop(arg))
    return out
```


```python
def f(per_boat, k, weights):
    boats = []
    victims = [w for w in weights if w > k]
    rescuable = [w for w in weights if w <= k]
    rescuable = sort_(rescuable)
    while rescuable:
        w1 = rescuable.pop(0)
        boat = [w1]
        _rescuable = sort_(rescuable, max=True)
        rescued = []
        for i, w2 in enumerate(_rescuable):
            if sum(boat + [_rescuable[j] for j in rescued]) + w2 <= k \
            and len(rescued) + 2 <= per_boat:
                rescued.append(i)
            if len(rescued) == per_boat:
                break
        remainder = [w for i, w in enumerate(_rescuable) if i not in rescued]
        boat += [w for i, w in enumerate(_rescuable) if i in rescued]
        boats.append(boat)
        rescuable = sort_(remainder)
    return len(boats), boats, victims

# test = [3, 4, 1, 5, 2]
# print sort_(test)

# test = [3, 4, 1, 5, 2]
# print sort_(test, max=True)
```


```python
for xp in range(10):
    k = random.choice(K)
    population = random.randrange(3, 10)
    weights = [random.choice(W) for _ in range(population)]
    per_boat = random.choice(PEOPLE_PER_BOAT)
    n_boats, survivors, victims = f(per_boat, k, weights)
    
    print '\n--- Experiment %d ---' % (xp + 1)
    print '# people per boat: %d' % per_boat
    print 'Max. weight per boat: %d' % k
    print '--'
    print 'Population weights (%d): %s' % (population, ', '.join([str(w) for w in weights]))
    print '--'
    print '# of boats: %d' % n_boats
    print 'Survivors: %s' % ', '.join(['/'.join([str(w) for w in boat]) for boat in survivors])
    print 'Victims: %s' % ', '.join([str(w) for w in victims])
    print
```

    
    --- Experiment 1 ---
    # people per boat: 4
    Max. weight per boat: 200
    --
    Population weights (4): 90, 145, 235, 125
    --
    # of boats: 3
    Survivors: 90, 125, 145
    Victims: 235
    
    
    --- Experiment 2 ---
    # people per boat: 4
    Max. weight per boat: 100
    --
    Population weights (3): 135, 210, 215
    --
    # of boats: 0
    Survivors: 
    Victims: 135, 210, 215
    
    
    --- Experiment 3 ---
    # people per boat: 3
    Max. weight per boat: 200
    --
    Population weights (6): 185, 55, 65, 180, 155, 90
    --
    # of boats: 5
    Survivors: 55/90, 65, 155, 180, 185
    Victims: 
    
    
    --- Experiment 4 ---
    # people per boat: 3
    Max. weight per boat: 500
    --
    Population weights (6): 200, 240, 175, 75, 125, 240
    --
    # of boats: 3
    Survivors: 75/240/175, 125/240, 200
    Victims: 
    
    
    --- Experiment 5 ---
    # people per boat: 1
    Max. weight per boat: 200
    --
    Population weights (6): 70, 140, 170, 80, 215, 145
    --
    # of boats: 5
    Survivors: 70, 80, 140, 145, 170
    Victims: 215
    
    
    --- Experiment 6 ---
    # people per boat: 2
    Max. weight per boat: 500
    --
    Population weights (4): 195, 130, 210, 115
    --
    # of boats: 2
    Survivors: 115/210, 130/195
    Victims: 
    
    
    --- Experiment 7 ---
    # people per boat: 3
    Max. weight per boat: 350
    --
    Population weights (5): 50, 225, 65, 155, 70
    --
    # of boats: 2
    Survivors: 50/225/70, 65/155
    Victims: 
    
    
    --- Experiment 8 ---
    # people per boat: 1
    Max. weight per boat: 100
    --
    Population weights (3): 125, 110, 180
    --
    # of boats: 0
    Survivors: 
    Victims: 125, 110, 180
    
    
    --- Experiment 9 ---
    # people per boat: 4
    Max. weight per boat: 200
    --
    Population weights (8): 195, 70, 240, 120, 220, 75, 225, 245
    --
    # of boats: 3
    Survivors: 70/120, 75, 195
    Victims: 240, 220, 225, 245
    
    
    --- Experiment 10 ---
    # people per boat: 2
    Max. weight per boat: 500
    --
    Population weights (8): 60, 110, 130, 55, 155, 200, 250, 165
    --
    # of boats: 4
    Survivors: 55/250, 60/200, 110/165, 130/155
    Victims: 
    

