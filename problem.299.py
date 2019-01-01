# This problem was asked by Samsung.
# 
# A group of houses is connected to the main water plant by means of a set of pipes. A house can either be connected by a set of pipes extending directly to the plant, or indirectly by a pipe to a nearby house which is otherwise connected.
# 
# For example, here is a possible configuration, where A, B, and C are houses, and arrows represent pipes:
# 
# A <--> B <--> C <--> plant
# Each pipe has an associated cost, which the utility company would like to minimize. Given an undirected graph of pipe connections, return the lowest cost configuration of pipes such that each house has access to water.
# 
# In the following setup, for example, we can remove all but the pipes from plant to A, plant to B, and B to C, for a total cost of 16.
# 
# pipes = {
#     'plant': {'A': 1, 'B': 5, 'C': 20},
#     'A': {'C': 15},
#     'B': {'C': 10},
#     'C': {}
# }

import json
import random


def f(test):

    def reverse(test):
        origins_by_destination = dict([])
        for origin, destinations in test.items():
            for destination, cost in destinations.items():
                if not origins_by_destination.has_key(destination):
                    origins_by_destination[destination] = []
                origins_by_destination[destination].append((origin, cost))
        return origins_by_destination
    
    def find_connected(connections):
        connected = set([])
        for a, b, _ in connections:
            connected.update([a, b])
        return len(connected)

    origins_by_destination = reverse(test)
    connections = []
    space = test.items()
    while space and find_connected(connections) < len(test.keys()):
        origin, destinations = space.pop(0)
        for destination, cost in destinations.items():
            connection = (origin, destination, cost)
            if not origins_by_destination.has_key(destination):
                connections.append(connection)
            elif cost == min(zip(*origins_by_destination[destination])[1]):
                connections.append(connection)
            else:
                continue
    return connections, len(connections), sum(zip(*connections)[-1])


def make_pipes():
    houses = 'A B C D E F G H I J K L M O P Q R S T U V W X Y Z'.split()
    town = houses[:random.randrange(3, len(houses))]
    
    def house(town):
        l = len(town)
        x = random.randrange(0, l)
        return town[x]
    
    def cost():
        return random.randrange(1, 21)
    
    pipes = {
        'plant': {
            house(town): cost()
            for _ in range(random.randrange(1, len(town)))
        }
    }
    for i, home in enumerate(town):
        pipes[home] = {
            house(town[:i] + town[i + 1:]): cost()
            for _ in range(random.randrange(0, 3))
        }
    return pipes
        

if __name__ == '__main__':

    tests = [
        {
            'plant': {'A': 1, 'B': 5, 'C': 20},
            'A': {'C': 15},
            'B': {'C': 10},
            'C': {}
        }
    ]
    
    tests = [
        make_pipes()
        for _ in range(10)
    ]
    
    for test in tests:
        print json.dumps(test, indent=4)
        connections, length, cost = f(test)
        print connections
        print length
        print cost
        print
