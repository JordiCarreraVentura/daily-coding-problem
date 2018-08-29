# This problem was asked by Google.
# 
# Given a string, split it into as few strings as possible such that each string is a palindrome.
# 
# For example, given the input string racecarannakayak, return ["racecar", "anna", "kayak"].
# 
# Given the input string abc, return ["a", "b", "c"].


def f(test):

    def ngrams(x, n):
        grams = []
        for i in range(0, len(x) - (n - 1)):
            grams.append(x[i:i + n])
        return grams

    space = test
    max_l = len(test)
    found = []
    for l in range(max_l, 0, -1):
        ww = ngrams(space, l)
        for i, w in enumerate(ww):
            if '#' in w:
                continue
            wr = ''.join(reversed(list(w)))
            if wr in space:
                found.append((w, wr))
                space = space[:i] + '#' * len(w) + space[i + len(w):]
    return found


if __name__ == '__main__':

    tests = [
        'racecarannakayak',
        'abc'
    ]
    
    for test in tests:
        for x in f(test):
            print x
        print
