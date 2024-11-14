import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    result = ''
    r,s = input().split()
    for char in s:
        for _ in range(int(r)):
            result += char
    print(result)
