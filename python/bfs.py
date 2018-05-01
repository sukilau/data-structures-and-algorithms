'''
BFS for Graph

1. Iteration implementation through queue (similar to BFS for tree).
2. Use boolean array visited to avoid visiting the same node because of cycle.
3. For disconnected graph, modify BFS to do traversal starting from all nodes one by one.

Run time : O(|V|+|E|)
Space time : O(|V|)

Reference
http://www.geeksforgeeks.org/breadth-first-traversal-for-a-graph/
'''
from collections import defaultdict

class Graph:
    '''This class represents a directed graph using adjacency list representation'''
    def __init__(self):
        self.a = defaultdict(list)

    def addEdge(self, u, v):
        self.a[u].append(v)

    def bfs(self, s):
        '''
        The idea is similar to level-order traversal for tree (using queue), 
        except that we have to keep a visited array. 
        Initilize a boolean visited array with False for all vertices except the start node 
        to avoid visiting the same node due to cycle in graph
        '''
        visited = [False]*(len(self.a))
        visited[s] = True
        q = [s]
        search_list = []

        while q:
            # dequeue 1st element and append it in search_list
            node = q.pop(0)
            search_list.append(node)
            # find all adjacent vertices of the dequeued vertex s 
            # if a adjacent vertex has not been visited, then mark it visited and enqueue it
            for i in self.a[node]:
                if visited[i] == False:
                    q.append(i)
                    visited[i] = True
        return search_list
