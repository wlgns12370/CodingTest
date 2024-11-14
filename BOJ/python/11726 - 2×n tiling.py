import sys
input = sys.stdin.readline
sys.setrecursionlimit(1001)

def dp(x):
    if x == 1: return 1
    elif x == 2: return 2
    #메모리가 비워진 경우
    if memory[x] == 0:
        memory[x] = dp(x-1) + dp(x-2)
    return memory[x]

n = int(input())
memory = [0] *(n+1)
print(dp(n)%10_007)
