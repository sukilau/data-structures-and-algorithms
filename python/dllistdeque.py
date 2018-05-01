'''
Implementation of Deque using Doubly Linked List 

Basic operations: 
add_first(x)	O(1) 	
remove_first()	O(1)
add_last(x)		O(1)
remove_last()	O(1)

Other operations:
getSize()       O(1)
isEmpty()       O(1)
get_node(i)     O(1 + min{i, n − i})    - helper function for get(), set(), add(), remove()
get(i)          O(1 + min{i, n − i})
set(i,x)        O(1 + min{i, n − i})
add(i,x)        O(1 + min{i, n − i})
remove(i)       O(1 + min{i, n − i})
'''
class Deque(object):

    class Node(object):
        def __init__(self, x):
            self.value = x
            self.next = None
            self.prev = None

    def __init__(self):
        self._initialize()

    def _initialize(self):
        self.size = 0
        self.dummy = DLList.Node(None)
        self.dummy.prev = self.dummy
        self.dummy.next = self.dummy

    def new_node(self, x):
        return DLList.Node(x)

    def get_node(self, i):
        '''
        Helper function for get(), set(), add(), remove().
        Get node value at index i by either starting from head and work forward, 
        or starting at tail and work backward.
        Return node at index i
        Run time: O(1 + min{i, n − i})
        '''
        if i < self.size/2:
            u = self.dummy.next     #dummy.next=head
            for _ in range(i):
                u = u.next
        else:
            u = self.dummy          #dummy.prev=tail
            for _ in range(self.size, i, -1):
                u = u.prev
        return u

    def get(self, i):
        '''Get node value by index i'''
        if (i<0 or i>=self.size): raise IndexError()
        return self.get_node(i).value

    def set(self, i, x):
        '''Set node value to x by index i, return original value'''
        if (i<0 or i>=self.size): raise IndexError()
        u = self.get_node(i)
        y = u.value
        u.value = x
        return y

    def add(self, i, x):
        '''Insert new node with value x at index i'''
        if (i<0 or i>self.size): raise IndexError()
        u = self.new_node(x)
        w = self.get_node(i)
        u.prev = w.prev
        u.next = w
        u.prev.next = u
        u.next.prev = u
        self.size += 1
        return x

    def remove(self, i):
        '''Remove node by index i, return value of removed node'''
        if (i<0 or i>=self.size): raise IndexError()
        w = self.get_node(i)
        y = w.value
        w.prev.next = w.next
        w.next.prev = w.prev
        self.size -= 1
        return y

    def getSize(self):
        '''Return size'''
        return self.size

    def isEmpty(self):
        '''Check if empty'''
        return self.size == 0

    def add_first(self, x):
        return self.add(0,x)

    def remove_first(self):
        return self.remove(0)

    def add_last(self, x):
        return self.add(self.size,x)

    def remove_last(self):
        return self.remove(self.size-1)
