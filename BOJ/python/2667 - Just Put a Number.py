"""

1. 아이디어
  시계 방향으로 탐색
  방문표시 후 카운트
  반복
2. 시간 복잡도
- DFS : O(V+E)
- V = N^2
- E = 4N^2
- V+E : 5N^2 ~= N^2 ~= 625 >> 가능

3. 자료구조
- 그래프 저장 : int[][]
- 결과값 : int[]

"""
import sys
input = sys.stdin.readline()
sys.setrecursionlimit(10**5)
dx = [0,-1,0,1]
dy = [1,0,-1,0]

def bfs(x,y):
  global each
  nx = 0
  ny = 0
  for k in range(4):
    nx = x + dx[k]
    ny = y + dy[k]
    if mat[nx][ny] == 1:
      mat[nx][ny] = 0
      each += 1
      bfs(nx,ny)

n = int(input())
mat = [[0]*(n+2) for x in range(n+2)]

for i in range(1,n+1):
  idx = 0
  data = input()  
  for j in range(1,n+1):
    mat[i][j] = int(data[idx])
    idx += 1  

each = 0
result = []

for i in range(1,n+1):
  for j in range(1,n+1):
    each = 0
    if mat[i][j] == 1:
      each += 1
      mat[i][j] = 0
      bfs(i,j)
      result.append(each)

print(len(result))
for data in sorted(result):
  print(data)
