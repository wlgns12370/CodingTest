import sys
from collections import deque
input = sys.stdin.readline

dx = [0,-1,0,1]
dy = [1,0,-1,0]

def run(mat,visited):
    global n,m
    queue = deque([])
    queue.append((0,0,0))
    visited[0][0][0] = 1
    while queue:
        x,y,crash_state = queue.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][crash_state]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                #다음이 벽이 아니고 아직 방문하지 않았다면
                if mat[nx][ny] == 0 and visited[nx][ny][crash_state] == 0:
                    visited[nx][ny][crash_state] = visited[x][y][crash_state] + 1
                    queue.append((nx,ny,crash_state))
                #다음이 벽이고 아직 방문하지 않았다면
                elif mat[nx][ny] == 1 and visited[nx][ny][crash_state] == 0:
                    #벽부수기 사용하기전
                    if crash_state == 0:
                        visited[nx][ny][1] = visited[x][y][crash_state] + 1
                        queue.append((nx,ny,1))
                    #벽부수기 사용후
                    else:
                        continue
    return -1

n,m = map(int,input().split())
mat = [[0]*(m) for _ in range(n)]
visited = [[[0]*(2) for _ in range(m)] for _ in range(n)]
for i in range(n):
    idx = 0
    data = input()
    for j in range(m):
        mat[i][j] = int(data[idx])
        idx += 1

print(run(mat,visited))
