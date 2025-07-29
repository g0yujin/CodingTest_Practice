import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())

    graph[a].append(b)
    graph[b].append(a)

# 작은 번호부터 방문
for i in range(N+1):
    graph[i].sort()

# dfs
def dfs(v, visited):
    visited.append(v)
    for j in graph[v]:
        if j not in visited:
            dfs(j, visited)

    return visited


# bfs
def bfs(v):
    visited = []
    queue = deque([v])
    visited.append(v)

    while queue:
        current = queue.popleft()

        for j in graph[current]:
            if j not in visited:
                queue.append(j)
                visited.append(j)

    return visited

visited = []
visited_dfs = dfs(V, visited)
visited_bfs = bfs(V)

print(*visited_dfs)
print(*visited_bfs)
