import sys

N, K = map(int, sys.stdin.readline().split())
position = list(sys.stdin.readline().strip())

answer = 0

for i in range(N):
    if position[i] == 'P':
        for j in range(i-K, i+K+1):
            if 0 <= j < N and position[j] == 'H':
                answer += 1
                position[j] = '0'
                break


print(answer)
