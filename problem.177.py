# This problem was asked by Airbnb.
# 
# Given a linked list and a positive integer k, rotate the list to the right by k places.
# 
# For example, given the linked list 7 -> 7 -> 3 -> 5 and k = 2, it should become 3 -> 5 -> 7 -> 7.
# 
# Given the linked list 1 -> 2 -> 3 -> 4 -> 5 and k = 3, it should become 3 -> 4 -> 5 -> 1 -> 2.


def f(k, test):
    out = []
    for i in range(k, len(test)) + range(k):
        out.append(test[i])
    return out


if __name__ == '__main__':

    tests = [
        (2, [7, 7, 3, 5]),
        (2, [1, 2, 3, 4, 5]),
        (3, [1, 2, 3, 4, 5])
    ]
    
    for k, test in tests:
        print
        print test
        print k, f(k, test)
