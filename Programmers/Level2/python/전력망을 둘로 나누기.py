from collections import deque

def bfs(start, adj, n):
    visited = [False for _ in range(n+1)]
    visited[start] = True
    cnt = 0
    queue = deque()
    queue.append(start)
    while queue:
        cnt += 1
        px = queue.popleft()
        for node in adj[px]:
            if not visited[node]:
                visited[node] = True
                queue.append(node)
    return cnt

def solution(n, wires):
    l = len(wires)
    adjs = [[[] for _ in range(n+1)] for _ in range(l)]

    #네트워크 하나씩 삭제
    for i in range(l):
        for idx in range(l):
            if idx == i:
                continue
            adjs[i][wires[idx][0]].append(wires[idx][1])
            adjs[i][wires[idx][1]].append(wires[idx][0])

    answer = 101
    for adj in adjs:
        for idx in range(1,l):
            if adj[idx]:
                node_cnt = bfs(idx, adj, n)
                break
        answer = min(abs(n - 2*node_cnt), answer)

    return answer