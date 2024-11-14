import sys
input = sys.stdin.readline

n,k = map(int,input().split())
dec = [int(input()) for _ in range(n)]

cnt = 0
for coin in reversed(dec):
    cnt += k // coin
    k = k % coin

print(cnt)
