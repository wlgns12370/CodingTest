import sys
input = sys.stdin.readline
from collections import deque

dx = [1,1,0,-1,-1,-1,0,1]
dy = [0,1,1,1,0,-1,-1,-1]
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1
    while queue:
        x_pos,y_pos = queue.popleft()
        for i in range(8):
            nx = x_pos + dx[i]
            ny = y_pos + dy[i]
            if 0 <= nx < h and 0 <= ny < w and visited[nx][ny] == 0 and mat[nx][ny] == 1:
                visited[nx][ny] = 1
                queue.append((nx,ny))


while True:
    w,h = map(int,input().split())
    if w == 0 and h == 0:
        break
    visited = [[0 for _ in range(w)] for _ in range(h)]
    mat = []
    for _ in range(h):
        mat.append(list(map(int,input().split())))
    cnt = 0
    for i in range(h):
        for j in range(w):
            if mat[i][j] == 1 and visited[i][j] == 0:
                bfs(i,j)
                cnt += 1
    print(cnt)
