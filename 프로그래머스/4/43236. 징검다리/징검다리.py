from collections import deque
def solution(distance, rocks, n):
    rocks.sort()
    rocks = [0] + rocks + [distance]
    l = len(rocks)
    
    def isOk(k):
        cnt = 0
        prev = 0
        for i in range(1,l):
            d = rocks[i] - prev
            if d < k:
                cnt+=1
            else:
                prev = rocks[i]    
        return cnt <= n
    
    lo = 0
    hi = 1000000000
    answer = 0
    while lo <= hi:
        mid = (lo+hi) // 2
        if isOk(mid):
            answer = mid
            lo = mid+1
        else:
            hi = mid-1

    return answer