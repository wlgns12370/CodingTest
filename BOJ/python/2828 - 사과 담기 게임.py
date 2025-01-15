import sys
input = sys.stdin.readline

n, m = map(int, input().split())
j = int(input())

left = 1
right = m
result = 0
for _ in range(j):
    p = int(input())
    if left <= p <= right:
        continue
    elif p > right:
        result += (p-right)
        left += (p-right)
        right = p
    elif left > p:
        result += (left-p)
        right -= (left-p)
        left = p
print(result)