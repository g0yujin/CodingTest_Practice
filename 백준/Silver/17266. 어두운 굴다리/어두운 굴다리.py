import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
position = list(map(int,sys.stdin.readline().split()))

height = 0

if M == 0:
    height = max(position[0], N-position[0])
else:
    height = position[0]

    for i in range(M-1):
        temp = (position[i+1] - position[i]) // 2 + (position[i+1] - position[i]) % 2
        height = max(height, temp)

    height = max(height, N-position[M-1])
print(height)
