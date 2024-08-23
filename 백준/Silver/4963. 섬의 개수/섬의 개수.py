import sys
from collections import deque


def island(graph, x, y):
    queue = deque()
    queue.append((x, y))  # 초기 위치


    while queue:
        x, y = queue.popleft()
        for dx, dy in (0, 1), (0, -1), (-1, 0), (1, 0), (-1, 1), (1, 1), (-1, -1), (1, -1):  # 상하좌우, 대각선 4개 포함
            nx, ny = x + dx, y + dy

            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
                graph[nx][ny] = 0  # 방문한 곳은 0으로
                queue.append((nx, ny))


while True:
    w, h = map(int, sys.stdin.readline().split())
    graph = []
    count = 0  # 섬의 개수

    if w == 0 and h == 0:   # 0 0 을 입력하면 종료
        break

    for _ in range(h):
        graph.append(list(map(int, sys.stdin.readline().split())))

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                island(graph, i, j)
                count += 1

    print(count)


