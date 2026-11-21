t = int(input())

def dfs(idx, s, c):
  global answer
  # 칼로리가 넘은 경우
  if c > l:
    return
  # 종료 조건
  if idx == n:
    answer = max(answer, s)
    return

  # 선택하는 경우
  dfs(idx+1, s+score[idx], c+cal[idx])
  # 선택하지 않는 경우
  dfs(idx+1, s, c)

for i in range(1,t+1):
  n,l = map(int, input().split())
  score = []
  cal = []
  answer = 0
  for _ in range(n):
    s,c = map(int, input().split())
    score.append(s)
    cal.append(c)

  dfs(0,0,0)
  print(f"#{i} {answer}")
