import sys

arr = [0] * 5
total = 0
for i in range(5):
    num = int(sys.stdin.readline())
    arr[i] = num
    total += num
print(int(total/5))
print(sorted(arr)[2])