import sys
input = sys.stdin.readline
table  = {"A+":4.5,"A0":4.0,"B+":3.5,"B0":3.0,"C+":2.5,"C0":2.0,"D+":1.5,"D0":1.0,"F":0.0,"P":0.0}

total = 0
divisor = 0
for _ in range(20):
  name,grade,rating = input().split()
  if rating != "P":
    divisor += float(grade)
    total += (table[rating]*float(grade))
    
print(total/divisor)
