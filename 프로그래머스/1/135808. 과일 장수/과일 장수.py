def solution(k, m, score):
    score.sort(key = lambda x : -x)
    l = len(score)
    idx = 0
    answer = 0
    
    while True:

        # idx + m 이 l보다 크다면 x
        if idx+m > l:
            break
        # i부터 i+m 사이에 최솟값 찾기
        temp = score[idx]
        for i in range(idx, idx+m):
            if temp > score[i]:
                temp = score[i]
        answer += (temp * m)
        idx += m
    
    return answer