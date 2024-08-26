import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
card = list(map(int, sys.stdin.readline().split()))
sum_list = []

for i in combinations(card, 3):
    if sum(i) <= M:
        sum_list.append(sum(i))

print(max(sum_list))


