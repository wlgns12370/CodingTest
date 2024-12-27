"""
    1. 아이디어
    - grid 변수 사각형의 안쪽을 0으로 채우고, 테두리 부분을 1로 채운다
    - ㄷ자 테두리에서 최단 거리가 아닌 테두리를 따라 이동해야 하기 때문에, 사각형 전체를 2배로 늘린다.
"""

from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    # -1:빈공간, 0:속, 1: 테두리
    grid = [[-1 for _ in range(102)] for _ in range(102)]
    visited = [[0 for _ in range(102)] for _ in range(102)]
    queue = deque([])
    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x: x*2, r)
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if x1 < i < x2 and y1 < j < y2:
                    grid[i][j] = 0
                elif grid[i][j] != 0:
                    grid[i][j] = 1

    queue.append((characterX*2, characterY*2))
    visited[characterX*2][characterY*2] = 1

    while queue:
        cx, cy = queue.popleft()
        if cx == itemX*2 and cy == itemY*2:
            break
        for n in range(4):
            px = cx + dx[n]
            py = cy + dy[n]
            if grid[px][py] == 1 and visited[px][py] == 0:
                visited[px][py] = visited[cx][cy] + 1
                print(px,py)
                queue.append((px,py))

    answer = visited[itemX*2][itemY*2] // 2

    return answer