from collections import deque
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(x,y,group,r,c,table,v):
    block = deque()
    block.append((x,y))
    # v는 방문 해야하는 체크 변수 xor을 활용하여 1->0 0->1
    table[x][y] = v^1

    while block:
        px, py = block.popleft()
        group.append([px,py])
        for  k in range(4):
            cx = px + dx[k]
            cy = py + dy[k]
            if 0 <= cx < r and 0 <= cy < c and table[cx][cy] == v:
                table[cx][cy] = v^1
                block.append((cx,cy))

def rotate(block):
    n = len(block)
    m = len(block[0])
    result = [[0 for i in range(n)] for j in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-1-i] = block[i][j]
    return result

def cnt(block):
    result = 0
    for i in range(len(block)):
        for j in range(len(block[0])):
            if block[i][j] == 1:
                result += 1
    return result


def solution(game_board, table):
    # 테이블에서 블록을 추출하기 블록을 0,0 기준으로 바꿔서 N*M blocks에 저장하기
    blocks = []
    r = len(game_board)
    c = len(game_board[0])

    for i in range(r):
        for j in range(c):
            if table[i][j] == 1:
                table_group = []
                bfs(i,j,table_group,r,c,table,1)

                # group 위치 0,0 기준으로 변경
                min_x = min(table_group, key=lambda x:x[0])[0]
                min_y = min(table_group, key=lambda x:x[1])[1]

                for k in range(len(table_group)):
                    table_group[k][0] -= min_x
                    table_group[k][1] -= min_y

                # 블록을 matrix에 담기
                max_x = max(table_group, key=lambda x:x[0])[0] + 1
                max_y = max(table_group, key=lambda x:x[1])[1] + 1
                matrix = [[0 for i in range(max_y)] for j in range(max_x)]
                for x,y in table_group:
                    matrix[x][y] = 1

                blocks.append(matrix)

    # 보드를 돌면서 빈공간을 추출해 0,0 기준으로 바꿔서 N*M empty_list에 저장하기
    empty = []

    for i in range(r):
        for j in range(c):
            if game_board[i][j] == 0:
                board_group = []
                bfs(i,j,board_group,r,c,game_board,0)

                # group 위치 0,0 기준으로 변경
                min_x = min(board_group, key=lambda x:x[0])[0]
                min_y = min(board_group, key=lambda x:x[1])[1]

                for k in range(len(board_group)):
                    board_group[k][0] -= min_x
                    board_group[k][1] -= min_y

                # 블록을 matrix에 담기
                max_x = max(board_group, key=lambda x:x[0])[0] + 1
                max_y = max(board_group, key=lambda x:x[1])[1] + 1
                matrix = [[0 for i in range(max_y)] for j in range(max_x)]
                for x,y in board_group:
                    matrix[x][y] = 1

                empty.append(matrix)

    answer = 0
    # 찾은 도형이랑 블록 리스트의 블록을 돌리면서 찾음
    for board in empty:
        for block in blocks:
            #넓이가 같은 경우 -> 90도 회전 하는 도형을 비교함
            if len(board)*len(board[0]) == len(block)*len(block[0]):
                temp = block
                flag = False
                for i in range(4):
                    if board == temp:
                        #하나의 값을 -1,-2로 만들어서 비교해도 안 맞게 만들기
                        flag = True
                        answer += cnt(block)
                        board[0][0] = -1
                        block[0][0] = -2
                        break
                    else:
                        temp = rotate(temp)
                if flag:
                    break
    return answer