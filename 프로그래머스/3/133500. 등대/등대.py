import sys
sys.setrecursionlimit(200000)

def solution(n, lighthouse):
    
    adj = [[] for _ in range(n+1)]
    
    for v,w in lighthouse:
        adj[v].append(w)
        adj[w].append(v)
    
    dp = [[0,0] for _ in range(n+1)]
    
    def dfs(node, parent):
        dp[node][0] = 0
        dp[node][1] = 1
        
        # i번째를 색칠할 경우
        for next in adj[node]:
            if next == parent:
                continue
            
            dfs(next, node)
            
            # 탑다운에서 올라오는 과정
            # 지금 꺼져있었다면 무조건 이전에는 켜져야함
            dp[node][0] += dp[next][1]
            # 지금 키는 경우라면 전의 노드가 켜진것과 꺼진것 둘다 고려.
            dp[node][1] += min(dp[next][0],dp[next][1])
    
    dfs(1,0)
    
    answer = min(dp[1][0],dp[1][1])
    
    return answer



