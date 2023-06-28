import sys
input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(str,input().split())))

arr.sort(key = lambda x:int(x[0]))
for data in arr:
    print(*data)
