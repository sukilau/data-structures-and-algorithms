'''
Implementation of Binary Heap
- 	A binary heap is a complete binary tree which satisfies the heap ordering property. The ordering can be one of two types:
-	the min-heap property: the value of each node is greater than or equal to the value of its parent, with the minimum-value element at the root.
-	the max-heap property: the value of each node is less than or equal to the value of its parent, with the maximum-value element at the root.

Basic operations:
getMin			O(1)
insert()		O(logn)
extractmin()	O(logn)

Application of Heaps
- heapSort O(nlogn)
- priority queue - insert(), remove(), extractmax(), decreaseKey(): O(nlogn)
- graph algoirthms - Dijkstra's Shortest Path, Prim's Minimum Spanning Tree

Reference:
https://www.geeksforgeeks.org/binary-heap/
https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/
'''
class BinaryHeap(object):
	'''Implementation of Minimum Heap'''
	def __init__(self, a):
		self.a = a 		#heap list
		self.size = len(a)
	
	def _parent(self, i):
		'''Helper method: Return index of parent node in heap list'''
		return (i-1)//2

	def _left(self, i):
		'''Helper method: Return index of left node in heap list'''
		return 2*i+1

	def _right(self, i):
		'''Helper method: Return index of right node in heap list'''
		return 2*(i+1) 

	def _moveup(self, i):
		'''Helper method for insert(): If a node is smaller than parent, swap wih parent'''
		p = self._parent(i)
		while i > 0 and self.a[i] < self.a[p]:
			self.a[i], self.a[p] = self.a[p], self.a[i]
			i = p
			# p = self._parent(i)
	
	def insert(self, val):
		'''
		Idea: Append new node at the end of the heap list
		and then swap with its parent 
		until it's no longer smaller than the parent node.
		
		Note that we do not need to resize the heap list (array) if we use Python list (which is a dynamic array)
		'''
		# if len(self.a)<self.size+1:
		# 	self.resize()
		self.a.append(val)
		self.size +=1 
		self._moveup(self.size-1)
		return True

	def _movedown(self, i):
		'''Helper method for extractmin()'''
		while i >= 0:
			j = -1
			r = self._right(i)
			l = self._left(i)
			# swap with the min child
			if r < self.size and self.a[i] > self.a[r]:
				if self.a[l] < self.a[r]:
						j = l
				else: j = r
			elif l < self.size and self.a[i] > self.a[l]:
				j = l
			if j >= 0:
				self.a[i], self.a[j] = self.a[j], self.a[i]
			i = j

	def extractmin(self):
		'''
		Idea: Replace the root with the last node
		and then swap with the smallest of its two children child 
		until it's no longer larger than any of its children		
		'''
		x = self.a[0]
		self.a[0] = self.a[self.size-1]
		self.a.pop()
		self.size -=1 
		self._movedown(0)
		return x 

	def getmin(self):
		if self.size == 0: raise IndexError()
		return self.a[0]

	def makeheap(self, a):
		'''Make a new heap from a unordered list'''
		self.a = a
		for i in range(self.size//2-1, -1, -1):
			self._movedown(i)




