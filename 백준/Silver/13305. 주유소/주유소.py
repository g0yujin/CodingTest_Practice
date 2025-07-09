import sys

N = int(sys.stdin.readline())

road = list(map(int, sys.stdin.readline().strip().split()))
oil = list(map(int, sys.stdin.readline().strip().split()))

need = 0
cheap = sys.maxsize
for i in range(N-1):
    cheap = min(cheap, oil[i])
    need += cheap * road[i]
print(need)

