import sys
from collections import deque


# 방문한 곳은 0 으로 바꾸기
def earthworm(graph, x, y):
    queue = deque()
    queue.append((x, y))   #초기 위치

    while queue:
        x, y = queue.popleft()

        for dx, dy in (0, 1), (0, -1), (-1, 0), (1, 0):
            nx, ny = x + dx, y + dy

            if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))

T = int(sys.stdin.readline())


for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split()) # M: 가로, N:세로, K:배추 위치
    ground = [[0] * N for _ in range(M)]
    count = 0

    for _ in range(K):
        a, b = map(int, sys.stdin.readline().split())
        ground[a][b] = 1

    for i in range(M):
        for j in range(N):
            if ground[i][j] == 1:
                earthworm(ground, i, j)
                count += 1

    print(count)




