def solution(answers):
    cnt = [0,0,0]
    l = len(answers)
    arr = [1,2,3,4,5] * ((l // 5) + 1)
    arr2 = [2,1,2,3,2,4,2,5] * ((l // 8) + 1)
    arr3 = [3,3,1,1,2,2,4,4,5,5] * ((l // 10) + 1)
    for i in range(l):
        if answers[i] == arr[i]:
            cnt[0] += 1
        if answers[i] == arr2[i]:
            cnt[1] += 1
        if answers[i] == arr3[i]:
            cnt[2] += 1
    max_value = max(cnt[0], cnt[1], cnt[2])
    answer = [i+1 for i,v in enumerate(cnt) if v == max_value]
    return answer