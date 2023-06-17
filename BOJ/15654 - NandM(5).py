import sys
input = sys.stdin.readline

def dfs(cnt,lis):
    if cnt == m:
        result.append(lis)
        return
    
    for j in range(0,n):
      #동일한 선택지 삭제
        if visited[j] == False:
            visited[j] = True
            dfs(cnt+1,lis+[seq[j]])
            visited[j] = False

result = []
n,m = map(int,input().split())
seq = sorted(list(map(int,input().split())))
visited = [False for _ in range(n)]
dfs(0,[])
for data in result:
    print(*data)
