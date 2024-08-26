import sys

N, K = map(int, sys.stdin.readline().split())
count = 0
for h in range(0, N+1):
    for m in range(60):
        for s in range(60):
            time = str(h).zfill(2) + str(m).zfill(2) + str(s).zfill(2)
            if str(K) in time:
                count += 1

print(count)

