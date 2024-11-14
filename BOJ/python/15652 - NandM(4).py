import sys
input = sys.stdin.readline

def dfs(cnt,start,temp):
    if cnt == m:
        result.append(temp)
        return
    for j in range(start,n+1):
        dfs(cnt+1,j,temp+[j])

result = []
n,m = map(int,input().split())
dfs(0,1,[])

for data in result:
    print(*data)
