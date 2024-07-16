import sys

N, M = map(int, sys.stdin.readline().split())
basket = []
for x in range(1,N+1):
    basket.append(x)

for y in range(M):
    i, j = map(int, sys.stdin.readline().split())
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1]

print(*basket)