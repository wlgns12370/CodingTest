"""
    1. 아이디어
    - 방문한 경로를 저장하는 his와 방문한 티켓을 저장하는 visited를 이용하여 BFS를 한다.
    - BFS를 하면서 his의 길이가 tickets의 길이 + 1이 되면 answer에 추가한다.
    - answer를 정렬하여 가장 빠른 경로를 반환한다.

    2. 시간 복잡도
    - O(N*N!) N : tickets의 길이 (3개 이상 10,000 이하 자연수)

    3. 자료구조
    - deque : BFS를 위한 자료구조
"""
from collections import deque

def solution(tickets):
    answer = []
    queue = deque()
    queue.append(("ICN",["ICN"],[]))
    while queue:
        cur, his, visited = queue.popleft()

        if (len(tickets)+1) == len(his):
            answer.append(his)

        for idx, ticket in enumerate(tickets):
            if ticket[0] == cur and idx not in visited:
                queue.append((ticket[1], his + [ticket[1]], visited + [idx]))

    answer.sort()
    return answer[0]