import sys
input = sys.stdin.readline

n,x = map(int,input().split())
a = list(map(int,input().split()))
for data in a:
    if data < x:
        print(data,end=" ")
