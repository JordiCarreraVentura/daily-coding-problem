# This problem was asked by Spotify.
# 
# There are N couples sitting in a row of length 2 * N. They are currently ordered randomly, but would like to rearrange themselves so that each couple's partners can sit side by side.
# 
# What is the minimum number of swaps necessary for this to happen?

import random


def cp(table):
    return [x for x in table]


def make_couples():
    n_couples = random.randrange(2, 6)
    people = list(range(n_couples * 2))
    couples = []
    for i in range(0, len(people), 2):
        couple = set([people[i], people[i + 1]])
        couples.append(couple)
    return couples


def arrange_table(couples):
    aa, bb = zip(*couples)
    people = list(aa) + list(bb)
    random.shuffle(people)
    return people




    
def check_status(couples, table):

    def update(couples, i, ab, in_place):
        for couple in couples:
            if set(couple) == ab:
                in_place += [i, i + 1]
                break
    
    def to_groups(out_of_place):
        groups = []
        group = []
        while out_of_place:
            person = out_of_place.pop(0)
            if person == None:
                if group:
                    groups.append([x for x in group])
                    group = []
            else:
                group.append(person)
        if group:
            groups.append(group)
        return groups

    in_place = []
    for i in range(len(table) - 1):
        a = table[i]
        b = table[i + 1]
        ab = set([a, b])
        update(couples, i, ab, in_place)

    out_of_place = to_groups([
        i if i not in in_place else None
        for i in range(len(table))
    ])

    return in_place, out_of_place





def f(test):

    def swap(couples, table):

        def simulate(couples, table, i, j):
            simulation = [x for x in table]
            a, b = simulation[i], simulation[j]
            simulation[i] = b
            simulation[j] = a
            keep, to_swap = check_status(couples, simulation)
            return len(keep)
        
        def apply(table, ranked):
            _, i, j = ranked[-1]
            a, b = table[i], table[j]
            table[i] = b
            table[j] = a
            return 1, table
        
        def are_couple(couples, i, j):
            for couple in couples:
                if i in couple and j in couple:
                    return True
            return False
        
        def rearrange(prev, couples, table, merged):
        
            def find_partner(couples, a):
                for couple in couples:
                    if a in couple:
                        return list(set(couple) - set([a]))[0]
                return None

            done = set([])
            swaps = 0
            for _group in merged:
                group = set(_group) - done
                if not group:
                    continue
                if len(group) == 1:
                    ia = list(group)[0]
                    a = table[ia]
                    b = find_partner(couples, a)
                    ib = table.index(b)
                    insertion = ia if ia < ib else ib
                    removal = ib if ia < ib else ia
                    x = table.pop(removal)
                    table.insert(insertion + 1, x)
                    done.update([ia, ib])
                    swaps += 1
                    print prev + swaps, table
            return swaps, table

        def find_moves(_in, couples, table):
            moves = []
            for i in range(len(table) - 1):
                for j in range(1, len(table)):
                    if are_couple(couples, table[i], table[j]) \
                    or i == j:
                        continue
                    score = simulate(couples, table, i, j)
                    if score <= len(_in):
                        continue
                    move = (score, i, j)
                    moves.append(move)
            return moves

        def is_complete(swaps, couples, table):
            print swaps, table
            _in, _out = check_status(couples, table)
            if len(_in) == len(table):
                return True, _out
            return False, _out

        swaps = 0
        _in, merged = check_status(couples, table)
        while True:
            moves = find_moves(_in, couples, table)
            if not moves:
                break
            ranked = sorted(moves, key=lambda x: x[0])
            _swaps, table = apply(table, ranked)
            swaps += _swaps

            complete, merged = is_complete(swaps, couples, table)
            if complete:
                break

            _swaps, table = rearrange(swaps, couples, cp(table), merged)
            swaps += _swaps        

            complete, merged = is_complete(swaps, couples, table)
            if complete:
                break

        _swaps, table = rearrange(swaps, couples, cp(table), merged)
        swaps += _swaps
        print swaps, table

        return swaps, table


    couples, table = test
    o = cp(table)
    swaps = 0
    print 'couples', couples
    print 'original', o
    print '--'
    while True:
        keep, to_swap = check_status(couples, table)
        if not to_swap:
            break
        _swaps, table = swap(couples, cp(table))
        swaps += _swaps
        print swaps, table
    return swaps, table


if __name__ == '__main__':

    to_tables = [
        make_couples() for i in range(10)
    ]
    
    tests = [
        (couples, arrange_table(couples))
        for couples in to_tables
    ]
    
#     tests = [
# #         ([set([0, 1]), set([2, 3]), set([4, 5])],
# #         [2, 3, 0, 5, 4, 1])
# #         ([set([0, 1]), set([2, 3]), set([4, 5])],
# #         [3, 0, 1, 5, 4, 2])
#         ([set([0, 1]), set([2, 3]), set([4, 5])],
#         [0, 5, 1, 2, 4, 3])
#     ]
    
    for test in tests:
        print '\n\n====='
        f(test)
