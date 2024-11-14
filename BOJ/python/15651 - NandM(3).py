import sys
input = sys.stdin.readline

def dfs(cnt,lis):
    #종료조건
    if cnt == m:
        result.append(lis)
        return

    for j in range(1,n+1):
        dfs(cnt+1,lis + [j])

result = []
n,m = map(int,input().split())
dfs(0,[])
for data in result:
    print(*data)
