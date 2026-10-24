import heapq
# 시작점에서 A, B 따로 가는경우, 시->A->B 가는경우, 시 -> B -> A가는 경우 cost비교
# 플로이드워셜 x 시 -> A, 시 -> B, A-> B, B->A 총 4번 수행 -> 4(V+E) logV
INF = int(1e9)
def solution(n, s, a, b, fares):
    
    adj = [[] for _ in range(n+1)]
    
    for v1, v2, w in fares:
        adj[v1].append([v2,w])
        adj[v2].append([v1,w])
        
    def get_cost(adj, n, start):
        q = []
        d = [INF for _ in range(n+1)]
        d[start]=0
        heapq.heappush(q,[0,start])
        
        while q:
            path, v = heapq.heappop(q)
            
            if d[v] < path:
                continue
            
            for nv,nw in adj[v]:
                cost = path+nw
                if d[nv] > cost:
                    d[nv] = cost
                    heapq.heappush(q,[cost,nv])
        return d
    #시 -> A -> B, 시 -> B -> A => 4(V+E) logV
    sd = get_cost(adj,n,s)
    ad = get_cost(adj,n,a)
    bd = get_cost(adj,n,b)
    
    answer = INF
    for k in range(1,n+1):
        temp = sd[k] + ad[k] + bd[k]
        if answer > temp:
            answer = temp
    return answer