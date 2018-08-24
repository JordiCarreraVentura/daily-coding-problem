# This problem was asked by Bloomberg.
# 
# Determine whether there exists a one-to-one character mapping from one string s1 to another s2.
# 
# For example, given s1 = abc and s2 = bcd, return true since we can map a to b, b to c, and c to d.
# 
# Given s1 = foo and s2 = bar, return false since the o cannot map to two characters.


def f(x, y, bijective=False):
    
    def pre_map(x):
        dup = []
        uniq = []
        for i, ch in enumerate(x):
            left, right = x[:i], x[i + 1:]
            if ch in left or ch in right:
                if ch not in dup:
                    dup.append(ch)
            else:
                uniq.append(ch)
        return dup, uniq
    
    dup1, uniq1 = pre_map(x)
    dup2, uniq2 = pre_map(y)
    
    if not bijective and len(uniq1 + dup1) >= len(uniq2 + dup2):
        return True
    elif len(uniq1 + dup1) == len(uniq2 + dup2):
        return True
    return False


if __name__ == '__main__':

    tests = [
        ('abc', 'bcd'),
        ('foo', 'bar'),
        ('bar', 'foo'),
        ('abcdefga', '1234'),
        ('abcdefga', '12345678'),
        ('abcdefga', '12345671')
    ]
    
    for x, y in tests:
        print 'a=%s b=%s  injective=%s  bijective=%s' % (
            x, y, f(x, y), f(x, y, bijective=True)
        )
