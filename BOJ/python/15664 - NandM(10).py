import sys
input = sys.stdin.readline

def dfs(cnt,s,lis):
    if cnt == m:
        result.append(lis)
        return
    prev = -1
    for k in range(s,n):
        #중복제거
        if prev != arr[k]:
            prev = arr[k]
            dfs(cnt+1,k+1,lis + [arr[k]])

result = []
n,m = map(int,input().split())
arr = sorted(list(map(int,input().split())))
dfs(0,0,[])

for data in result:
    print(*data)
