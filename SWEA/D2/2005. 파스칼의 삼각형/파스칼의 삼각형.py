T = int(input())


for i in range(1, T+1):
    N = int(input())
    print(f'#{i}')

    result = [[1]]
    if N > 1:
        for j in range(2, N+1):
            temp = []
            for k in range(j):
                if k == 0 or k == j-1:
                    temp.append(1)
                else:
                    temp.append(sum(result[j-2][k-1:k+1]))

            result.append(temp)

    for i in range(len(result)):
        print(*result[i])
