import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int,input().split())))
#구간합 배열
seg = [0 for _ in range(n)]
seg[0] = arr[0]
for idx in range(1,n):
    seg[idx] = arr[idx] + seg[idx-1]

print(sum(seg))
