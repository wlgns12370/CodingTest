import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
tree = [0] * (n + 1)
for i in range(n + 1):
    tree[i] = i
check = [0] * (m + 1)

def FindParent(node):
    if tree[node] == node:
        return node
    tree[node] = FindParent(tree[node])
    return tree[node]

def UNION(node, node2):
    node_Parent = FindParent(node)
    node2_Parent = FindParent(node2)
    if node_Parent < node2_Parent:
        tree[node2_Parent] = node_Parent
    else:
        tree[node_Parent] = node2_Parent

for i in range(n):
    data = list(map(int,sys.stdin.readline().split()))
    for j in range(i+1,n):
        if data[j] == 1:
            UNION(i,j)

check = list(map(int,sys.stdin.readline().split()))

flag = 0
for i in check:
    if FindParent(check[0]-1) != FindParent(i-1):
        flag = 1
        break
print("YES") if flag == 0 else print("NO")

# checking = set(tree[i-1] for i in check)
# print("YES") if len(checking) == 1 else print("NO")
# print(checking)