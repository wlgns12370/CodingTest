import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(100001)

def solve(start):
    visited_data[start] = 1
    dfs((start,0))

def dfs(v):
    for node in adj_list[v[0]]:
            if visited_data[node[0]] == 0:
                visited_data[node[0]] = visited_data[v[0]] + node[1]
                dfs(node)
    return

v = int(input())
adj_list = [[] for _ in range(v+1)]
visited_data = [0 for _ in range(v+1)]

for _ in range(v):
    data = list(map(int,input().split()))
    # i+1 인덱스 = 가중치
    for i in range(1,len(data)-2,2):
        adj_list[data[0]].append((data[i],data[i+1]))

solve(1)
start = visited_data.index(max(visited_data))

visited_data = [0 for _ in range(v+1)]
solve(start)

print(max(visited_data)-1)
