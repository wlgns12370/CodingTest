import sys
from collections import deque
input = sys.stdin.readline

def bfs(v):
    visited[v] = 1
    queue = deque([v])
    while queue:
        pop_data = queue.popleft()
        for node in mat[pop_data]:
            if visited[node] == 0:
                #탐색할때 부모노드를 result에 저장
                result[node] = pop_data
                visited[node] = 1
                queue.append(node)

n = int(input())
mat = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
result = [0 for _ in range(n+1)]
for _ in range(n-1):
    u,v = map(int,input().split())
    mat[u].append(v)
    mat[v].append(u)
bfs(1)

for data in result[2:]:
    print(data)
