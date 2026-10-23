from collections import deque
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
S, T = map(int, input().split())

adj = [[] for _ in range(n+1)]
reverse_adj = [[] for _ in range(n+1)]

for v,w in edges:
    adj[v].append(w)
    reverse_adj[w].append(v)

def findMinLoad(arr, n, start, end):
    q = deque([])
    q.append(start)

    d = [False for _ in range(n+1)]
    d[start] = True

    while q:
        
        node = q.popleft()

        if node == end:
            continue

        for new in arr[node]:
            if d[new] == False:
                d[new] = True
                q.append(new)

    return d

# S -> X -> T
to_s = findMinLoad(adj, n, S, T)
from_s = findMinLoad(reverse_adj, n, T, -1)

to_t = findMinLoad(adj, n, T, S)
from_t = findMinLoad(reverse_adj, n, S, -1)

answer = 0
for idx in range(1,n+1):
    if idx == S or idx == T:
        continue

    if to_s[idx] and to_t[idx] and from_s[idx] and from_t[idx]:
        answer += 1

print(answer)