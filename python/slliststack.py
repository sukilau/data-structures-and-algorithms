'''
Implementation of Stack using Singly Linked List

Basic operations: 
get(i)			O(n)
set(i,x)		O(n)
add(i,x)		O(n)
remove(i)		O(n)

push(x)			O(1)
pop()			O(1)

peek()			O(1)
getSize()		O(1)
isEmpty()		O(1)
'''
class Stack(object):

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
		return Stack.Node(x)

	def push(self, x):
		'''Add new node with value x at the start'''
		u = self.new_node(x)
		u.next = self.head
		self.head = u
		if self.size == 0:
			self.tail = u
		self.size += 1
		return x

	def pop(self):
		'''Remove node at the start'''
		if self.size == 0:
			return None
		u = self.head
		self.head = u.next 
		if self.size == 1:
			self.tail = None
		self.size -= 1
		return u.value

	def peek(self):
		'''Return node value at the start'''
		return self.head.value
		
	def getSize(self):
		'''Return size'''
		return self.size

	def isEmpty(self):
		'''Check if empty'''
		return self.size == 0