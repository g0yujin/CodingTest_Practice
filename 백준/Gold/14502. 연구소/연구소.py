import copy
import sys
from itertools import combinations
from collections import deque

N, M = map(int, sys.stdin.readline().split())

graph = []
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().strip().split())))


# 바이러스와 빈공간 찾기
virus = []
empty_space = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            empty_space.append((i,j))
        elif graph[i][j] == 2:
            virus.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, virus):
    queue = deque(virus)

    while queue:

        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                graph[nx][ny] = 2
                queue.append((nx, ny))






answer = 0
# 가능한 모든 조합으로 벽 설치해서 최대 안전 영역 개수 구하기
for wall_xy in combinations(empty_space,3):
    temp_graph = copy.deepcopy(graph)

    for x, y in wall_xy:
        temp_graph[x][y] = 1

    bfs(temp_graph, virus)

    # 안전지대 개수 계산
    count = 0
    for i in range(N):
        for j in range(M):
            if temp_graph[i][j] == 0:
                count += 1

    answer = max(answer, count)


print(answer)
