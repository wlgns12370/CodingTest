import sys
input = sys.stdin.readline
sys.setrecursionlimit(10*6)

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

dp_cnt = 0
n = int(input())
fibo = [1,1]


for i in range(2,n):
    fibo.append(fibo[i-1]+fibo[i-2])
    dp_cnt+=1

print(fib(n),dp_cnt)
