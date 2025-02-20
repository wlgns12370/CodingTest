import  sys
input = sys.stdin.readline

answer = 0
n,k = map(int,input().split())
known = ['a','n','t','i','c']
# 배워야 할 단어
un_arr = [input().rstrip() for _ in range(n)]

def dfs(start, depth):
    global  answer

    if depth == k:
        cnt = 0
        for w in un_arr:
            flag = True
            for d in w:
                if key[(ord(d) - ord('a'))] == 0:
                    flag = False
                    break
            if flag:
                cnt += 1
        answer = max(answer,cnt)
        return

    for i in range(start,26):
        if key[i] == 0:
            key[i] = 1
            dfs(i,depth+1)
            key[i] = 0

if k < 5:
    print(0)
elif k == 26:
    print(n)
else:
    key = [0 for _ in range(26)]
    # 무조건 배우는 단어
    for data in known:
        key[(ord(data)-ord('a'))] = 1

    dfs(0,5)
    print(answer)