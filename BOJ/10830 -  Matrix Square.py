import sys
input = sys.stdin.readline
div = 1000
def power(A,B,n):
    temp = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                temp[i][j] += (A[i][k] * B[k][j])%div
    return temp
    
#분할정복
def DivideAndConquer(a,b,n):
    #종료조건
    if b == 1:
        for i in range(n):
            for j in range(n):
                a[i][j] %= div 
        return a

    #Start a^(b//2)
    powerd_a = DivideAndConquer(a,b//2,n)
    if b % 2 == 0:
        return power(powerd_a,powerd_a,n)
    #홀수일경우(3이상) (제곱한A)*a 연산을 해준다
    else:
        return power(power(powerd_a,powerd_a,n),a,n)


n,b = map(int,input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int,input().split())))

result = DivideAndConquer(matrix,b,n)
for i in range(n):
    for j in range(n):
        result[i][j] %= div 
for row in result:
    print(*row)
