T = int(input())

for testcase in range(1, T+1):
    N, M = map(int, input().split())
    num = []
    result = []
    for i in range(N):
        temp = list(map(int, input().split(' ')))
        num.append(temp)


    for i in range(N-M+1):
        j = 0
        while j+M-1 <= N-1:
            hap = 0
            for k in range(i, i+M):
                hap += sum(num[k][j:j+M])

            j += 1
            result.append(hap)


    print(f'#{testcase} {max(result)}')

