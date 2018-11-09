# This problem was asked by Palantir.
# 
# The ancient Egyptians used to express fractions as a sum of several terms where each numerator is one. For example, 4 / 13 can be represented as 1 / 4 + 1 / 18 + 1 / 468.
# 
# Create an algorithm to turn an ordinary fraction a / b, where a < b, into an Egyptian fraction.

def f(test):

    def subtract(num, denom, _num, _denom):
        __denom = denom * _denom
        ratio = __denom / denom
        _ratio = __denom / _denom
        num_ = num * ratio
        _num_ = _num * _ratio
        __num = num_ - _num_
        print '(%d/%d) - (%d/%d) = %d/%d' % (
            num_, __denom, _num_, __denom,
            __num, __denom
        )
        return __num, __denom

    out = []
    num, denom = test
    if num == 1:
        return [test]
    while num > 1:
        factor = denom / num
        remainder = denom % num
        if not remainder:
            out.append((1, factor))
            break
        elif remainder:
            _num, _denom = 1, int(factor) + 1
            out.append((_num, _denom))
            num, denom = subtract(num, denom, _num, _denom)
            if num == 1:
                out.append((num, denom))
                break
    return out


if __name__ == '__main__':

    for test in [
        (4, 13),
        (2, 5),
        (7, 51)
    ]:
        print test
        print f(test)
        print
