def solution(n, stations, w):
    # k개를 추가하면 모두 데이터를 받을 수 있는가?
    # 각 구간에 연속되는 0의 개수를 카운트하고 2w+1을 나누고 딱떨어지지 않는 다면 +1을 한다.
    # 또한 각 구간에 연속되는 0의 개수가 2w+1보다 작다면 +1을 한다.
    def total_find(w,n):
        weight = 2*w+1
        total = 0
        zero_cnt = 0
        start = 0
        # 0개수 구하기
        # 앞부분 처리
        for station in stations:
            zero_cnt = station-w-start-1
            # 필요개수 구하기
            if zero_cnt % weight == 0:
                total += (zero_cnt // weight)
            else:
                total += (zero_cnt // weight) + 1
            start = station+w
        
        # 뒷부분 처리
        if start < n:
            zero_cnt = n-start
            if zero_cnt % weight == 0:
                total += (zero_cnt // weight)
            else:
                total += (zero_cnt // weight) + 1
        return total
        
    answer = 0
    answer = total_find(w,n)
                        
    return answer