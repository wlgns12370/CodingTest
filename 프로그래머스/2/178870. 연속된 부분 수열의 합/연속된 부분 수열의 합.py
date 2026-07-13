def solution(sequence, k):
    
    if sequence[0] == k:
        return [0,0]
    answer = [-1,-1]
    l = len(sequence)
    range_cnt = l+2
    s=0
    e=1
    temp = sequence[0]+sequence[1]
    while True:
        if temp < k and e >= l-1:
            break
        if temp == k:
            if e-s < range_cnt:
                answer[0] = s
                answer[1] = e
                range_cnt = e-s
            temp -= sequence[s]
            s+=1
            
        elif temp < k:
            e+=1
            temp += sequence[e]
        elif temp > k:
            temp -= sequence[s]
            s+=1
            
    return answer