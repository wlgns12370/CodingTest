import sys
from math import sqrt

def fibo(n):
    result = 1/sqrt(5)*((((1+sqrt(5))/2)**n) - (((1-sqrt(5))/2)**n))
    return int(result)

n = int(sys.stdin.readline())
print(fibo(n))