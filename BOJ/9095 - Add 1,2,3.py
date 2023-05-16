import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    memory = [0,1,2,4]
    for i in range(4,n+1):
        memory.append(memory[i-1]+memory[i-2]+memory[i-3])
    print(memory[n])
