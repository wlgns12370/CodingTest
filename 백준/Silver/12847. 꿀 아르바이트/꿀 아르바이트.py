import sys
input = sys.stdin.readline

n, m = map(int,input().split())
t = list(map(int,input().split()))

sal = 0
for i in range(0,m):
    sal += t[i]

temp = sal
for i in range(m, n, 1):
    temp = temp - t[i-m] + t[i]
    if sal < temp:
        sal = temp

print(sal)