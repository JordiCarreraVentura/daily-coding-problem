
# Problem #276

> This problem was asked by Dropbox.
> 
> Implement an efficient string matching algorithm.
> 
> That is, given a string of length N and a pattern of length k, write a program that searches for the pattern in the string with less than O(N * k) worst-case time complexity.
> 
> If the pattern is found, return the start index of its location. If not, return False.


```python
# Dependencies and constants

from collections import (
    Counter,
    defaultdict as deft
)

import time
import random

LETTERS = list('abcdefghijklmnopqrstuvwxyz')
```


```python
# Function to generate test data

def choose_letter():
    x = random.random()
    prev = LETTERS[0]
    for i, letter in enumerate(LETTERS):
        r = (i + 1) / float(len(LETTERS))
        if r > x:
            return prev
        prev = letter
    return prev


# Functions to measure the complexity and actual complexity
def complexity(word, pattern):
    return len(word) * len(pattern)


def actual_complexity(word, pattern):
    start = time.time()
    _ = f(word, pattern)
    return time.time() - start
```


```python
# Pattern search

def f(word, pattern):
    start = None
    l = len(word)
    p = len(pattern)
    for i in range(l - (p - 1)):
        h = word[i:i + p]
        if pattern == h:
            return i
    return False
```


```python
# Sanity test

word = 'That is, given a string of length N and a pattern of length k' + \
', write a program that searches for the pattern in the string with ' + \
'less than O(N * k) worst-case time complexity.'

pattern = 'of'

worst_case = complexity(word, pattern)

f(word, pattern)
```




    24




```python
# Helper function to aggregate measurements during testing
def simplify(n):
    if n > 20:
        return 20
    elif n > 15:
        return 15
    elif n > 10:
        return 10
    elif n > 5:
        return 5
    else:
        return 1

# Test
worst_cases = deft(list)
actual_cases = deft(list)
for z in range(1000000):

    # Set random evaluation parameters
    k = random.randrange(2, 5)
    n = random.randrange(2, 26)

    # Generate test case
    word = ''.join([choose_letter() for _ in range(n)])
    pattern = ''.join([choose_letter() for _ in range(k)])
    
    # Estimate worst case complexity and measure actual complexity
    worst_case = complexity(word, pattern)
    actual_case = actual_complexity(word, pattern)
    
    # Store actual and measured complexities for final check later
    case = (k, simplify(n))
    worst_cases[case].append(worst_case)
    actual_cases[case].append(actual_case)
        
```


```python
# Measure and compare complexities
cases = sorted(worst_cases.items())
worst_averages = []
actual_averages = []

print 'Expected duration\t', 'Actual duration\t', '\tNx improvement', '\t# cases\t', 'k, N'
for i, (case, worst) in enumerate(cases):
    actual = actual_cases[case]
    actual_average = sum(actual) / len(actual)
    worst_average = sum(worst) / len(worst)
    if case[1] > 2:
        prev_worst = worst_averages[-1]
        prev_actual = actual_averages[-1]
        delta = worst_average - prev_worst
        improvement = (prev_actual * delta) / actual_average
        print prev_actual * delta, '\t', actual_average, '\t', improvement, '\t', len(worst), '\t', case
    worst_averages.append(worst_average)
    actual_averages.append(actual_average)
```

    Expected duration	Actual duration		Nx improvement 	# cases	k, N
    1.63403775326e-05 	2.2921251865e-06 	7.12892019546 	69114 	(2, 5)
    2.2921251865e-05 	3.03517985746e-06 	7.55185950799 	69869 	(2, 10)
    2.73166187171e-05 	3.70286585074e-06 	7.37715591604 	69171 	(2, 15)
    4.07315243581e-05 	4.34138389207e-06 	9.38215218252 	69288 	(2, 20)
    2.05863297077e-05 	2.29316125651e-06 	8.9772708523 	69238 	(3, 5)
    3.21042575912e-05 	2.92315150254e-06 	10.9827552774 	69927 	(3, 10)
    4.67704240407e-05 	3.61293950951e-06 	12.9452552188 	69651 	(3, 15)
    5.41940926427e-05 	4.39504024278e-06 	12.330738662 	69741 	(3, 20)
    2.32218797563e-05 	2.28776291557e-06 	10.1504747709 	68717 	(4, 5)
    4.8043021227e-05 	2.8350320271e-06 	16.9462005253 	69349 	(4, 10)
    5.38656085149e-05 	3.5480334742e-06 	15.181820833 	69419 	(4, 15)
    7.09606694839e-05 	4.27614386228e-06 	16.5945468089 	69695 	(4, 20)

