def solution(topping):
    answer = 0
    l=len(topping)
    for idx in range(1,l):
        # idx번 기준으로 자르기 a,b로
        a = topping[0:idx]
        b = topping[idx:]
        
        a_s = set(a)
        b_s = set(b)
        
        if len(a_s) == len(b_s):
            answer += 1
        
    return answer