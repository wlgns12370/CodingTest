from collections import deque

t = int(input())

for idx in range(1,t+1):
  v, m = map(int, input().split())
  adj = [[] for _ in range(v+1)]
  for _ in range(m):
    n1, n2 = map(int, input().split())
    adj[n1].append(n2)
    adj[n2].append(n1)
  s, g = map(int, input().split())

  visited = [0 for _ in range(v+1)]
  visited[s] = 1

  q = deque([])
  q.append(s)

  while q:
    x = q.popleft()

    if x == g:
      break

    for data in adj[x]:
      if visited[data] == 0:
        visited[data] = visited[x] + 1
        q.append(data)

  print("#"+str(idx)+ " "+str(max(0, visited[g]-1)))