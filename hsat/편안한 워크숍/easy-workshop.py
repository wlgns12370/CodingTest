from collections import deque
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

def check(X):
    visited = [[0] * N for _ in range(N)]
    queue = deque()

    for i in range(N):
        for j in range(N):
            queue.append([i, j, 1])
            visited[i][j] = 1

    while queue:
        px, py, pi = queue.popleft()
        if pi >= K:
            return True
        
        if pi < visited[px][py]:
            continue

        for dx, dy in [(0,1), (1,0), (-1,0), (0,-1)]:
            cx = px + dx
            cy = py + dy
            if 0 <= cx < N and 0 <= cy < N:
                diff = grid[cx][cy] - grid[px][py]
                if 0 < diff <= X:
                    if visited[cx][cy] < pi + 1:
                        visited[cx][cy] = pi + 1
                        queue.append([cx, cy, pi + 1])
    
    return False

lo = 0
hi = 10**9
answer = -1

while lo <= hi:
    mid = (lo + hi) // 2
    if check(mid):
        answer = mid
        hi = mid - 1
    else:
        lo = mid + 1

print(answer)