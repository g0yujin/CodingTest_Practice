N = int(input())

answer = []
for i in range(1, N+1):
    if N % i == 0:
        answer.append(i)
print(*answer)
