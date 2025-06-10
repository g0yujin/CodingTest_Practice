import sys

N, K = map(int, sys.stdin.readline().split())
answer = []

for i in range(1, N+1):
    if N % i == 0:
        answer.append(i)

if K > len(answer):
    print(0)
else:
    print(answer[K-1])
