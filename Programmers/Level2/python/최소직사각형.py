def solution(sizes):
    answer = 0
    temp = 0
    # 명함을 큰것, 작은것으로 바꾸기
    for size in sizes:
        if size[0] < size[1]:
            temp = size[0]
            size[0] = size[1]
            size[1] = temp
    max_x = max(sizes, key = lambda x:x[0])[0]
    max_y = max(sizes, key = lambda x:x[1])[1]
    return max_x * max_y