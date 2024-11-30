"""
  1. 아이디어
    - bfs를 통해 최단 거리를 찾는다

  2. 시간 복잡도
  - O(N+E) : Node + Edge

  3. 자료구조
  - visited[][] 방문을 표시하기 위한 2차원 배열
"""
from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[0 for i in range(m)] for i in range(n)]
    dt = [(0,1),(1,0),(0,-1),(-1,0)]

    queue = deque([])
    queue.append((0,0))

    while queue:
        cy, cx = queue.popleft()
        for dy, dx in dt:
            ny = cy + dy
            nx = cx + dx
            if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] == 1 and visited[ny][nx] == 0:
                maps[ny][nx] = 2
                visited[ny][nx] = visited[cy][cx] + 1
                queue.append((ny,nx))

    if visited[n-1][m-1] != 0:
        answer = visited[n-1][m-1]+1
    else:
        answer = -1
    return answer