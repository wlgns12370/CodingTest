import sys
input = sys.stdin.readline

n = int(input())
memory = [1,2]
for i in range(2,n):
    memory.append((memory[i-1] + memory[i-2]) % 15746)
print(memory[n-1])
