import sys
from itertools import permutations

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

for i in permutations(arr, M):
    print(*i)