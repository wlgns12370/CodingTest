import sys
input = sys.stdin.readline

while True:
    arr = list(map(int,input().split()))
    long_len = max(arr)
    if sum(arr) == 0:
        break
    arr.remove(long_len)
    if arr[0]**2 + arr[1]**2 == long_len**2:
        print("right")
    else:
        print("wrong")
