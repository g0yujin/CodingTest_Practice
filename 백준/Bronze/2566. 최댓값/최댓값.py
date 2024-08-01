import sys

mylist = []
index = []
for i in range(9):
    mylist.append(list(map(int, sys.stdin.readline().split())))

max_value = max(map(max, mylist))

for i in range(9):
    for j in range(9):
        if mylist[i][j] == max_value:
            index.extend([i+1, j+1])

print(max_value)
print(*index)