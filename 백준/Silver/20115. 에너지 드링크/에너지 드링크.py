import sys

N = int(sys.stdin.readline())
amount = list(map(int,sys.stdin.readline().split()))

amount.sort(reverse=True)  # 오름차순
result = amount[0]

for i in range(1, N):
    result += amount[i] / 2

print(result)