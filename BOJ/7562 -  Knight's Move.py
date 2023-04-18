import sys
from collections import deque
input = sys.stdin.readline

dx = [-2,-1,1,2,2,1,-1,-2]
dy = [1,2,2,1,-1,-2,-2,-1]

def bfs(x,y):
  global destination_i , destination_j
  queue = deque([])
  queue.append((x,y)) 
  mat[x][y] = 1
  while queue:
    ex,ey = queue.popleft()
    for i in range(8):
      nx = ex + dx[i]
      ny = ey + dy[i]
      if 0 <= nx < l and 0 <= ny < l and mat[nx][ny] == 0:
        mat[nx][ny] = mat[ex][ey] + 1
        queue.append((nx,ny))
        if nx == destination_i and ny == destination_j:
          break
      
t = int(input())
for _ in range(t):
  l = int(input())
  mat = [[0]*(l) for _ in range(l)]
  start_i , start_j = map(int,input().split())
  destination_i , destination_j = map(int,input().split())
  bfs(start_i,start_j)
  print(mat[destination_i][destination_j]-1)
