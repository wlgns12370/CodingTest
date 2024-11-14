import sys
input = sys.stdin.readline
a = int(input())
b = int(input())
c = int(input())

cnt = [0 for _ in range(10)]
result = str(a*b*c)

for data in result:
    cnt[int(data)] += 1

for data in cnt:
    print(data)
