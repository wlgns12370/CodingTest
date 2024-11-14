import sys
input = sys.stdin.readline

def dfs(cnt,temp):
    if cnt == m:
        result.append(temp)
        return
    for j in range(1,n+1):
				# 같은 수를 선택하는 선택지를 삭제
        if visited[j] == False:
            visited[j] = True
            dfs(cnt+1,temp+[j])
            visited[j] = False

result = []
n,m = map(int,input().split())
visited = [False for _ in range(n+1)]
dfs(0,[])

for data in result:
    print(*data)
