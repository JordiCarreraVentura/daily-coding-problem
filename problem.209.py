# This problem was asked by YouTube.
# 
# Write a program that computes the length of the longest common subsequence of three given strings. For example, given "epidemiologist", "refrigeration", and "supercalifragilisticexpialodocious", it should return 5, since the longest common subsequence is "eieio".


def f(test):
    
    def find_common_letters(test):
        U = set(test[0])
        for w in test[1:]:
            U = U.intersection(set(w))
        return U
    
    def subtract_uncommon_letters(test, common_letters):
        skeletons = []
        for w in test:
            skeleton = [ch for ch in list(w) if ch in common_letters]
            skeletons.append(skeleton)
        return skeletons
    
    def count_letters(space):
        counts = dict([])
        for w in space:
            for ch in set(w):
                if not counts.has_key(ch):
                    counts[ch] = 0
                counts[ch] += 1
        return counts
    
    def find_longest_common(skeletons):
    
        def get_next(space):
            letter_counts = count_letters(space)
            common = [
                ch for ch, count in letter_counts.items()
                if count == len(space)
            ]
            continuations = []
            for ch in common:
                subspace = []
                for word in space:
                    i = word.index(ch)
                    continuation = (i, ch)
                    subspace.append(word[i + 1:])
                continuations.append((ch, subspace))
            return continuations
        
        hh = [
            [[], [x for x in skeletons]]
        ]
        while True:
            new = []
            for h, space in hh:
                continuations = get_next(space)
                for next_letter, subspace in continuations:
                    _h = [x for x in h] + [next_letter]
                    new.append((_h, subspace))
            if not new:
                break
            hh = new
        if not hh:
            return ''
        return ''.join(sorted(hh, key=lambda x: len(x[0]))[-1][0])
    
    common_letters = find_common_letters(test)
    
    skeletons = subtract_uncommon_letters(test, common_letters)
    
    longest = find_longest_common(skeletons)

    return longest


if __name__ == '__main__':
    
    for test in [
        [
            'epidemiologist',
            'refrigeration',
            'supercalifragilisticexpialodocious'
        ],
        [
            'sdas',
            'asdasd',
            'alphaasdasdasdbeta',
            'asdas_',
            'asdasdasdasd',
            'barasdasdasdasdfoo'
        ],
        [
            'a1ei4ou56',
            'aeiou1456',
            'b14cde5fg6',
            'bcd145ef6g',
            'b14c5d6efg'
        ]
    ]:
        print test
        print f(test)
        print
