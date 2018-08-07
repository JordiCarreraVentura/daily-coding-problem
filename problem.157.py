
# Given a string, determine whether any permutation of it is a palindrome.
# 
# For example, carrace should return true, since it can be rearranged to form racecar, which is a palindrome. daily should return false, since there's no rearrangement that can form a palindrome.


V = [
    'racecar',
    'carrace',
    'daily',
    'loof',
    'fool',
    'tip',
    'pit',
    'black',
    'dog',
    'god',
    'white'
]

def f(v):
    for x in V:
        if x == v:
            continue
        s1 = list(v)
        s2 = list(x)
        while s1 and s2:
            c1 = s1.pop(0)
            if c1 not in s2:
                break
            s2.pop(s2.index(c1))
        if not (s1 and s2):
            print '+%s %s' % (v, x)
            return True
    else:
        print '-%s' % v
        return False


if __name__ == '__main__':
    for v in V:
        f(v)
