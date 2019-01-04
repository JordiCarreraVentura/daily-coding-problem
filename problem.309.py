# This problem was asked by Walmart Labs.
# 
# There are M people sitting in a row of N seats, where M < N. Your task is to redistribute people such that there are no gaps between any of them, while keeping overall movement to a minimum.
# 
# For example, suppose you are faced with an input of [0, 1, 1, 0, 1, 0, 0, 0, 1], where 0 represents an empty seat and 1 represents a person. In this case, one solution would be to place the person on the right in the fourth seat. We can consider the move of a solution to be the sum of the absolute distance each person must move, so that the move here would be five.
# 
# Given an input such as the one above, return the lowest possible move of moving people to remove all gaps.

import random    

def cost(moves):
    out = 0
    for person, position in moves:
        out += abs(person - position)
    return out


def f(test):

    def find_best_region(test, people):    
        maxim, argmaxim = 0, None
        people = sum(test)
        for i in range(len(test) - (people - 1)):
            region = test[i:i + people]
            density = sum(region)
            if density > maxim:
                argmaxim = i
                maxim = density
        return argmaxim
    
    def all_ones_together(test, people):
        for i in range(len(test) - (people - 1)):
            if sum(test[i:i + people]) == people:            
                return True
        return False

    def initialize_space(test, best_region, people):
        people_in_place, people_out_of_place, free_slots = [], [], []
        best_region_area = set(range(best_region, best_region + people))
        for i, person in enumerate(test):
            if person and i in best_region_area:
                people_in_place.append(i)
            elif person:
                people_out_of_place.append(i)
            elif not person:
                free_slots.append(i)
        return people_in_place, people_out_of_place, free_slots
    
    def spawn(people_out_of_place, free_slots, moves):
        return [x for x in people_out_of_place], \
               [x for x in free_slots], \
               [x for x in moves]
    
    def is_filled(best_region, people, space, _moves):
        minim = min([i for i, x in enumerate(space) if x])
        maxim = max([i + 1 for i, x in enumerate(space) if x])
        if sum(space[minim:minim + people]) == people \
        and sum(space[maxim - people:maxim]) == people:
            return True
        return False
    
    def make_move(people_out_of_place, free_slots):
        for person in people_out_of_place:
            for slot in free_slots:
                yield (person, slot)
    
    def redistribute(
        test, people, best_region, people_in_place,
        people_out_of_place, free_slots, moves
    ):
    
        hypotheses = []
        for move in make_move(
            people_out_of_place, free_slots
        ):
            _people_out_of_place, _free_slots, _moves = spawn(
                people_out_of_place, free_slots, moves
            )
            person, position = move
            _moves.append(move)
            _people_out_of_place.pop(_people_out_of_place.index(person))
            _free_slots.pop(_free_slots.index(position))
            if _people_out_of_place:
                hypotheses += redistribute(
                    test, people, best_region, people_in_place,
                    _people_out_of_place, _free_slots, _moves
                )
            else:
                space = [x for x in test]
                for person, position in _moves:
                    space[position] = 1
                    space[person] = 0
                hypothesis = (space, _moves)
                hypotheses.append(hypothesis)

        hypotheses = sorted(
            [(space, _moves) for (space, _moves) in hypotheses
             if is_filled(best_region, people, space, _moves)],
            key=lambda x: cost(x[-1])
        )

        return hypotheses

    people = sum(test)
    
    if sum(test) < 2 \
    or all_ones_together(test, people):
        return [(test, [])]

    best_region = find_best_region(test, people)

    people_in_place, people_out_of_place, free_slots = initialize_space(
        test, best_region, people
    )
   
    hypotheses = redistribute(
        test, people, best_region, people_in_place,
        people_out_of_place, free_slots, []
    )

    return hypotheses


if __name__ == '__main__':

    tests = [
        [0, 1, 0],
        [0, 1, 1],
        [0, 1, 1, 0, 1, 0, 0, 0, 1],
        [0, 1, 0, 0, 1, 0, 1, 1, 1]
    ] + [
        [1 if random.random() >= 0.5 else 0 for _ in range(random.randrange(2, 15))]
        for _ in range(96)
    ]
    
#     tests = [
#         [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0]
#     ]
    
    for test in tests:
        print test
        for space, moves in f(test):
            print space, moves, cost(moves)
            print '---'
        print
