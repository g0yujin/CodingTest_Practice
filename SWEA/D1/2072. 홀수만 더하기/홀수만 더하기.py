T = int(input())

for test_case in range(1, T+1):
    nums = list(map(int, input().split()))
    result = 0

    for i in range(10):
        if nums[i] % 2 != 0:
            result += nums[i]

    print(f'#{test_case} {result}')