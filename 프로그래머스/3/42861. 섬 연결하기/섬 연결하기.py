import heapq

def solution(n, costs):
    answer = 0
    adj = [[] for _ in range(n)]
    
    for data in costs:
        adj[data[0]].append([data[2],data[1]])
        adj[data[1]].append([data[2], data[0]])
    
    visited = [False for _ in range(n)]
    hq = [[0,0]]
    v_node = 0
    
    while hq:
        cost, pos = heapq.heappop(hq)
        
        # 같은 장소로 가는 더 큰 값 제거
        if visited[pos] == True:
            continue
            
        visited[pos] = True
        answer += cost
        v_node += 1
        
        # 종료조건
        if v_node == n:
            break        
        
        for min_cost, min_pos in adj[pos]:
            # 노드 선택 후 이동
            if visited[min_pos] == False:
                heapq.heappush(hq, [min_cost, min_pos])
    
    return answer