from collections import deque
import sys
input=sys.stdin.readline
n, m, k = map(int, input().split())

INF = int(1e9)
adj = [[] for _ in range(n)]

for _ in range(m):
    x, y = map(int, input().split())
    adj[x-1].append(y-1)

start_points = list(map(lambda x: int(x) - 1, input().split()))

# Please write your code here.

def findTable(n, start):
    road = [INF] * n
    road[start] = 0
    q = deque([start])

    while q:
        node = q.popleft()

        for nn in adj[node]:
            if road[nn] == INF:
                road[nn] = road[node] + 1
                q.append(nn)

    return road
# 모든 노드의 최단거리 dp[a][b] a에서 b로 가는 최단 거리 n^3이니까.. 10^15되어서 VKlogV로 할 수 있는 

d_table = []

for s in start_points:
    r = findTable(n, s)
    d_table.append(r)

#print(d_table)

answer = INF
# k가 만약 노드라면 값 계산하기
for k in range(n):

    temp = -1
    # 노드들에서 최단거리중에 가장 긴거 찾기 
    for d in d_table:
        temp = max(temp,d[k])

    if answer > temp:
        answer=temp
    
print(answer if answer != INF else -1)
