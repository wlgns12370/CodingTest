import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

def Dijkstra(start):
    # 현재 노드 , 가중치
    heap = [[0,start]]
    dist[start] = 0

    while heap:
        ew,ev = heapq.heappop(heap)
        #최신 값인지 확인
        if dist[ev] != ew:
            continue
        for nw,nv in adj_list[ev]:
            if dist[nv] > nw + ew:
                dist[nv] = nw + ew  
                heapq.heappush(heap,[dist[nv],nv])

v,e = map(int,input().split())
start = int(input())
adj_list = [[] for _ in range(v+1)]
dist = [INF] * (v+1)
for _ in range(e):
    u,v,w = map(int,input().split())
    adj_list[u].append((w,v))

Dijkstra(start)
for result in dist[1:]:
    print("INF") if result == INF
