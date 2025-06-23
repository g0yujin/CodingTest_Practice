import sys

H, W, N, M = map(int, sys.stdin.readline().split())

if W % (M + 1) == 0:
    row = W // (M + 1)
else:
    row = (W // (M + 1)) + 1

if H % (N + 1) == 0:
    column = H // (N + 1)
else:
    column = (H // (N + 1)) + 1

print(row * column)