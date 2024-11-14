"""
    알고리즘
    - 삼각형이 아래층으로 내려올 때, 최대가 되는 값을 가지는 dp 배열을 사용한다.
    - 가장 아래층에서 최댓값을 선택하면 이제까지 선택된 수의 합이 최대가 되는 경로의 합이다.
	
    시간복잡도
    - O(N^2)
	
    자료구조
    - 2차원 배열
"""

import sys
input = sys.stdin.readline

arr = []
n = int(input())
dp = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(n):
    data = list(map(int, input().split()))
    arr.append(data)

dp[0][0] = arr[0][0]

for i in range(n-1):
    for j in range(i+1):
        dp[i+1][j] = max(dp[i+1][j], dp[i][j]+arr[i+1][j])
        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+arr[i+1][j+1])

print(max(dp[n-1]))