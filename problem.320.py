# This problem was asked by Amazon.
# 
# Given a string, find the length of the smallest window that contains
# every distinct character. Characters may appear more than once in
# the window.
# 
# For example, given "jiujitsu", you should return 5, corresponding to 
# the final five letters.

def f(w):
    chars = set([char for char in w])
    l = len(chars)
    for j in range(l, len(w)):
        for i in range(len(w) - (j - 1)):
            candidate = [char for char in w[i:i + j]]
            hypothesis = set(candidate)
            if len(hypothesis.intersection(chars)) == len(chars):
                return ''.join(candidate)
    return w
    


if __name__ == '__main__':
    text = """This problem was asked by Amazon.

Given a string, find the length of the smallest window that contains
every distinct character. Characters may appear more than once in
the window.

For example, given "jiujitsu", you should return 5, corresponding to 
the final five letters."""

    for word in text.lower().split():
        w = word.strip('",.;')
        print w, f(w)
