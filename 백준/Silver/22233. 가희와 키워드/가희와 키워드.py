import sys

N, M = map(int, sys.stdin.readline().split())

keyword = set()
for i in range(N):
    word = sys.stdin.readline().strip()
    keyword.add(word)


for i in range(M):
    title = sys.stdin.readline().strip().split(',')

    for j in title:
        if j in keyword:
            keyword.remove(j)

    print(len(keyword))
