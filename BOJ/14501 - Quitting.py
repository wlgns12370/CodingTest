import sys
input = sys.stdin.readline

n = int(input())
t = [0 for _ in range(n+1)]
p = [0 for _ in range(n+1)]
dp = [0 for _ in range(n+2)]

for i in range(1,n+1):
    t_num, p_num = map(int,input().split())
    t[i] = t_num
    p[i] = p_num

for i in range(n,0,-1):
    if t[i]+i > n+1:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(p[i] + dp[i + t[i]], dp[i+1])
print(max(dp))
