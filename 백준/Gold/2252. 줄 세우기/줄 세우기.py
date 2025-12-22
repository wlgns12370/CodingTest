import sys
input = sys.stdin.readline
from collections import deque

def Topological_Sort():
    queue = deque()
    for i in range(1,n+1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        pop_node = queue.popleft()
        result.append(pop_node)
        for node in line[pop_node]:
            indegree[node] -= 1
            if indegree[node] == 0:
                queue.append(node)

result = []
n,m = map(int,input().split())
line = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]
for _ in range(m):
    u,v = map(int,input().split())
    #단방향 연결
    line[u].append(v)
    indegree[v] += 1

Topological_Sort()
print(*result)