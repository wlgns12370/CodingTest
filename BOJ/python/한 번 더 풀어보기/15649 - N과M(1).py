import  sys
input = sys.stdin.readline

answer = []
def dfs(idx, l):
    global m
    if idx == m:
        answer.append(l)
        return
    for i in range(1,n+1):
        if visited[i] == False:
            visited[i] = True
            dfs(idx+1, l + [i])
            visited[i] = False

n,m = map(int,input().split())
visited = [False for i in range(n+1)]
dfs(0,[])
for data in answer:
    print(*data)