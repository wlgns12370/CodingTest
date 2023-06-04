import sys
input = sys.stdin.readline

A, B = map(int, input().split())
C = int(input())

hour = (B+C)//60
min = (B+C)%60

if(B + C >= 60):
  if(A+hour >= 24):
    A = A - 24
  A = A + hour
  print(A, min)

else:
  if(A >= 24):
    A = A - 24
  print(A, B+C)
