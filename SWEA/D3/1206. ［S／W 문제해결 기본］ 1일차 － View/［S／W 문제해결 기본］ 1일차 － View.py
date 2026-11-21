for idx in range(1,11):
  n = int(input())

  arr = list(map(int,input().split()))
  s = 2
  e = len(arr)-2

  answer = 0
  for i in range(s,e):
    # 높은 건물이 하나라도 더 있는 경우
    if not (arr[i] - arr[i - 2] >= 0 and
        arr[i] - arr[i - 1] >= 0 and
        arr[i] - arr[i + 1] >= 0 and
        arr[i] - arr[i + 2] >= 0):
      continue

    # 가장 높은 건물과 차이 구하기
    temp = -1
    temp = arr[i] - max(
        arr[i-2],arr[i-1],arr[i+1],arr[i+2]
    )
    answer+=temp

  print(f"#{idx} {answer}")
