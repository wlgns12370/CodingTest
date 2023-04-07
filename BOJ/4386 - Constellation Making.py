import math
import sys

def hypotenuse(x1,y1,x2,y2):
  result = math.sqrt((math.pow(abs(x2-x1),2)) + (math.pow(abs(y2-y1),2)))
  return result

def find_parent(node):
  if parents[node] == node:
    return node
  else:
    parents[node] = find_parent(parents[node])
    return parents[node]

def UNION(node,node2):
  node_parent = find_parent(node)
  node2_parent = find_parent(node2) 

  if node_parent >= node2_parent:
    parents[node2_parent] = node_parent
  else:
    parents[node_parent] = node2_parent

n = int(sys.stdin.readline())
star = []
tree = []
k = 0
cnt = 0
distance = 0.0

for _ in range(n):
  x,y = map(float,sys.stdin.readline().split())
  star.append([x,y,k])
  k+=1    

for i in range(n):
  for j in range(i+1,n):
    tree.append([star[i],star[j],hypotenuse(star[i][0],star[i][1],star[j][0],star[j][1])])
tree.sort(key = lambda x: x[2])

parents = [x for x in range(k)]

for x,y,value in tree:
  if find_parent(x[2]) != find_parent(y[2]):
    UNION(x[2],y[2])
    distance += value 
    cnt += 1
  if cnt >= n-1:
    break

print(distance)
