import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

# 2차원 리스트 생성
graph = []
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))


#    상  하  좌  우
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 미로 찾기는 BFS!!
def bfs(x, y):
    queue = deque()
    queue.append((x, y))   # 초기 위치

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]

            if 0 <= next_x < N and 0 <= next_y < M:  # 범위 확인
                if graph[next_x][next_y] == 1:       # 경로 확인
                    queue.append((next_x, next_y))
                    graph[next_x][next_y] = graph[x][y] + 1  # value 자체를 이동 횟수로 사용

    return graph[N-1][M-1]

print(bfs(0,0))




