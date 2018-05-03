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
        self.a = defaultdict(list)

    def addEdge(self, u,v ):
        self.a[u].append(v)

    def dfs(self, s):
        '''
        The idea is similar to dfs for tree 
        except that we have to keep a boolean visited array to keep track of visited node
        '''
        search_list = []
        visited = [False]*len(self.a)
        return self._dfs(s, search_list, visited)

    def _dfs(self, s, search_list, visited):
        '''Helper method using recursion'''
        visited[s] = True
        search_list.append(s)
        for i in self.a[s]:
            if not visited[i]:
                self._dfs(i, search_list, visited)
        return search_list
