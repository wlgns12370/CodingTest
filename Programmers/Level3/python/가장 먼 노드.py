from collections import deque

def solution(n, edge):
    adj = [[] for i in range(n+1)]
    visited = [0 for i in range(n+1)]
    q = deque()
    
    for v1,v2 in edge:
        adj[v1].append(v2)
        adj[v2].append(v1)
    
    visited[1] = 1
    for i in range(n+1):
        for data in adj[i]:
            if visited[data] == 0:
                visited[data] = visited[i] + 1
    
    m_data = max(visited)
    
    answer = 0
    for k in visited:
        if k == m_data:
            answer+=1
    return answer
