import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    stack = []
    flag = 1
    ps = input().strip()
    for data in ps:
        if data == '(':
            stack.append(data)
        else:
            if len(stack) != 0:
                stack.pop()
            else:
                flag = 0
    if len(stack) != 0:
        flag = 0
    print("YES") if flag == 1 else print("NO")
