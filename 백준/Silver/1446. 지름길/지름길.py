import sys

N, D = map(int, sys.stdin.readline().split())
expressway = []

for i in range(N):
    expressway.append(list(map(int, sys.stdin.readline().strip().split())))

expressway.sort()

dp = [i for i in range(D+1)]

k=0

for i in range(D+1):
    dp[i] = min(dp[i-1]+1, dp[i])

    while k < N:
        if i == expressway[k][0]:
            if expressway[k][1] <= D:
                dp[expressway[k][1]] = min(dp[i] + expressway[k][2], dp[expressway[k][1]])
            k += 1

        else: break
print(dp[D])