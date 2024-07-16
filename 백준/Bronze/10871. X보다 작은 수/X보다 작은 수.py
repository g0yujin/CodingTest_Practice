import sys

N, X = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

small = []
for i in A:
    if i < X:
        small.append(i)

print(*small)