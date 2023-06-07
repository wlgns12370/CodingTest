import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    coins = list(map(int,input().split()))
    amount = int(input())
    dp = [0 for _ in range(amount+1)]
    #0을 선택하는 방법은 1가지 R)아무것도 선택하지 않는다. 
    dp[0] = 1

    for i in range(n):
        for j in range(coins[i],amount+1):
            dp[j] += dp[j-coins[i]]
    print(dp[amount])
