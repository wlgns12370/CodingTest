import sys
import heapq
input = sys.stdin.readline

maxHeap = []
n = int(input())
for _ in range(n):
    x = int(input())
    if x == 0:
        if len(maxHeap):
            print(-heapq.heappop(maxHeap))
        else:
            print(0)
        
    else:
        heapq.heappush(maxHeap,-x)
