'''
Implementation fo adjancecy list representation of a graph

Basic operations	
add_edge(i,j)				O(1)
remove_edge(i,j)			O(deg(i))
has_edge(i,j)				O(deg(i))
out_edges(i)				O(1)
out_degree(i)				O(1), 
in_edges(i)					O(|V|+|E|), |V|=num of vertices, |E|=num of edges
in_degree(i)				O(|V|+|E|), |V|=num of vertices, |E|=num of edges


Space for AdjacencyList = O(n+m)
'''
class AdjacencyList(object):
    def __init__(self, n):
        self.n = n
        self.a = [None]*n
        for i in range(self.n):
        	self.a[i] = []
        	# self.a[i] = ArrayStack()

    def add_edge(self, i, j):
        self.a[i].append(j)

    def remove_edge(self, i, j):
        self.a[i].remove(j)

    def has_edge(self, i, j):
        if j in self.a[i]: return True
        return False

    def out_edges(self, i):
        '''Get all edges from the node'''
        return self.a[i]

    def out_degree(self, i):
        '''Compute number of edges to the node'''
        return len(self.a[i])

    def in_edges(self, i):
        '''Get all edegs to the node'''
        _in = []
        for j in range(self.n):
            if self.has_edge(j,i): 
                _in.append(j)
        return _in

    def in_degree(self, i):
        '''Compute number of edges from the node'''
        deg = 0
        for j in range(self.n):
            if self.has_edge(j,i): 
                deg += 1
        return deg
