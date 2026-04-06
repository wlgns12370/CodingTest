import sys
import heapq
input = sys.stdin.readline

MAX_VALUE = 1000001
def minValue(adj, n, x):
    dist = [MAX_VALUE for _ in range(n+1)]

    pq = [[0,1]]
    dist[1] = 0

    while pq:
        c_w, c_p = heapq.heappop(pq)
        
        if dist[c_p] < c_w:
            continue

        for f_w, f_p in adj[c_p]:
            cost = 0 if f_w <= x else 1
            d = cost + dist[c_p]
            if dist[f_p] > d:
                dist[f_p] = d
                heapq.heappush(pq, [d, f_p])

    return dist[n]

n, m, k = map(int, input().split())

adj = [[] for _ in range(n+1)]

for _ in range(m):
    u,v,w =map(int, input().split())
    adj[u].append([w,v])
    adj[v].append([w,u])
lo = 0
hi = 1000000

flag = 0
while lo < hi:
    mid = (lo + hi) // 2
    
    mv = minValue(adj, n, mid)
    if (mv == MAX_VALUE):
        print(-1)
        flag=1
        break

    if (mv <= k):
        hi = mid
    elif (mv > k):
        lo = mid + 1

if flag == 0:
    print(lo)