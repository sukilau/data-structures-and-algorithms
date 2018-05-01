'''
Implementation fo adjancecy matrix representation of a graph

Basic operations	
add_edge(i,j)				O(1)
remove_edge(i,j)			O(1)
has_edge(i,j)				O(1)
out_edges(i)				O(|V|), |V|=num of vertices
in_edges(i)					O(|V|), |V|=num of vertices
in_degree(i)				O(|V|), |V|=num of vertices
out_degree(i)				O(|V|), |V|=num of vertices

Space for AdjacencyMatrix = O(n^2)
'''
import numpy   

class AdjacencyMatrix(object):
	def __init__(self, n):
		self.n = n
		self.a = numpy.zeros([n,n])
		# self.a = numpy.zeros([n, n], numpy.bool_)

	def add_edge(self, i, j, w):
		self.a[i][j] = w

	def remove_edge(self, i, j):
		self.a[i][j] = 0

    def has_edge(self, i, j):
        return (self.a[i][j]>0)

	def out_edges(self, i):
		'''Get all edges from the node'''
		out = []
		for j in range(self.n):
			if self.a[i][j]>0: out.append(j)
		return out

	def in_edges(self, i):
		'''Get all edegs to the node'''
		_in = []
		for j in range(self.n):
			if self.a[j][i]>0: _in.append(j)
		return _in

	def out_degree(self, i):
		'''Compute number of edges to the node'''
		deg = 0
		for j in range(self.n):
			if self.a[i][j]>0:
				deg += 1
		return deg

	def in_degree(self, i):
		'''Compute number of edges from the node'''
		deg = 0
		for j in range(self.n):
			if self.a[j][i]>0:
				deg += 1
		return deg
