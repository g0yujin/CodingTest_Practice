import sys

chess = [1, 1, 2, 2, 2, 8]
have = list(map(int, sys.stdin.readline().split()))

find = []
for ci,hi in zip(chess,have):
    find.append(ci-hi)

print(*find)