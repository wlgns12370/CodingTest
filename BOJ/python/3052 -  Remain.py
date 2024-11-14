import sys
input=sys.stdin.readline
remain = [0 for _ in range(42)]
for _ in range(10):
    num = int(input())
    remain[num%42] += 1

cnt = 0
for data in remain:
    if data != 0:
        cnt += 1
print(cnt)
