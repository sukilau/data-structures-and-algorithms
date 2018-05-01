'''
Implementation of Graph using Node and Edge class

Graph Representation
- Edge list
- Adjacency list
- Adjacency matrix

Graph Trasversal
- Depth First Search
- Breadth First Search

Basic operations:
add_node()
add_edge()
get_edge_list()
get_adj_list()
get_adj_matrix()
'''

class Graph(object):

	class Node(object):
		def __init__(self, val=None):
			self.value = val
			self.edges = []
	
	class Edge(object):
		def __init__(self, val=None, node_from=None, node_to=None):
			self.value = val
			self.node_from = node_from 
			self.node_to = node_to

	def __init__(self, nodes=[], edges=[]):
		self.nodes = nodes
		self.edges = edges

	def add_node(self, val):
		new_node = Graph.Node(val)
		self.nodes.append(new_node)
       
	def add_edge(self, node_from_val, node_to_val, new_edge_val):
	    from_found = None
	    to_found = None
	    for node in self.nodes:
	        if node_from_val == node.value:
	            from_found = node
	        if node_to_val == node.value:
	            to_found = node
	    if from_found == None:
	        from_found = Graph.Node(node_from_val)
	        self.nodes.append(from_found)
	    if to_found == None:
	        to_found = Graph.Node(node_to_val)
	        self.nodes.append(to_found)
	    new_edge = Graph.Edge(new_edge_val, from_found, to_found)
	    from_found.edges.append(new_edge)
	    to_found.edges.append(new_edge)
	    self.edges.append(new_edge)

	def get_edge_list(self):
		edge_list = []
		for e in self.edges:
			edge = (e.node_from.value, e.node_to.value, e.value)
			edge_list.append(edge)
		return edge_list

	def _max_index(self):
	    max_index = -1
	    if len(self.nodes):
	        for node in self.nodes:
	            if node.value > max_index:
	                max_index = node.value
	    return max_index

	def get_adj_list(self):
	    max_index = self._max_index()
	    adj_list = [None] * (max_index + 1)
	    for i in range(max_index + 1):
        	adj_list[i] = []
	    for e in self.edges:
	        if adj_list[e.node_from.value]:
	            adj_list[e.node_from.value].append((e.node_to.value, e.value))
	        else:
	            adj_list[e.node_from.value] = [(e.node_to.value, e.value)]
	    return adj_list

	def get_adj_matrix(self):
	    max_index = self._max_index()
	    adj_matrix = [[0 for i in range(max_index + 1)] for j in range(max_index + 1)]
	    for e in self.edges:
	        adj_matrix[e.node_from.value][e.node_to.value] = e.value
	    return adj_matrix



