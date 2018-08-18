# This problem was asked by Amazon.
# 
# You are given a list of data entries that represent entries and exits of groups of people into a building. An entry looks like this:
# 
# {"timestamp": 1526579928, count: 3, "type": "enter"}
# 
# This means 3 people entered the building. An exit looks like this:
# 
# {"timestamp": 1526580382, count: 2, "type": "exit"}
# 
# This means that 2 people exited the building. timestamp is in Unix time.
# 
# Find the busiest period in the building, that is, the time with the most people in the building. Return it as a pair of (start, end) timestamps. You can assume the building always starts off and ends up empty, i.e. with 0 people inside.

import random
import time


def movement_type():
    if random.random() > 0.5:
        return 'enter'
    else:
        return 'exit'


def busiest(movements):
    
    #   find most stacked
    are_inside = 0
    _busiest = 0
    _reached = 0
    movements.sort(key=lambda x: x['timestamp'])
    for m in movements:
        if m['type'] == 'enter':
            are_inside += m['count']
        else:
            are_inside -= m['count']
        if are_inside < 0:
            are_inside = 0
        if are_inside > _busiest:
            _busiest = are_inside
            _reached = m['timestamp']

    #   find start time and end time of most stacked
    for m in movements:
        if m['timestamp'] < _reached:
            continue
        elif m['timestamp'] > _reached and m['type'] == 'exit':
            _until = m['timestamp']
            break
    
    return _reached, _until


if __name__ == '__main__':

    end_time = round(time.time())
    start_time = end_time - 86400

    movements = [
        {
            "timestamp": random.randint(start_time, end_time),
            "count": random.randint(1, 5),
            "type": movement_type()
        } for i in range(5000)
    ]
    
    print busiest(movements)
