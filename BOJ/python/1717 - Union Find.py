import sys

n, m = map(int, sys.stdin.readline().split())
tree = [0] * (n + 1)
for i in range(n + 1):
    tree[i] = i

if (n > 1000):
    sys.setrecursionlimit(10 ** 5)


def getParentNode(node):
    if tree[node] == node:
        return node
    tree[node] = getParentNode(tree[node])
    return tree[node]

def Union(a, b):
    node = getParentNode(a)
    node2 = getParentNode(b)
    if node < node2:
        tree[node2] = node
    else:
        tree[node] = node2

for i in range(m):
    option, a, b = map(int, sys.stdin.readline().split())
    if option:
        node = getParentNode(a)
        node2 = getParentNode(b)
        print("YES") if node == node2 else print("NO")
    else:
        Union(a, b)
