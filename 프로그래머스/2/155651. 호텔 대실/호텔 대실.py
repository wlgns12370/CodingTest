def solution(book_time):
    
    def stringToMin(time):
        h,m = time.split(":")
        return int(h)*60+int(m)
        
    a = [0 for _ in range(1440)]
    
    for s_time, e_time in book_time:
        s = stringToMin(s_time)
        e = min(1439, stringToMin(e_time)+10)
        
        for i in range(s,e):
            a[i] += 1
    
    answer = max(a)
    return answer