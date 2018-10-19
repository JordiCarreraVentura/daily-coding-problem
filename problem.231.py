# This problem was asked by IBM.
# 
# Given a string with repeated characters, rearrange the string so that no two adjacent characters are the same. If this is not possible, return None.
# 
# For example, given "aaabbc", you could return "ababac". Given "aaab", return None.
import random


ALPHABET = list('abcdefghijklmnopqrstuvwxyz')


def new_word():
    
    def some_letter():
        return ALPHABET[random.randrange(0, len(ALPHABET))]
    
    l = random.randrange(2, 8)
    
    letters = []
    for char in range(l):
        if not letters or random.random() > 0.3:
            letters.append(some_letter())
        elif letters:
            letters.append(letters[-1])

    return ''.join(letters)


def f(test):

    def get_char_map(test):
        char_map = dict([])
        for char in list(test):
            if not char_map.has_key(char):
                char_map[char] = 0
            char_map[char] += 1
        return char_map
    
    def generate(char_map):
        w = []
        candidates = sorted(char_map.items(), reverse=True, key=lambda x: x[1])
        while candidates:
            _candidates = []
            for letter, times in candidates:
                w.append(letter)
                if times > 1:
                    _candidates.append((letter, times - 1))
            candidates = _candidates
        return ''.join(w)
    
    def has_duplicates(word):
        dups = []
        for j in range(1, len(word)):
            i = j - 1
            if word[i] == word[j]:
                dups.append((i, j))
        return dups
    
    def amend(rearranged, duplicates):
        ii, jj = zip(*duplicates)
        w = [
            rearranged[i] for i in range(len(rearranged))
            if i not in jj
        ]
        ii = list(ii)
        while ii:
            i = ii.pop(0)
            char = rearranged[i]
            for _i in range(len(w) - 1):
                j = _i + 1
                if w[_i] != char and w[j] != char:
                    w = w[:_i + 1] + [char] + w[j:]
                    break
        return ''.join(w)

    char_map = get_char_map(test)
    
    rearranged = generate(char_map)
    
    duplicates = has_duplicates(rearranged)
    print duplicates
    if duplicates:
        amended = amend(rearranged, duplicates)
        if len(amended) < len(rearranged) \
        or has_duplicates(amended):
            return None
        else:
            return amended
    return rearranged


if __name__ == '__main__':
    
    tests = [
        'aaabbc',
        'aaab'
    ] + [
        new_word() for i in range(18)
    ]

    for test in tests:
        print test
        print f(test)
        print
