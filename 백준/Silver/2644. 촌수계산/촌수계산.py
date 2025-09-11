import sys
from collections import deque


def bfs(start, end):
    queue = deque()
    queue.append((start, 0))  # (노드, 거리)
    visited = [False] * (N + 1)
    visited[start] = True

    while queue:  # 큐가 비어있지 않을 때까지
        current_node, distance = queue.popleft()

        if current_node == end:
            return distance

        for next_node in graph[current_node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append((next_node, distance + 1))

    return -1  # 경로가 없을 경우


N = int(sys.stdin.readline())
A, B = map(int, sys.stdin.readline().split())
M = int(sys.stdin.readline())

graph = [[] for _ in range(N + 1)]
for i in range(M):
    X, Y = map(int, sys.stdin.readline().split())
    graph[X].append(Y)
    graph[Y].append(X)

result = bfs(A, B)
print(result)