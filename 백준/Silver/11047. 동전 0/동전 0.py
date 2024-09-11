import sys

N, K = map(int, sys.stdin.readline().split())

coin = [int(sys.stdin.readline()) for i in range(N)]

cnt_coin = 0
for j in range(N-1, -1, -1):
    if coin[j] <= K:
        cnt_coin += K // coin[j]
        K = K % coin[j]

print(cnt_coin)
