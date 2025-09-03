import sys

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def dfs(x, y):
    graph[x][y] = 2

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < H and 0 <= ny < W and graph[nx][ny] == 1:
            dfs(nx, ny)


while True:
    W, H = map(int, sys.stdin.readline().split())
    if W == 0 and H == 0:
        break

    graph = []

    for i in range(H):
        graph.append(list(map(int, sys.stdin.readline().strip().split())))


    answer = 0
    for i in range(H):
        for j in range(W):
            if graph[i][j] == 1:
                dfs(i, j)
                answer += 1

    print(answer)

