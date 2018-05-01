'''
Implementation of Binary Tree
* Binary Tree: At most two children for each node

Basic operations:
				Worst case
search(x)		O(n), n = number of nodes
insert(x)		O(n)	
remove(x)		O(n)

Tree traversals:
				Wost case
pre-order		O(n)
in-orrder		O(n)
post-order		O(n)
level-order		O(n)
'''
class BinaryTree(object):
	class Node(object):
		def __init__(self, val):
			self.left = None
			self.right = None
			# self.parent = None
			self.value = val

	def __init__(self):
		self.root = None

	def new_node(self, val):
		return BinaryTree.Node(val)

	def printTree(self):
		print("Print tree in preorder traversal: ", self.preorder(self.root, traversal=[]))
		print("Print tree in inorder traversal: ",self.inorder(self.root, traversal=[]))
		print("Print tree in postorder traversal: ",self.postorder(self.root, traversal=[]))
		print("Print tree in levelorder traversal: ",self.levelorder(self.root, traversal=[]))

	def inorder(self, node, traversal):
		'''
		Helper method
		Implemented by recursion: traverse the left subtree => visit the root => traverse the right subtree
		'''
		if node:
			self.inorder(node.left, traversal)
			traversal.append(node.value)
			self.inorder(node.right, traversal)
			return traversal

	def preorder(self, node, traversal):
		'''
		Helper method
		Implemented by recursion: visit the root => traverse the left subtree => traverse the right subtree
		'''
		if node:
			traversal.append(node.value)
			self.preorder(node.left, traversal)
			self.preorder(node.right, traversal)
			return traversal

	def postorder(self, node, traversal):
		'''
		Helper method
		Implemented by recursion: traverse the left subtree => traverse the right subtree => visit the root
		'''
		if node:
			self.postorder(node.left, traversal)
			self.postorder(node.right, traversal)
			traversal.append(node.value)
			return traversal

	def levelorder(self, node, traversal):
		'''
		Helper method: implemented by iteration using queue
		'''
		if node:
			queue = [node]
			while len(queue) > 0:
				node = queue.pop(0)				#deque first element
				traversal.append(node.value)
				if node.left is not None:
					queue.append(node.left)		#enqueue left child
				if node.right is not None:
					queue.append(node.right)	#deque right child
			return traversal


	def search(self, val):
		return self._search(self.root, val)

	def _search(self, node, val):
		'''Helper method for search(): preorder search'''
		if node:
			if node.value == val:
				return True
			else:
				return self._search(node.left, val) or self._search(node.right, val)
		return False

	def insert(self, val):
		pass
		
	def remove(self, val):
		pass

	# def depth(self, node):
	# 	'''Find depth of a node. Note that depth(root node)=0'''
	# 	d = 0
	# 	while (node != self.root):
	# 		node = node.parent
	# 		d += 1
	# 	return d

	def size(self):
		'''Find size (number of nodes) of the tree'''
		return self._size(self.root)

	def _size(self, node):
		'''Helper method for size()'''
		if node is None: 
			return 0
		return 1 + self._size(node.left) + self._size(node.right)

	def height(self):
		'''Find height of the tree'''
		return self._height(self.root)

	def _height(self, node):
		'''Helper method for size()'''
		if node is None: 
			return 0
		return 1 + max(self._height(node.left), self._height(node.right))













