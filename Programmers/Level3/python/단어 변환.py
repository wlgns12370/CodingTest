"""
    1. 아이디어
    - bfs로 단어가 변경될 수 있는 모든 경우를 탐색한다. 이때 target과 같은 단어가 Queue에서 나온다면 탐색을 멈춘다.
    - 변경된 횟수 current P

    2. 시간 복잡도
    - O(NM) N: 3 이상 10 이하이며 모든 단어의 길이, M: 3개 이상 50개 이하의 단어 집합 길이

    3. 자료구조
    - int형 변수 cs : Current String
    - int형 변수 cp : Current Position
"""
from collections import deque
def check(a,b):
    cnt = 0
    for i in range(n):
        if a[i] != b[i]:
            cnt += 1
    if cnt == 1:
        return True
    else:
        return False

def solution(begin, target, words):
    global n
    n = len(begin)
    queue = deque([])
    queue.append((0,begin))
    answer = 0

    while queue:
        cp, cs = queue.popleft()
        print(cp, cs)
        if cs == target:
            answer = cp
            break
        if cp > n+1:
            break
        for data in words:
            if check(cs, data):
                queue.append((cp+1, data))

    return answer