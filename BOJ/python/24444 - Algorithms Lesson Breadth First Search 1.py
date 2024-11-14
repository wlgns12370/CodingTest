import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def bfs(mat,start,visited):
  cnt = 1
  visited[start] = cnt
  queue = deque([start])
  while queue:
    pop = queue.popleft()
    for node in mat[pop]: 
      if visited[node] == 0:
        cnt += 1
        visited[node] = cnt
        queue.append(node)
  return


n,m,r = map(int,input().split())

mat = [[]for i in range(n+1)]
visited = [0]*(n+1)

for _ in range(m):
  u,v = map(int,input().split())
  mat[u].append(v)
  mat[v].append(u)
  
#sort
for i in range(n+1):
  mat[i].sort()

bfs(mat,r,visited)

for data in visited[1:]:
  print(data)
