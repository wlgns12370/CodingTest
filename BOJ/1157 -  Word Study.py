word = input()
Up_word = word.upper()
word_list = list(set(Up_word))

cnt = []

for data in word_list:
    count = Up_word.count(data)
    cnt.append(count)

print("?") if cnt.count(max(cnt)) > 1 else print(word_list[cnt.index(max(cnt))])
