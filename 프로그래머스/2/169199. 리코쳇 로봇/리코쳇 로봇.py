from collections import deque

def solution(board):
    r_len = len(board)
    c_len = len(board[0])
    max_len = r_len * c_len
    
    k_len = max(r_len, c_len)
    
    s_pos = [0,0]
    e_pos = [0,0]
    for i in range(r_len):
        for j in range(c_len):
            if board[i][j] == 'R':
                s_pos[0] = i
                s_pos[1] = j
            
            elif board[i][j] == 'G':
                e_pos[0] = i
                e_pos[1] = j
    
    q = deque()
    q.append(s_pos + [0])
    answer = -1
    temp = max_len
    
    visited = set()
    visited.add((s_pos[0], s_pos[1]))
    
    while q:
        
        c_x, c_y, cnt = q.popleft()
        
        # 찾는 조건
        if c_x == e_pos[0] and c_y == e_pos[1]:
            answer = cnt
            break
        
        for dx,dy in ((0,1),(1,0),(0,-1),(-1,0)):
            # 왔던길에서 돌아가는거 자르면 효율성이 높아질 듯
            for k in range(1,k_len+1):
                f_x = c_x + dx*k
                f_y = c_y + dy*k
                
                # 벽 이거나 장애물을 만났다면 이전 값을 queue에 저장
                if not (0 <= f_x < r_len and 0 <= f_y < c_len) or board[f_x][f_y] == 'D':
                    stop = (c_x + dx * (k - 1), c_y + dy * (k - 1))
                    if stop not in visited:
                        visited.add(stop)
                        q.append([stop[0], stop[1], cnt + 1])
                    break
    
    return answer