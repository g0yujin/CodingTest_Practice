import sys

N = int(sys.stdin.readline())

num = []

for i in range(N):
    num.append(int(sys.stdin.readline()))

num.sort(reverse=True) # 내림차순 정렬

for j in range(N):
    num[j] = num[j] * (j+1)

print(max(num))