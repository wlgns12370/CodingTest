import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
def dfs(start):
    visited[start] = True
    for node in graph[start]:
        if visited[node] == False:
            dfs(node)
    return

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
for i in range(1,n+1):
    if visited[i] == False:
        dfs(i) 
        cnt+=1

print(cnt)