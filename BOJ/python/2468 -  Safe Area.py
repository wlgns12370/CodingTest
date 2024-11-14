import sys
input = sys.stdin.readline
from collections import deque

dt = [(1,0),(0,1),(-1,0),(0,-1)]

def bfs(x,y,i):
    queue = deque([])
    queue.append((x,y))
    visited[x][y] = 1

    while queue:
        cx,cy = queue.popleft()
        for dx,dy in dt:
            nx = cx + dx
            ny = cy + dy
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] >= i and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx,ny))

n = int(input())
arr = []
for _ in range(n):
    data = list(map(int, input().split()))
    arr.append(data)

result = []
for k in range(1,max(map(max,arr))+1):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] >= k and visited[i][j] == 0:
                bfs(i,j,k)
                cnt += 1
    result.append(cnt)

print(max(result))