T = int(input())

for t in range(1, T+1):
    num = list(map(int, input().split()))

    num.sort()
    result = round(sum(num[1:9]) / 8)
    print(f'#{t} {result}')