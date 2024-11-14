import sys
input = sys.stdin.readline

def dfs(cnt,s,lis):
    if cnt == m:
        result.append(lis)
        return
    prev = -1
    for j in range(s,n):
        #과거의 노드와 현재 노드의 동등여부 체크
        if prev != arr[j]:
            prev = arr[j]
            dfs(cnt+1,j,lis+[arr[j]])

result = []
n,m = map(int,input().split())
arr = sorted(list(map(int,input().split())))
visited = [False for _ in range(n)]
dfs(0,0,[])
for data in result:
    print(*data)
