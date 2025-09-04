import sys
from collections import deque

T = int(sys.stdin.readline())

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]

def bfs(i, j):
    queue = deque()
    queue.append((i, j))

    while queue:
        x, y = queue.popleft()

        if x == gx and y == gy:
            return 0

        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < I and 0 <= ny < I and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

                if nx == gx and ny == gy:
                    return graph[nx][ny]




for test_case in range(T):
    I = int(sys.stdin.readline()) # 체스판 한 변의 길이
    cx, cy = map(int, sys.stdin.readline().split())
    gx, gy = map(int, sys.stdin.readline().split())

    graph = [[0] * I for _ in range(I)]

    print(bfs(cx, cy))


