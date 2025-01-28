def solution(s):
    total = 0
    i = 0
    while True:
        cnt = s.count("0")
        if s == "1":
            break
        total += cnt
        i += 1
        s = bin(s.count("1"))[2:]
    answer = [i,total]
    return answer