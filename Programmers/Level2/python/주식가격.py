def solution(prices):
    answer = []
    l = len(prices)
    for i in range(l):
        cnt = 0
        for j in range(i+1,l):
            cnt += 1
            if prices[i] > prices[j]:
                break
        answer.append(cnt)
    return answer