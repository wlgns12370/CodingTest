def solution(land):
    l=len(land)
    dp = [[0,0,0,0] for _ in range(l)]
    for i in range(4):
        dp[0][i] = land[0][i]
    
    for i in range(1,l):
        for j in range(4):
            val = 0
            for k in range(4):
                if j != k:
                    val = max(val, dp[i-1][k])
                
            dp[i][j] = land[i][j] + val
    
    return max(dp[-1])