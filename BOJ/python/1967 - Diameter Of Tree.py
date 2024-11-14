import sys
from collections import deque
sys.setrecursionlimit(10001)
input = sys.stdin.readline

def solve(start):
    visited_data[start] = 1
    dfs((start,0))

def dfs(v):
    for node in adj_list[v[0]]:
            if visited_data[node[0]] == 0:
                visited_data[node[0]] = visited_data[v[0]] + node[1]
                dfs(node)
    return


n = int(input())

adj_list = [[] for _ in range(n+1)]
visited_data = [0 for _ in range(n+1)]
for _ in range(n-1):
    u,v,w = map(int,input().split())
    #tuple 1번째 인덱스는 가중치이다
    adj_list[u].append((v,w))
    adj_list[v].append((u,w))

solve(1)
start = visited_data.index(max(visited_data))

visited_data = [0 for _ in range(n+1)]
solve(start)

print(max(visited_data)-1)
