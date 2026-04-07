def solution(cards1, cards2, goal):
    n1 = len(cards1)
    n2 = len(cards2)
    c1 = 0
    c2 = 0
    flag = 0
    for word in goal:
        if n1 != c1 and cards1[c1] == word:
            c1 +=1
        elif n2 != c2 and cards2[c2] == word:
            c2 +=1
        else:
            flag=1
            break
    
    answer = "Yes" if flag == 0 else "No"
    return answer