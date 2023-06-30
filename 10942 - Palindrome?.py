import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int,input().split()))
m = int(input())
dp = [[False] * (n+1) for _ in range(n+1)]

for point in range(n):
    for start in range(n-point):
        
        end = start + point
        # 숫자열이 1개일 경우
        if start == end:
            dp[start][end] = True
        #처음과 끝이 같다면
        if numbers[start] == numbers[end]:
            # 숫자열이 2개일 경우
            if start+1 == end:
                dp[start][end] = True
            # 처음과 끝 빼고 중간이 팰린드롬 이라면
            elif dp[start+1][end-1] == True:
                dp[start][end] = True

for _ in range(m):
    s,e = map(int,input().split())
    print(1) if dp[s-1][e-1] else print(0)
