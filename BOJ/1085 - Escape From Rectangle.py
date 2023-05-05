import sys
input = sys.stdin.readline

x,y,w,h = map(int,input().split())
x_pos = ((w-x) if x > (w-x) else x)
y_pos = ((h-y) if y > (h-y) else y)
print(y_pos if x_pos > y_pos else x_pos)
