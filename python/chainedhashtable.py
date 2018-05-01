'''
Set Implementation of Hash Table using Chaining

Basic operations: 
get(x)          O(1)
add(x)        	O(1)
remove(x)       O(1)

Note:
- 	Hash Table: maps key to value for higher efficiency look up
- 	Hash function: maps a key (big no. or string) to a smaller integer, which indicates index in the array
- 	Collison: when two key maps to the same value
- 	Two ways to handle collision: 
	- 	Chaining : store data as an array of linked lists
	- 	Linear Probing (also called Open Addressing) 

Chaining
- 	The idea is to make each cell of hash table point to 
	a linked list of records that have same hash function value. 
- 	Chaining is simple, but requires additional memory outside the table.
'''
class ChainedHashTable(object):
	'''
	An implementation of a HashTable class that stores strings in a hash table, 
	where keys are calculated using the first two letters of the string.

	Note that
	- we have used list of list here for convenience
	- we have not resized the array
	'''
    def __init__(self):
    '''Initialize an array (size=1000000) of empty linked lists'''
        self.t = [None]*100000
        
    def hashFunction(self, x):
		'''Return hash value for string x'''
        value = ord(x[0])*100 + ord(x[1])
        return value  

    def add(self, x):
		'''Add string x to hash table'''
        hv = self.hashFunction(x)
        if hv != -1:
            if self.t[hv] != None:
                self.t[hv].append(x)
            else:
                self.t[hv] = [x]
        return x

    def get(self, x):
		'''Find string x in hash table'''
        hv = self.hashFunction(x)
        if hv != -1:
            if self.t[hv] != None:
                if x in self.t[hv]:
                    return hv
        return -1






'''
A more detailed example using mulitplicatiive hash function and storing data in a array of stack
Note that we need to resize the array if number of elements exceed the size
''' 
import numpy
import random
from arraystack import StaticArrayStack
w = 32

def new_array(n, dtype=numpy.object):
	return numpy.empty(n, dtype)

class ChainedHashTable2(object):
    def __init__(self, iterable=[]):
	'''Store data as an array, t, of lists'''
        self._initialize()
        self.add_all(iterable)
        
    def _initialize(self):
 		''' 
		d keep track of the array size
		t hash table initialized with size = 2^d
		z random odd number
		n keep track of total number of elements in all list
		'''
        self.d = 1
        self.t = self._alloc_table((1<<self.d))
        self.z = self._random_odd_int()
        self.n = 0

    def _random_odd_int(self):
		'''Generate a random odd integer in {1,..., 2^w-1}'''
        return random.randrange(1<<w) | 1
            
    def clear(self):
        self.d = 1
        self.t = self._alloc_table((1<<self.d))
        self.n = 0
        
    def _alloc_table(self, s):
		'''
		Set an array (size s) of empty lists
		Note that we use an array of array for convenience instead
		'''
        return [ArrayStack() for _ in range(s)]
    
    def _resize(self):
		'''Double of size of array or shrink if needed'''
        self.d = 1
        while (1 << self.d) <= self.n: self.d += 1 		#condition: 2^d <= n
        self.n = 0
        old_t = self.t
        self.t = self._alloc_table(1<<self.d)
        for i in range(len(old_t)):
            for x in old_t[i]:
                self.add(x)
    
    def _hash(self, x):
		'''
		Implement multiplcative hashing
		Set hash function hash(x) = ((z * x) mod (2^w)) div 2^(w-d),
		where z is a radom odd integer in {1,..., 2^w-1}
		'''
        return ((self.z * hash(x)) % (1<<w)) >> (w-self.d)
    
    def add(self, x):
        if self.find(x) is not None: return False
        if self.n+1 > len(self.t): self._resize()
        self.t[self._hash(x)].append(x)
        self.n += 1
        return True
    
    def remove(self, x):
        ell = self.t[self._hash(x)]
        for y in ell:
            if y == x:
                ell.remove_value(y)
                self.n -= 1
                if 3*self.n < len(self.t): self._resize() 
                return y
        return None 
        
    def find(self, x):
        for y in self.t[self._hash(x)]:
            if y == x:
                return y
        return None
    
    def __iter__(self):
        for ell in self.t:
            for x in ell:
                yield x

