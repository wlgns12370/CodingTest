
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
adj = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
parent = [0] * (n+1)
order = []
for _ in range(n-1):
    u, v = map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)
queue = deque()
queue.append(1)
visited[1] = 1
# 부모 찾기
while queue:
    x = queue.popleft()
    order.append(x)
    for data in adj[x]:
        if visited[data] == 0:
            visited[data] = 1
            parent[data] = x
            queue.append(data)

# 0은 얼리어답터 x 1은 얼리어답터 o
dp = [[0,1] for _ in range(n+1)]

# 아래부터 완성하며 올라가기
for cur in reversed(order):
    next = parent[cur]

    if next != 0:
        # 부모가 얼리어답터가 아니기 때문에 자식은 얼리어답터야 한다.
        dp[next][0] += dp[cur][1]
        # 부모가 얼리어답터면 자식은 얼리어답터 이거나 아닐 수 있다 -> 문제는 얼리어답터 최소 수여서 min
        dp[next][1] += min(dp[cur][0], dp[cur][1])

print(min(dp[1][0], dp[1][1]))