import sys
input = sys.stdin.readline

dy = [-1,0,1,0]
dx = [0,1,0,-1]
n,m = map(int,input().split())
current_row,current_col,d = map(int,input().split())
room = [list(map(int,input().split())) for _ in range(n)]

room[current_row][current_col] = 2
cnt = 1
# 0 빈칸 1 벽 2 청소완료
while 1:

    IsClean = False

    for i in range(4):
        # 반시계 방향으로 90도 회전
        d = (d + 3) % 4
        robot_position_row = current_row + dy[d]
        robot_position_col = current_col + dx[d]
        if 0 <= robot_position_row < n and 0 <= robot_position_col < m:
            if room[robot_position_row][robot_position_col] == 0:
                # 청소
                room[robot_position_row][robot_position_col] = 2
                current_row = robot_position_row
                current_col = robot_position_col
                cnt += 1
                IsClean = True
                break
    
    # 뒤로가기
    if IsClean == False:
        robot_position_row = current_row - dy[d]
        robot_position_col = current_col - dx[d]
        #뒤로갔는데 벽이 아님
        if 0 <= robot_position_row < n and 0 <= robot_position_col < m and room[robot_position_row][robot_position_col] != 1:
            current_row = robot_position_row
            current_col = robot_position_col
        else:
            print(cnt)
            break
