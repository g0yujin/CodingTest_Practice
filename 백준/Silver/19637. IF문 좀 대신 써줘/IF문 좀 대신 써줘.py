import sys

# N: 칭호의 개수, M: 캐릭터들의 개수
N, M = map(int, sys.stdin.readline().split())
name = []
power = []

for i in range(N):
    n, p = sys.stdin.readline().strip().split()
    name.append(n)
    power.append(int(p))

for i in range(M):
    temp = int(sys.stdin.readline())

    # 이분 탐색
    left, right = 0, N-1
    result = 0

    while left <= right:
        mid = (left + right) // 2

        if power[mid] >= temp:
            result = mid
            right = mid-1

        else:
            left = mid + 1

    print(name[result])
