import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
x = int(input())

arr.sort()
l = 0
r = n-1
temp = 0
cnt = 0
while(True):
    temp = arr[l] + arr[r]
    if (l==r or l > r):
        break

    if x > temp:
        l+=1
        
    elif x < temp:
        r-=1

    elif x == temp:
        cnt+=1
        l+=1
        r-=1

print(cnt)