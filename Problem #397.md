# Problem #397

> This problem was asked by Microsoft.
>
> You are given a list of jobs to be done, where each job is represented by a start time and end time. Two jobs are compatible if they don't overlap. Find the largest subset of compatible jobs.
> 
> For example, given the following jobs (there is no guarantee that jobs will be sorted):
> 
> ```
> [(0, 6),
> (1, 4),
> (3, 5),
> (3, 8),
> (4, 7),
> (5, 9),
> (6, 10),
> (8, 11)]
> ```
> 
> Return:
> 
> ```
> [(1, 4),
> (4, 7),
> (8, 11)]
> ```


```python
from copy import deepcopy as cp
```


```python
JOBS = [
    (0, 6),
    (1, 4),
    (3, 5),
    (3, 8),
    (4, 7),
    (5, 9),
    (6, 10),
    (8, 11)
]

```


```python


class Job:
    
    def __init__(self, job_index):
        self.index = job_index
        job_tuple = JOBS[self.index]
        self.start, self.end = job_tuple
    
    def area(self):
        return set(range(self.start, self.end))



class Subset:
    
    def __init__(self, job):
        self.anchor = job
        self.items = [job.index]
        self.area = self.anchor.area()
    
    def __len__(self):
        return len(self.items)

    def extension(self):
        return len(self.area)
    
    def __str__(self):
        areas = [
            '-'.join([str(i) for i in sorted(list(Job(i).area()))])
            for i in self.items
        ]
        return '<Subset anchor=<%d,%d> areas=<%s>>' % (
            self.anchor.start, self.anchor.end,
            ' ... '.join(areas)
        )
    
    def add(self, item):
        self.items.append(item.index)
        self.area.update(item.area())
    
    def __contains__(self, job):
        if job.area().intersection(self.area):
            return True
        return False


def run(jobs):
    space = cp(jobs)
    subsets = []
    while space:
        space.pop(0)
        job_index = len(jobs) - (len(space) + 1)
        job = Job(job_index)
        if not subsets:
            subset = Subset(job)
            subsets.append(subset)
        else:
            included = False
            for subset in subsets:
                if job not in subset:
                    #_job = 
                    included = True
                    subset.add(job)
            if not included:
                subsets.append(Subset(job))

    # display by order of generation
    print('\nby order of generation:')
    for subset in subsets:
        print(subset)

    # display by size of the covered area
    print('\nby covered area:')
    for subset in sorted(subsets, key=lambda x: x.extension(), reverse=True):
        print(subset)

    # display by size of the subset
    print('\nby size of the subset:')
    for subset in sorted(subsets, key=lambda x: len(x), reverse=True):
        print(subset)
```


```python
run(JOBS)
```

    
    by order of generation:
    <Subset anchor=<0,6> areas=<0-1-2-3-4-5 ... 6-7-8-9>>
    <Subset anchor=<1,4> areas=<1-2-3 ... 4-5-6 ... 8-9-10>>
    <Subset anchor=<3,5> areas=<3-4 ... 5-6-7-8>>
    <Subset anchor=<3,8> areas=<3-4-5-6-7 ... 8-9-10>>
    
    by covered area:
    <Subset anchor=<0,6> areas=<0-1-2-3-4-5 ... 6-7-8-9>>
    <Subset anchor=<1,4> areas=<1-2-3 ... 4-5-6 ... 8-9-10>>
    <Subset anchor=<3,8> areas=<3-4-5-6-7 ... 8-9-10>>
    <Subset anchor=<3,5> areas=<3-4 ... 5-6-7-8>>
    
    by size of the subset:
    <Subset anchor=<1,4> areas=<1-2-3 ... 4-5-6 ... 8-9-10>>
    <Subset anchor=<0,6> areas=<0-1-2-3-4-5 ... 6-7-8-9>>
    <Subset anchor=<3,5> areas=<3-4 ... 5-6-7-8>>
    <Subset anchor=<3,8> areas=<3-4-5-6-7 ... 8-9-10>>

