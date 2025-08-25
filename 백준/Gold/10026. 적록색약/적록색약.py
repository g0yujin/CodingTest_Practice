import sys
sys.setrecursionlimit(10000)

N = int(sys.stdin.readline())
graph = []
for i in range(N):
    graph.append(list(sys.stdin.readline().strip()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited_1 = [[0] * N for _ in range(N)]
visited_2 = [[0] * N for _ in range(N)]

# 적록 색약 x
def dfs_see(x, y, word):
    visited_1[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny <N and visited_1[nx][ny] == 0 and graph[nx][ny] == word:
            dfs_see(nx, ny, word)


# 적록 색약  o
def dfs_rg(x, y, word):
    visited_2[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and visited_2[nx][ny] == 0:
            if word == 'B':
                if graph[nx][ny] == 'B':
                    dfs_rg(nx, ny, word)

            else:
                if graph[nx][ny] == 'R' or  graph[nx][ny] == 'G':
                    dfs_rg(nx, ny, word)


answer_1 = 0
answer_2 = 0
for i in range(N):
    for j in range(N):
        if visited_1[i][j] == 0:
            dfs_see(i, j, graph[i][j])
            answer_1 += 1


for i in range(N):
    for j in range(N):
        if visited_2[i][j] == 0:
            dfs_rg(i, j, graph[i][j])
            answer_2 += 1

print(answer_1, answer_2)


