import sys
sys.setrecursionlimit(10**6)

# 1. 입력 및 초기화
N = int(sys.stdin.readline())

# 2. 그래프 정보 입력
graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
house = 1
result = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    global house
    graph[x][y] = 0  # 1을 0으로 바꿔서 방문 처리

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1:
            house += 1
            dfs(nx, ny)



for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            dfs(i, j)
            result.append(house)
            house = 1

result.sort()
print(len(result))
for i in result:
    print(i)
