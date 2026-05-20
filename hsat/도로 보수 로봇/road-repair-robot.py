N, K = map(int, input().split())
positions = list(map(int, input().split()))
length=len(positions)

# l의 길이인 테이프 K개를 통해서 N개의 모든 구멍을 막을 수 있는가?
def is_ok(l):

    temp = 0
    cnt = 0
    for i in range(length):
        if i == 0:
            temp = positions[i] + l
            cnt +=1
        
        if temp > positions[i]:
            continue
        
        temp = positions[i] + l
        cnt+=1
    return cnt <= K

lo = 1
hi = max(positions)+1
answer = 0
while lo <= hi:
    mid = (lo+hi) // 2
    if is_ok(mid):
        answer = mid
        hi = mid-1
    else:
        lo = mid+1
    
print(answer)