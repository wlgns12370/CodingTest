import heapq
from collections import deque
def solution(land, height):
    d=[[0,1],[-1,0],[0,-1],[1,0]]
    hq = []
    n = len(land)
    INF = 10001
    temp=10001
    s_p=[0,0]
    
    visited = [[False for _ in range(n)] for _ in range(n)]
    answer = 0
    
    def g(s):
        q = deque()
        q.append(s)
        visited[s[0]][s[1]]=True
        
        while q:
            
            x,y = q.popleft()
            
            for dx,dy in d:
                nx = x+dx
                ny = y+dy
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    
                    # 넘어갈 수 있는 경우
                    dif= abs(land[nx][ny] - land[x][y])
                    if dif<= height:
                        visited[nx][ny]=True
                        q.append([nx,ny])
                    else:
                        heapq.heappush(hq,[dif,nx,ny])
        
        return -1
            
    heapq.heappush(hq,[0,0,0])
    # 가중치 차이로 인해 못넘어가는 서브셋을 구하고 hq에서 다음 길을 선택하고 모두 방문여부를 visited로 확인
    while hq:
        
        cost,x,y = heapq.heappop(hq)
        
        if visited[x][y] == True:
            continue
        
        answer += cost
        
        g([x,y])
    
    return answer