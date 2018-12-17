# This problem was asked by Quora.
# 
# You are given a list of (website, user) pairs that represent users visiting websites. Come up with a program that identifies the top k pairs of websites with the greatest similarity.
# 
# For example, suppose k = 1, and the list of tuples is:
# 
# [('a', 1), ('a', 3), ('a', 5),
#  ('b', 2), ('b', 6),
#  ('c', 1), ('c', 2), ('c', 3), ('c', 4), ('c', 5)
#  ('d', 4), ('d', 5), ('d', 6), ('d', 7),
#  ('e', 1), ('e', 3), ('e': 5), ('e', 6)]
# Then a reasonable similarity metric would most likely conclude that a and e are the most similar, so your program should return [('a', 'e')].

import random


def f(visits):

    def __M(visits):
        N = set([])
        M = set([])
        for site, user in visits:
            M.add(site)
            N.add(user)
        MN = [[0 for _ in range(len(N))] for _ in range(len(M))]
        return list(M), list(N), MN

    def populate_matrix(visits, M, N, MN):
        for site, user in visits:
            j = N.index(user)
            i = M.index(site)
            MN[i][j] = 1
    
    def __sim(site1, site2):
        total = float(sum(site1) + sum(site2))
        matches = 0
        for user1, user2 in zip(site1, site2):
            if user1 and user2:
                matches += 1
        return matches / total

    M, N, MN = __M(visits)
    populate_matrix(visits, M, N, MN)
    
    L = len(M)
    sims = []
    for i in range(L - 1):
        site1 = MN[i]
        for j in range(i + 1, L):
            site2 = MN[j]
            sim = __sim(site1, site2)
            sims.append((M[i], M[j], sim))

    sims.sort(key=lambda x: x[2])    
    for sim in sims[-10:]:
        print sim
    print '---'
    return sims.pop()


if __name__ == '__main__':

    # test
    test = [
        ('a', 1), ('a', 3), ('a', 5),
        ('b', 2), ('b', 6),
        ('c', 1), ('c', 2), ('c', 3), ('c', 4), ('c', 5),
        ('d', 4), ('d', 5), ('d', 6), ('d', 7),
        ('e', 1), ('e', 3), ('e', 5), ('e', 6)
    ]
    print f(test)
    exit()
    # end of test
    
#     websites = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
#     users = [random.randrange(1, 10) for _ in range(1000)]
#     
#     for _ in range(10):
#         test = []
#         while len(test) < 50:
#             site = random.sample(websites, 1)[0]
#             user = random.sample(users, 1)[0]
#             test.append((site, user))
#         print f(test)
#         print
