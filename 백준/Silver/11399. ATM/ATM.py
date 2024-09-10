import sys

N = int(sys.stdin.readline())
time = list(map(int, sys.stdin.readline().strip().split()))

time.sort()

result = 0
for i in range(N):
    result += sum(time[0:i+1])


print(result)