import sys
input = sys.stdin.readline

def check(mid):
     temp = 0
     for data in tree:
          if data > mid:
               temp += data-mid
     return temp>=m

n,m = map(int,input().split())
tree = list(map(int,input().split()))

lo = 0
hi = 1000000000
while lo+1 < hi:
     mid = (lo+hi)//2
     if check(mid):
          lo = mid
     else:
          hi = mid

print(lo)