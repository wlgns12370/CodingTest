def solution(n, times):
    
    def ok(k):#28
        temp = 0
        for data in times: # 28 7-> 4 28// 10 -> 2
            # 26 8,8,8
            temp += k//data
        
        return temp
        
    answer = 0
    lo = 1
    hi = max(times) * n
    while lo <= hi:
        mid = (lo+hi) // 2
        num = ok(mid)
        if num < n:
            lo = mid+1
        else:
            answer = mid
            hi = mid - 1
            
    return answer