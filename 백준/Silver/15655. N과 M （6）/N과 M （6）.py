import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

for i in combinations(arr, M):
    print(*i)