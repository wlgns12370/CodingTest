import sys
input = sys.stdin.readline

set_seq = []
def DFS(cnt):

    #M개 고른 수열
    if cnt == M:
        print(*set_seq)
        return
    
    for i in range(N):
        if visited[i] == False:
            visited[i] = True
            set_seq.append(seq[i])
            DFS(cnt+1)
            set_seq.pop()
            for clear in range(i+1,N):
                visited[clear] = False
    

N,M = map(int,input().split())
seq = [i for i in range(1,N+1)]
visited = [False] * (N)

DFS(0)
