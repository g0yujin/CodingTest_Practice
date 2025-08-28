import sys

T = int(sys.stdin.readline())

dp = [1] * 10001

for i in range(2, 10001):
    dp[i] += dp[i - 2]

for i in range(3, 10001):
    dp[i] += dp[i - 3]

for test_case in range(T):
    N = int(sys.stdin.readline())
    print(dp[N])

