import sys
input = sys.stdin.readline

cnt = 0
def promising(row):
    for col in range(row):
        # col is same & diagonal is same
        if board[row] == board[col] or (row - col == abs(board[row]-board[col])):
            return False
    return True

def check(row):
    global cnt
    if row == n:
        cnt += 1
        return

    for col in range(n):
        #재방문할 경우 Pass
        if visited[col] == 1:
            continue
        board[row] = col
        # 유망하지 않다면 가지치기
        if promising(row):
            visited[col] = 1
            check(row+1)
            visited[col] = 0

n = int(input())
board = [0] * (n)
visited = [0] * (n)
check(0)
print(cnt)
