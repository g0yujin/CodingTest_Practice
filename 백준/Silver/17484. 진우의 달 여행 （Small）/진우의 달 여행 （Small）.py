import sys

N, M = map(int ,sys.stdin.readline().strip().split())
graph = [list(map(int, sys.stdin.readline().strip().split())) for i in range(N)]

dx = [1, 1, 1]
dy = [-1, 0, 1]


def dfs(x, y, cost, direction):
    global answer
    cost += graph[x][y]

    # 종료 조건
    if x == N-1:
        answer = min(answer, cost)
        return

    for i in range(3):
        if i == direction: continue
        else:
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                dfs(nx, ny, cost, i)




# 모든 첫 번쨰 줄에서 실행
answer = sys.maxsize
for i in range(M):
    cost = 0
    direction = 1
    dfs(0, i, cost, -1)


print(answer)