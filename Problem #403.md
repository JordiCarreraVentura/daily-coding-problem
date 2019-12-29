# Problem #403

> This problem was asked by Two Sigma.

> Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability, implement a function rand7() that returns an integer from 1 to 7 (inclusive).

I will assume the second function, `rand7`, must also return random integers with a uniform probability.



```python
import random

from tqdm import tqdm

from collections import Counter

N_TESTS = 10000
```


```python
def rand5():
    return random.randrange(1, 6)
    
def rand7():
    return random.randrange(1, 8)

def naive():
    r = rand5()
    if r == 5:
        return random.choice([6, 7])
    else:
        return r



def one_in_three():
    r = rand5()
    if r in [1, 2]:
        return True
    return False


def generate():
    r = one_in_three()
    if not r:
        return rand5()
    else:
        r21 = one_in_three()
        r22 = one_in_three()
        if r21 and r22:
            return rand5()
        else:
            r3 = rand5()
            if r3 < 3:
                return 6
            elif r3 > 3:
                return 7
            else:
                return generate()

```


```python


settings = [
    ('base', rand5),
    ('ideal', rand7),
    ('ideal_test', rand7),
    ('naive', naive),
    ('generate', generate)
]

results = {
    name: Counter() for name, _ in settings
}



for name, f in settings:
    for _ in range(N_TESTS):
        results[name][f()] += 1
    t = float(sum(results[name].values()))
    print(name, [(v, round(f / t, 2)) for v, f in results[name].most_common()])
print()


test_series = []
gen_series = []
for _ in tqdm(range(100)):
    for _ in range(10000):
        test_diff = []
        gen_diff = []

        for method in ['base', 'naive', 'ideal_test', 'generate']:
            ideal_dist = results['ideal']
            method_dist = results[method]
            tot = sum([
                abs(ideal_dist[n] - method_dist[n])
                for n in ideal_dist.keys()
            ])
            diff = 1 - (tot / float(N_TESTS))
        
            if method == 'ideal_test':
                test_diff.append(diff)
            elif method == 'generate':
                gen_diff.append(diff)

        #print('err\t', '%s\t' % method, 1 - (diff / float(N_TESTS)))
    
    avg_test_diff = sum(test_diff) / len(test_diff)
    avg_gen_diff = sum(gen_diff) / len(gen_diff)
    #print('\nideal_test', avg_test_diff)
    #print('generate', avg_gen_diff)
    test_series.append(avg_test_diff)
    gen_series.append(avg_gen_diff)

print('test_series', sum(test_series) / len(test_series))
print('gen_series', sum(gen_series) / len(gen_series))
```

      0%|          | 0/100 [00:00<?, ?it/s]

    base [(2, 0.21), (5, 0.2), (4, 0.2), (3, 0.2), (1, 0.2)]
    ideal [(1, 0.15), (5, 0.14), (4, 0.14), (2, 0.14), (7, 0.14), (3, 0.14), (6, 0.14)]
    ideal_test [(4, 0.15), (7, 0.15), (2, 0.14), (6, 0.14), (3, 0.14), (5, 0.14), (1, 0.13)]
    naive [(2, 0.2), (1, 0.2), (4, 0.2), (3, 0.2), (7, 0.1), (6, 0.1)]
    generate [(5, 0.15), (6, 0.15), (1, 0.14), (3, 0.14), (7, 0.14), (2, 0.14), (4, 0.13)]
    


    100%|██████████| 100/100 [00:13<00:00,  7.59it/s]

    test_series 0.9579999999999987
    gen_series 0.9590000000000021


    



```python

```
