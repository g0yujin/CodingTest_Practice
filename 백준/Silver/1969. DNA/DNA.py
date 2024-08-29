import sys

N, M = map(int, sys.stdin.readline().split())
HD = []
for i in range(N):
    HD.append(list(sys.stdin.readline().strip()))

count, HD_sum = 0, 0
result =''

for i in range(M):
    A, C, G, T = 0, 0, 0, 0

    for j in range(N):
        if HD[j][i] == 'A':
            A += 1
        elif HD[j][i] == 'G':
            G += 1
        elif HD[j][i] == 'T':
            T += 1
        elif HD[j][i] == 'C':
            C += 1

    if max(A, C, G, T) == A:
        result += 'A'
        HD_sum += C + G + T
    elif max(A, C, G, T) == C:
        result += 'C'
        HD_sum += A + G + T
    elif max(A, C, G, T) == G:
        result += 'G'
        HD_sum += A + C + T
    elif max(A, C, G, T) == T:
        result += 'T'
        HD_sum += A + C + G

print(result)
print(HD_sum)

