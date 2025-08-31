import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().split())


graph = [[list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)] for _ in range(H)]

# 상하좌우위아래
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

queue = deque()

# 익은 토마토의 좌표를 q에 저장
for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 1:
                queue.append((i, j, k))


while queue:
    z, x, y = queue.popleft()

    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]

        if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H:
            if graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] = graph[z][x][y] + 1
                queue.append((nz, nx, ny))


answer = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 0:
                print(-1)
                exit()
            answer = max(answer, graph[i][j][k])

print(answer-1)


