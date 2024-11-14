import sys
input = sys.stdin.readline
from collections import deque
t = int(input())
for _ in range(t):
    IsError = 0
    p = input()
    n = int(input())
    arr = deque(map(str,input().strip()[1:-1].split(',')))
    if n == 0:
        arr = []

    rev = 0
    for fun in p:
        if fun == "R":
            rev += 1
        elif fun == "D":
            #arr is not Empty
            if len(arr) != 0:
                #rev가 짝수면 왼쪽팝
                if rev % 2 == 0:                    
                    arr.popleft()
                #rev가 홀수면 오른쪽팝
                else:
                    arr.pop()
            #arr is Empty
            else:
                IsError = 1
                break

    if IsError == 1:
        print("error")
    else:
        if rev % 2 != 0:
            arr.reverse()
        print("["+",".join(arr)+"]")
