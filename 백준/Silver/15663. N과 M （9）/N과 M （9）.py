import sys
from itertools import permutations

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

result = []
for i in permutations(arr, M):
    result.append(i)

result = list(set(result))
result.sort()
for j in result:
    print(*j)

