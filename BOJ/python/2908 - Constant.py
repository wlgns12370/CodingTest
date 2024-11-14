import sys

st1,st2 = sys.stdin.readline().split()

rst1 = st1[::-1]
rst2 = st2[::-1]

print(rst1) if int(rst1) > int(rst2) else print(rst2)