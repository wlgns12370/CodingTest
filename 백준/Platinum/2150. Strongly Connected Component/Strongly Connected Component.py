from collections import deque
import sys

sys.setrecursionlimit(110000)

class Digraph:
    def __init__(self, V): # Constructor
        self.V = V # Number of vertices
        self.E = 0 # Number of edges
        self.adj = [[] for _ in range(V)]   # adj[v] is a list of vertices pointed from v

    def addEdge(self, v, w): # Add a directed edge v->w. Self-loops and parallel edges are allowed
        self.adj[v].append(w)        
        self.E += 1

    def outDegree(self, v):
        return len(self.adj[v])

    def __str__(self):
        rtList = [f"{self.V} vertices and {self.E} edges\n"]
        for v in range(self.V):
            for w in self.adj[v]:
                rtList.append(f"{v}->{w}\n")
        return "".join(rtList)        

    def reverse(self): # return a digraph with all edges reversed
        g = Digraph(self.V)
        for v in range(self.V):
            for w in self.adj[v]: g.addEdge(w, v)
        return g


def topologicalSort(g):
    def recur(v):        
        visited[v] = True        
        for w in g.adj[v]:            
            if not visited[w]: recur(w)
        reverseList.append(v) # Add v to the stack if all adjacent vertices were visited                

    assert(isinstance(g, Digraph))
    visited = [False for _ in range(g.V)]
    reverseList = []
    for v in range(g.V): 
        if not visited[v]: recur(v)

    reverseList.reverse()
    return reverseList

class SCC:
    def __init__(self, g):
        
        reverseTopologicalSort = topologicalSort(g.reverse())

        def dfs(v):
            self.id[v] = self.count
            for w in g.adj[v]:
                if self.id[w] < 0:
                    dfs(w)
        
        self.g = g
        self.id = [-1 for _ in range(g.V)]
        self.count = 0
        for v in reverseTopologicalSort:
            if self.id[v] < 0:
                dfs(v)
                self.count += 1

    def connected(self, v, w):
        return self.id[v] == self.id[w]


if __name__ == "__main__":
    input = sys.stdin.readline
    V, E = map(int, input().split())
    g = Digraph(V)
    for _ in range(E):
        A, B = map(int, input().split())
        g.addEdge(A - 1, B - 1)
    scc = SCC(g)
    K = scc.count
    print(K)
    components = [[] for _ in range(K)]
    for v in range(V):
        scc_id = scc.id[v]
        components[scc_id].append(v + 1)
    for comp in components:
        comp.sort()
    components.sort(key=lambda x: x[0])
    for comp in components:
        print(*comp, end=" -1\n")