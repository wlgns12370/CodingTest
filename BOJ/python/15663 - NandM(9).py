import sys
input = sys.stdin.readline

def dfs(cnt,lis):
    if cnt == m:
        result.append(lis)
        return
      
    prev = -1
    for j in range(0,n):
        #방문여부와 과거의 노드와 현재의 노드 동등여부 체크
        if visited[j] == False and prev != arr[j]:
            prev = arr[j]
            visited[j] = True
            dfs(cnt+1,lis+[arr[j]])
            visited[j] = False

result = []
n,m = map(int,input().split())
arr = sorted(list(map(int,input().split())))
visited = [False for _ in range(n)]
dfs(0,[])
for data in result:
    print(*data)
