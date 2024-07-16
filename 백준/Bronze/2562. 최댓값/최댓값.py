A = []
for i in range(9):
    N = int(input())
    A.append(N)
big = max(A)
print(big)
print(A.index(big)+1)