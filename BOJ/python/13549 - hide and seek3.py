import sys
input = sys.stdin.readline
from collections import deque
max_len = 100_001

def bfs(x):
    global k
    mattrix[x] = 0
    queue = deque([x])

    while queue:
        current_pos = queue.popleft()
        if current_pos == k:
            return mattrix[k] 

        for new_pos in (current_pos+1,current_pos-1,2*current_pos):
            if 0 <= new_pos < max_len and mattrix[new_pos] == -1:
                if new_pos == (2*current_pos):
                    mattrix[new_pos] = mattrix[current_pos]
										#시간이 빠르기 때문에 가장 앞에 삽입
                    queue.appendleft(new_pos)
                else:
                    mattrix[new_pos] = mattrix[current_pos] + 1
                    queue.append(new_pos)
                
n,k = map(int,input().split())
mattrix = [-1 for _ in range(max_len)]

print(bfs(n))
