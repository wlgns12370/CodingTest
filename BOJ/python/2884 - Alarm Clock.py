import sys
input = sys.stdin.readline

h,m = map(int,input().split())

sub_m = m - 45
if sub_m > 0:
    print(h,sub_m)
elif sub_m == 0:
    print(h,0)
else:
    sub_m += 60
    sub_h = h-1
    if sub_h < 0:
        print(23,sub_m)
    else:
        print(sub_h,sub_m)
