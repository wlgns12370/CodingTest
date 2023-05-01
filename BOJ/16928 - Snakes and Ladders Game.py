import sys
from collections import deque
input = sys.stdin.readline
max_len = 100

def bfs(start):
    global n,m
    temp = 0
    mat[start] = 0
    queue = deque([start])
    while queue:
        current_pos = queue.popleft()
        if current_pos == max_len:
            return mat[max_len]
        for px in range(1,7):
            nx = current_pos + px
            if 0 <= nx <= max_len and mat[nx] == -1:
                for idx in range(n+m):
                    if nx == ladder_snake[idx][0]:
                        nx = ladder_snake[idx][1]
                #뱀 or 사다리를 탔을경우에 nx를 업데이트 해주고 한번더 검증해야한다.
                if mat[nx] == -1:
                    mat[nx] = mat[current_pos] + 1
                    queue.append(nx)
    return


ladder_snake = []
#사다리수, 뱀의수
n,m = map(int,input().split())
for _ in range(n+m):
    x,y = map(int,input().split())
    ladder_snake.append([x,y])
mat = [-1 for _ in range(max_len+1)]

print(bfs(1))
