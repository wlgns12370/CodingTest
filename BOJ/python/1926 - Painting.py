import sys
from collections import deque
input = sys.stdin.readline

dx = [0,-1,0,1]
dy = [1,0,-1,0]
def bfs(x,y):
  global cnt,n,m
  queue.append((x,y))
  while queue:
    ex,ey = queue.popleft()
    for i in range(4):
      kx = ex + dx[i]
      ky = ey + dy[i]
      if mat[kx][ky] == 1:
        mat[kx][ky] = 0
        cnt+=1
        queue.append((kx,ky))

n,m = map(int,input().split())
mat = [[0]*(m+2) for _ in range(n+2)]
queue = deque([])

for i in range(1,n+1):
  idx = 0
  data = input().split(' ')
  for j in range(1,m+1):
    mat[i][j] = int(data[idx])
    idx += 1

result = []
cnt = 0
for i in range(1,n+1):
  for j in range(1,m+1):
    if mat[i][j] == 1:
      mat[i][j] = 0
      cnt+=1
      bfs(i,j)
      result.append(cnt)
      cnt = 0
      
print(len(result))
if result == []:
  print(0)
else:
  print(max(result))
