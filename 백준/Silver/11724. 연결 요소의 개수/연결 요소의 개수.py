import sys

N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for i in range(M):
    U, V = map(int, sys.stdin.readline().split())
    graph[U].append(V)
    graph[V].append(U)

def dfs(v):
    visited[v] = 1

    for j in graph[v]:
        if visited[j] == 0:
            dfs(j)

answer = 0

for i in range(1, N+1):
    if visited[i] == 0:
        dfs(i)
        answer += 1



print(answer)




