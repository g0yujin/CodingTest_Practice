import sys
from collections import deque

M, N = map(int,sys.stdin.readline().strip().split())

graph = []
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))


tomato = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            tomato.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 토마토가 있는 곳
queue = deque()
for r, c in tomato:
    queue.append((r, c, 0))

max_day = 0

while queue:
    x, y, day = queue.popleft()
    max_day = max(max_day, day)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N  and 0 <= ny < M and graph[nx][ny] == 0:
            queue.append((nx, ny, day+1))
            graph[nx][ny] = 1

complete = True

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            complete = False

if complete:
    print(max_day)
else:
    print(-1)


