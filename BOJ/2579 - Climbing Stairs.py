import sys
input = sys.stdin.readline
memory = [0]
n = int(input())

for _ in range(n):
    data = int(input())
    memory.append(data)

g = [0,0]
h = [0,memory[1]]
for i in range(2,n+1):
    g.append(h[i-1]+memory[i])
    h.append(max(h[i-2],g[i-2])+memory[i])
print(max(g[n],h[n]))
