'''
Implementation of Binary Search Tree

BST
-	At most 2 children for each node
-	The left subtree of a node contains only nodes with keys lesser than the node’s key.
-	The right subtree of a node contains only nodes with keys greater than the node’s key.
-	The left and right subtree each must also be a binary search tree. There must be no duplicate nodes.

Basic operations (not necessarily balanced):
				Worst
insert(x)		O(h) = O(n) for skewed tree, h=height, n=num of nodes
search(x)		O(h) = O(n) for skewed tree, h=height, n=num of nodes
remove(x)		O(h) = O(n) for skewed tree, h=height, n=num of nodes
printTree()			
size()			
height()		

Reference:
https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/
https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/
https://www.geeksforgeeks.org/complexity-different-operations-binary-tree-binary-search-tree-avl-tree/
'''
class BinarySearchTree(object):

	class Node(object):
		def __init__(self, val):
			self.left = None
			self.right = None
			self.value = val

	def __init__(self):
		self.root = None

	def new_node(self, val):
		return BinarySearchTree.Node(val)

	def insert(self, val):
		'''
		Insert a new node as a child of leaf node.
		Note that this may lead to a long unbalanced BST
		'''
		self._insert(self.root, val)

	def _insert(self, node, val):
		'''Helper method for insert() using recursion'''
		if node.value < val:
			if node.right:
				self._insert(node.right, val)
			else: 
				node.right = self.new_node(val)
		else:
			if node.left:
				self._insert(node.left, val)
			else:
				node.left = self.new_node(val)

	def search(self, val):
		return self._search(self.root, val)

	def _search(self, node, val):
		'''Helper method for search() using recursion'''
		if node:
			if node.value == val:
				return True
			elif node.value < val:
				return self._search(node.right, val)
			else:
				return self._search(node.left, val)
		return False


	def remove(self, val):
		'''
		Note that when we delete a node, there are 3 possibilities
		-	Node to be deleted is leaf: Simply remove from the tree
		-	Node to be deleted has only one child: Copy the child to the node and delete the child
		-	Node to be deleted has two children
		'''
		if self.root is None: return None
		return self._remove(self.root, val)

	def _remove(self, node, val):
		'''Helper method for remove() using recursion'''

		# Base case: return new root
		if node is None:
			return node

		# Traverse to left subtree if val<node.value
		if val < node.value:
			node.left = self._remove(node.left, val)

		# Traverse to right subtree if val>node.value
		elif val > node.value:
			node.right = self._remove(node.right, val)

		# Delete node if the val=node.value
		else:
			# Case when node has no child or only one child
			if node.left is None:
				temp = node.right
				node = None
				return temp
			elif node.right is None:
				temp = node.left
				node = None
				return temp
			# Case when node has 2 children: get inorder sucessor i.e. smallest in the right substree
			temp = self._minInorder(node.right)
			# Copy inorder sucessor's value to this node and delete the inorder sucessor
			node.value = temp.value
			node.right = self._remove(node.right, temp.value)

		return node

	def _minInorder(self, node):
		'''
		Helper method for remove()
		Return node with minimum value
		''' 
		curr = node
		while curr.left is not None:
			curr = curr.left
		return curr

	def printTree(self):
		'''Print tree in sorted order using in-order traversal'''
		print("In-order traversal: ", self.inorder(self.root, traversal=[]))

	def inorder(self, node, traversal):
		'''Helper method for printTree() using in-order traversal'''
		if node:
			self.inorder(node.left, traversal)
			# print(node.value)
			traversal.append(node.value)
			self.inorder(node.right, traversal)
		return traversal

	def size(self):
		'''Find size (number of nodes) of the tree'''
		return self._size(self.root)

	def _size(self, node):
		'''Helper method for size() using recursion'''
		if node is None: 
			return 0
		return 1 + self._size(node.left) + self._size(node.right)

	def height(self):
		'''Find height of the tree'''
		return self._height(self.root)

	def _height(self, node):
		'''Helper method for height() using recursion'''
		if node is None: 
			return 0
		return 1 + max(self._height(node.left), self._height(node.right))



