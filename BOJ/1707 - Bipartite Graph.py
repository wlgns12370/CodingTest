import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    global is_bipartite_graph
    queue = deque([start])
    visited[start] = 1
    while queue:
        pop_data = queue.popleft()
        for node in adj_mat[pop_data]:
            if visited[node] == 0:
                #이전 노드와 다른 집합으로 대입
                visited[node] = -(visited[pop_data])
                queue.append(node)
            elif visited[node] == visited[pop_data]:
                #이분 그래프가 아닌 경우
                is_bipartite_graph = 0
                break
    return

t = int(input())
for _ in range(t):
    v,e = map(int,input().split())
    adj_mat = [[] for _ in range(v+1)]
    visited = [0 for _ in range(v+1)]
    for i in range(e):
        u,v = map(int,input().split())
        adj_mat[u].append(v)
        adj_mat[v].append(u)
    #이분 그래프인 경우
    is_bipartite_graph = 1
    for i in range(1,v+1):
        if visited[i] == 0:
            bfs(i)
        if is_bipartite_graph == 0:
            break
    print("YES") if is_bipartite_graph else print("NO") 
