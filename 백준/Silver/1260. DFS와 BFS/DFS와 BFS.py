import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort()

visited_dfs = [False] * (N+1)   # dfs 방문 기록
visited_bfs = [False] * (N+1)   # bfs 방문 기록

def dfs(graph, visited_dfs, V):
    visited_dfs[V] = True
    print(V, end=' ')

    for i in graph[V]:
        if not visited_dfs[i]:
            dfs(graph, visited_dfs, i)


def bfs(graph, visited_bfs, V):
    queue = deque([V])
    visited_bfs[V] = True

    while queue:
        V = queue.popleft()
        print(V, end=' ')

        for i in graph[V]:
            if not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i] = True



dfs(graph, visited_dfs, V)
print()
bfs(graph, visited_bfs, V)