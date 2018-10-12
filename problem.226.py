# This problem was asked by Airbnb.
# 
# You come across a dictionary of sorted words in a language you've never seen before. Write a program that returns the correct order of letters in this language.
# 
# For example, given ['xww', 'wxyz', 'wxyw', 'ywx', 'ywz'], you should return ['x', 'z', 'w', 'y'].



def f(test):

    def get_V(test):
        V = set([])
        for w in test:
            V.update(set(w))
        return V
    
    def all_letters_as_values(O, V):
        as_values = set([])
        for letter, letters in O.items():
            as_values.update(letters)
        if as_values.intersection(letters) == V:
            return True
        return False

    def bin_words(test, l):
        bins = []
        bin = []
        last = test[0][:l]
        for w in test:
            key = w[:l]
            if key != last:
                bins.append([_w for _w in bin])
                bin = [w]
            else:
                bin.append(w)
            last = key
        if bin:
            bins.append(bin)
        return bins
    
    def update_letters(O, l, bins):
        for bin in bins:
            first_letters = [w[l] for w in bin if len(w) > l]
            _l = len(first_letters)
            for i in range(_l - 1):
                l1 = first_letters[i]
                for j in range(i + 1, _l):
                    l2 = first_letters[j]
                    if l1 == l2:
                        continue
                    O[l1].add(l2)
                    O[l1].update(O[l2])
        print bins
        print O
        print '---'

    V = get_V(test)
    O = dict([(letter, set([])) for letter in V])
    l = 0
    maxim = max(len(w) for w in test)
    
    while not all_letters_as_values(O, V) and l < maxim:
        bins = bin_words(test, l)
        update_letters(O, l, bins)
        l += 1
    
    return sorted(
        O.keys(),
        key=lambda x: len(O[x]),
        reverse=True
    )


if __name__ == '__main__':
    
    tests = [
        ['xww', 'wxyz', 'wxyw', 'ywx', 'ywz']  # ['x', 'z', 'w', 'y']
    ]

    
    for test in tests:
        print test
        print f(test)
        print
