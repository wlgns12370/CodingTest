import sys
input = sys.stdin.readline

while True:
    data = input()
    if data == "0": break
    print('yes') if data == data[::-1] else print('no')
