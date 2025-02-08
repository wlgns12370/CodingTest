from collections import deque
def solution(priorities, location):
    l = len(priorities)
    arr = deque(enumerate(priorities))
    process = []

    while len(process) != l:
        idx, pop_data = arr.popleft()
        max_data = -1
        # pop_data를 제외한 나머지 값중 가장 큰 값 찾기
        for i, data in arr:
            if max_data < data:
                max_data = data

        if max_data <= pop_data:
            process.append((idx, pop_data))
        elif max_data > pop_data:
            arr.append((idx, pop_data))

    cnt = 1
    for idx, data in process:
        if idx == location:
            break
        cnt += 1
    answer = cnt
    return answer