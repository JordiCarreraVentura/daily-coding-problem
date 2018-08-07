
# Given a string, return the first recurring character in it, or null if there is no recurring chracter.
# 
# For example, given the string "acbbac", return "b". Given the string "abcdef", return null.


def f(x):
    recurr_i = None
    recurr_j = None
    for i in range(len(x) - 1):
        char = x[i]
        for j in range(i + 1, len(x)):
            _char = x[j]
            if char == _char \
            and (
                (not recurr_j and not recurr_i)
                or (j - i) < (recurr_j - recurr_i)
            ):
                recurr_i = i
                recurr_j = j
    if recurr_i != None:
        return x[recurr_i]
    return recurr_i


if __name__ == '__main__':
    
    for test in [
        'acbbac',
        'acbfac',
        'a',
        'aa',
        'aabbcc',
        'abcdef'
    ]:
        print test, f(test)
