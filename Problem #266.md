
# Problem #266

> This problem was asked by Pivotal.
> 
> A step word is formed by taking a given word, adding a letter, and anagramming the result. For example, starting with the word "APPLE", you can add an "A" and anagram to get "APPEAL".
> 
> Given a dictionary of words and an input word, create a function that returns all valid step words.

## Approach

1. First, we need to load a dictionary to be able to use it as the reference vocabulary. I will be using Freeling's.
2. As the input word parameter, we will loop over some random subset of the vocabulary we collect in the previous step.
3. To speed things up, it will probably be a good idea to keep an inverted index mapping letters to the words they appear in, so that we can quickly find any potential candidate anagrams for a given input word.
4. We will also need to take into account the letter frequency distribution in the input and the candidate words, as they can only differ by one character. If we only considered the set of unique characters in each, we may match two words differing by several characters if they contain several instances of some character.
5. The step for adding a letter is trivial and can be implemented as choosing randomly from a list containing the alphabet.


```python
import random

from collections import defaultdict as deft

HOME = '../../freeling/data/en/dictionary/entries/'

DICTIONARY_FILES = [
    '%sadjs' % HOME,
    '%sadjs.comp' % HOME,
    '%sadv' % HOME,
    '%sadv.comp' % HOME,
    #'%scontraccions' % HOME,
    '%sextra' % HOME,
    #'%sinterj' % HOME,
    '%snoms' % HOME,
    '%snumbers.DT' % HOME,
    '%snumerals.dat' % HOME,
    '%stanc' % HOME,
    '%sverbs' % HOME,
    '%sverbs.aux' % HOME
]
```


```python
def read_vocabulary():
    char2word = deft(set)
    V = set([])
    for f in DICTIONARY_FILES:
        with open(f, 'r') as rd:
            for line in rd:
                form, _, _ = line.strip().split()
                V.add(form)
                for ch in form:
                    char2word[ch].add(form)
    return V, char2word
```


```python
def ch_dist(word):
    return {ch: word.count(ch) for ch in set(list(word))}

def subtract_dist(target_dist, candidate_dist):
    for ch in target_dist:
        if ch not in candidate_dist:
            return -1
        elif candidate_dist[ch] < target_dist[ch]:
            return -1
    diff = 0
    for ch in candidate_dist:
        if ch not in target_dist:
            diff += candidate_dist[ch]
        else:
            diff += candidate_dist[ch] - target_dist[ch]
    return diff

def get_candidates(word):
    candidates = dict([])
    for ch in word:
        for candidate in char2word[ch]:
            if candidate in candidates:
                candidates[candidate] += 1
            else:
                candidates[candidate] = 1
    return candidates
                
def step_words(word):
    target_dist = ch_dist(word)
    stepwords = []
    
    # Look up the char2vec reverse index to retrieve
    # potential step word candidates for the input word.
    candidates = get_candidates(word)

    # Go over the list of candidates and find any matches. The traversal is done
    # in descending order of shared letters. This means that the most likely 
    # candidates will be considered first and that, once we reach the point where
    # the number of shared letters is less than 1 (the maximum number of edits we
    # allow) we can interrupt the iteration.
    for c, common_letters in sorted(
        candidates.items(),
        key=lambda x: x[1],
        reverse=True
    ):
        # Exit loop as per the logic in the previous comment.
        if common_letters < len(word) - 1:
            break
        
        # Ignore a candidate (but do not exit the loop) if
        # it has fewer letters than the target word.
        if len(c) < len(word):
            continue

        # For any candidates remaining up until this step, we will subtract 
        # their character counts.
        # Any characters (letter tokens) in the input word that are missing
        # from the candidate will trigger an immediate exit with negative
        # results.
        # For any other characters, we will add up the difference in their
        # letter counts between the input word and the candidate, and return
        # the final value, which will then be used in the 'if' statement 
        # below.
        candidate_dist = ch_dist(c)
        if subtract_dist(target_dist, candidate_dist) == 1:
            stepwords.append(c)
    return stepwords
        
```


```python
V, char2word = read_vocabulary()

tests = random.sample(V, 30)
for test in tests:
    print(test, step_words(test))
```

    re-presentation ['re-presentations']
    sunbathers []
    craning ['prancing', 'cranking', 'ranching']
    refreshments []
    condemns []
    fowler ['fowlers', 'flowery', 'flowers']
    assenting ['assignment', 'fastenings']
    balsam ['abysmal', 'lambast', 'balsams', 'lambdas']
    fulminating []
    pegging []
    adieus []
    chairing ['archiving']
    postoperative []
    polyphenols []
    suing ['fusing', 'musing', 'genius', 'signum', 'busing']
    resided ['deciders', 'descried', 'presided']
    buggers []
    flagellate ['flagellates']
    birder ['birders', 'berried']
    pantries ['terrapins', 'spearmint', 'transpire', 'patronise']
    damsel ['damsels', 'slammed', 'sampled', 'mislead', 'medials']
    desperadoes []
    alchemy []
    aussies []
    afraid []
    pub ['burp', 'bump', 'pubs']
    mime ['mimes', 'mimed']
    re-instating []
    piteous []
    dander ['drained', 'adorned', 'danders', 'branded']



```python

```
