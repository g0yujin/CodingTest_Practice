import sys
import math

# 입력 받기
N = int(sys.stdin.readline())

# DP 테이블 초기화 (최댓값으로 초기화)
dp = [float('inf')] * (N + 1)

# 0은 0개의 제곱수로 표현 가능하므로 초기값 설정
dp[0] = 0

# 제곱수 리스트 구하기
for i in range(1, int(math.sqrt(N)) + 1):
    square = i * i
    for j in range(square, N + 1):
        dp[j] = min(dp[j], dp[j - square] + 1)

# 결과 출력
print(dp[N])
