import sys
input = sys.stdin.readline
word = input().strip()

table = [-1 for _ in range(26)]

#아스키코드 a ~ z : 97 ~ 122
for data in word:
    if table[ord(data)-97] == -1:
        table[ord(data)-97] = word.index(data)

for result in table:
    print(result,end=" ")
