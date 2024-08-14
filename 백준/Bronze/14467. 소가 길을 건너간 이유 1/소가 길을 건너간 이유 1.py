import sys

N = int(sys.stdin.readline())
cow = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
count = 0

for i in range(N):
    num, position = map(int, sys.stdin.readline().split())
    if cow[num-1] == 3:
        cow[num-1] = position

    elif cow[num-1] == 0 and position == 1:
        cow[num-1] = position
        count += 1

    elif cow[num-1] == 1 and position == 0:
        cow[num-1] = position
        count += 1

print(count)