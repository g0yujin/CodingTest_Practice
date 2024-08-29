import sys
from itertools import permutations

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
num = [sys.stdin.readline().strip()for _ in range(n)]
result = []

for i in permutations(num,k):
    result.append("".join(i))

print(len(set(result)))