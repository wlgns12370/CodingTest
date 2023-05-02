import sys
input=sys.stdin.readline

def prime(num):
    IsPrime = 1
    if num == 1:
        return 0
    else:
        for i in range(2,num):
            if num % i == 0:
                IsPrime = 0
                return IsPrime
        return IsPrime

cnt = 0
n = int(input())
num_list = list(map(int,input().split()))
for i in range(n):
    if prime(num_list[i]):
        cnt+=1
print(cnt)
