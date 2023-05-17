import sys
from collections import deque
input = sys.stdin.readline
max_len = 500_001

def bfs(start):
    queue = deque()
    queue.append((start,0))
    mattrix[0][start] = 0

    while queue:
        current_pos,sipping = queue.popleft()
        #홀짝 변경해주기
        flag = sipping % 2
        for new_pos in (current_pos-1,current_pos+1,current_pos*2):
            if 0 <= new_pos < max_len and mattrix[1-flag][new_pos] == -1:
                mattrix[1-flag][new_pos] = sipping + 1
                queue.append((new_pos,sipping+1))

n,k = map(int,input().split())
# 위치 홀짝 여부
mattrix = [[-1 for _ in range(max_len)] for _ in range(2)]

bfs(n)

time = 0
flag = 0
result = -1

while k < max_len:
    if mattrix[flag][k] != -1:
        if mattrix[flag][k] <= time:
            result = time
            break
    flag = 1 - flag
    #1sec increase
    time += 1
    k += time
print(result)
