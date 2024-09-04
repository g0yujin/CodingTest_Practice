import sys
from itertools import product

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

for i in product(arr, repeat=M):
    print(*i)