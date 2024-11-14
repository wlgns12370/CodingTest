import sys
input = sys.stdin.readline
from collections import deque

# 위 아래 왼쪽 오른쪽 앞 뒤
dz = [1,-1,0,0,0,0]
dy = [0,0,0,0,1,-1]
dx = [0,0,-1,1,0,0]

def tomato_search():
    global m,n,h
    queue = deque([])
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if mat[i][j][k] == 1:
                    queue.append((i,j,k)) 

    while queue:
        ez,ey,ex = queue.popleft()
        for i in range(6):
            nx = ex + dx[i]
            ny = ey + dy[i]
            nz = ez + dz[i]
            if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h and mat[nz][ny][nx] == 0:
                mat[nz][ny][nx] = mat[ez][ey][ex] + 1
                queue.append((nz,ny,nx))

m,n,h = map(int,input().split())
mat = [[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]
tomato_search()

flag = 0
min_data = 1
for i in range(h):
        for j in range(n):
            for k in range(m):
                if mat[i][j][k] == 0:
                    flag = 1
                    break
                else:
                    if mat[i][j][k] > min_data:
                        min_data = mat[i][j][k]

if flag == 1:
    print(-1) 
else:
    if min_data == 1:
        print(0)
    else:
        print(min_data-1)
