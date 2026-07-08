def solution(n):
    arr = [0]*2000
    arr[0] = 1
    arr[1] = 2
    
    for i in range(2, n):
        arr[i] = (arr[i-1] + arr[i-2])%1234567
    
    return arr[n-1]