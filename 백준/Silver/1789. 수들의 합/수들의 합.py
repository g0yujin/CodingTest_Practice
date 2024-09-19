import sys

S = int(sys.stdin.readline())

sum_list = []
result = 0
i = 1

while True:
    if i + 1 > S - (result+i):
        break

    result += i
    sum_list.append(i)
    i += 1

print(len(sum_list)+1)