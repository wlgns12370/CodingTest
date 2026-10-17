def solution(scores):
    wa, wb = scores[0]
    wanho_sum = wa + wb

    # 완호의 인센티브 여부
    for a, b in scores:
        if a > wa and b > wb:
            return -1
    
    scores.sort(key=lambda x :(-x[0], x[1]))
        
    max_b = -1
    answer = 1
    for idx in range(len(scores)):
        
        # 이전값중에 동료평가가 높은 지 비교
        if max_b > scores[idx][1]:
            continue
            
        if scores[idx][0] + scores[idx][1] > wanho_sum:
            answer+=1
        
        if max_b < scores[idx][1]:
            max_b = scores[idx][1]
    
    return answer