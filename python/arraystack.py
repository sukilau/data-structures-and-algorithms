'''
Implementation of Stack using Array

Basic operations: 
get(i)          O(1)
set(i,x)        O(1)
add(i,x)        O(n-i)
remove(i)       O(n-i)

push(x)         O(1)
pop()           O(1)

peek()          O(1)
getSize()       O(1)
isEmpty()       O(1)
'''
import numpy
def new_array(n, dtype=numpy.object):
    return numpy.empty(n, dtype)

class StaticArrayStack(object):
    '''
    Implementation of Stack using static array (numpy.empty(n)) 
    Note that 
    - we need to resize if number of elements exceed the array
    - we ignore the cost of the potential call to resize()
    '''
    def __init__(self):
        self._initialize()
        
    def _initialize(self):
        self.a = new_array(1)
        self.n = 0

    def _resize(self):
        '''
        Helper function for add() and remove()
        It allocates a new array b whose size is 2n 
        and copies the n elements of a into the first n positions in b, and then sets a to b. 
        '''
        b = new_array(max(1, 2*self.n))
        b[0:self.n] = self.a[0:self.n]
        self.a = b

    def get(self, i):
        if i < 0 or i >= self.n: raise IndexError()
        return self.a[i]

    def set(self, i, x):
        if i < 0 or i >= self.n: raise IndexError()
        y = self.a[i]
        self.a[i] = x
        return y

    def add(self, i, x): 
        if i < 0 or i > self.n: raise IndexError()
        if self.n == len(self.a): self._resize()
        self.a[i+1:self.n+1] = self.a[i:self.n]
        self.a[i] = x
        self.n += 1

    def remove(self, i): 
        if i < 0 or i >= self.n: raise IndexError()
        x = self.a[i]
        self.a[i:self.n-1] = self.a[i+1:self.n]
        self.n -= 1
        if len(self.a) >= 3*self.n: self._resize()
        return x
  
    def push(self, x):
        '''Add element at the end'''
        self.add(self.n, x)
        return x

    def pop(self):
        '''Remove element at the end'''
        return self.remove(self.n-1)

    def getSize(self):
        return self.n

    def isEmpty(self):
        return self.n == 0

    def peek(self):
        return self.a[self.n-1]




class DynmaicArrayStack(object):
    '''
    Implementation of Stack using dynamic array (List) 
    Note that 
    - "List" in Python is a dynamic array
    - It has built-in function pop(), append(), insert()
    '''
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []



