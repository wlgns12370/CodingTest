import sys
input = sys.stdin.readline

n = int(input())
coordinates = []
for _ in range(n):
    x,y = map(int,input().split())
    coordinates.append((x,y))

#sort key 우선순위
coordinates.sort(key = lambda x : (x[0],x[1]))

for data in coordinates:
    print(*data)
