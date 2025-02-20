from itertools import combinations

arr = [1, 2, 3, 4]
for comb in combinations(arr, 2):  # 길이 2짜리 조합
    print(comb)