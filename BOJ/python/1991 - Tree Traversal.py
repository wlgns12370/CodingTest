import sys

n = int(sys.stdin.readline())
tree = {}


def preorder(node):
    if node != '.':
        print(node, end="")
        preorder(tree[node][0])
        preorder(tree[node][1])


def inorder(node):
    if node != '.':
        inorder(tree[node][0])
        print(node, end="")
        inorder(tree[node][1])


def postorder(node):
    if node != '.':
        postorder(tree[node][0])
        postorder(tree[node][1])
        print(node, end="")


for i in range(n):
    data = list(map(str, sys.stdin.readline().split()))
    tree[data[0]] = data[1], data[2]

preorder('A')
print()
inorder('A')
print()
postorder('A')
