import sys

N = int(sys.stdin.readline())

graph = []
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().strip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

house = 1

def dfs(x, y):
    global house
    graph[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1:
            house += 1
            dfs(nx, ny)



answer = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            dfs(i, j)
            answer.append(house)
            house = 1

answer.sort()
print(len(answer))
for i in answer:
    print(i)