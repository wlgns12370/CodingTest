import sys
input = sys.stdin.readline
from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(start_x, start_y):
    queue = deque([])
    queue.append((start_x, start_y))
    visited[start_x][start_y] = 1
    cx = 0
    cy = 0
    while queue:
        cx,cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < row and 0 <= ny < col and visited[nx][ny] == 0 and arr[nx][ny] == "L":
                visited[nx][ny] = visited[cx][cy] + 1
                queue.append((nx,ny))
    return visited[cx][cy]

row,col = map(int, input().split())

arr = []
for _ in range(row):
    data = []
    num = input()
    for i in range(col):
        data.append(num[i])
    arr.append(data)

result = 0
for i in range(row):
    for j in range(col):
        if arr[i][j] == "L":
            visited = [[0 for _ in range(col)] for _ in range(row)]
            result = max(result, bfs(i,j))

print(result-1)