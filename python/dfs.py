'''
DFS for Graph

Use Recursion
1. Print visited node
2. Traverse to unvisited adjacent nodes by recursion

For disconnected graph, we should repeat for every vertex as strating point.

Run time : O(|V|+|E|)

Reference
http://www.geeksforgeeks.org/depth-first-traversal-for-a-graph/
'''
from collections import defaultdict

class Graph:
    '''This class represents a directed graph using adjacency list representation'''
    def __init__(self):
        self.graph = defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)

def dfsHelper(g, v, visited):
    visited[v] = True
    print v,
    for i in g.graph[v]:
        if not visited[i]:
            dfsHelper(g, i, visited)

def dfs(g, v):
    visited = [False]*(len(g.graph))
    dfsHelper(g, v, visited)
