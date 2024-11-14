import sys
input = sys.stdin.readline

data = input()

flag = 0
for i in range(len(data)):
    if data[i] == "-":
        flag = i
        break

if flag != 0:
    front = list(map(int, filter(None,data[:flag].split("+"))))
    back = list(map(int, filter(None, data[flag:].replace("-","+").split("+"))))
    print(sum(front)-sum(back))
    
else:
    arr = list(map(int, data.split("+")))
    print(sum(arr))