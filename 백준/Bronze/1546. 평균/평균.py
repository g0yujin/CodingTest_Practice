N = int(input())
score = list(map(int, input().split()))
M = max(score)
avg = 0

for i in score:
    avg += i / M * 100

print(avg/N)
