import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    dp0 = [0,1,1,1]
    dp1 = [0,1,1,2]
    n = int(input())
    for i in range(4,n+1):
        dp0.append(dp0[i-1]+dp0[i-2])
        dp1.append(dp1[i-1]+dp1[i-2])
    if n == 0:
        print(1,0)    
    elif n == 1:
        print(0,1)
    else:
        print(dp0[n],dp1[n])
