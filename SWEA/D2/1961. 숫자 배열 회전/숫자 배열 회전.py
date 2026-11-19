import copy

t = int(input())

z = []
for idx in range(1,t+1):
  print(f"#{idx}")
  n = int(input())

  arr = [[] for _ in range(n)]

  result = [[] for _ in range(n)]

  matrix = []
  change_matrix = [[0 for _ in range(n)] for _ in range(n)]

  for _ in range(n):
    data = list(map(int, input().split()))
    matrix.append(data)

  for k in range(3):
    for i in range(n):
      for j in range(n):
        change_matrix[j][n - i - 1] = matrix[i][j]

    for i in range(n):
      temp = ""
      for j in range(n):
        temp += str(change_matrix[i][j])

      result[i].append(temp)

    matrix = copy.deepcopy(change_matrix)
  for row in result:
    print(" ".join(row))