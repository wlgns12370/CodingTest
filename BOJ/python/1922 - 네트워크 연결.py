"""
    1. 아이디어
    - 크루스칼 알고리즘으로 트리의 최소비용을 찾는다

    2. 시간 복잡도
    - O(MLogM) 연결할 수 있는 선의 수 M (1 ≤ M ≤ 100,000)

    3. 자료구조
    - 부모 노드를 저장하는 p
    - 간선의 가중치로 정렬한 배열 arr
"""
import sys
input = sys.stdin.readline

def find(a):
    if p[a] == a:
        return a
    p[a] = find(p[a])
    return p[a]

def union(a,b):
    if a < b:
        p[a] = b
    else:
        p[b] = a

n = int(input())
m = int(input())

p = [i for i in range(n+1)]

arr = []
result = 0
for i in range(m):
    a,b,c = map(int,input().split())
    arr.append((a,b,c))

arr.sort(key= lambda x : x[2])
for a,b,c in arr:
    p_a = find(a)
    p_b = find(b)
    if p_a != p_b:
        union(p_a, p_b)
        result += c
print(result)