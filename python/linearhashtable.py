'''
Set Implementation of Hash Table using Linear Probing

Basic operations: 
get(x)          O(1)
add(x)        	O(1)
remove(x)       O(1)

Open Addressing with Linear Probing
	- 	In open addressing, all elements are stored in the hash table itself. 
	- 	Each table entry contains either a record or NIL. When searching for an element, 
		we one by one examine table slots until the desired element is found or it is clear that the element is not in the table.
	- Open addresisng can be done by linear probing, i.e. we linearly probe for next slot.

Reference: https://www.geeksforgeeks.org/hashing-set-3-open-addressing/
'''
class LinearHashTable(object):
    
    def __init__(self,size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size
        
    def put(self,key,data):
        #Note, we'll only use integer keys for ease of use with the Hash Function
        
        # Get the hash value
        hashvalue = self.hashfunction(key,len(self.slots))

        # If Slot is Empty
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        
        else:
            
            # If key already exists, replace old value
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  
            
            # Otherwise, find the next available slot
            else:
                
                nextslot = self.rehash(hashvalue,len(self.slots))
                
                # Get to the next slot
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot,len(self.slots))
                
                # Set new key, if NONE
                if self.slots[nextslot] == None:
                    self.slots[nextslot]=key
                    self.data[nextslot]=data
                    
                # Otherwise replace old value
                else:
                    self.data[nextslot] = data 

    def hashfunction(self,key,size):
        # Remainder Method
        return key%size

    def rehash(self,oldhash,size):
        # For finding next possible positions
        return (oldhash+1)%size
    
    def get(self,key):    
        # Getting items given a key
        
        # Set up variables for our search
        startslot = self.hashfunction(key,len(self.slots))
        data = None
        stop = False
        found = False
        position = startslot
        
        # Until we discern that its not empty or found (and haven't stopped yet)
        while self.slots[position] != None and not found and not stop:
            
            if self.slots[position] == key:
                found = True
                data = self.data[position]
                
            else:
                position=self.rehash(position,len(self.slots))
                if position == startslot:
                    
                    stop = True
        return data

    # Special Methods for use with Python indexing
    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)








'''
A more detailed example  -	A Set implementation that uses hashing with linaer probing
'''
import numpy

w = 32

def new_array(n, dtype=numpy.object):
	return numpy.empty(n, dtype)

class LinearHashTable2(Object):
    
    def __init__(self, iterable=[]):
        self._initialize()
        self.initialize()
        self.add_all(iterable)
        
    def _initialize(self):
        self.dl = object()
        
    def initialize(self):
    	'''
    	There are 3 types of entries stored in t
    	1. data values
    	2. nil values
    	3. del values

    	q keep track of numeber of elements of Types 1 and 3 (non-nil values)
    	n keep track of number of element in hash table
    	len(t) = 2^d 
    	'''
        self.d = 1
        self.t = new_array((1<<self.d))
        self.q = 0
        self.n = 0
        
    def _resize(self):
        self.d = 1
        while ((1<<self.d) < 3*self.n): self.d += 1
        told = self.t
        self.t = new_array((1<<self.d))
        self.q = self.n
        for x in told:
            if x is not None and x != self.dl:
                i = self._hash(x)
                while self.t[i] is not None: 
                    i = (i+1) % len(self.t)
                self.t[i] = x

    def hash_code(self, x):
        return hash(x)
    
    def _hash(self, x):
        h = self.hash_code(x)
        return  (self.tab[0][h&0xff] \
                 ^ self.tab[1][(h>>8)&0xff] \
                 ^ self.tab[2][(h>>16)&0xff] \
                 ^ self.tab[3][(h>>24)&0xff]) >> (w-self.d)
                  
    def add(self, x):
    	'''
    	If x is not already stored in the table,
    	we search t[i], t[(i+1) mod len(t)],...
    	until we find a nil or del
    	'''
        if self.find(x) is not None: return False
        if 2*(self.q+1) > len(self.t): self._resize()
        i = self._hash(x)
        while self.t[i] is not None and self.t[i] != self.dl:
            i = (i + 1) % len(self.t)
        if self.t[i] is None: self.q += 1
        self.n += 1
        self.t[i] = x
        return True
      
    def find(self, x):
    	'''
    	Start at array entry t[i] where i=hash(x)
    	and search entries t[i], t[(i+1) mod len(t)],...
    	until we find an index i' such that t[i']=x or t[i']=nil
    	'''
        i = self._hash(x)
        while self.t[i] is not None:
            if self.t[i] != self.dl and x == self.t[i]: 
                return self.t[i]
            i = (i + 1) % len(self.t)
            
    def remove(self, x):
    	'''
    	Search t[i], t[(i+1) mod len(t)],...
    	until we find an index i' such that t[i']=x or t[i']=nil
    	if t[i']=x, set t[i']=del
    	'''
        i = self._hash(x)
        while self.t[i] is not None:
            y = self.t[i]
            if y != self.dl and x == y:
                self.t[i] = self.dl
                self.n -= 1
                if 8*self.n < len(self.t): resize()
                return y
            i = (i + 1) % len(self.t)
        return None
    
    def clear(self):
        self.initialize()
        
    def __iter__(self):
        for x in self.t:
            if x is not None and x != self.dl:
                yield x
