def solution(m, n, puddles):
    dp = [[0 for i in range(n+1)] for j in range(m+1)]
    
    for pudd in puddles:
        dp[pudd[0]][pudd[1]] = -1
    dp[1][1] = 1
    print(dp)
    print()
    for i in range(1,m+1):
        for j in range(1,n+1):
            if i == 1 and j == 1:
                continue
            if dp[i][j] == -1:
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1])%1_000_000_007
    
    print(dp)
    return dp[m][n]