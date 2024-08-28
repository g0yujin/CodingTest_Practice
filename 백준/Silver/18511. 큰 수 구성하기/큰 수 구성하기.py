import sys
from itertools import product

N, K = map(int, sys.stdin.readline().split())
K_list = list(map(str, sys.stdin.readline().split()))
N_length = len(str(N))

# 중복 허용 = 중복 순열 사용 (product)
while True:
    temp = list(product(K_list, repeat=N_length))
    result = []
    for i in temp:
        if N >= int("".join(i)):
            result.append(int("".join(i)))
    if len(result) > 0:
        print(max(result))
        break
    else:
        N_length -= 1