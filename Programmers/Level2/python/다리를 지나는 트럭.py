from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    start = deque(truck_weights)
    bridge = deque()
    total_weight = 0

    while True:
        # 종료 조건
        if len(start) == 0 and len(bridge) == 0:
            break

        # 다리를 지남
        if len(bridge) != 0 and bridge[0][0] == bridge_length:
            idx, pop_weight = bridge.popleft()

        # 대기 트럭이 다리로 올라갈 수 있는가?
        if len(start) != 0 and sum(row[1] for row in bridge) + start[0] <= weight:
            truck = start.popleft()
            bridge.append([0,truck]) # 다리 위로 트럭이 올라감

        # 시간이 지남
        for data in bridge:
            data[0] += 1
        time += 1

    print(time)
    return time