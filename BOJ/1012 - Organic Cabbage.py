"""
  1012 - 유기농 배추

  1. 아이디어
    -DFS
  2. 시간 복잡도
  - DFS : O(V+E)
  - V = M*N
  - E = K
  - V+E : M*N + K ~= N^2 ~= 2500 >> 가능

  3. 자료구조
  - 그래프 저장 : int[][]
  - 결과값 : int[]
"""
import sys
input = sys.stdin.readline
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
      
t = int(input())
for _ in range(t):
  m,n,k = map(int,input().split())
  mat = [[0]*(n+2) for _ in range(m+2)]
  #input
  for _ in range(k):
    v,u = map(int,input().split())
    mat[(v+1)][(u+1)] = 1
  
  each = 0
  result = []
  for i in range(1,m+1):
    for j in range(1,n+1):
      each = 0
      if mat[i][j] == 1:
        each += 1
        mat[i][j] = 0
        bfs(i,j)
        result.append(each)
  print(len(result))
