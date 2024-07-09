T = int(input())
data = []

for i in range(T):
    A, B = map(int, input().split())
    data.append(A+B)

print(*data, sep='\n')