import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = list(map(int,input().split()))
segment_sum = [0]

for i in range(n):
    segment_sum.append(segment_sum[i] + arr[i])

for _ in range(m):
    i,j = map(int,input().split())
    if i == j:
        print(arr[i-1])
    else:
        print(segment_sum[j] - segment_sum[i-1])
