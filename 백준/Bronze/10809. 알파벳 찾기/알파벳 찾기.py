import sys, string

S = sys.stdin.readline().rstrip()
lower = [i for i in string.ascii_lowercase]
result = []

for i in lower:
    if i in S:
        result.append(S.index(i))
    else:
        result.append(-1)

print(*result)