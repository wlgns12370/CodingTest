import math
import sys
input = sys.stdin.readline()
def ccw(i, j, k):
    area2 = (j[0]-i[0]) * (k[1]-i[1]) - (j[1]-i[1]) * (k[0] - i[0])
    if area2 > 0: return True
    else: return False

def shellSort(a):
    N = len(a)
    h = 1
    while h < N / 3:
        h = 3 * h + 1

    numSwapsTotal = 0
    while h >= 1:        
        _, numSwaps = hInsertionSort(a, h)
        numSwapsTotal += numSwaps
        h = h // 3
    
    return a, numSwapsTotal

def hInsertionSort(a, h):
    numSwaps = 0  
    for i in range(h, len(a)):
        key = a[i]
        j = i - h
        while j >= 0 and a[j] > key:
            a[j + h] = a[j]
            numSwaps += 1
            j -= h
        a[j + h] = key
    return a, numSwaps

def grahamScan(points):
    p = min(points, key=lambda point: (point[1], -point[0]))
    tan_points = []
    angle_point_pairs=[]
    for point in points:
        if point == p:
            continue
        angle = math.atan2(point[1] - p[1], point[0] - p[0])
        dist = (point[0] - p[0])**2 + (point[1] - p[1])**2
        angle_point_pairs.append((angle, dist, point[0], point[1]))

    sorted_pairs, _ = shellSort(angle_point_pairs)
    tan_points = [(i, j) for _, _, i, j in sorted_pairs]

    stack = [p, tan_points[0]]
    
    for point in tan_points[1:]:
        while len(stack) >= 2 and not ccw(stack[-2], stack[-1], point):
            stack.pop()
        stack.append(point)

    return stack

n = int(input)

points = []
for _ in range(n):
    a,b = map(int,sys.stdin.readline().split())
    points.append((a,b))
print(len(grahamScan(points)))
