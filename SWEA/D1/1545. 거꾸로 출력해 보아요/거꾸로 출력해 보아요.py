n = int(input())

answer = []
for i in range(n, -1, -1):
    answer.append(i)

print(*answer)