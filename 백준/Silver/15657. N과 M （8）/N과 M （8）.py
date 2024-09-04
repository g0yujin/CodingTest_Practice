import sys
from itertools import combinations_with_replacement

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

for i in combinations_with_replacement(arr, M):
    print(*i)