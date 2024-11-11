T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))
    cost = 0
    max_price = price[-1]

    for i in range(N-2, -1, -1):  # N-1부터 시작해 0까지 순회
        if price[i] < max_price:
            cost += (max_price - price[i])
        else:
            max_price = price[i]

    print(f'#{test_case} {cost}')
