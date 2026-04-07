def solution(name, yearning, photo):
    answer = []    
    dic = dict(zip(name,yearning))
    
    for data in photo:
        temp = 0
        
        # 한줄 검사
        for p_name in data:
            #딕셔너리 검사해서 잇으면 점수 + 없으면 + x
            if dic.get(p_name) != None:
                temp += dic.get(p_name)
        answer.append(temp)
        
    return answer