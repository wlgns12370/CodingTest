import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
cnt = 0

def dfs(v):
  global cnt
  cnt += 1
  visited[v] = cnt

  for node in mat[v]:
    if visited[node] == 0:
      dfs(node)
  return


n,m,r = map(int,input().split())
mat = [[] for x in range(n+1)]
visited = [0 for x in range(n+1)]
for _ in range(m):
  u,v = map(int,input().split())
  mat[u].append(v)
  mat[v].append(u)
#sort
for i in range(n):
  mat[i].sort()
dfs(r)
for i in range(1,n+1):
  print(visited[i])
