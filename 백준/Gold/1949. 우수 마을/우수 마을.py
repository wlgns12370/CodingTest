import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

score_table = list(map(int,input().split()))

# 탐색
adj = [[] for _ in range(n)]
visited = [0 for _ in range(n)]
parent = [-1] * (n)

order = []
for _ in range(n-1):
    u, v = map(int,input().split())
    adj[u-1].append(v-1)
    adj[v-1].append(u-1)


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

#0번이 우수 선정, 1번이 우수 미선정
dp = [[0,0] for _ in range(n)]
for idx, data in enumerate(score_table):
    dp[idx][0] = data

for curr in reversed(order):
    next = parent[curr]
    if next != -1:
        # curr이 우수면 next는 미우수, curr이 미우수면 next가 우수
        dp[next][1] += max(dp[curr][0], dp[curr][1])
        dp[next][0] += dp[curr][1]

print(max(dp[0][0], dp[0][1]))