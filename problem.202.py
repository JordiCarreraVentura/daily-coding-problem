# This problem was asked by Palantir.
# 
# Write a program that checks whether an integer is a palindrome. For example, 121 is a palindrome, as well as 888. 678 is not a palindrome. Do not convert the integer into a string.


def f(test):

    def find_maximum_order(test):
        max_order = 1
        while True:
            divr = (max_order ** 10)
            divd = test / divr
            if divd < 1:
                break
            max_order += 1
        return max_order

    def get_orders(curr, max_order):
        orders = []
        while max_order > 0:
            divr = (10 ** max_order)
            divd = curr / divr
            curr -= (divr * divd)
            if max_order < 1:
                break
            if orders or divd:
                orders.append((max_order, divd))
            max_order -= 1
        orders.append((0, curr))
        return orders

    max_order = find_maximum_order(test)
    
    orders = get_orders(test, max_order)
    
    if len(orders) < 2:
        return False
    
    values = zip(*orders)[1]
    if values == tuple(reversed(values)):
        return True

    return False


if __name__ == '__main__':

    tests = [
        (121, True),
        (888, True),
        (88, True),
        (88443334488, True),
        (678, False),
        (13, False),
        (1, False),
        (88130499, False)
        
    ]
    
    for test, expected in tests:
        print 'test: %d\texpected: %s\treturned: %s' % (test, expected, f(test))
#         f(test)
