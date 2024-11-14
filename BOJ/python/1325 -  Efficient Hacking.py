import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    visited = [0 for _ in range(n+1)]
    visited[start] = 1
    queue = deque([])
    queue.append(start)
    cnt = 1
    while queue:
        cx = queue.popleft()
        for data in adj[cx]:
            if visited[data] == 0:
                visited[data] = 1
                queue.append(data)
                cnt += 1
    return cnt

n,m = map(int, input().split())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    j,i = map(int,input().split())
    adj[i].append(j)

maxCnt = 0
maxBuf = []
for i in range(1, n+1):
    cnt = bfs(i)
    if maxCnt < cnt:
        maxCnt = cnt
        maxBuf = [i]
    elif maxCnt == cnt:
        maxBuf.append(i)

print(*maxBuf)