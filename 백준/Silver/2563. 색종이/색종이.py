import sys

N = int(sys.stdin.readline())
arr = [[0] * 100 for _ in range(100)]

for i in range(N):
    x, y = map(int, sys.stdin.readline().split())

    for j in range(y-1, y+9):
        for k in range(x-1, x+9):
            if arr[k][j] == 0:
                arr[k][j] = 1
            else:
                pass


count_ones = sum(row.count(1) for row in arr)
print(count_ones)
