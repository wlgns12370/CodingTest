"""
    알고리즘
    - 배열 뒤에서 부터 순차적으로 탐색한다.
    - dp 배열에 최대 상자의 개수를 저장한다
    - n-1 ~ 0을 탐색하는 i를 시작으로 자신보다 작은 수의 최대 상자의 개수를 buf에 저장한다.
    - buf에 가장 큰 값에 1을 더해 dp[i]에 저장한다.
	
    시간복잡도
    - O(n^2)
	
    자료구조
    - 1차원 배열
"""
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [0 for _ in range(n)]

for i in range(n-1,-1,-1):
    buf = []
    for j in range(i+1,n):
        if arr[i] < arr[j]:
            buf.append(dp[j])
    if buf != []:
        dp[i] = max(buf) + 1

print(max(dp)+1)