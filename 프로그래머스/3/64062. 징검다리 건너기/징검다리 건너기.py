def solution(stones, k):
    
    def isOk(num,l):
        flag = 0
        for stone in stones:
            stone = stone-(num-1)
            if stone > 0:
                flag = 0
            else:
                flag += 1
                if flag > k-1:
                    return False
        return True
    
    answer = 0
    lo = 0
    hi = max(stones)+1
    a_l = len(stones)
    while lo <= hi:
        mid = (lo+hi) // 2
        if isOk(mid,a_l):
            answer = mid
            lo = mid+1
        else:
            hi = mid-1
    return answer