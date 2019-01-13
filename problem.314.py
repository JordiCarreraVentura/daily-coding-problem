# This problem was asked by Spotify.
# 
# You are the technical director of WSPT radio, serving listeners nationwide. For simplicity's sake we can consider each listener to live along a horizontal line stretching from 0 (west) to 1000 (east).
# 
# Given a list of N listeners, and a list of M radio towers, each placed at various locations along this line, determine what the minimum broadcast range would have to be in order for each listener's home to be covered.
# 
# For example, suppose listeners = [1, 5, 11, 20], and towers = [4, 8, 15]. In this case the minimum range would be 5, since that would be required for the tower at position 15 to reach the listener at position 20.
# 

import random

TERRITORY = 1000
TERRITORY = 100


class Tower:
    def __init__(self, position):
        self.position = position
        self.boosting_factor = 0
        self()
    
    def __str__(self):
        return '<Tower attributes=<location=%d area=<start=%d end=%d>>>' % (
            self.position, min(self.coverage), max(self.coverage)
        )
    
    def boost(self):
        self.boosting_factor += 1
    
    def start(self):
        return min(self())
    
    def __call__(self):
        if not self.boosting_factor:
            self.coverage = set([self.position])
        else:
            minim = self.position - self.boosting_factor
            maxim = self.position + self.boosting_factor + 1
            minim = minim if minim > -1 else 0
            self.coverage = set(range(minim, maxim))
        return self.coverage
        

class Audience:
    def __init__(self, area, n):
        self.households = random.sample(area, n)
    
    def is_covered(self, towers):
        to_cover = set(self.households)
        coverage = set([])
        for tower in towers:
            coverage.update(tower())
        common = to_cover.intersection(coverage)
        ratio = round(len(common) / float(len(to_cover)), 2)
        if len(common) == len(to_cover):
            print ratio, [str(tower) for tower in towers]
            return True
        missing = sorted(to_cover - common)
        return False
    
    def first(self):
        return min(self.households)
    
    def last(self):
        return max(self.households)


def show(towers):
    frequency_map = [['.' for _ in range(TERRITORY)] for _ in towers]
    for i, tower in enumerate(towers):
        for x in tower():
            if x >= TERRITORY:
                continue
            frequency_map[i][x] = '#'
    for tower in frequency_map:
        print ''.join(tower)



if __name__ == '__main__':
    
    # m = radio towers
    # n = listeners

    tests = [
        (4, 35)
    ] + [
        (random.randrange(2, 10), random.randrange(20, 50))
        for _ in range(9)
    ]

    area = list(range(TERRITORY))
    for (m, n) in tests:
        audience = Audience(area, n)
        towers = sorted(
            [Tower(i) for i in random.sample(area, m)],
            key=lambda x: x.start()
        )
        
        args = (m, n, audience.first(), audience.last())
        print '\ntowers=%d households=%d (%d-%d)' % args
        while not audience.is_covered(towers):
            for tower in towers:
                tower.boost()
        show(towers)
        print 'required signal strength=%d' % (tower.boosting_factor)
