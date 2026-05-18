from collections import deque
def solution(distance, rocks, n):
    rocks.sort()
    rocks = [0] + rocks + [distance]
    l = len(rocks)
            
    # 최소 거리가 되기 위해서 제거해야하는 바위의 개수를 확인해 바위를 둘 수 있는 지 판단
    # 거리의 최솟값이 되기 위해서 제거해야하는 돌의 개수와 n비교
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
    
    # 이분탐색
    lo = 0
    hi = 1000000000
    # 바위 사이의 거리의 최솟값
    answer = 0
    while lo <= hi:
        mid = (lo+hi) // 2
        temp = isOk(mid)
        print(mid, temp)
        if temp:
            answer = mid
            lo = mid+1
        else:
            hi = mid-1

    return answer