import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 제한을 늘림


def dfs(graph, v, visited):
    visited[v] = True  # 현재 노드(v) 방문 처리

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N+1)
count = 0   # 연결 요소의 수

for i in range(1, N+1):
    if not visited[i]:
        dfs(graph, i, visited)
        count += 1      # dfs가 끝나면 연결 요소의 수 += 1

print(count)
