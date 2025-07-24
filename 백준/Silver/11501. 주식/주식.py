import sys

T = int(sys.stdin.readline())

for test_case in range(T):
    N = int(sys.stdin.readline())
    days = list(map(int, sys.stdin.readline().strip().split()))
    maxPrice = 0        # 최고 주가
    money = 0           # 총 이익

    for i in range(N-1, -1, -1):
        if days[i] > maxPrice:
            maxPrice = days[i]
        else:
            money += maxPrice - days[i]

    print(money)

