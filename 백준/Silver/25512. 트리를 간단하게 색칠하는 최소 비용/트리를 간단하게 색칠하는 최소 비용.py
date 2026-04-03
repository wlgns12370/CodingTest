import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

# 탐색
adj = [[] for _ in range(n)]
visited = [0 for _ in range(n)]
parent = [-1] * (n)

order = []
for _ in range(n-1):
    u, v = map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)

dp = [[0,0] for _ in range(n)]
for k in range(n):
    w, b = map(int,input().split())
    dp[k][0] = w
    dp[k][1] = b

queue = deque()
queue.append(0)
visited[0] = 1
while queue:
    curr = queue.popleft()
    order.append(curr)
    for next in adj[curr]:
        if visited[next] == 0:
            visited[next] = 1
            parent[next] = curr
            queue.append(next)


for curr in reversed(order):
    next = parent[curr]
    if next != -1:
        # 부모가 black이면 자식은 white, 부모가 white면 자식이 black
        dp[next][1] += dp[curr][0]
        dp[next][0] += dp[curr][1]

print(min(dp[0][0], dp[0][1]))
