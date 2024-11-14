import sys
input = sys.stdin.readline
def search(network,v,visited):
  visited[v] = 1
  for node in network[v]:
    if visited[node] == 0:
      visited[node] = 1
      search(network,node,visited)
  return

n = int(input())
m = int(input())

network = [[] for _ in range(n+1)]
visited = [0]*(n+1)
cnt = 0
for _ in range(m):
  u,v = map(int,input().split())
  network[u].append(v)
  network[v].append(u)
search(network,1,visited)
for node in visited[1:]:
  if node == 1:
    cnt += 1
print(cnt-1)
