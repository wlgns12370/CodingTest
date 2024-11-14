import sys
input = sys.stdin.readline
from collections import deque

def bfs(start,cnt):
    queue = deque()
    queue.append((start,cnt))

    while queue:
        cur_pos,cur_cnt = queue.popleft()
        if cur_pos == b:
            return cur_cnt
        for pre_pos in (cur_pos*2,cur_pos*10+1):
            if a <= pre_pos <= b:
                queue.append((pre_pos,cur_cnt+1))
    return -1


a,b = map(int,input().split())
print(bfs(a,1))
