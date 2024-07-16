import sys

N, M = map(int, input().split())

bucket = [0] * N

for i in range(M):
    I, J, K = map(int, sys.stdin.readline().split())
    for x in range(I,J+1):
        bucket[x-1] = K

print(*bucket)