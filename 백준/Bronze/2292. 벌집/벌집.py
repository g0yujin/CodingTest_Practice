import sys

N = int(sys.stdin.readline())

num = 1
i = 1
while True:
    if num >= N:
        print(i)
        break
    else:
        num = num + (6 * i)
    i += 1

