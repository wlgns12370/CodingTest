answer = -1
def dfs(hp, cnt, dungeons, min_hp):
    global answer
    answer = max(answer, cnt)

    if hp < min_hp:
        return

    for i in range(l):
        if dungeons[i][0] <= hp and visited[i] == False:
            visited[i] = True
            dfs(hp-dungeons[i][1], cnt+1, dungeons,min_hp)
            visited[i] = False

def solution(k, dungeons):
    global l, visited
    l = len(dungeons)
    min_hp = min([row[0] for row in dungeons])
    visited = [False for _ in range(l)]
    dfs(k,0,dungeons,min_hp)
    print(answer)
    return answer