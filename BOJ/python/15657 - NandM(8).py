import sys
input = sys.stdin.readline

def dfs(cnt,s,lis):
    if cnt == m:
        result.append(lis)
        return
    for j in range(s,n):
        dfs(cnt+1,j,lis+[arr[j]])

result = []
n,m = map(int,input().split())
arr = sorted(list(map(int,input().split())))

dfs(0,0,[])
for data in result:
    print(*data)
