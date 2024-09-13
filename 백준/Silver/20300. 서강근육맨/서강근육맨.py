import sys

N = int(sys.stdin.readline())
muscle = list(map(int, sys.stdin.readline().split()))
muscle.sort()

result = []
if N % 2 == 0:
    for i in range(N//2):
        result.append(muscle[i]+muscle[N-1-i])

elif N % 2 == 1:
    result.append(muscle[N-1])
    for i in range(N//2):
        result.append(muscle[i]+muscle[N-2-i])

print(max(result))