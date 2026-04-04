import sys
input = sys.stdin.readline

n, k = map(int,input().split())

arr = [[0,0]]
for _ in range(n):
    w,v = map(int,input().split())
    arr.append([w,v])

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1,n+1):
    w,v = arr[i]
    for max_w in range(1,k+1):
        if max_w < w:
            dp[i][max_w] = dp[i-1][max_w]
        else:
            dp[i][max_w] = max(dp[i-1][max_w], dp[i-1][max_w-w]+v)
        
print(dp[n][k])