# Given a list of words, return the shortest unique prefix of each word. For example, given the list:
# 
# dog
# cat
# apple
# apricot
# fish
#
#
# Return the list:
# 
# d
# c
# app
# apr
# f


def f(w):
    space = [x for x in V]
    curr = ''
    while len(space) > 1 and len(curr) < len(w):
        curr += w[len(curr)]
        space = [x for x in space if x.startswith(curr)]
    return curr


V = 'dog cat apple apricot fish applet apple foo'.split()


if __name__ == '__main__':
    
    for w in V:
        print w, f(w)
