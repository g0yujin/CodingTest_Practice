import sys

sys.setrecursionlimit(10000)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

temp = 0
def dfs(x, y):
    global temp
    graph[x][y] = 1
    temp += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] == 0:
            dfs(nx, ny)


M, N, K = map(int, sys.stdin.readline().split())

graph = [[0] * N for _ in range(M)]

for i in range(K):
    lx, ly, rx, ry = map(int, sys.stdin.readline().split())

    for j in range(ly, ry):
        for k in range(lx, rx):
            graph[j][k] = 1


answer = []
for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            temp = 0
            dfs(i, j)
            answer.append(temp)

answer.sort()
print(len(answer))
print(*answer)