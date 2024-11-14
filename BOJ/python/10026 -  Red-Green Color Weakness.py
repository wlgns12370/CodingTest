import sys
input = sys.stdin.readline
from collections import deque

dy = [1,0,-1,0]
dx = [0,-1,0,1]

def bfs(i,j,color):
    queue = deque()
    queue.append((i,j))
    while queue:
        current_x,current_y = queue.popleft()
        for i in range(4):
            future_x = current_x + dx[i]
            future_y = current_y + dy[i]
            if 0 <= future_x < n and 0 <= future_y < n and painting[future_x][future_y] == color and visited[future_x][future_y] == 0:
                visited[future_x][future_y] = 1
                queue.append((future_x,future_y))
    
n = int(input())
painting = [input() for _ in range(n)]
visited = [[0]*(n) for _ in range(n)]

# 색약X
cnt = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            visited[i][j] = 1
            bfs(i,j,painting[i][j])
            cnt += 1

for i in range(n):
    painting[i] = painting[i].replace('G','R')

print(cnt)
#방문 초기화
visited = [[0]*(n) for _ in range(n)]

# 색약O
red_blue_cnt = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            visited[i][j] = 1
            bfs(i,j,painting[i][j])
            red_blue_cnt += 1

print(red_blue_cnt)
