N = int(input())

answer = [1]
num = 1
for i in range(N):
    num *= 2
    answer.append(num)

print(*answer)