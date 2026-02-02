import sys
from collections import deque

input = sys.stdin.readline

n,m,k,x = map(int, input().rstrip().split())

adj_list = [[] for _ in range(n+1)]
visited = [-1 for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().rstrip().split())
    adj_list[a].append(b)

queue = deque()
queue.append(x)
visited[x] = 0

result = []

while queue:
    cx = queue.popleft()
    
    for pos in adj_list[cx]:
        if visited[pos] == -1:
            visited[pos] = visited[cx] + 1
            if visited[pos] == k:
                result.append(pos)
            queue.append(pos)

result.sort(key = lambda x : x)
if result == []:
    print(-1)
else:
    print(*result)