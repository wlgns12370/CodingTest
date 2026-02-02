def solution(s):
    a = list(map(int,s.split()))
    s = str(min(a)) + " " + str(max(a))
    return s