import sys

X = int(sys.stdin.readline())
stick = 64
count = 0

while X > 0:
    if stick > X:
        stick //= 2
    else:
        count += 1
        X -= stick


print(count)