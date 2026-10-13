import heapq
def solution(n, cores):
    answer=0
    
    l=len(cores)
    if n <= l:
        return n
    
    #k 초 일때 작업이 완벽하게 끝나는가?
    def isOk(k):
        #작업의 모든 개수
        temp = 0
        for c in cores:
            #각 코어별 작업 횟수
            temp+= k // c + 1
        # 전체 n보다 코어 할당 개수가 많다
        return temp >= n
        
    # N번째 작업이 코어에 할당되는 최소 시간
    lo = 0
    hi = int(1e9)
    while lo <= hi:
        mid = (lo+hi)//2
        if isOk(mid):
            answer=mid
            hi = mid-1
        else:
            lo = mid+1

    # n초때
    temp = 0
    for data in cores:
        temp += (answer - 1) // data + 1 #2//1-> 3,2//2 ->2,2//3 -> 1 6

    for idx, data in enumerate(cores):
        if answer % data == 0: #6, 1,2,3 000
            temp += 1

            if temp == n:
                return idx + 1     
    
    return answer