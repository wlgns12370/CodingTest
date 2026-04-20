import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
num = [int(input()) for _ in range(n)]

seg_tree = [0 for _ in range(4*n)]

def build_tree(x,left,right):
    if left == right:
        seg_tree[x] = num[left]
        return seg_tree[x]
    mid = (left + right)//2
    left_value = build_tree(2*x,left,mid)
    right_value = build_tree(2*x+1,mid+1,right)
    seg_tree[x] = left_value + right_value
    return seg_tree[x]

build_tree(1,0,n-1)

def find_tree(b,c,x,left,right):
    if c < left or right < b:
        return 0
    if b <= left and right <=c:
        return seg_tree[x]
    mid = (left + right)//2
    left_value = find_tree(b,c,x*2,left,mid)
    right_value = find_tree(b,c,x*2+1,mid+1,right)
    return left_value + right_value

def update_tree(x,left,right,idx,val):
    if left == right == idx:
        seg_tree[x] = val
        return
    if idx < left or right < idx:
        return
    
    mid = (left + right)//2
    update_tree(x*2,left,mid,idx,val)
    update_tree(x*2+1,mid+1,right,idx,val)
    
    seg_tree[x] = seg_tree[x*2] + seg_tree[x*2+1]
    
for _ in range(m+k):
    a,b,c = map(int,input().split())
    if a == 1:
        update_tree(1,0,n-1,b-1,c)
    else:
        s = find_tree(b-1,c-1,1,0,n-1)
        print(s)