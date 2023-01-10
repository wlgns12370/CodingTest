import sys
n = int(sys.stdin.readline())
arr = [0] * n
def b_sort():
    temp = 0
    for i in range(n):
        for j in range (n-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

for i in range(n):
    num = int(sys.stdin.readline())
    arr[i] = num

b_sort()
for i in arr:
    print(i)