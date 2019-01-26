# This problem was asked by Pinterest.
# 
# At a party, there is a single person who everyone knows,
# but who does not know anyone in return (the "celebrity").
# To help figure out who this is, you have access to an O(1)
# method called knows(a, b), which returns True if person a
# knows person b, else False.
# 
# Given a list of N people and the above operation, find a 
# way to identify the celebrity in O(N) time.

import math
import random
import time
import tqdm

from collections import (
    Counter,
    defaultdict as deft
)

from tqdm import tqdm

def knows(a, b):
    return b in connections[a]

def init_connections(celebrity, people):
    connections = dict([])
    l = len(people)
    
    # everybody knows the celebrity:
    for person in people:
        connections[person] = [celebrity]
    
    # the celebrity knows noone
    # so, nothing here
    
    # some other people know each other:
    for i in range(l - 1):
        person_a = people[i]
        minim = 1
        maxim = 100
        n_acquaintances = random.randrange(minim, maxim)
        n_acquaintances = n_acquaintances if n_acquaintances <= l else l
        acquaintances = [
            person for person in
            random.sample(people, n_acquaintances)
            if person != person_a and person != celebrity
        ]
        for person_b in acquaintances:
            connections[person_a].append(person_b)

    return connections
    

def find_celebrity(size, celebrity_status, people, celebrity, connections):
    
    # Will use this variable to track how many person Bs are known.
    # If that number reaches the celebrity_status threshold at any
    # point, the function returns that value (2nd return statement)
    bb_hist = dict([])
    
    for i in range(len(people) - 1):

        # "progress bar"
        if i and not i % 1000:
            print i

        # Used to count how many person Bs know person A; if the first
        # 'celebrity_status' number of people know A, then A is the
        # celebrity (as the probability that all those random people
        # happen to know the same person is really small).
        person_a = people[i]    # if this is the celebrity, every k(b, a) == True
        bb_count = 0
        candidate_acquaintances = random.sample(
            people,
            celebrity_status if celebrity_status <= len(people) else len(people)
        )
        for z, j in enumerate(candidate_acquaintances):
            person_b = people[j]    # if this is the celebrity, every k(a, b) == True
            if knows(person_a, person_b):
                if not bb_hist.has_key(person_b):
                    bb_hist[person_b] = 0
                bb_hist[person_b] += 1
            if knows(person_b, person_a):
                bb_count += 1
            if z >= celebrity_status and len(people) > celebrity_status * 5:
                break

        if bb_count >= celebrity_status:
            return person_a

        # Applying the code in the block below only every
        # 20 iterations because there's probably no need
        # to do it any more often, as the results will not
        # change and we'll be saving up 19x as much 
        # computation:
        if i and not i % 20:
            for person_b, count in bb_hist.items():
                if count >= celebrity_status:
                    return person_b

    # If nothing has been returned yet, the list of people
    # is probably too short; in this case we can probably
    # simply iterate again over all the observed people an
    # return the argmax over the frequencies of such
    # observations.
    if bb_hist.keys():
        return [a for a, b in bb_hist.items() if b == max(bb_hist.values())][0]

    return -1


if __name__ == '__main__':
    
    n_experiments = 100
    sizes = [10, 100, 1000, 10000, 100000]
#     sizes = [10, 100, 1000, 10000]
#     sizes = [10, 100, 1000]
    
    times = deft(list)
    for i in range(n_experiments):
        size = random.choice(sizes)
        celebrity_status = int(round(math.log(size, 2))) * 10
        people = range(size)
        celebrity_status = celebrity_status if celebrity_status >= 10 else 10
        celebrity = random.randrange(0, size)
        connections = init_connections(people[celebrity], people)
        start = time.time()
        found = find_celebrity(size, celebrity_status, people, celebrity, connections)
        duration = time.time() - start
        times[size].append(duration)
        print i, size, celebrity, found, duration
    
    durations = [
        (size, sum(_durations) / len(_durations))
        for size, _durations in sorted(times.items())
    ]
    _, base_duration = durations[0]
    for size, duration in durations:
        print size, len(times[size]), duration, duration / base_duration
        base_duration = duration
        
    
            
