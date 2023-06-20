import sys
input = sys.stdin.readline

a,b,c = map(int,input().split())

def DivideAndConquer(a,b,c):
    if b == 0:
        return 1
    if b == 1:
        return a%c

    Divide_a = DivideAndConquer(a,b//2,c)

    #차수가 짝수
    if b % 2 == 0:
        return Divide_a * Divide_a % c

    #차수가 홀수
    else:
        return Divide_a * Divide_a * a % c

result = DivideAndConquer(a,b,c)
print(result)
