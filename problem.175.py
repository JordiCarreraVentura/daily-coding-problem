# This problem was asked by Google.
# 
# You are given a starting state start, a list of transition probabilities for a Markov chain, and a number of steps num_steps. Run the Markov chain starting from start for num_steps and compute the number of times we visited each state.
# 
# For example, given the starting state a, number of steps 5000, and the following transition probabilities:
# 
# [
#   ('a', 'a', 0.9),
#   ('a', 'b', 0.075),
#   ('a', 'c', 0.025),
#   ('b', 'a', 0.15),
#   ('b', 'b', 0.8),
#   ('b', 'c', 0.05),
#   ('c', 'a', 0.25),
#   ('c', 'b', 0.25),
#   ('c', 'c', 0.5)
# ]
# One instance of running this Markov chain might produce { 'a': 3012, 'b': 1656, 'c': 332 }.

import json
import random

from collections import OrderedDict

def run(transitions, steps):

    def update(out, state):
        if out.has_key(state):
            out[state] += 1
        else:
            out[state] = 1

    out = dict([])
    curr = 'a'
    while steps:
        candidates = [(b, c, d) for a, b, c, d in transitions if a == curr]
        prob = random.random()
        for state, start, end in candidates:
#             print state, start, end, '\t', prob >= start and prob < end
            if prob >= start and prob < end:
                update(out, state)
                break
        steps -= 1
    return OrderedDict(
        [(state, out[state]) for state in 'a b c'.split() if out.has_key(state)]
    )



if __name__ == '__main__':

    probs = [
      ('a', 'a', 0.6),
      ('a', 'b', 0.325),
      ('a', 'c', 0.065),
      ('b', 'a', 0.15),
      ('b', 'b', 0.8),
      ('b', 'c', 0.05),
      ('c', 'a', 0.25),
      ('c', 'b', 0.25),
      ('c', 'c', 0.5)
    ]
    
    transitions = []
    for i, (start, end, prob) in enumerate(probs):
        if not i:
            transitions.append((start, end, 0.0, prob))
        else:
            prev = transitions[i - 1]
            if prev[0] == start:
                transitions.append((start, end, prev[-1], prev[-1] + prob))
            else:
                transitions.append((start, end, 0, prob))
    
    experiments = 50
    n = 5000
    for experiment in range(experiments):
        print experiment, run(transitions, n)
