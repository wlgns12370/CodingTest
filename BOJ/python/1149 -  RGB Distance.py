import sys
input = sys.stdin.readline

n = int(input())
dp = []

#min(previous_color) 이전집을 현재색을 제외한 나머지 색으로 칠한 최소 가격
dp.append((r,g,b))

for _ in range(1,n):
    current_r,current_g,current_b = [int(x) for x in input().split()]
    previous_r,previous_g,previous_b = dp[-1]
    r = current_r + min(previous_g,previous_b)
    g = current_g + min(previous_r,previous_b)
    b = current_b + min(previous_r,previous_g)
    dp.append((r,g,b))

print(dp)
print(min(dp[-1]))
