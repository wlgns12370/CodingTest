from collections import deque
def solution(n, computers):
    adj = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            if computers[i][j] == 1:
                adj[i].append(j)
                adj[j].append(i)
    visited = [0 for i in range(n)]
    cnt = 0
    for i in range(n):
        if visited[i] == 0:
            cnt+=1
            # bfs
            q = deque([])
            q.append(i)
            visited[i] = cnt
            
            while q:
                cur = q.popleft()
                for pre in adj[cur]:
                    if visited[pre] == 0:
                        visited[pre] = cnt
                        q.append(pre)
            
    return cnt