import sys

N = int(sys.stdin.readline())
link = int(sys.stdin.readline())

arr = [[] for _ in range(N+1)]
answer = []
for i in range(link):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)


def dfs(v):
    answer.append(v)
    for j in arr[v]:
        if j in answer:
            continue
        else:
            if j != 1:
                answer.append(j)
                dfs(j)


for i in arr[1]:
    dfs(i)

print(len(set(answer)))