import statistics

check = dict()
cnt = int(input())
numbers = [int(input()) for i in range(cnt)]
for i in numbers:
    check[i] = 0
for i in numbers:
    check[i] += 1
sort_check = dict(sorted(check.items()))
mode = statistics.mode(numbers)
validData = sort_check[mode]
k = 1
for i in sort_check:
    if sort_check[i] == validData:
        mode = i
        if k == 2:
            break
        k += 1

print(round(statistics.mean(numbers)))
print(statistics.median(numbers))
print(mode)
print(max(numbers) - min(numbers))
