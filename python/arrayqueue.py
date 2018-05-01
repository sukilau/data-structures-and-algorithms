'''
Implementation of Queue using Circular Array 

Basic operations: 
enqueue(x)      O(1)
dequeue()       O(1)
'''
import numpy
def new_array(n, dtype=numpy.object):
    return numpy.empty(n, dtype)

class CircularArrayQueue(object):
    '''
    Implementation of Queue using circular array (numpy.empty(n)) 
    Note that 
    - we need to resize if number of elements exceed the array
    - using modular arithmetic we can store the queue elements at array locations 
        a[j mod length(a)],a[(j+1) mod length(a)],...,a[(j+n−1) mod length(a)].
        This treats the array a like a circular array in which 
        array indices larger than length(a) − 1 “wrap around” to the beginning of the array.
    Reference:
    https://stackoverflow.com/questions/12755139/why-implement-queues-as-circular-array
    '''
    def __init__(self):
        self._initialize()
        
    def _initialize(self):
        self.a = new_array(1)
        self.j = 0           #j is used to keep track of the position of the first element
        self.n = 0
    
    def _resize(self):
        '''
        Helper function for add() and remove()
        It allocates a new array b whose size is 2n 
        and copies the n elements of a into the first n positions in b, and then sets a to b. 
        '''
        b = new_array(max(1, 2*self.n))
        for k in range(self.n):
            b[k] = self.a[(self.j+k) % len(self.a)]
        self.a = b
        self.j = 0
    
    def enqueue(self, x):
        if self.n + 1 > len(self.a): self._resize()
        self.a[(self.j+self.n) % len(self.a)] = x       #assign x to the position (j+n) mod len(a)
        self.n += 1                                     #increment n
        return True

    def dequeue(self):
        if self.n == 0: raise IndexError()
        x = self.a[self.j]                              #remove
        self.j = (self.j + 1) % len(self.a)             #increment j
        self.n -= 1                                     #decrement n
        if len(self.a) >= 3*self.n: self._resize()
        return x






class DynamicArrayQueue(object):
    '''
    Implementation of Queue using dynamic array (List) 
    Note that 
    - "List" in Python is a dynamic array
    - It has built-in function pop(), append(), insert()
    '''
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []