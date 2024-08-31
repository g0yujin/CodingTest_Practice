import sys
from itertools import combinations

# N: 회원 수, M: 치킨 종류
N, M = map(int, sys.stdin.readline().split())

like = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

sum_list = []
for a, b, c in combinations(range(M), 3):    # 조합 사용
    temp_sum = 0
    for i in range(N):
        temp_sum += max(like[i][a], like[i][b], like[i][c])
        sum_list.append(temp_sum)

print(max(sum_list))
