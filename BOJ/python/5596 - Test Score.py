import sys
input = sys.stdin.readline

a,b,c,d = map(int,input().split())
e,f,g,h = map(int,input().split())

ta = a+b+c+d
tb = e+f+g+h

print(ta) if ta > tb else print(tb)
