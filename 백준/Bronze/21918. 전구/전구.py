import sys

N, M = map(int, sys.stdin.readline().split())
s = list(map(int, sys.stdin.readline().split()))

for i in range(M):
    a, b, c = map(int, sys.stdin.readline().split())

    if a == 1:
        s[b-1] = c

    elif a == 2:
        for j in range(b-1, c):
            if s[j] == 1:
                s[j] = 0
            else:
                s[j] = 1

    elif a == 3:
        for j in range(b-1, c):
            s[j] = 0

    elif a == 4:
        for j in range(b-1, c):
            s[j] = 1

print(*s)