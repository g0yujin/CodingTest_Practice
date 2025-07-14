import sys

num = sys.stdin.readline().strip()

answer = 0
idx = 0

while True:
    answer += 1

    for i in str(answer):
        if idx < len(num) and num[idx] == i:
            idx += 1

    if idx == len(num):
        break

print(answer)