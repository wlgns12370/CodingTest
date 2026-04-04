import sys
input = sys.stdin.readline

n,k = map(int,input().split())
memory = [[0]*(k+1) for _ in range(n+1)]

bag = [(0,0)] 
for _ in range(n):
    w,v = map(int,input().split())
    bag.append((w,v))

for j in range(1,n+1):
    w,v = bag[j]
    for i in range(1,k+1):
        # weight가 더 큰 경우
        if w > i:
            memory[j][i] = memory[j-1][i]
        else:
            memory[j][i] = max(memory[j-1][i] , memory[j-1][i-w]+v)

print(memory[n][k])