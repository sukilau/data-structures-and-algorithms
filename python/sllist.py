'''
Implementation of Singly Linked List

Basic operations (by index): 
get(i)			O(n)
set(i,x)		O(n)
add(i,x)		O(n)
remove(i)		O(n)

Additional operations:
peek()			O(1)
getSize()		O(1)
isEmpty()		O(1)
get_node(i)		O(n)	- helper dunction for get(), set(), add(), remove()
push(x)			O(1)   	- helper function for add()
pop()			O(1)	- helper function for remove()
enqueue(x)		O(1)
dequeue(x)		O(1)

Note that Stack and Queue can be implemented using Singly Linked List
Stack operations: 	push(x), pop()	
Queue operations:	enqueue(x), dequeue()
'''
class SLList(object):

    class Node(object):
        def __init__(self, x):
            self.value = x
            self.next = None

    def __init__(self):
        self._initialize()

    def _initialize(self):
        self.size = 0
        self.head = None
        self.tail = None

    def new_node(self, x):
        return SLList.Node(x)

    def get_node(self, i):
        '''
        Helper function for get(), set(), add(), remove().
        Return node at index i.
        '''
        u = self.head
        for _ in range(i):
            u = u.next
        return u

    def push(self, x):
        '''
        Helper function for add()
        Add new node with value x at the start
        '''
        u = self.new_node(x)
        u.next = self.head
        self.head = u
        if self.size == 0:
            self.tail = u
        self.size += 1

    def pop(self):
        '''
        Helper function for remove()
        Remove node at the start
        '''
        if self.size == 0:
            return None
        u = self.head
        self.head = u.next 
        if self.size == 1:
            self.tail = None
        self.size -= 1
        return u.value

    def get(self, i):
        '''Get node value by index i'''
        if (i<0 or i>=self.size): raise IndexError()
        return self.get_node(i).value

    def set(self, i, x):
        '''Set node value to x by index i'''
        if (i<0 or i>=self.size): raise IndexError()
        u = self.get_node(i)
        y = u.value
        u.value = x
        return y

    def add(self, i, x):
        '''Insert new node with value x at index i'''
        if (i<0 or i>self.size): raise IndexError()
        if i == 0: 
            self.push(x)
            return True
        else:
            u = self.new_node(x)
            w = self.get_node(i-1)
            u.next = w.next
            w.next = u
        self.size += 1
        return True

    def remove(self, i):
        '''Remove node by index i'''
        if (i<0 or i>=self.size): raise IndexError()
        if i == 0: 
            return self.pop()
        u = self.get_node(i-1)
        w = u.next
        u.next = u.next.next
        self.size -= 1
        return w.value 

    def peek(self):
        '''Return node value at the start'''
        return self.head.value

    def getSize(self):
        '''Return size'''
        return self.size

    def isEmpty(self):
        '''Check if empty'''
        return self.size == 0

    def enqueue(self, x):
        '''Add node value x at the end'''
        u = self.new_node(x)
        if self.size == 0:
            self.head = u
        else:
            self.tail.next = u
        self.tail = u
        self.size += 1

    def dequeue(self):
        '''Remove node at the start'''
        return self.pop()