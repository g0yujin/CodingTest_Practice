import itertools
import sys
from itertools import combinations_with_replacement

N, M = map(int, sys.stdin.readline().split())
arr = list(set(map(int, sys.stdin.readline().split()))) # 미리 중복 제거
arr.sort()

nums = itertools.product(arr, repeat=M)
result = []

if M == 1:
    for i in arr:
        print(i)
else:
    for combination in combinations_with_replacement(arr, M):
        print(*combination)




