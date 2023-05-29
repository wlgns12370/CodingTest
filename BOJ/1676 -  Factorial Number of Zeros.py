import sys
input = sys.stdin.readline

dp = [1]
n = int(input())
for i in range(2,n+1):
    dp.append(dp[i-2]*i)
fac = str(dp[n-1])
cnt = 0
for data in reversed(fac):
    if data == '0':
        cnt += 1
    else:
        print(cnt)
        break
