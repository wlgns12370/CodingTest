import sys
input = sys.stdin.readline
from collections import deque
max_len = 100_001

dx = [-1,1]
def bfs(x):
  global k
  matrix[x] = 1
  queue = deque([x])
  while queue:
    pop_x = queue.popleft()
    for i in range(3):
      if i == 2:
        nx = pop_x * 2
      else:
        nx = pop_x + dx[i]
      if 0 <= nx < max_len and matrix[nx] == 0:
        matrix[nx] = matrix[pop_x] + 1
        queue.append(nx)
        if nx == k:
          break 

n,k = map(int,input().split())
matrix = [0 for _ in range(max_len)]
bfs(n)
print(matrix[k]-1)
