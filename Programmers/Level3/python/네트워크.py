"""
    1. 아이디어
    - union find 알고리즘으로 네트워크의 부모 노드를 각각 설정한다
    - set 함수를 통해 전체 네트워크의 개수를 구한다

    2. 시간 복잡도
    - O(N^2) 컴퓨터의 개수 n은 1 이상 200 이하인 자연수입니다

    3. 자료구조
    - 부모 노드를 저장하는 p
"""
def find(a):
    if p[a] == a:
        return a
    p[a] = find(p[a])
    return p[a]

def union(a,b):
    if a <= b:
        p[b] = a
    else:
        p[a] = b

def solution(n, computers):
    global p
    p = [i for i in range(n)]
    for i in range(n):
        for j in range(n):
            p_a = find(i)
            p_b = find(j)
            if i != j and computers[i][j] == 1 and p_a != p_b:
                union(p_a,p_b)
    return len(set(p))