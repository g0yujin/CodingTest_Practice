import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
result = list(set(combinations(arr, M)))

result.sort()
for i in result:
    print(*i)