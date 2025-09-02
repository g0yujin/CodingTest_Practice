import sys
from collections import deque

N = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]
for i in range(N-1):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    graph[B].append(A)

parent = [0] * (N+1)
visited = [False] * (N+1)

queue = deque()
queue.append(1)

while queue:
    v = queue.popleft()
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            parent[i] = v
            queue.append(i)

for i in range(2, N+1):
    print(parent[i])

