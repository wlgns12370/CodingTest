"""
    알고리즘
    - 이전까지의 합(dp[i-1])과 앞으로 더해질 값(arr[i])이 앞으로 더해질 값(arr[i]) 보다 작다면 더 이상 계산해 보지 않아도 된다.
    - max(dp[i-1]+arr[i],arr[i])를 사용하여 다이나믹 프로그래밍으로 풀어내면 된다.
	
    시간복잡도
    - O(n)
	
    자료구조
    - 1차원 배열
"""
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [0 for _ in range(n)]
dp[0] = arr[0]

for i in range(1,n):
    dp[i] = max(dp[i-1]+arr[i],arr[i])

print(max(dp))