import sys
input = sys.stdin.readline

n = input()
arr = [x for x in n]
arr.pop()
arr.sort(reverse=True)

for data in arr:
    print(data,end="")