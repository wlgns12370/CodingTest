from itertools import permutations
from math import sqrt

def isPrime(number):
    flag = True
    if number == 1:
        return False
    for i in range(2,int(sqrt(number))+1):
        if number % i == 0:
            flag = False
            return flag
    return flag

def solution(numbers):
    # 숫자 골라내기
    arr = []
    for r in range(1,len(numbers)+1):
        for per in permutations(numbers,r):
            temp = ""
            for p in per:
                temp += p
            data = temp.lstrip('0')
            if data != '':
                i_data = int(data)
                if i_data not in arr:
                    arr.append(i_data)
    # 소수 검증
    answer = 0
    print(arr)
    for data in arr:
        if isPrime(data):
            answer += 1
    return answer