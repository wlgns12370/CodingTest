from math import sqrt
def solution(brown, yellow):
    answer = []
    # 약수 추출
    div = []
    num = brown + yellow
    for i in range(3,int(sqrt(num))+1):
        if num % i == 0:
            div.append((i, num/i))
    # 테두리와 갈색 격자의 수가 같은 상황 찾기
    for d in div:
        out_line = d[1]*2 + 2*(d[0]-2)
        if out_line == brown:
            answer.append(d[1])
            answer.append(d[0])
    return answer