# X 바다, 숫자 무인도

from collections import deque
def solution(maps):
    answer = []

    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    ly = len(maps)
    lx = len(maps[0])

    visited = [[0 for i in range(lx)] for j in range(ly)]
    flag = 0
    for i in range(ly):
        for j in range(lx):
            if visited[i][j] == 0 and maps[i][j] != "X":
                flag = 1
                total = 0
                queue = deque()
                queue.append((i,j))
                visited[i][j] = 1
                while queue:
                    cy, cx = queue.popleft()
                    total = total + int(maps[cy][cx])
                    for k in range(4):
                        py = cy + dy[k]
                        px = cx + dx[k]
                        if 0 <= py < ly and 0 <= px < lx and visited[py][px] == 0 and maps[py][px] != "X":
                            visited[py][px] = 1
                            queue.append((py,px))
                answer.append(total)
    if flag == 0:
        answer.append(-1)
    answer.sort()
    return answer