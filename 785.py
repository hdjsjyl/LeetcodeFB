"""
785. Is Graph Bipartite?
Medium

1463

162

Add to List

Share
Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split it's set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B.

The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.  Each node is an integer between 0 and graph.length - 1.

There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.
"""

## TC: O(E+V), MC: O(E)

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = [0 for i in range(len(graph))]
        for i in range(len(graph)):
            if visited[i] == 0:
                visited[i] = 1
                q = []
                q.append(i)
                while q:
                    v = q.pop(0)
                    for x in graph[v]:
                        if visited[x] == 0:
                            visited[x] = 3-visited[v]
                            q.append(x)
                        elif visited[x] == visited[v]:
                            return False
        return True