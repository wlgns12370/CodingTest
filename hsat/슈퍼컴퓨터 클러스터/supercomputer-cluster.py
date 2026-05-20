import math
N, B = map(int, input().split())
a = list(map(int, input().split()))

# a배열에서 k라는 숫자가 최소의 성능이 될 수 있는가?
def isOk(a,k):
    temp = 0
    for data in a:
        if data < k:
            temp += (k-data)**2
    
    return temp <= B

lo = 1
hi = max(a) + int(math.sqrt(B))
answer = 0
while lo <= hi:
    mid = (lo+hi) // 2
    if isOk(a, mid):
        answer = mid
        lo = mid+1
    else:
        hi = mid-1
    
print(answer)