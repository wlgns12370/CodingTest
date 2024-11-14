import sys
from collections import deque
input = sys.stdin.readline

def tree_find(start):
    queue = deque([start])
    is_cycle = False

    while queue:
        pop_data = queue.popleft()

        if visited[pop_data] == 1:
            is_cycle = True
            
        visited[pop_data] = 1

        for node in adj_list[pop_data]:
            if visited[node] == 0:
                queue.append(node)
    return is_cycle


case_number = 1
while True:
    n,m = map(int,input().split())
    cnt = 0

    if n == 0 and m == 0:
        break

    adj_list = [[] for _ in range(n+1)]
    visited = [0 for _ in range(n+1)]

    for _ in range(m):
        u,v = map(int,input().split())
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    for i in range(1,n+1):
        if visited[i] == 0:
            if tree_find(i) == False:
                cnt += 1
    
    if cnt == 0:
        print(f"Case {case_number}: No trees.")
    elif cnt == 1:
        print(f"Case {case_number}: There is one tree.")
    else:
        print(f"Case {case_number}: A forest of {cnt} trees.")
    case_number += 1
