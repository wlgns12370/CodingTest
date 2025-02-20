from itertools import permutations
import  sys
input = sys.stdin.readline

arr = [1, 2, 3]
for perm in permutations(arr):  # 기본값은 len(arr)
    print(perm)
for perm in permutations(arr, 2):  # 길이 2짜리 순열
    print(perm)