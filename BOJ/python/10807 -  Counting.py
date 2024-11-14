import sys
input = sys.stdin.readline
n = int(input())
arr = []
data = input().split()
check = int(input())
cnt = 0
for idx in range(n):
    if check == int(data[idx]):
        cnt += 1
print(cnt)
