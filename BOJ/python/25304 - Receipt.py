import sys
input = sys.stdin.readline

n = int(input())
sum = 0

for _ in range(int(input())):
    a, b = map(int, input().split())
    sum += a * b

print("Yes") if sum == n else print("No")
