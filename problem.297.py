# This problem was asked by Amazon.
# 
# At a popular bar, each customer has a set of favorite drinks, and will happily accept any drink among this set. For example, in the following situation, customer 0 will be satisfied with drinks 0, 1, 3, or 6.
# 
# preferences = {
#     0: [0, 1, 3, 6],
#     1: [1, 4, 7],
#     2: [2, 4, 7, 5],
#     3: [3, 2, 5],
#     4: [5, 8]
# }
# A lazy bartender working at this bar is trying to reduce his effort by limiting the drink recipes he must memorize. Given a dictionary input such as the one above, return the fewest number of drinks he must learn in order to satisfy all customers.
# 
# For the input above, the answer would be 2, as drinks 1 and 5 will satisfy everyone.

import json
import random

def f(test):

    def get_people_by_drink(test):
        people_by_drink = dict([])
        for person, drinks in test.items():
            for drink in drinks:
                if not people_by_drink.has_key(drink):
                    people_by_drink[drink] = set([])
                people_by_drink[drink].add(person)
        return people_by_drink
    
    people_by_drink = get_people_by_drink(test)
    
    served = set([])
    drinks = set([])
    preferences = sorted(
        people_by_drink.items(),
        reverse=True,
        key=lambda x: len(x[1])
    )
    while served < set(test.keys()):
        drink, people = preferences.pop(0)
        served.update(people)
        drinks.add(drink)
    return drinks



if __name__ == '__main__':

    tests = [
        {
            0: [0, 1, 3, 6],
            1: [1, 4, 7],
            2: [2, 4, 7, 5],
            3: [3, 2, 5],
            4: [5, 8]
        }
    ]
    
    for test in tests:
        drinks = f(test)
        print len(drinks), drinks
