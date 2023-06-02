import sys
import heapq
input = sys.stdin.readline

minHeap = []
n = int(input())
for _ in range(n):
    x = int(input())
    if x == 0:
        if len(minHeap):
            print(heapq.heappop(minHeap))
        #First Input Zero
        else:
            print(0)
        
    else:
        heapq.heappush(minHeap,x)
