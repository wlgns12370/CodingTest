import sys
input = sys.stdin.readline
INF = sys.maxsize
n = int(input())
memory = [0,0,1,1]
for i in range(4,n+1):
    node = (memory[i//3] if i % 3 == 0 else INF)
    node2 = (memory[i//2]  if i % 2 == 0 else INF)
    node3 = memory[i-1]
    memory.append(min(node,node2,node3) + 1)
print(memory[n])
