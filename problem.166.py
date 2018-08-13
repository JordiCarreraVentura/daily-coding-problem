# This problem was asked by Uber.
# 
# Implement a 2D iterator class. It will be initialized with an array of arrays, and should implement the following methods:
# 
# next(): returns the next element in the array of arrays. If there are no more elements, raise an exception.
# has_next(): returns whether or not the iterator still has elements left.
# For example, given the input [[1, 2], [3], [], [4, 5, 6]], calling next() repeatedly should output 1, 2, 3, 4, 5, 6.
# 
# Do not use flatten or otherwise clone the arrays. Some of the arrays can be empty.

class Iterator2DIterationEndException(Exception):
    pass



class Iterator2D:

    def __init__(self, arrays):
        self._data = arrays
        self.i = 0
        self.j = 0

    def next(self):
        if self.has_next():
            return self.__pop()
        else:
            raise Iterator2DIterationEndException()
    
    def __pop(self):
        array = self._data[self.i]
        out = array[self.j]
        self.j += 1
        return out
    
    def has_next(self):
        while self.i < len(self._data):
            if self.j < len(self._data[self.i]):
                return True
            else:
                self.j = 0
                self.i += 1
        return False
    
    def __str__(self):
        return '%d/%d' % (self.i, self.j)



if __name__ == '__main__':

    test = [[1, 2], [3], [], [4, 5, 6]]
    
    c = Iterator2D(test)
    
    while c.has_next():
        print c, c.next()
