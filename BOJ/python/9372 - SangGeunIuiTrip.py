import sys

t = int(sys.stdin.readline())
tree = []
for _ in range(t):
  n,m = map(int,sys.stdin.readline().split())
  for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    tree.append((a,b))
  print(n-1)
