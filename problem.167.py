
# This problem was asked by Airbnb.
# 
# Given a list of words, find all pairs of unique indices such that the concatenation of the two words is a palindrome.
# 
# For example, given the list ["code", "edoc", "da", "d"], return [(0, 1), (1, 0), (2, 3)].


def f(words):
    pls = []
    for i, w in enumerate(words):
        for j, v in enumerate(words):
            if i == j:
                continue
            h = w + v
            if h == h[::-1]:
                pls.append((i, j))
    return pls


if __name__ == '__main__':

    test = ["code", "edoc", "da", "d"]
    
    print f(test)
