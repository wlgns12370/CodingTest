import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
l_arr = []
max_score = max(arr)
for i in range(n):
    l_arr.append((arr[i]/max_score)*100)
print(sum(l_arr)/n)
