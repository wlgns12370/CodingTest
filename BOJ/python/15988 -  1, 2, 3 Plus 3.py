import sys
input = sys.stdin.readline
div = 1_000_000_009
max_len = 1_000_001
result = []
memory = [0,1,2,4]
for i in range(4,max_len):
    memory.append((memory[i-1]%div) + (memory[i-2]%div) + (memory[i-3]%div))

t = int(input())
for _ in range(t):
    n = int(input())
    result.append(memory[n]%div)    

for data in result:
    print(data)
