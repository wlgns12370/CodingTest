import sys
input = sys.stdin.readline

n,k = map(int,input().split())

bag = [0 for _ in range(k+1)]
bag[0] = 1
coin = []
for _ in range(n):
    coin.append(int(input()))

for i in range(n):
    for j in range(k+1):
        
        #동전을 넣을 수 있는 경우
        if coin[i] <= j:
            bag[j] += bag[j-coin[i]]

        #동전을 넣을 수 없는 경우
        else:
            continue

print(bag[k])
