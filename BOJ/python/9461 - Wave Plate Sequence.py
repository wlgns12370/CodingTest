import sys
input = sys.stdin.readline
MAX_N = 100

dp = [1,1,1,2,2]

t = int(input())

for i in range(5,MAX_N):
    dp.append(dp[i-1]+dp[i-5])

for _ in range(t):
    num = int(input())
    print(dp[num-1])