import sys

T = int(sys.stdin.readline())

result = []

for i in range(T):
    word = list(sys.stdin.readline().strip())
    result.append(word[0] + word[-1])

print(*result, sep='\n')