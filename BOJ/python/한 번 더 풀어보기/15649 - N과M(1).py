import  sys
input = sys.stdin.readline
from itertools import permutations

n,m = map(int,input().split())
a = [i for i in range(1,n+1)]
for perm in permutations(a, m):
    print(*perm)