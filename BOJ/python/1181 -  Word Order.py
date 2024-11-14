words = []
n = int(input())
for _ in range(n):
    word = input()
    words.append(word)
set_words = list(set(words))

set_words.sort()
set_words.sort(key = lambda x : len(x))

for data in set_words:
    print(data)
