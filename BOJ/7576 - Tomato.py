import sys
from collections import deque
input = sys.stdin.readline

dx = [0,-1,0,1]
dy = [1,0,-1,0]

def tomato_search(mat):
  global m,n
  queue = deque([])
  for i in range(n):
    for j in range(m):
      if mat[i][j] == 1:
        queue.append((i,j)) 

  while queue:
    ex,ey = queue.popleft()
    for i in range(4):
      nx = ex + dx[i]
      ny = ey + dy[i]
      if 0 <= nx < n and 0 <= ny < m and mat[nx][ny] == 0:
        mat[nx][ny] = mat[ex][ey] + 1
        queue.append((nx,ny))

m,n = map(int,input().split())
mat = [[0]*(m) for _ in range(n)]
for i in range(n):
    idx = 0
    data = input().split()
    for j in range(m):
        mat[i][j] = int(data[idx])
        idx += 1
     
tomato_search(mat)

#flag 1 >> 안익은 토마토가 존재 하는 경우 , 0 >> 익은 토마토가 존재 하는 경우
flag = 0
min = 1
for i in range(n):
    for j in range(m):
        if mat[i][j] == 0:
            flag = 1
            break
        else:
            if mat[i][j] > min:
                min = mat[i][j]

print(-1) if flag == 1 else print(min-1)
