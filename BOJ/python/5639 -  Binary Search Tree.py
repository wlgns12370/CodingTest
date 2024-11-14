import sys
input = sys.stdin.readline
sys.setrecursionlimit(10001)

def post_order(start,end):
    if start > end:
        return
    # 모두 루트보다 작을때 처리하기 위해서 end + 1
    mid = end + 1
    for i in range(start+1,end+1):
        if pre_order[start] < pre_order[i]:
            mid = i
            break

    post_order(start+1,mid-1)
    post_order(mid,end)
    # 루트출력
    print(pre_order[start])

pre_order = []
while True:
    try:
        pre_order.append(int(input()))
    except:
        break

post_order(0,len(pre_order)-1)
