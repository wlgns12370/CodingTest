import sys
input = sys.stdin.readline
from collections import deque
max_len = 100_001

def path(pos,length):
    global k
    result = []
    result.append(pos)
    start = move[pos]
    for _ in range(length):
        result.append(start)
        start = move[start]
    result.reverse()
    for data in result:
        print(data,end=" ")

def bfs(x):
    global k
    mattrix[x] = 0
    queue = deque([x])

    while queue:
        current_pos = queue.popleft()
        
        if current_pos == k:
            print(mattrix[k])
            path(k,mattrix[k])
            return  

        for new_pos in (current_pos+1,current_pos-1,2*current_pos):
            if 0 <= new_pos < max_len and mattrix[new_pos] == -1:
                mattrix[new_pos] = mattrix[current_pos] + 1
                #이전 위치 저장
                move[new_pos] = current_pos
                queue.append(new_pos)
                
n,k = map(int,input().split())
mattrix = [-1 for _ in range(max_len)]
move = [0] * (max_len)

bfs(n)
