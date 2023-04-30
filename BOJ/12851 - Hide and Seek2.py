import sys
from collections import deque
input = sys.stdin.readline
max_len = 200_001

def bfs(start_pos):
    global k,cnt
    break_level = max_len
    mattrix[start_pos] = 0
    queue = deque()
    # 이동수 , 위치
    queue.append((0,start_pos))
    while queue:
        steps,current_pos = queue.popleft()
        if steps > break_level:
            return

        if k == current_pos:
            break_level = steps
            cnt += 1

        for nx in (current_pos - 1,current_pos + 1, 2*current_pos):
            if 0 <= nx < max_len:
                if mattrix[nx] == -1:
                    mattrix[nx] = mattrix[current_pos] + 1
                    queue.append((mattrix[nx],nx))

                elif mattrix[nx] == mattrix[current_pos] + 1:
                    queue.append((mattrix[nx],nx))
    return


n,k = map(int,input().split())
cnt = 0
mattrix = [-1 for _ in range(max_len)]
bfs(n)

print(mattrix[k])
print(cnt)
