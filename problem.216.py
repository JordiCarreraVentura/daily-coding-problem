# This problem was asked by Facebook.
# 
# Given a number in Roman numeral format, convert it to decimal.
# 
# The values of Roman numerals are as follows:
# 
# {
#     'M': 1000,
#     'D': 500,
#     'C': 100,
#     'L': 50,
#     'X': 10,
#     'V': 5,
#     'I': 1
# }
# In addition, note that the Roman numeral system uses subtractive notation for numbers such as IV and XL.
# 
# For the input XIV, for instance, you should return 14.


VALUES = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}


def f(test):
    letters = list(test)
    q = 0
    while letters:
        letter = letters.pop(0)
        l = len(letters)
        if l and VALUES[letters[0]] > VALUES[letter]:
            q += VALUES[letters[0]] - VALUES[letter]
            letters.pop(0)
        else:
            q += VALUES[letter]
    return q


if __name__ == '__main__':
    
    tests = [
        ('XIV', 14),
        ('VI', 6),
        ('LXX', 70),
        ('IV', 4),
        ('IX', 9),
        ('MCMLXXXIV', 1984),
        ('MMXVIII', 2018),
        ('MCDXCII', 1492),
        ('XCIX', 99)
        
    ]
    
    for test, expected in tests:
        print test, f(test)
        assert expected == f(test)
