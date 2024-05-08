import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]
    
def union(x,y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x
        network_count[x] += network_count[y]
    print(network_count[x])

t = int(input())
for _ in range(t):
    parent = {}
    network_count = {}
    f = int(input())
    for _ in range(f):
        user1, user2 = input().split()
        if user1 not in parent:
            parent[user1] = user1
            network_count[user1] = 1
        if user2 not in parent:
            parent[user2] = user2
            network_count[user2] = 1
        union(user1, user2)