import sys

N = int(sys.stdin.readline())
request = list(map(int, sys.stdin.readline().strip().split()))
max_cost = int(sys.stdin.readline())

# 모든 요청 배정 가능
if sum(request) <= max_cost:
    print(max(request))

# 모든 요청 배정 불가능
else:
    left = 1
    right = max(request)
    answer = 0
    while left <= right:
        count = N
        total = 0

        mid = (left + right) // 2

        for i in range(N):
            if request[i] <= mid:
                total += request[i]
                count -= 1

        # 더 큰 값 찾기
        if total + (mid * count) > max_cost:
            right = mid - 1
        else:
            answer = mid
            left = mid + 1
            
    print(answer)
