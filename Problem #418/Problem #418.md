# Problem #418

> This problem was asked by Atlassian.
> 
> MegaCorp wants to give bonuses to its employees based on how many lines of codes they have written. They would like to give the smallest positive amount to each worker consistent with the constraint that if a developer has written more lines of code than their neighbor, they should receive more money.
> 
> Given an array representing a line of seats of employees at MegaCorp, determine how much each one should get paid.
> 
> For example, given `[10, 40, 200, 1000, 60, 30]`, you should return `[1, 2, 3, 4, 2, 1]`.


```python
def f(x):
    
    def is_ascending(group):
        if group[-1] > group[0]:
            return True
        return False
    
    def make_groups(x):
        groups = []
        space = [e for e in x]
        group = [space.pop(0)]
        while space:
            e = space.pop(0)
            if len(group) < 2:
                group.append(e)
            elif is_ascending(group):
                if e < group[-1]:
                    groups.append(group)
                    group = [e]
                else:
                    group.append(e)
            else:
                if e < group[-1]:
                    group.append(e)
                else:
                    groups.append(group)
                    group = [e]
        if group:
            groups.append(group)
        return groups

    def make_base_bonus(groups):
        base_bonus = []
        for group in groups:
            bonus = list([i + 1 for i in range(len(group))])
            if not is_ascending(group):
                bonus.reverse()
            base_bonus.append(bonus)
        return base_bonus

    def solve_ties(groups, base_bonus):
        for i in range(len(base_bonus) - 1):
            group_a, group_b = groups[i:i + 2]
            bonus_a, bonus_b = base_bonus[i:i + 2]
            if bonus_a[-1] == bonus_b[0]:
                if group_a[-1] > group_b[0]:
                    base_bonus[i][-1] += 1
                else:
                    base_bonus[i + 1][0] += 1
    
    def flatten(base_bonus):
        flattened = []
        for base in base_bonus:
            flattened += base
        return flattened
        
    groups = make_groups(x)
    
    base_bonus = make_base_bonus(groups)
    
    solve_ties(groups, base_bonus)

    return flatten(base_bonus)
```


```python
tests = [
    [10, 40, 200, 1000, 60, 30],
    [10, 40, 200, 1000, 60, 30, 10, 5],
    [10, 40, 200, 1000, 60, 30, 5, 10],
    [10, 200, 40, 1000, 5, 10, 30, 60],
    [10, 200, 40, 1000, 5, 30, 10, 60]
]

for test in tests:
    print(test, f(test))
```

    [10, 40, 200, 1000, 60, 30] [1, 2, 3, 4, 2, 1]
    [10, 40, 200, 1000, 60, 30, 10, 5] [1, 2, 3, 5, 4, 3, 2, 1]
    [10, 40, 200, 1000, 60, 30, 5, 10] [1, 2, 3, 4, 3, 2, 1, 2]
    [10, 200, 40, 1000, 5, 10, 30, 60] [1, 2, 1, 2, 1, 2, 3, 4]
    [10, 200, 40, 1000, 5, 30, 10, 60] [1, 2, 1, 2, 1, 2, 1, 2]

