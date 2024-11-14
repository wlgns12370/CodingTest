"""
    알고리즘
    - 특정 원소를 제거하지 않은 경우
        - dp[0][i] = max(dp[0][i-1] + arr[i], arr[i])
    - 특정 원소를 제거한 경우
        - dp[1][i] = max(dp[0][i-1], dp[1][i-1] + arr[i])
        - dp[0][i-1]에 arr[i]를 더하지 않음으로 특정 원소 제거하는 경우
        - dp[1][i-1]는 특정 원소가 하나 제거된 경우
	
    시간복잡도
    - O(n)
	
    자료구조
    - 2차원 배열
"""

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [[data for data in arr] for _ in range(2)]

dp[0][0] = arr[0]
for i in range(1,n):
    dp[0][i] = max(dp[0][i-1] + arr[i], arr[i])
    dp[1][i] = max(dp[0][i-1], dp[1][i-1] + arr[i])

print(max(max(dp[0]),max(dp[1])))
