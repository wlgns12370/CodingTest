import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    h,w,n = map(int,input().split())
    
    #호수
    num = n // h + 1
    #층수
    floor = n % h
    if n % h == 0:
        floor = h
        num -= 1
    print(floor*100 + num)
