import sys
input = sys.stdin.readline
n = int(input())
memory = [0,1]
for i in range(2,n+1):
    memory.append(memory[i-1]+memory[i-2])
print(memory[n])
