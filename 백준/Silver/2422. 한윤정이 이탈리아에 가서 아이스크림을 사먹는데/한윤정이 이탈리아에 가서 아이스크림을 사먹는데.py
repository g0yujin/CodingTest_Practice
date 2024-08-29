import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())

# 3가지를 고르는 아이스크림 조합 (중복 허용 x)
# 모든 가능한 조합을 리스트가 아닌 set으로 저장
result = set(combinations(range(1, N+1), 3))


for _ in range(M):          # 먹으면 안되는 조합 삭제
    a, b = map(int, sys.stdin.readline().split())

    for c in range(1, N+1):
        if c != a and c != b:
            combo = tuple(sorted((a, b, c)))
            if combo in result:
                result.remove(combo)


print(len(result))