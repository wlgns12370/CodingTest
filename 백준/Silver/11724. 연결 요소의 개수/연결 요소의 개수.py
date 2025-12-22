import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(start, num):
    visited[start] = num
    for next in adj[start]:
        if visited[next] == -1:
            dfs(next,num)


n,m = map(int, input().split())
visited = [-1]*(n+1)

adj = [[] for _ in range(n+1)]
for _ in range(m):
    v,w = map(int, input().split())
    adj[v].append(w)
    adj[w].append(v)

cnt = 0
for v in range(1,n+1):
    if visited[v] == -1:
        dfs(v,cnt)
        cnt += 1

print(cnt)