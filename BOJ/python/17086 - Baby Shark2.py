import sys
input = sys.stdin.readline
from collections import deque

dx = [0,1,1,1,0,-1,-1,-1]
dy = [1,1,0,-1,-1,-1,0,1]
def bfs(start):
    queue = deque()
    for data in start:
        queue.append(data)
    
    while queue:
        x_pos,y_pos = queue.popleft()
        for i in range(8):
            fx_pos = x_pos + dx[i]
            fy_pos = y_pos + dy[i]
            if 0 <= fx_pos < n and 0 <= fy_pos < m and space[fx_pos][fy_pos] == 0:
                space[fx_pos][fy_pos] = space[x_pos][y_pos] + 1
                queue.append((fx_pos,fy_pos)) 
    return    


n,m = map(int,input().split())
space = []
start = []
for i in range(n):
    data = list(map(int,input().split()))
    space.append(data)
    for j in range(m):
        if space[i][j] == 1:
            start.append((i,j))

bfs(start)
print(max(map(max,space))-1)