import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
visit = 1

def bfs(mat,start,visited):
  global visit
  visited[start] = visit
  bfs_result.append(start)
  queue = deque([start])
  while queue:
    pop = queue.popleft()
    for node in mat[pop]: 
      if visited[node] == 0:
        visited[node] = visit
        bfs_result.append(node)
        queue.append(node)
  return

def dfs(mat,v,visited):
  global visit
  dfs_result.append(v)
  visited[v] = visit

  for node in mat[v]:
    if visited[node] == 0:
      dfs(mat,node,visited)
  return

n,m,r = map(int,input().split())
mat = [[] for x in range(n+1)]
bfs_visited = [0 for x in range(n+1)]
dfs_visited = [0 for x in range(n+1)]
bfs_result = []
dfs_result = []
for _ in range(m):
  u,v = map(int,input().split())
  mat[u].append(v)
  mat[v].append(u)

#sort
for i in range(n+1):
  mat[i].sort()
dfs(mat,r,dfs_visited)
bfs(mat,r,bfs_visited)
for node in dfs_result:
  print(node,end=" ")
print('')
for node in bfs_result:
  print(node,end=" ")
